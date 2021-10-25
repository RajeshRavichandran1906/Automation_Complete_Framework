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
import testrail as tr

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]

testtool='6'
root=os.getcwd()

suiteDir=root+'/sikuli/'+suite

client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'

rel = {'8105m': '2', '8106': '3', 'head': '4', '8200': '5', 'headcont': '6', '8106cont': '7', '8200m': '8', '8201': '9', '8201cont': '10',
        '8201m': '11', '8202': '14'}
conf = {'bue1':'55','bue2':'56','wf1':'57','wf2':'82','wf3':'65','as1':'58','507':'31','500':'28','wf4':'66','wf5':'67','623':'78','660':'87'}
prod={'wf':'1','as':'2','wq':'3','wx':'4','wb':'5'}
R = {'ie': '2', 'cr': '29', 'ff': '27','eg':'28'}

suitename=re.sub(r'_.*','',suite)
suiteid=re.sub(r'S','',suitename)
confid=conf[confid]
product=prod[product]
browser=R[browser]
release=rel[release]

#ruunig tests
os.chdir(suiteDir)

result=client.send_get('get_cases/'+project_id+'&suite_id='+suiteid)
for i in range(len(result)):
    if result[i]['custom_automation_status'] == 4:
        testid=str(result[i]['id'])
        test='C'+testid
#         print('test no '+test+" started to run")
        runtest='true'
        defects=''
        status=''
        
        try:
            cmd='get_results_for_case/'+runid+'/'+testid+'&limit=1'
            if client.send_get(cmd):
                output=client.send_get(cmd)
                if output[0]['defects']:
                    defects=output[0]['defects']
                    status='6' 
                    runtest='false' 
        except :
#             print (test+' testrun causing error')
            continue
        if runtest == 'true':
            for file in glob.glob("*.sikuli"):
                """ Verify Test case Exist in current directory """
                if file[:-7] == test:
                    resp=subprocess.call('C:/Sikuli/runsikulix.cmd -r '+test)
#                     resp=os.system('C:/Sikuli/runsikulix.cmd -r '+test)
                    if resp != 0:
                        continue
                    for name in glob.glob(suiteDir+'/reports/*'+test+'*.xml'):
                        tree = ET.parse(name)
                        root = tree.getroot()
                        fail=root.attrib.get('failures')
                        err=root.attrib.get('errors')
                        if fail != '0' or err != '0': 
                            status='5'
                        else:
                            status='1'
                        break
        cmd='add_result_for_case/'+runid+'/'+testid
        resp=''
        try:
            resp=client.send_post(cmd,{ 'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser,
                'custom_configurations':confid,'custom_run_mode':testtool,'custom_release':release,
                'custom_prodid':product,'custom_atm_issues':1,'defects':defects})
        except:
            continue
            #print(sys.exc_info())