import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from configparser import ConfigParser
import shutil
import testrail as tr
# from driver import testrailapi
from runnerfactory import RunnerFactory 

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]
test_tool_name=sys.argv[9] 
status_to_test=sys.argv[10]
status_to_assign=sys.argv[11]
author_credit=sys.argv[12]
test_result_status_name = sys.argv[13]
build_credit=sys.argv[14]

cases_from_suite = 0
cases_requested_automation_status = 0
cases_nomatch_automation_status = 0
cases_could_not_run = 0

failed_test_result_status_name = 'failed'

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

special_runner = RunnerFactory.RunnerFactory.getInstance(product, confid, release)
special_runner.execute()

root=os.getcwd()
seleniumDir="qa/selenium/"
suiteDir=root+'/'+seleniumDir+suite

conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
parser = ConfigParser()
parser.read(conf_file)

section='testrail'
client = tr.APIClient(parser[section]['tr_link'])
client.user = parser[section]['tr_uid']
client.password = parser[section]['tr_pwd']
print("Connect to TR with userId {0} and Pass {1}".format(client.user,client.password))
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
    if result_fields[i]['name'] == 'run_mode':
        run_mode_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(test_tool_name)       

if release_key is None:
    raise KeyError('The requested release ' + release + ' is not currently a valid release choice in TestRail.')
if product_key is None:
    raise KeyError('The requested product ' + product + ' is not currently a valid product choice in TestRail.')
if configuration_key is None:
    raise KeyError('The requested configuration ' + confid + ' is not currently a valid configuration choice in TestRail.')
if browser_key is None:
    raise KeyError('The requested browser [' + browser + '] is not currently a valid browser choice in TestRail.')
if run_mode_key is None:
    raise KeyError('The requested run mode [' + test_tool_name + '] is not currently a valid run mode choice in TestRail.')

result_fields=client.send_get('get_case_fields')
current_value = result_fields[0]['configs'][0]['options']['items']
if current_value.find(status_to_test) == -1:
    msg = "Requested status to test [" + status_to_test + "] is not present in the testrail database."
    raise ValueError(msg)
case_status_dictionary = getFieldsDictionary(current_value)

status_test_key = case_status_dictionary.get(status_to_test.replace(" ", ""))
if status_test_key is None:
    msg = "Requested status to test [" + status_to_test + "] is not present in the testrail database."
    raise ValueError(msg)
status_assignment_key = case_status_dictionary.get(status_to_assign.replace(" ", ""))
if status_assignment_key is None:
    msg = "Requested status to assign [" + status_to_assign + "] is not present in the testrail database."
    raise ValueError(msg)

good_test_result_status = None
failed_test_result_status = None
result_fields=client.send_get('get_statuses')
for i in range(len(result_fields)):
    current_status_from_DB = result_fields[i]['name']
    if  current_status_from_DB == test_result_status_name:
        good_test_result_status = result_fields[i]['id']
    if current_status_from_DB == failed_test_result_status_name:
        failed_test_result_status = result_fields[i]['id']        
    current_status_from_DB = result_fields[i]['label']
    if  current_status_from_DB == test_result_status_name:
        good_test_result_status = result_fields[i]['id']

if good_test_result_status is None:
    msg = "Requested test status to assign [" + test_result_status_name + "] is not present in the testrail database."
    raise ValueError(msg)    
if failed_test_result_status is None:
    msg = "Requested test status for failed tests [" + failed_test_result_status_name + "] is not present in the testrail database."
    raise ValueError(msg)    

build_comment="["+build_credit+ "] has launched this build." 
author_comment="[" + author_credit + "] has modified a case promoted from " + status_to_test + " to " +  status_to_assign + " by the automation infrastructure."
passing_result_comment=build_comment + author_comment
failing_result_comment="[" + author_credit + "] further work on this case is required."
case_update_info={"custom_automation_status": status_assignment_key}

suitename=re.sub(r'_.*','',suite)
suiteid=re.sub(r'S','',suitename)

if os.path.isdir(root+'/qa/selenium/'+suite+'/common'):
    os.system('rm -r '+root+'/qa/selenium/'+suite+'/common')
shutil.move(root+'/qa/selenium/common', root+'/qa/selenium/'+suite+'/')
shutil.move(root+'/qa/selenium/driver/singlerunner.py', root+'/qa/selenium/'+suite+'/')

#running tests
os.chdir(suiteDir)
cmd = 'get_cases/'+project_id+'&suite_id='+suiteid
result=client.send_get(cmd)
cases_from_suite = len(result)
print(cmd + " This is the number of cases pulled form TR {0}".format(str(len(result))))
for i in range(cases_from_suite):
    case_object = result[i]
    if case_object['custom_automation_status'] == int(status_test_key.strip()):
        cases_requested_automation_status += 1
        testid=str(case_object['id'])
        test='C'+testid
        try:
            resp=subprocess.call('python singlerunner.py '+test)
        except Exception as e:
            cases_could_not_run += 1
            print("failing case [" + test + "], case status will not be changed")
            print("Case " + test + " could not be run. Exception is: " + str(e))
            continue
        print("Launched this test " + test)
        found_in_folder = False
        passing_result = False
        bad_update = False
        failing_details = ""
        the_glob = glob.glob(suiteDir+'/results/*'+test+'*.xml')
        print("Results folder has " + str(len(the_glob)))
        for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
            tree = ET.parse(name)
            root = tree.getroot()
            fail=root.attrib.get('failures')
            err=root.attrib.get('errors')
            found_in_folder = True
            if fail == '0' and err == '0': 
                try:         
                    test_result_status = good_test_result_status
                    cmd='add_result_for_case/'+runid+'/'+testid
                    resp=client.send_post(cmd,{ 'status_id':test_result_status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
                                               'custom_configurations':configuration_key,'custom_run_mode':run_mode_key,'custom_release':release_key,
                                               'custom_prodid':product_key,'custom_atm_issues':1,'defects':'','comment': passing_result_comment})
                    cmd='update_case/'+testid
                    resp=client.send_post(cmd,case_update_info)                               
                    passing_result = True
                except tr.APIError as e:
                    failing_details = "Attempt to modify case and test results failed due to API error. Case "+ case_object['id'] +" " + str(e)
                    print(failing_details)
                    bad_update = True
            else:
                for failure_node in root.iter('failure'):
                    failure_message = failure_node.attrib.get('message')
                    failure_type = failure_node.attrib.get('type')
                    failing_details += " " + failure_message + " " + failure_type
            break
        if found_in_folder and not passing_result and not bad_update:
            test_result_status = failed_test_result_status
            comment_to_send = failing_result_comment + failing_details
            cmd='add_result_for_case/'+runid+'/'+testid
            try:
                resp=client.send_post(cmd,{ 'status_id':test_result_status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
                                        'custom_configurations':configuration_key,'custom_run_mode':run_mode_key,'custom_release':release_key,
                                        'custom_prodid':product_key,'custom_atm_issues':1,'defects':'','comment': comment_to_send}) 
                
            except tr.APIError as e:
                failing_details = "Attempt to modify case and test results failed due to API error. Case "+ case_object['id'] +" " + str(e)
                print(failing_details)
                bad_update = True
                 
        if bad_update:
            case_comment = failing_details + " Please update this comment when this condition is cleared.\n" + case_object['custom_comment'] 
            case_comment_info={"custom_comment": case_comment}              
            cmd='update_case/'+testid
            resp=client.send_post(cmd,case_comment_info)         
    else:
        cases_nomatch_automation_status += 1 
special_runner.close()

print("Some stats should go here")