import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from configparser import ConfigParser
import shutil
from testrail import testrail as tr
import time
from selenium import webdriver
from urllib.error import URLError

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
group=sys.argv[7]
runid=sys.argv[8]
browser=sys.argv[9]
env=sys.argv[10]

runcmd='python singlerunner.py '
if (env == 'sikuli'):
    runcmd='C:/Sikuli/runsikulix.cmd -r '

testtool='7'
root=os.getcwd()
seleniumDir="qa/selenium/"
suiteDir=root+'/'+seleniumDir+suite

if (release == "8201m"):
    aspath = 'D:/ibi/AppStudio82/bin/Focshell.exe'
else:
    aspath='D:/'+confid+'/ibi/AppStudio82/bin/AppStudio.exe'
    
try:
    os.system('start /min c:/Winium.Desktop.Driver.exe')
    time.sleep(10)
except URLError:
    print("Winium.driver.exe not started")

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
        print(aspath + "cannot be located in the given path")
        exit()

def getFieldsDictionary( fields_str ) :
    theDictionary = {}
    for item in fields_str.split('\n'):
            pair = item.split(',')
            if len(pair) > 1:
                if bool(re.match('.*:.*', pair[1])):
                    reobj=re.match('(.*):.*', pair[1])
                    theDictionary.update({reobj.group(1): pair[0].strip()})
                else:
                    theDictionary.update({re.sub(' ','', pair[1]): pair[0].strip()})
    return theDictionary
conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
conf_pair = {}
parser = ConfigParser()
parser.read(conf_file)

section='testrail'
client = tr.APIClient(parser[section]['tr_link'])
client.user = parser[section]['tr_uid']
client.password = parser[section]['tr_pwd']

section='browser'
browser=browser+parser[section][browser]

result_fields=client.send_get('get_result_fields')
for i in range(len(result_fields)):
    if result_fields[i]['name'] == 'release':
        release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.lower())
        if release_key == None:
            release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.upper())
    if result_fields[i]['name'] == 'prodid':  
        product_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(product)
    if result_fields[i]['name'] == 'configurations':
        configuration_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(confid)
    if result_fields[i]['name'] == 'browsers':
        browser_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(browser)  
         
if release_key is None:
    raise KeyError('The requested release ' + release + ' is not currently a valid release choice in TestRail.')
if product_key is None:
    raise KeyError('The requested product ' + product + ' is not currently a valid product choice in TestRail.')
if configuration_key is None:
    raise KeyError('The requested configuration ' + confid + ' is not currently a valid configuration choice in TestRail.')
if browser_key is None:
    raise KeyError('The requested browser [' + browser + '] is not currently a valid browser choice in TestRail.')

suitename=re.sub(r'_.*','',suite)
suiteid=re.sub(r'S','',suitename)

if os.path.isdir(root+'/qa/selenium/'+suite+'/common'):
    os.system('rm -r '+root+'/qa/selenium/'+suite+'/common')
shutil.move(root+'/qa/selenium/common', root+'/qa/selenium/'+suite+'/')
shutil.copy(root+'/qa/selenium/driver/singlerunner.py', root+'/qa/automation/P'+project_id+'/S'+suite+'/G'+group+'/')

#ruunig tests
os.chdir(suiteDir)

result=client.send_get('get_cases/'+project_id+'&suite_id='+suiteid)
for i in range(len(result)):
    if result[i]['custom_automation_status'] == 4:
        testid=str(result[i]['id'])
        test='C'+testid
        #print('test no '+test+" started to run")
        runtest='true'
        defects=''
        status=''
        
        try:
            #cmd='get_results_for_case/'+runid+'/'+testid+'&limit=1'
            cmd='get_results_for_case/'+runid+'/'+testid+'&status_id=5,6&limit=1'
            if client.send_get(cmd):
                output=client.send_get(cmd)
                if output[0]['defects']:
                    defects=output[0]['defects']
                    status='6' 
                    runtest='false' 
        except :
            #print (test+' testrun causing error')
            continue
        if runtest == 'true':
            print('test no '+test+" started to run after checking True.")
            print(runcmd+test)
            resp=subprocess.call(runcmd+test)
            print(resp)
            if resp != 0:
                continue
            for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
                tree = ET.parse(name)
                root = tree.getroot()
                fail=root.attrib.get('failures')
                err=root.attrib.get('errors')
                if fail != '0' or err != '0': 
                    status='5'
                else :
                    status='1'
                break
        cmd='add_result_for_case/'+runid+'/'+testid
        resp=''
        try:
            resp=client.send_post(cmd,{ 'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
                'custom_configurations':configuration_key,'custom_run_mode':testtool,'custom_release':release_key,
                'custom_prodid':product_key,'custom_atm_issues':1,'defects':defects})
        except:
            print(sys.exc_info())
print ("Suite run Completed....Hence Stopping the winium driver...")
os.system("taskkill /f /im  Winium.Desktop.Driver.exe")