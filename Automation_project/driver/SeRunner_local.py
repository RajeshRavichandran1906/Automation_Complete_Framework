import os 
import glob
import os
import re
import subprocess
import sys
import bz2
import xml.etree.ElementTree as ET
import configparser
import shutil



product=sys.argv[1]
release = sys.argv[2]
confid=sys.argv[3]
suite=sys.argv[4]
suitename=sys.argv[5]
browser=sys.argv[6]

testtool='4'
root=os.getcwd()

if (product=='wf'):
   installfolder='webfocus' 
elif(product=='wb'):
   installfolder='webfocus_bue'
pkgpath='\\\\bigport\\rels_development\\'+release+'\\'+installfolder

if not(os.path.isdir(pkgpath)):
   cmd='net use o: '+pkgpath+' orion1 /user:ibi\\bigscm'
   os.system(cmd)
os.chdir(pkgpath)
all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
latest_subdir = max(all_subdirs, key=os.path.getmtime)
os.chdir(latest_subdir)
all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
pkgname = max(all_subdirs, key=os.path.getmtime).rstrip()
print(pkgname)
os.chdir(root)

seleniumDir="qa/selenium/"
suiteDir=root+'/'+seleniumDir+suite


b= b'BZh91AY&SY\x8d\xf6\xd6\xc7\x00\x00\x02\x0b\x80!`\x04\x00\x00\x04\x8c  \x00"\x06!\xa1\x000`\x83\xb8\xf9\x9f\x17rE8P\x90\x8d\xf6\xd6\xc7'
suiteid=re.sub(r'S','',suite)



rel = {'8105m': '2', '8106': '3', 'head': '4', '8200': '5', 'headcont': '6', '8106cont': '7', '8200m': '8', '8201': '9', '8201cont': '10'}
conf = {'bue1':'55','bue2':'56','wf1':'57','as1':'58'}
prod={'wf':'1','as':'2','wq':'3','wx':'4','wb':'5'}

confid=conf[confid]
product=prod[product]
R = {'ie': '11', 'ff': '46', 'cr': '50'}
browserrel=R[browser]


if os.path.isdir(root+'/qa/selenium/'+suite+'/common'):
   os.system('rm -r '+root+'/qa/selenium/'+suite+'/common')
shutil.move(root+'/qa/selenium/common', root+'/qa/selenium/'+suite+'/')


    #ruunig tests
os.chdir(suiteDir)
print(suiteDir)
os.system("python Test_Suite.py")

tests = [test.rstrip('\n') for test in open('testinfo.txt')]
testlist=','.join(tests)
testlist=re.sub(r'C','',testlist)

   #create env for run
e=bz2.decompress(b).decode(encoding='UTF-8')
cmd='\\\\bigrepos01\\bigscm\\TA\\admin\\php\\php \\\\bigrepos01\\bigscm\\'+\
       'TA\\admin\\php\\get_suite.php '+e+' '+suiteid
#resp=subprocess.check_output(cmd)
text=resp.decode(encoding='windows-1252')
projectid=re.search(r"\[project_id\]\s\=\>\s\d.*?\n",text).group(0).split('=>')[1].rstrip()
cmd ='\\\\bigrepos01\\bigscm\\TA\\admin\\php\\php \\\\bigrepos01\\bigscm\\'+\
     'TA\\admin\\php\\create_run.php '+e+' '+projectid+' '+suiteid+' "Automated '+\
     release+' run for '+suitename+' in '+browser+' '+browserrel+'- '+pkgname+'" '+testlist
#print (cmd)
#resp=subprocess.check_output(cmd)
#text=resp.decode(encoding='windows-1252')
runid=re.search(r"\[\"id\"\]\=\>\n\s+int\((\d+)\)",text).group(0).split('=>')[1].rstrip()
runid=re.sub(r'\)','',re.sub(r'int\(','',runid)).strip()

D = {'ie': '2', 'cr': '11', 'ff': '12'}
browser=D[browser]
release=rel[release]

for test in tests:
    for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
        tree = ET.parse(name)
        root = tree.getroot()
        fail=root.attrib.get('failures')
        err=root.attrib.get('errors')
        if fail== '1' or err == '1': 
    	    result='5'
        else :
            result='1'
        testid=re.sub(r'C','',test)
        cmd ='\\\\bigrepos01\\bigscm\\TA\\admin\\php\\php   \\\\bigrepos01\\bigscm\\'+\
         'TA\\admin\\php\\add_result.php '+e+' '+runid+' '+testid+' '+result+' '+\
          pkgname+' '+browser+' '+release+' '+confid+' '+testtool+' '+product;
        #print(cmd)
        #os.system(cmd)