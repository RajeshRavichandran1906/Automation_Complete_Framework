'''
Created on Jan 31, 2019
@author: Ming Li
@description: This code is meant to use Python to launch smoke tests to run in parallel on docker containers.
'''

import glob
import subprocess
import os
import io
import re
import sys
import json
import xml.etree.ElementTree as ET
import shutil
from datetime import datetime
from utility.case_result import Case_Result as CR
from utility.selenium_utility import Selenium_Utility 


start_time=datetime.now()
print('\n')
print("Test run started : "+ start_time.strftime('%y/%m/%d %H:%M:%S'))

expected_param_num = 13
params_num = len(sys.argv)
if (params_num != expected_param_num):
    msg = "Parameters required is " + str(expected_param_num) + ". Parameters received: " + str(params_num) + "."
    raise RuntimeError(msg)

confid = sys.argv[1]
product = sys.argv[2]
release = sys.argv[3]
pkgname = sys.argv[4]
runner_box = sys.argv[5]
build_number = sys.argv[6]
project = sys.argv[7] 
suite = sys.argv[8]
section = sys.argv[9]
planid = sys.argv[10]
runid = sys.argv[11]
browser = sys.argv[12]

print('***********************************************************')
print('Parameter values:')
print('confid: ' + confid)
print('product: ' + product)
print('release: ' + release)
print('pkgname: ' + pkgname)
print('runner box: ' + runner_box)
print('build number: ' + build_number)
print('project: ' + project)
print('suite: ' + suite)
print('section: ' + section)
print('planid: ' + planid)
print('runid: ' + runid)
print('browser: ' + browser)
print('***********************************************************', flush=True)

case_runner = 'singlerunner.py'
script_lst = glob.glob('./scripts/C*.py')
se_grid = Selenium_Utility.parseinitfile('','se_grid_env')
if se_grid == 'NA':
    for script in script_lst:
        testcase = script[script.index('/C')+1:script.index('.py')]
        if testcase != 'C8792737' and testcase != 'C8792775':
            print('Running case ' + testcase + '...')
            subprocess.call(['sudo', 'python3', case_runner, testcase])
else:
    ON_POSIX = 'posix' in sys.builtin_module_names
    input_fd, output_fd = os.pipe()
    for script in script_lst:
        testcase = script[script.index('\C')+1:script.index('.py')]
        if testcase != 'C9318159' and testcase != 'C9332918':  #excludes JOIN case which cannot be remotely deployed  
            print('Distributing test case '  + testcase)
            subprocess.Popen([sys.executable, case_runner, testcase], stdout=output_fd, close_fds=ON_POSIX)
    os.close(output_fd)
    with io.open(input_fd, 'r', buffering=1) as file:
        for line in file:
            print(line, end = '')
    
tr_data = json.loads(open('./data/tr_data.json').read())
project_name = tr_data['project'][project]
suite_name = tr_data['suite'][suite]
section_name = tr_data['section'][section]
cases = tr_data['cases']
browser_key = tr_data['browser'][browser]
configuration_key = tr_data['configurations'][confid]
run_mode_key = tr_data['run_mode']['se']
release_key = tr_data['release'][release]
product_key = tr_data['product'][product]

failed_status = '5' 
passing_status = '1'  
failed_case_count = 0
passed_case_count = 0 
if sys.platform == 'linux':
    cd_data_dir = '/bigshare/cd_data/temp/'
    tr_data_dir = '/bigshare/tr_data/temp/'
    result_dir = '/bigshare/jenkins_data/temp/'    
else:
    cd_data_dir = '\\\\bigscmstr\\bigshare\\cd_data\\temp'
    tr_data_dir = '\\\\bigscmstr\\bigshare\\tr_data\\temp'
    result_dir = '\\\\bigscmstr\\bigshare\\jenkins_data\\temp\\'   

result_lst = glob.glob('./results/*.xml')
for name in result_lst:
    case = re.search('C[0-9]+', name).group(0)
    tree = ET.parse(name)
    root = tree.getroot()
    fail = root.attrib.get('failures')
    err = root.attrib.get('errors')
    case_start_time = root.attrib.get('runner_start_time')
    case_end_time = root.attrib.get('runner_end_time')

    if fail != '0':
        status_to_testrail = failed_status
        failed_case_count += 1
        for failure_node in root.iter('failure'):
            failure_message = failure_node.attrib.get('message')
            failure_type = failure_node.attrib.get('type')
            comment_to_testrail = failure_message + " " + failure_type
    elif err != '0':
        status_to_testrail = failed_status
        failed_case_count += 1
        for error_node in root.iter('error'):
            error_message = error_node.attrib.get('message')
            error_type = error_node.attrib.get('type')
            comment_to_testrail = error_message + " " + error_type
    else:
        status_to_testrail = passing_status
        passed_case_count += 1
        comment_to_testrail = 'Passing test.'

    caserun_file = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runner_box + '_' + str(build_number) + '_' + suite + '_' + str(planid) + '_' + str(runid) + '.caserun'
    caserun_file_status =  product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runner_box + '_' + str(build_number) + '_' + suite + '_' + str(planid) + '_' + str(runid) + '.caserun.done'
    caserun_file_object = open(caserun_file, 'a')
    
    if sys.platform == 'linux':
        run_user = 'seluser'
    else:
        run_user = 'qarunner1'
    test_tool_name = 'Selenium'
        
    if status_to_testrail == '1':  
        status = 'pass'
    else:
        status = 'fail'

    content_list = []
    content_list.append('job_id ' + build_number + '\n')
    content_list.append('runner_id ' + runner_box + '\n')
    content_list.append('browser_id ' + browser[:2].upper() + '\n')
    content_list.append('auto_tool_name ' + test_tool_name + '\n')
    content_list.append('dispatch_tool ' + 'Jenkins' + '\n')
    content_list.append('conf_id ' + str(confid) + '\n')
    content_list.append('prodid ' + product + '\n')
    content_list.append('relid ' + release + '\n')
    content_list.append('pkgname ' + pkgname + '\n')
    content_list.append('plan_id ' + str(planid) + '\n')
    content_list.append('run_id ' + str(runid) + '\n')
    content_list.append('run_user ' + run_user + '\n')
    content_list.append('project_id ' + project + '\n')
    content_list.append('project_name ' + project_name + '\n')
    content_list.append('suite_id ' + suite + '\n')
    content_list.append('suite_name ' + suite_name + '\n')
    content_list.append('section_id ' + section + '\n')
    content_list.append('section_name ' + section_name + '\n')
    content_list.append('case_id ' + case + '\n')
    content_list.append('case_name ' + cases[case] + '\n')
    content_list.append('start_time ' + case_start_time.split('.')[0] + '\n')
    content_list.append('end_time ' + case_end_time.split('.')[0] + '\n')
    content_list.append('status ' + status + '\n')
    content_list.append('count ' + str(len(result_lst)) + '\n')
    if status == 'fail':
        content_list.append('comment ' + comment_to_testrail + '\n')        
                
    full_content = ''.join(content_list)
    caserun_file_object.write(full_content)
    caserun_file_object.write('\n')
    caserun_file_object.close()   
    
    resultDataDict = {   
        'custom_pkgname':pkgname,
        'custom_browsers':browser_key,
        'custom_configurations':configuration_key,
        'custom_run_mode':run_mode_key,
        'custom_release':release_key,
        'custom_prodid':product_key,
        'custom_atm_issues':'1',
        'defects':None,
        'run_id': str(runid[1:]),
        'case_id': case[1:],
        'status_id': status_to_testrail,
        'comment': comment_to_testrail
        }
    
    caseresult_file = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runner_box + '_' + str(build_number) + '_' + suite + '_' + str(planid) + '_' + str(runid) + '_' + case + '.caseresult'
    with open(caseresult_file, 'w') as file:
        file.write(json.dumps(resultDataDict)) 
        
    try:
        if sys.platform == 'linux':
            subprocess.call(['sudo', '-u', 'nobody', 'cp', caseresult_file, tr_data_dir])
            subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', tr_data_dir + caseresult_file])
        else:
            shutil.copy(caseresult_file, tr_data_dir)
    except:
        print('Unable to copy file ' + caseresult_file + ' to ' + tr_data_dir)
        
    caseresult_xml = case + '.xml'
    os.rename(name, './results/' + caseresult_xml)
    caseresult_folder = product + '_' + release + '_' + pkgname + '_' + str(confid) + '_' + runner_box + '_' + browser[:2].lower() + '_' + str(build_number) + '_' + suite + '_' + str(planid) + '_' + str(runid) + '_' + case 
    try:
        os.makedirs(caseresult_folder)
    except:
        print('Unable to create case result directory locally: ' + caseresult_folder)        
    #copy result xml files locally to case result directory
    try:
        shutil.copy('./results/' + caseresult_xml, caseresult_folder)
    except:
        print('Unable to copy file ' + caseresult_xml + ' locally to ' + caseresult_folder)         
    #move verification screenshots to case result directory
    for png in glob.glob(case + '*.png'):
        try:
            shutil.move(png, caseresult_folder)
        except:
            print('Unable to copy file ' + png + ' locally to ' + caseresult_folder) 
    #copy failure screenshot         
    failure_capture_file = './failure_capture/test_' + case + '.png'
    if os.path.isfile(failure_capture_file):
        try:
            shutil.copy(failure_capture_file, caseresult_folder)
        except:
            print('Unable to copy file ' + failure_capture_file + ' locally to ' + caseresult_folder)
    #generate HTML test result page        
    CR.generate_html(caseresult_folder)    
    #copy case result directory to jenkins_data
    copy_status_file = caseresult_folder + '.done'
    with open(copy_status_file, 'w') as f:
        f.write('')
    try:
        if sys.platform == 'linux':
            subprocess.call(['sudo', '-u', 'nobody', 'cp', '-r', caseresult_folder, result_dir])
            subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', result_dir + caseresult_folder])
        else:
            shutil.copytree('./' + caseresult_folder, result_dir + caseresult_folder)
        try:
            if sys.platform == 'linux':
                subprocess.call(['sudo', '-u', 'nobody', 'cp', copy_status_file, result_dir])
                subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', result_dir + copy_status_file])
            else:
                shutil.copy(copy_status_file, result_dir)
        except:
            print('Unable to copy status file ' + copy_status_file + ' to ' + result_dir)
    except:
        print('Unable to copy case result folder ' + caseresult_folder + ' to ' + result_dir)
           
try:
    if sys.platform == 'linux':
        subprocess.call(['sudo', '-u', 'nobody', 'cp', caserun_file, cd_data_dir])
        subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', cd_data_dir + caserun_file])
    else:
        shutil.copy(caserun_file, cd_data_dir)
    try:
        caserun_file_status_object = open(caserun_file_status, 'a')
        caserun_file_status_object.write(' ')
        caserun_file_status_object.close()
        if sys.platform == 'linux':
            subprocess.call(['sudo', '-u', 'nobody', 'cp', caserun_file_status, cd_data_dir])
            subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', cd_data_dir + caserun_file_status])
        else:
            shutil.copy(caserun_file_status, cd_data_dir)
    except:
        print('Unable to copy file ' + caserun_file_status + ' to ' + cd_data_dir)
except:
    print('Unable to copy file ' + caserun_file + ' to ' + cd_data_dir)
        
print('\n')
print('Test run summary:')
print('--------------------')
print('Cases ran       : ' + str(len(result_lst)))
print('Cases failed    : ' + str(failed_case_count))
print('Cases passed    : ' + str(passed_case_count))
print('--------------------')
print('\n')
end_time= datetime.now()
print("Test run ended : "+end_time.strftime('%y/%m/%d %H:%M:%S'))
run_duration=(end_time - start_time)
print("Duration of test run : " + str(run_duration))