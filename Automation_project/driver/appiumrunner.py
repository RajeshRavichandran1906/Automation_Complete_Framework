print("Started")

import glob
import os
import re
import time
import subprocess
import sys
import xml.etree.ElementTree as ET
import shutil
from testrail import testrail as tr
from configparser import ConfigParser

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]

if browser=='sf':
    browser='sf8'
if browser=='cr':
    browser='cr_current'

testtool='8'
root=os.getcwd()
seleniumDir="qa/selenium/"
suiteDir=root+'/'+seleniumDir+suite
driverDir=root+'/'+seleniumDir+'/driver'
testtesultDir=suiteDir+'/results/test_results.txt'

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
conf_file=os.getcwd() + "/qa/selenium/driver/config.ini"
conf_pair = {}
parser = ConfigParser()
parser.read(conf_file)

section='testrail'
client = tr.APIClient(parser[section]['tr_link'])
client.user = parser[section]['tr_uid']
client.password = parser[section]['tr_pwd']

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
shutil.move(root+'/qa/selenium/driver/mobile_singlerunner.py', root+'/qa/selenium/'+suite+'/')

#ruunig tests
os.chdir(suiteDir)
os.system('open -a Terminal /usr/local/bin/appium')
os.chdir(driverDir)
subprocess.call('/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 Mobile_Setup.py '+suite,shell=True)
os.chdir(suiteDir)
time.sleep(60)

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
            cmd='get_results_for_case/'+runid+'/'+testid+'&limit=1'
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
                resp=subprocess.call('/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 mobile_singlerunner.py '+test,shell=True)
                if resp != 0:
                    continue
                for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
                    tree = ET.parse(name)
                    root = tree.getroot()
                    fail=root.attrib.get('failures')
                    err=root.attrib.get('errors')
                    result_file=open(testtesultDir,'a')
                    if fail != '0' or err != '0': 
                        status='5'
                        result_file.write(test+' - FAILED \n')
                        result_file.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
                        result_file.write(root[0][0].text + " \n")
                        result_file.write('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
                    else :
                        status='1'
                        result_file.write(test+' - PASSED \n')
                    result_file.close()
                    break
        cmd='add_result_for_case/'+runid+'/'+testid
        resp=''
        try:
            resp=client.send_post(cmd,{ 'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
                'custom_configurations':configuration_key,'custom_run_mode':testtool,'custom_release':release_key,
                'custom_prodid':product_key,'custom_atm_issues':1,'defects':defects})
        except:
            continue
            print(sys.exc_info())
os.system('killall Terminal')