import sys
import time
import re
import os
import shutil
import subprocess
import testrail as tr
from selenium import webdriver

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
suite=sys.argv[5]
test=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]
print("test=",test)
testtool='6'
root=os.getcwd()
print("root=", root)
suiteDir=root+'/sikuli/'+suite
print("suiteDir=", suiteDir)
aspath='D:/'+confid+'/ibi/AppStudio82/bin/Focshell.exe'
os.system('start /min c:/Winium.Desktop.Driver.exe')

if os.path.isfile(aspath):
   driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={'debugConnectToRunningApp': 'false',
        'app': aspath
    })
   time.sleep(60)
   if driver.find_element_by_name('Close').is_displayed():
      driver.find_element_by_name('Close').click()
else:
   print(aspath)
   exit()

rel = {'8105m': '2', '8106': '3', 'head': '4', '8200': '5', 'headcont': '6', '8106cont': '7', '8200m': '8', '8201': '9', '8201cont': '10', '8201m': '11'}
conf = {'bue1':'55','bue2':'56','wf1':'57','wf3':'65','as1':'58','as8':'80','507':'31','500':'28','wf4':'66','wf5':'67'}
prod={'wf':'1','as':'2','wq':'3','wx':'4','wb':'5'}

suiteid=re.sub(r'S','',suite)
confid=conf[confid]
product=prod[product]
print("suiteid=", suiteid)
print("confid=", confid)
print("product=", product)
#ruunig tests
os.chdir(suiteDir)

client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'

R = {'ie': '2', 'cr': '25', 'ff': '12','eg':'22'}
browser=R[browser]
release=rel[release]
print("browser=", browser)
print("release=", release)
os.system("del suiteDir/Screenshots/*")

try:
   print("in try 1")
   result=5
   p=subprocess.Popen(('C:/Sikuli/runsikulix.cmd -r '+test),stdout=subprocess.PIPE)      
   result=p.communicate()[0].decode(encoding='windows-1252')
   print("result=",result)
   result=re.search(r'passed|failed',result).group()
   if result == 'passed':
       result=1
   if result == 'failed':
       result=5
except OSError:
   print("in exception 1")
   print (test+' testrun causing error')    
testid=re.sub(r'C','',test)
print("testid",testid)
cmd='add_result_for_case/'+runid+'/'+testid
print("cmd",cmd)
try:
   print("in try 2") 
   result = client.send_post(
       cmd,
       { 'status_id': result,'custom_pkgname':pkgname,'custom_browsers':browser,'custom_configurations':confid,'custom_run_mode':testtool,'custom_release':release,'custom_prodid':product,
       'custom_atm_issues':1}
       )
except:
   print("in exception 2")
   print(sys.exc_info())
print("Before task kill")
os.system("taskkill /f /im  Winium.Desktop.Driver.exe")
print("After task kill")
