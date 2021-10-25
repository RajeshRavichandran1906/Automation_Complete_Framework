'''
Created on March 8, 2018
@author: Elena Martinez
This code is meant to use python to launch tests, using a variety of tools. 
At some point this code should become a class with proper methods.
Modifications made for AUTO-1585 on Dec 6, 2018 by Ming Li.
'''

import glob
import os
import re
import time
import subprocess
import sys
import traceback
import xml.etree.ElementTree as ET
from configparser import ConfigParser
import shutil
import tr_exception_check as trchecker
from testrail import testrail as tr
from test.sortperf import flush
from datetime import datetime
from logging import _startTime
import json
from testrail_dao import TR_DAO

print("\n\n") 
startTime=datetime.now()
print("Test run started : "+ startTime.strftime('%y/%m/%d %H:%M:%S'))

index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1
'''********************************AUTO-1585*************************************************'''
expected_count = 16
'''******************************************************************************************'''
#expected_count = 15
params_num = len(sys.argv)

if (params_num != expected_count):
    msg = "Parameters required is " + str(expected_count) + ". Parameters received: " + str(params_num) + "." + parameters_msg
    raise RuntimeError(msg)

product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5].lower()
suite=sys.argv[6]
subsection=sys.argv[7]
runid=sys.argv[8]
browser=sys.argv[9].lower()
case_status_to_test=sys.argv[10]
test_result_status_name=sys.argv[11]
test_tool_name=sys.argv[12] 
runnerBox=sys.argv[13]
build_credit=sys.argv[14]
'''********************************AUTO-1585*************************************************'''
build_number=sys.argv[15]
'''******************************************************************************************'''

# permit either numeric project number or 'p' prefix project number
index_of_p = project_id.find('p')
if (index_of_p == 0):
    project_id = project_id[1:]
if (not project_id.isdigit()):
    msg = "Project provided is not numeric: " + project_id
    raise RuntimeError(msg)

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
total_cases_skipped_no_rerun = 0

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
subsection_dir= os.path.join(suite_dir, subsection)
common_dir = os.path.join(tool_root_dir, common_folder_name)

print('Settings in Python Runner:')
print('***************************************************************************************************************')
print(parameters_msg)
print('suitename [' + suitename + ']')
print('suiteid [' + suiteid + ']')
print('subsection [' + subsection + ']')
print('browser [' + browser + ']')
print('root folder ' + root + ']')
print('root folder for tool [' + tool_root_dir + ']')
print('suite directory [' + suite_dir + ']')
print('subsection [' + subsection_dir + ']')
print('common directory [' + common_dir + ']')
print('case runner script name ['+ case_runner_source + ']')
print('***************************************************************************************************************', flush=True)
print("testing0")
print('\n', flush=True)
print("testing1")
trcheck = trchecker.Tr_Exception_Check()
print("testing2")
'''********************************AUTO-1585*************************************************'''
run_object = trcheck.testrail_get('get_run/' + str(runid))
plan_id = run_object['plan_id']
project_object = trcheck.testrail_get('get_project/' + project_id)
project_name = project_object['name']
suite_object = trcheck.testrail_get('get_suite/' + suite[1:])
suite_name = suite_object['name']
section_object = trcheck.testrail_get('get_section/' + subsection[1:])
section_name = section_object['name']
while section_object['parent_id'] is not None:
    section_object = trcheck.testrail_get('get_section/' + str(section_object['parent_id']))
    section_name = section_object['name'] + '->' + section_name
'''******************************************************************************************'''

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

#Get the custom results specifications from testrail. These are required when creating a test result.
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

#Get the case fields from testrail. These are required when creating a filtering a case.
case_fields=trcheck.testrail_get('get_case_fields')
current_value = case_fields[0]['configs'][0]['options']['items']
msg = "Requested status to test [" + case_status_to_test + "] is not present in the testrail database. [" + current_value + "]."
if current_value.find(case_status_to_test) == -1:
    raise ValueError(msg)
case_status_dictionary = getFieldsDictionary(current_value)
status_test_key = case_status_dictionary.get(case_status_to_test.replace(" ", "")).strip()
if status_test_key is None:
    raise ValueError(msg)
requested_case_automation_status = int(status_test_key)
msg = "Requested status to test key in testrail: " + str(requested_case_automation_status)
print(msg)
msg = ''

#Get the test status from testrail. These are required when filtering a case.
good_test_result_status = None
filter_previous = False
result_fields=trcheck.testrail_get('get_statuses')
for i in range(len(result_fields)):
    current_status_from_DB = result_fields[i]['name']
    if  current_status_from_DB == test_result_status_name:
        good_test_result_status = result_fields[i]['id']    
    current_status_from_DB = result_fields[i]['label']
    if  current_status_from_DB == test_result_status_name:
        good_test_result_status = result_fields[i]['id']

if good_test_result_status == None:
    filter_previous = False
    msg = "Requested test status to filter [" + test_result_status_name + "] is not present in the testrail database. All cases will be run."
else:
    filter_previous = True
    msg = "All cases with a previous status of " + test_result_status_name + " will be run."        
print(msg)

old_suite_common = os.path.join(subsection_dir, common_folder_name)
if os.path.isdir(old_suite_common):
    os.system('rm -r ' + old_suite_common)
shutil.move(common_dir, subsection_dir)
shutil.copy(case_runner_source, subsection_dir +'/')

resultDataDict = {   
        'custom_pkgname':pkgname,
        'custom_browsers':browser_key,
        'custom_configurations':configuration_key,
        'custom_run_mode':run_mode_key,
        'custom_release':release_key,
        'custom_prodid':product_key,
        'custom_atm_issues':1,
}

os.chdir(subsection_dir)
target_py_scripts = subsection_dir + case_script_match
testcases=[re.match('.*(C\d+).py', elem).group(1) for elem in glob.glob(target_py_scripts)]
if len(testcases) == 0:
    msg = "No python automation scripts were found in the target directory: " + str(target_py_scripts)
    raise RuntimeError(msg)
msg = str(len(testcases)) + " python automation scripts were found in the target directory: " + str(target_py_scripts) 
print(msg)

tr_dao_obj = TR_DAO()
try_count = 0
while try_count < 5:
    try:
        section_cases_in_run = tr_dao_obj.get_section_cases_for_run(int(runid))[suite][subsection]
        break
    except tr.APIError:
        time.sleep(60)
        try_count += 1
total_cases_found = len(section_cases_in_run)
'''********************************AUTO-1585*************************************************'''
test_id_title = {}
for case in section_cases_in_run:
    test_id_title[str(case)] = tr_dao_obj.get_case(case)['title']
total_cases_to_run = 0
index_of_cases_to_run = []
'''******************************************************************************************'''
if sys.platform == 'linux':
    cd_data_dir = '/bigshare/cd_data/temp'
    tr_data_dir = '/bigshare/tr_data/temp'
    result_dir = '/bigshare/jenkins_data/temp/'    
else:
    cd_data_dir = '\\\\bigscmstr\\bigshare\\cd_data\\temp'
    tr_data_dir = '\\\\bigscmstr\\bigshare\\tr_data\\temp'
    result_dir = '\\\\bigscmstr\\bigshare\\jenkins_data\\temp\\'   

#loop over cases in suite, according to testrail
for i in range(total_cases_found):
    testid = str(section_cases_in_run[i])
    test='C'+testid
    case_data = tr_dao_obj.get_case(case)
    
    #omit the cases that are not implemented in this suite or subsuite  
    if test not in testcases:
        status_to_testrail = failed_status
        result_comment = test + ": " + release +" not present. Check suite folder in cvs: " + suite
        total_cases_not_implemented += 1

        msg = result_comment
        #Skip this message for now, it produces too much noise
        #print(msg) 
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
        print("attempt match " + str(output[0]['status_id']))
        previous_result = output[0]['status_id']
        match_previous = good_test_result_status == previous_result
        if filter_previous and not match_previous:
            total_cases_skipped_no_rerun += 1
            msg = test + ": skipped because previous result was not " + test_result_status_name + "."
            print(msg)    
            msg = ''        
            continue
        
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
        #CICD-5
        resultDataDict['run_id'] = str(runid) 
        resultDataDict['case_id'] = testid
        resultDataDict['status_id'] = status_to_testrail
        resultDataDict['comment'] = comment_to_testrail
        caseresult_file1 = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runnerBox + '_' + str(build_number) + '_' + suite + '_R' + str(plan_id) + '_R' + str(runid) + '_' + test + '.caseresult'
        with open(caseresult_file1, 'w') as file:
            file.write(json.dumps(resultDataDict)) 
            
        try:
            shutil.copy(caseresult_file1, tr_data_dir)
        except:
            print('Unable to copy file ' + caseresult_file1 + 'to ' + tr_data_dir)

        continue
    '''********************************AUTO-1585*************************************************'''    
    total_cases_to_run += 1
    index_of_cases_to_run.append(i)

for i in index_of_cases_to_run:
    testid = str(section_cases_in_run[i])
    test='C'+testid     
    
    cmd='add_result_for_case/'+runid+'/'+testid
    comment_to_testrail = ''
    status_to_testrail = 0
    '''******************************************************************************************'''        
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
        continue   
    
    if resp != 0:
        status_to_testrail = failed_status
        result_comment = msg + ' ' + str(resp) 
        total_cases_runner_failed += 1
        comment_to_testrail = build_comment + "\n" + result_comment;        
        continue
    
    #the balance of the cases ran
    total_cases_run += 1    
    for name in glob.glob(subsection_dir+'/results/*'+test+'*.xml'):
        tree = ET.parse(name)
        root = tree.getroot()
        fail=root.attrib.get('failures')
        err=root.attrib.get('errors')
        '''********************************AUTO-1585*************************************************'''
        case_start_time = root.attrib.get('runner_start_time')
        case_end_time = root.attrib.get('runner_end_time')
        '''******************************************************************************************'''
            
        #failures
        if fail != '0':
            status_to_testrail = failed_status
            total_cases_failed += 1
            for failure_node in root.iter('failure'):
                failure_message = failure_node.attrib.get('message')
                failure_type = failure_node.attrib.get('type')
                comment_to_testrail += " " + failure_message + " " + failure_type 
            comment_to_testrail = build_comment + "\n" + comment_to_testrail            
        
        #errors          
        elif err != '0': 
            status_to_testrail = failed_status
            total_cases_error += 1
            for error_node in root.iter('error'):
                error_message = error_node.attrib.get('message')
                error_type = error_node.attrib.get('type')
                comment_to_testrail += " " + error_message + " " + error_type                               
            comment_to_testrail = build_comment + "\n" + comment_to_testrail   
      
        #success
        else:  
            total_cases_succeeded += 1   
            status_to_testrail = passing_status
            comment_to_testrail = build_comment + "\n" + passing_comment         
              
        '''********************************AUTO-1585*************************************************'''
        if test_tool_name == 'se':
            test_tool_name = 'Selenium'
        #Prod might not use runnerboxes 013-014, but it can use them if needed.
        runnerNum = int(runnerBox[-3:])
        if runnerNum <= 14:
            run_user = 'qaauto'
        elif runnerNum >=15:
            run_user = 'qarunner1'    
        else:
            run_user = 'Unknown'    
            
        if status_to_testrail == '1':  
            status = 'pass'
        else:
            status = 'fail'
        
        if release[-4:] == '_cdr':    #for the time being, hardcode this as requested 
            release = '8205'

        caseresult_folder = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runnerBox + '_' + browser[:2].lower() + '_' + str(build_number) + '_' + suite + '_R' + str(plan_id) + '_R' + str(runid) + '_' + test 
        if sys.platform == 'linux':
            html_file_location = '/bigshare/jenkins_data/'
            html_output_file = html_file_location + caseresult_folder + '/index.html \n'
        else:
            html_file_location = '\\\\bigscmstr\\bigshare\\jenkins_data\\'
            html_output_file = html_file_location + caseresult_folder + '\\index.html \n'
        
        caserun_file = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runnerBox + '_' + str(build_number) + '_' + suite + '_R' + str(plan_id) + '_R' + str(runid) + '.caserun'
        caserun_file_status =  product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runnerBox + '_' + str(build_number) + '_' + suite + '_R' + str(plan_id) + '_R' + str(runid) + '.caserun.done'
        caserun_file_object = open(caserun_file, 'a')

        content_list = []
        content_list.append('job_id ' + build_number + '\n')
        content_list.append('runner_id ' + runnerBox + '\n')
        content_list.append('browser_id ' + browser[:2].upper() + '\n')
        content_list.append('auto_tool_name ' + test_tool_name + '\n')
        content_list.append('dispatch_tool ' + 'Jenkins' + '\n')
        content_list.append('conf_id ' + str(confid) + '\n')
        content_list.append('prodid ' + product + '\n')
        content_list.append('relid ' + release + '\n')
        content_list.append('pkgname ' + pkgname + '\n')
        content_list.append('plan_id ' + 'R' + str(plan_id) + '\n')
        content_list.append('run_id ' + 'R' + str(runid) + '\n')
        content_list.append('run_user ' + run_user + '\n')
        content_list.append('project_id ' + 'P' +project_id + '\n')
        content_list.append('project_name ' + project_name + '\n')
        content_list.append('suite_id ' + suite + '\n')
        content_list.append('suite_name ' + suite_name + '\n')
        content_list.append('section_id ' + subsection + '\n')
        content_list.append('section_name ' + section_name + '\n')
        content_list.append('case_id ' + test + '\n')
        content_list.append('case_name ' + test_id_title[testid] + '\n')
        content_list.append('start_time ' + case_start_time.split('.')[0] + '\n')
        content_list.append('end_time ' + case_end_time.split('.')[0] + '\n')
        content_list.append('status ' + status + '\n')
        content_list.append('count ' + str(total_cases_to_run) + '\n')
        if status == 'fail':
            comment_lines = comment_to_testrail.split('\n')
            for j in range(len(comment_lines)):
                content_list.append('comment ' + comment_lines[j] + '\n')
        full_content = ''.join(content_list)
        caserun_file_object.write(full_content)
        caserun_file_object.write('\n')
        caserun_file_object.close()
        
        #CICD-5
        resultDataDict['run_id'] = str(runid) 
        resultDataDict['case_id'] = testid
        resultDataDict['status_id'] = status_to_testrail
        resultDataDict['comment'] = comment_to_testrail + "\n" + html_output_file +  "\n"
        resultDataDict['defects'] = None
        caseresult_file = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runnerBox + '_' + str(build_number) + '_' + suite + '_R' + str(plan_id) + '_R' + str(runid) + '_' + test + '.caseresult'
        with open(caseresult_file, 'w') as file:
            file.write(json.dumps(resultDataDict)) 
        
        try:
            shutil.copy(caseresult_file, tr_data_dir)
        except:
            print('Unable to copy file ' + caseresult_file + 'to ' +  tr_data_dir)

        caseresult_xml = test + '.xml'
        os.rename(name, subsection_dir + '/results/' + caseresult_xml)
        try:
            os.makedirs(caseresult_folder)
        except:
            print('Unable to create case result directory locally: ' + caseresult_folder)        
        #copy result xml file locally to case result directory
        try:
            shutil.copy('./results/' + caseresult_xml, caseresult_folder)
        except:
            print('Unable to copy file ' + caseresult_xml + ' locally to ' + caseresult_folder)
        #copy verification screenshots to case result directory
        try:
            verification_image_path = os.path.join(os.getcwd(), glob.glob(test)[0])        
            for png in glob.glob(os.path.join(verification_image_path, '*'+test+'*.png')):
                try:
                    shutil.copy(png, caseresult_folder)
                except:
                    print('Unable to copy file ' + png + ' locally to ' + caseresult_folder)
            del verification_image_path, png
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file *'+str(test)+'*.png found in ' + test + ' directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy verification html to case result directory
        try:
            verification_image_path = os.path.join(os.getcwd(), glob.glob(test)[0])        
            for html in glob.glob(os.path.join(verification_image_path, 'index.html')):
                try:
                    shutil.copy(html, caseresult_folder)
                except:
                    print('Unable to copy file ' + html + ' locally to ' + caseresult_folder)
            del verification_image_path, html
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file '+str(test)+'_verificaiton.html found in ' + test + ' directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy step screenshots to case result directory
        try:
            verification_image_path = os.path.join(os.getcwd(), glob.glob('actual_images')[0])
            for png in glob.glob(os.path.join(verification_image_path, test+'_actual_image_*.png')):
                try:
                    shutil.copy(png, caseresult_folder)
                except:
                    print('Unable to copy file ' + png + ' locally to ' + caseresult_folder)
            del verification_image_path, png
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file '+str(test)+'_actual_image_*.png found in actual_images directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy step html to case result directory
        try:
            verification_image_path = os.path.join(os.getcwd(), glob.glob('actual_images')[0])        
            for png in glob.glob(os.path.join(verification_image_path, test+'*.html')):
                try:
                    shutil.copy(png, caseresult_folder)
                except:
                    print('Unable to copy file ' + png + ' locally to ' + caseresult_folder)
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file '+str(test)+'.html found in actual_images directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy step expected screenshots to case result directory
        try:
            verification_image_path = os.path.join(os.getcwd(), glob.glob('images*')[0])        
            for png in glob.glob(os.path.join(verification_image_path, test+'_expected_image_*.png')):
                try:
                    shutil.copy(png, caseresult_folder)
                except:
                    print('Unable to copy file ' + png + ' locally to ' + caseresult_folder)
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file '+str(test)+'_expected_image_*.png found in images* directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy failure screenshot  to case result directory
        try:
            failure_capture_file = os.path.join(os.path.join(os.getcwd(), glob.glob('failure_capture*')[0]), 'test_' + test + '.png')        
            if os.path.isfile(failure_capture_file):
                try:
                    shutil.copy(failure_capture_file, caseresult_folder)
                except:
                    print('Unable to copy file ' + failure_capture_file + ' locally to ' + caseresult_folder)
        except Exception as e:
            try:
                exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
                if 'index' in exception_[0]:
                    print('No such file test_'+str(test)+'.png found in failure_capture* directory to copy locally to ' + caseresult_folder)
                else:
                    print(Exception(e))
            except Exception as e:
                print(Exception(e))
        #copy case result directory to jenkins_data    
        try:
            shutil.copytree('./' + caseresult_folder, result_dir + caseresult_folder)
        except Exception as e:
            print('Unable to copy case result folder ' + caseresult_folder + ' to ' + result_dir)
       
        try:
            shutil.copy(caserun_file, cd_data_dir)
            try:
                caserun_file_status_object = open(caserun_file_status, 'a')
                caserun_file_status_object.write(' ')
                caserun_file_status_object.close()
                shutil.copy(caserun_file_status, cd_data_dir)
            except:
                print('Unable to copy file ' + caserun_file_status + 'to ' + cd_data_dir)
        except:
            continue
        '''******************************************************************************************'''

print("\n\n\n\n")       
print('Summary of status:')
print('-----------------')
print('Cases run                            : ' + str(total_cases_run))
print('Cases found in run and section       : ' + str(total_cases_found))
print('Cases skipped by status              : ' + str(total_cases_wrong_status))
print('Cases selected by status             : ' + str(total_cases_selected_status))
print('Cases not mapped to run              : ' + str(total_cases_wrong_runid))
print('Cases not found in cvs               : ' + str(total_cases_not_implemented))
print('Cases skipped lacking test results   : ' + str(total_cases_skipped_no_test_results))
print('Cases skipped for defects            : ' + str(total_cases_defective))
print('Cases skipped for filtering previous : ' + str(total_cases_skipped_no_rerun))
print('Cases in error                       : ' + str(total_cases_error))
print('Cases failed                         : ' + str(total_cases_failed))
print('Cases that failed to run             : ' + str(total_cases_runner_failed))
print('Cases succeeded                      : ' + str(total_cases_succeeded))
print('Cases reported to testrail           : ' + str(total_cases_to_report))
print('Cases found in cvs ' + subsection + ' : '+ str(len(testcases)))
print("\n") 
endTime= datetime.now()
print("Test run ended : "+endTime.strftime('%y/%m/%d %H:%M:%S'))
runDuration=(endTime - startTime)
print("Duration of test run : " + str(runDuration))

#TODO:  write code to log into a file

