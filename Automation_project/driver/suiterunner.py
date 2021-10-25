'''
Created on March 8, 2018
@author: Elena Martinez
This code is meant to use python to launch tests using a variety of tools. 
At some point this code should become a class with proper methods.
'''

import glob
import os
import re
import time
import subprocess
import sys
import xml.etree.ElementTree as ET
from configparser import ConfigParser
import shutil
import tr_exception_check as trchecker
from testrail import testrail as tr
from test.sortperf import flush

index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1

expected_count = 13
params_num = len(sys.argv)

if (params_num != expected_count):
    msg = "Parameters required is " + params_num + ". Unexpected number of parameters received: " + parameters_msg
    raise RuntimeError(msg)

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]
status_to_test=sys.argv[9]
test_tool_name=sys.argv[10] 
runnerBox=sys.argv[11]
build_credit=sys.argv[12]

build_comment="["+ build_credit + "] has launched this build, running on node [" + runnerBox + "]";
runCaseComboError = "No (active) test found for the run/case combination."
passing_comment = "Passing test."
failed_status = '5'
defective_status = '6'
passing_status = '1'
upper_limit = 15
sleep_time = 300
total_cases_found = 0
total_cases_run = 0
total_cases_error = 0
total_cases_failed = 0
total_cases_wrong_status = 0
total_cases_selected_status = 0
total_cases_runner_failed = 0
total_cases_succeeded = 0
total_cases_wrong_runid = 0
total_cases_to_report = 0
total_cases_defective = 0
total_cases_not_implemented = 0
total_cases_skipped_no_test_results = 0

case_script_match = "\\scripts\\*.py"
qa_folder_name = 'qa'
#TODO pass this in depending on tool 
tool_folder_name = "selenium"
common_folder_name = 'common'
driver_folder_name = 'driver'
config_file_name = 'config.ini'
root=os.getcwd()
tool_root_dir= os.path.join(root, qa_folder_name)
tool_root_dir = os.path.join(tool_root_dir, tool_folder_name)
case_runner_folder= os.path.join(tool_root_dir, driver_folder_name)
#TODO figure this out depending on tool
case_runner = 'singlerunner.py'
case_runner_source = os.path.join(case_runner_folder, case_runner)
conf_file = os.path.join(case_runner_folder, config_file_name)

suitename=re.sub(r'_.*','',suite)
suiteid=re.sub(r'S','',suitename)
suite_dir=os.path.join(tool_root_dir, suite)
common_dir = os.path.join(tool_root_dir, common_folder_name)

print('Settings in Python Runner:')
print('***************************************************************************************************************')
print(parameters_msg)
print('suitename [' + suitename + ']')
print('suiteid [' + suiteid + ']')
print('root folder ' + root + ']')
print('root folder for tool [' + tool_root_dir + ']')
print('suite directory [' + suite_dir + ']')
print('common directory [' + common_dir + ']')
print('case runner script name ['+ case_runner_source + ']')
for environVar in os.environ:
    msg = environVar + " : " + os.environ[environVar]
    print(msg)
print('***************************************************************************************************************', flush=True)
print('\n', flush=True)

subprocess.call('pip list ')
conf_pair = {}
parser = ConfigParser()
parser.read(conf_file)
section='browser'
browser=browser+parser[section][browser]

trcheck = trchecker.Tr_Exception_Check()

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

result_fields=trcheck.testrail_get('get_result_fields')
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
    raise KeyError('The requested run mode [' + test_tool_name + '] is not currently a valid mode choice in TestRail.')

case_fields=trcheck.testrail_get('get_case_fields')
current_value = case_fields[0]['configs'][0]['options']['items']
msg = "Requested status to test [" + status_to_test + "] is not present in the testrail database. [" + current_value + "]."
if current_value.find(status_to_test) == -1:
    raise ValueError(msg)
case_status_dictionary = getFieldsDictionary(current_value)
status_test_key = case_status_dictionary.get(status_to_test.replace(" ", "")).strip()
if status_test_key is None:
    raise ValueError(msg)
requested_case_automation_status = int(status_test_key)
msg = "Requested status to test key in testrail: " + str(requested_case_automation_status)
print(msg)
msg = ''

old_suite_common = os.path.join(suite_dir, common_folder_name)
if os.path.isdir(old_suite_common):
    os.system('rm -r ' + old_suite_common)
#shutil.move(common_dir, suite_dir +'/')
shutil.move(common_dir, suite_dir)
shutil.move(case_runner_source, suite_dir +'/')

resultDataDict = {   
        'custom_pkgname':pkgname,
        'custom_browsers':browser_key,
        'custom_configurations':configuration_key,
        'custom_run_mode':run_mode_key,
        'custom_release':release_key,
        'custom_prodid':product_key,
        'custom_atm_issues':1,
}
os.chdir(suite_dir)
testcases=[re.match('.*(C\d+).py', elem).group(1) for elem in glob.glob(os.getcwd()+case_script_match)]
cmd = 'get_cases/'+project_id+'&suite_id='+suiteid
print("Attempt to get cases from project and suite " + cmd, flush=True)
result=trcheck.testrail_get(cmd)
total_cases_found = len(result)

#loop over cases in suite, according to testrail
for i in range(total_cases_found):
    case_data = result[i]
    testid=str(case_data['id'])
    test='C'+testid
    
    #omit the cases that are not implemented in this suite or subsuite  
    if test not in testcases:
        status_to_testrail = failed_status
        result_comment = test + ": " + release +" not present. Check suite folder in cvs: " + suite
        total_cases_not_implemented += 1

        msg = result_comment
        print(msg) 
        msg = ''       
        continue    
            
    #select the cases to run by automation status
    if case_data['custom_automation_status'] != requested_case_automation_status:
        total_cases_wrong_status += 1
        msg = test + ": skipped automation status : " + str(case_data['custom_automation_status'])
        print(msg)
        msg = ''
        continue
    
    total_cases_selected_status += 1
    #select the cases to run by runid
    cmd='get_results_for_case/'+runid+'/'+testid+'&limit=1'
    output = None
    defects = None
    
    try:
        output=trcheck.testrail_get(cmd)
    except tr.APIError as e:
        error_msg = str(e)
        if runCaseComboError in error_msg:
            total_cases_wrong_runid += 1
            msg = test + ": case is not part of this runid [" + runid + "] " + cmd 
            print(msg)
            msg = ''
            continue
        else:
            #something bad happened, quit
            raise(e)
    
    #read output to determine if this case is defective
    if (output == None):
        total_cases_skipped_no_test_results += 1
        msg = test + ": no test results returned from TestRail. "
        print(msg)    
        msg = ''
        continue
    
    if (len(output) > 0):
        defects = output[0]['defects']
    
    #the balance of the cases should report to testrail
    total_cases_to_report += 1      
    cmd='add_result_for_case/'+runid+'/'+testid
    comment_to_testrail = ''
    status_to_testrail = 0
    
    #omit the cases that are defective  
    resultDataDict['defects'] = defects 
    if defects:
        status_to_testrail = defective_status
        result_comment = 'Defective case not run.'
        total_cases_defective += 1  
        comment_to_testrail = build_comment + "\n" + result_comment;
        
        resultDataDict['status_id'] = status_to_testrail
        resultDataDict['comment'] = comment_to_testrail
        resp=trcheck.testrail_post(cmd, resultDataDict)
        msg = test + ": defective. "
        print(msg)     
        msg = ''
        continue
     
    #attempt to run the remaining cases
    case_run_command = 'python' + ' ' + case_runner + ' ' + test
    try:
        msg = " Case " + test + " could not be run with " + case_run_command
        resp=subprocess.call(case_run_command)
    except Exception as e:
        status_to_testrail = failed_status 
        result_comment = msg + str(e)
        total_cases_runner_failed += 1
        comment_to_testrail = build_comment + "\n" + result_comment;
        
        resultDataDict['status_id'] = status_to_testrail
        resultDataDict['comment'] = comment_to_testrail
        resp=trcheck.testrail_post(cmd, resultDataDict)
        print(msg) 
        msg = ''   
        continue    
    
    if resp != 0:
        status_to_testrail = failed_status
        result_comment = msg + ' ' + resp 
        total_cases_runner_failed += 1
        comment_to_testrail = build_comment + "\n" + result_comment;
        
        resultDataDict['status_id'] = status_to_testrail
        resultDataDict['comment'] = comment_to_testrail
        resp=trcheck.testrail_post(cmd, resultDataDict)
        print(msg) 
        msg = ''         
        continue
    
    #the balance of the cases ran
    total_cases_run += 1       
    for name in glob.glob(suite_dir+'/results/*'+test+'*.xml'):
        tree = ET.parse(name)
        root = tree.getroot()
        fail=root.attrib.get('failures')
        err=root.attrib.get('errors')
        
        #failures
        if fail != '0':
            status_to_testrail = failed_status
            total_cases_failed += 1
            for failure_node in root.iter('failure'):
                failure_message = failure_node.attrib.get('message')
                failure_type = failure_node.attrib.get('type')
                comment_to_testrail += " " + failure_message + " " + failure_type 
            comment_to_testrail = build_comment + "\n" + comment_to_testrail 
              
            resultDataDict['status_id'] = status_to_testrail
            resultDataDict['comment'] = comment_to_testrail
            resp=trcheck.testrail_post(cmd, resultDataDict)
            msg = test + ": ran and produced a failure."
            print(msg)   
            msg = ''           
        
        #errors          
        elif err != '0': 
            status_to_testrail = failed_status
            total_cases_error += 1
            for error_node in root.iter('error'):
                error_message = error_node.attrib.get('message')
                error_type = error_node.attrib.get('type')
                comment_to_testrail += " " + error_message + " " + error_type                               
            comment_to_testrail = build_comment + "\n" + comment_to_testrail 
              
            resultDataDict['status_id'] = status_to_testrail
            resultDataDict['comment'] = comment_to_testrail
            resp=trcheck.testrail_post(cmd, resultDataDict)    
            msg = test + ": ran and produced an error."
            print(msg)  
            msg = ''  
      
        #success
        else:  
            total_cases_succeeded += 1   
            status_to_testrail = passing_status
            comment_to_testrail = build_comment + "\n" + passing_comment         
                   
            resultDataDict['status_id'] = status_to_testrail
            resultDataDict['comment'] = comment_to_testrail
            resp=trcheck.testrail_post(cmd, resultDataDict)   
            msg = test + ": ran and produced a success."
            print(msg)  
            msg = ''
              
print("\n\n\n\n")       
print('Summary of stats:')
print('-----------------')
print('Cases run                            : ' + str(total_cases_run))
print('Cases found in suite                 : ' + str(total_cases_found))
print('Cases skipped by status              : ' + str(total_cases_wrong_status))
print('Cases selected by status             : ' + str(total_cases_selected_status))
print('Cases not mapped to run              : ' + str(total_cases_wrong_runid))
print('Cases not found in cvs               : ' + str(total_cases_not_implemented))
print('Cases skipped lacking test results   : ' + str(total_cases_skipped_no_test_results))
print('Cases skipped for defects            : ' + str(total_cases_defective))
print('Cases in error                       : ' + str(total_cases_error))
print('Cases failed                         : ' + str(total_cases_failed))
print('Cases that failed to run             : ' + str(total_cases_runner_failed))
print('Cases succeeded                      : ' + str(total_cases_succeeded))
print('Cases reported to testrail           : ' + str(total_cases_to_report))
msg = 'Cases found in cvs ' + suite + ' : ' + str(len(testcases))
print(msg)
