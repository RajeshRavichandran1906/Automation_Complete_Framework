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
from testrail import testrail as tr

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]


testtool='4'
root=os.getcwd()

seleniumDir="qa/selenium/"
suiteDir=root+'/'+seleniumDir+suite

client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'

rel = {'8105m': '2', '8106': '3', 'head': '4', '8200': '5', 'headcont': '6', '8106cont': '7', '8200m': '8', '8201': '9', '8201cont': '10', '8201m': '11'}
conf = {'bue1':'55','bue2':'56','wf1':'57','wf3':'65','as1':'58','507':'31','500':'28','wf4':'66','wf5':'67'}
prod={'wf':'1','as':'2','wq':'3','wx':'4','wb':'5'}

suiteid=re.sub(r'S','',suite)
confid=conf[confid]
product=prod[product]

if os.path.isdir(root+'/qa/selenium/'+suite+'/common'):
   os.system('rm -r '+root+'/qa/selenium/'+suite+'/common')
shutil.move(root+'/qa/selenium/common', root+'/qa/selenium/'+suite+'/')
shutil.move(root+'/qa/selenium/driver/singlerunner.py', root+'/qa/selenium/'+suite+'/')

#ruunig tests
os.chdir(suiteDir)

tests=[]
result=client.send_get('get_cases/'+project_id+'&suite_id='+suiteid+'&custom_automation_status=4')
for i in range(len(result)-1):
    tests.append(str(result[i]['id']))
testlist=','.join(tests)
testlist=re.sub(r'C','',testlist)

R = {'ie': '2', 'cr': '21', 'ff': '12','eg':'22'}
browser=R[browser]
release=rel[release]

for test in tests:
    print('test no '+test)
    runtest='false'
    try:
      cmd='get_results_for_case/'+runid+'/'+test+'&status_id=5,6&limit=1'
      print(cmd)
      if client.send_get(cmd):
         output=client.send_get('get_results_for_case/'+runid+'/'+test+'&status_id=5,6&limit=1')
         if output[0]['defects']:
            defects=output[0]['defects']
            result='6'  
         else:
            runtest='true'
      else:
         runtest='true'
    except OSError:
         print (test+' testrun causing error')
         continue
    
    if runtest == 'true':
       defects=''
       test='C'+test
       result=''
       try:
         print (test)
         subprocess.call('python singlerunner.py '+test)
       except OSError:
         print (test+' testrun causing error')
         continue
       for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
        tree = ET.parse(name)
        root = tree.getroot()
        fail=root.attrib.get('failures')
        err=root.attrib.get('errors')
        if fail != '0' or err != '0': 
           result='5'
        else :
            result='1'
        break
    testid=re.sub(r'C','',test)
    cmd='add_result_for_case/'+runid+'/'+testid
    print(cmd)
    result = client.send_post(
    cmd,
    { 'status_id': result,'custom_pkgname':pkgname,'custom_browsers':browser,'custom_configurations':confid,'custom_run_mode':testtool,'custom_release':release,'custom_prodid':product,
     'custom_atm_issues':1,'defects':defects}
    )
    print(result)