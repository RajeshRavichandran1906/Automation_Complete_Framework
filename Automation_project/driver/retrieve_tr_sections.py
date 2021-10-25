'''
Created on March 8, 2018
@author: Elena Martinez, Jesmin Aktar, Ming Li
starting with a test plan to retrieve suite section names to test 
'''
import xml.etree.ElementTree as ET
import tr_exception_check as trchecker
import testrail as tr
import sys


try:
    cvstrack_subfolder = sys.argv[3].lower()
except:
    cvstrack_subfolder=''
    print("Optional: cvstrack folder encountered exception. Continuing execution.")
    

if cvstrack_subfolder!='':
    qa_root = cvstrack_subfolder + '/' + 'qa' + '/' + 'automation'
else:
    qa_root = 'qa' + '/' + 'automation'

qa_key = 'scm'
index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1

'''commenting the below lines temporarily'''
# expected_count = 3
# params_num = len(sys.argv)
#
# if (params_num < expected_count):
#     msg = "Parameters required is " + str(params_num) + ". Unexpected number of parameters received: " + parameters_msg
#     raise RuntimeError(msg)
'''end of commenting'''
    
trcheck = trchecker.Tr_Exception_Check()

plan_id = sys.argv[1].lower()
file_name = sys.argv[2]

# permit either numeric plan number or 'r' prefix plan number
index_of_r = plan_id.find('r')
if (index_of_r == 0):
    plan_id = plan_id[1:]
if (not plan_id.isdigit()):
    msg = "Plan provided is not numeric: " + plan_id
    raise RuntimeError(msg)

cmd = 'get_plan/'+plan_id
plan_result=trcheck.testrail_get(cmd)
if(plan_result == None):
    msg = "Plan provided is not found in testrail: " + plan_id
    raise RuntimeError(msg)   

plan_name = plan_result['name']
project_id = plan_result['project_id']
plan_description = plan_result['description']
print("Plan description [" + str(plan_description) + "]")
requested_config = ''
requested_asconf = ''
if plan_description != None:
    xml_root = ET.fromstring(str(plan_description))
    for node in xml_root.iter('config'):
        requested_config = node.attrib['id']
    for node in xml_root.iter('asconf'):
        requested_asconf = node.attrib['id']

'''
list_of_suites = []
suite_to_run_dict = {}

for entry in plan_result['entries']:
    current_id = entry['id']
    if (current_id != plan_id):
        top_suite_id = entry['suite_id']
        runs = entry['runs']
        for run in runs:
            run_level_suite_id = run['suite_id']
            run_id = run['id']
            list_of_suites.append(run_level_suite_id)
            if (run_level_suite_id not in suite_to_run_dict):
                suite_to_run_dict[run_level_suite_id] = []
            suite_run_list = suite_to_run_dict[run_level_suite_id]
            suite_run_list.append(run_id)
            
set_of_suites = set(list_of_suites)

list_of_sections = []
for suite_id in set_of_suites:
    cmd = 'get_sections/'+ str(project_id) + '&suite_id='+str(suite_id)
    sections_result=trcheck.testrail_get(cmd)
    list_of_sections.append(sections_result)

if requested_asconf == '':
    general_info = 'project_id=' + str(project_id) + ',' + 'plan_id=' + str(plan_id) + ",browser=" + requested_browser + ",browser_version=" + requested_browser_version + ",config_id=" + requested_config
else:
    general_info = 'project_id=' + str(project_id) + ',' + 'plan_id=' + str(plan_id) + ",browser=" + requested_browser + ",browser_version=" + requested_browser_version + ",config_id=" + requested_config + ",asconf=" + requested_asconf

file_object  = open(file_name, 'w') 
for section_result in list_of_sections:
    for section in section_result:
        section_id = section['id']
        suite_id = section['suite_id']
        depth = section['depth']
        plan_folder = "P" + str(project_id)
        section_name = "G" + str(section_id)
        suite_plus_section = "S" + str(suite_id) +  "/" + section_name
        name = plan_folder + "_" + suite_plus_section
        scm_path = qa_root + '/' + plan_folder + '/' + suite_plus_section
        runid_list = []
        if (suite_id not in suite_to_run_dict):
            # raise an error here?
            runid_list.append("")
        else:
            runid_list = suite_to_run_dict[suite_id]
        line_list = []
        line_list.append("name=" + name)
        line_list.append(',')
        line_list.append(qa_key + "=" + scm_path)
        line_list.append(',')     
        line_list.append("id=" + str(section_id))
        line_list.append(',')
        line_list.append('suite_id=' + str(suite_id))
        line_list.append(',') 
        line_list.append('depth=' + str(depth))
        line_list.append(',')
        line_list.append('folder='+ plan_folder)
        line_list.append(',')     
        line_list.append('subfolder='+ suite_plus_section)
        line_list.append(',')
        line_list.append('subsection='+ section_name)
        line_list.append(',')
        line_list.append(general_info)

        full_line = "".join(line_list)       
        line = "name=" + name + "," + "scm=" + scm_path + ","+ "id=" + str(section_id) + ','+ 'suite_id=' + str(suite_id) + ',' + 'depth=' + str(depth) + ',' + 'folder='+ suite_plus_section + ',' + 'subfolder='+ suite_plus_section + ',' + general_info
        for run_id in runid_list:
            line = full_line + ",run_id=" + str(run_id)
            file_object.write(line)
        file_object.write('\n')
file_object.close()
'''
for entry in plan_result['entries']:
    run_id=entry['runs'][0]['id']
    description=entry['runs'][0]['name']
    suite_id=entry['runs'][0]['suite_id']
    plan_id=entry['runs'][0]['plan_id']
    '''Step 2. Read the test case IDs from each run ID within the plan'''
    list_of_sections=[]
    for test_case in trcheck.testrail_get('get_tests/' + str(run_id)):
        case_section_id=trcheck.testrail_get('get_case/' + str(test_case['case_id']))['section_id']
        if case_section_id not in list_of_sections:
            list_of_sections.append(case_section_id)
    for section_id in list_of_sections:
        list_of_section_details=[]
        result_file_entry_dict={}
        result_file_entry_dict['run_id']=run_id
        result_file_entry_dict['suite_id']=suite_id
        result_file_entry_dict['section_id']=section_id
        result_file_entry_dict['depth']=trcheck.testrail_get('get_section/' + str(section_id))['depth']
        list_of_section_details.append(result_file_entry_dict)
        if requested_asconf == '':
            general_info = 'project_id=' + str(project_id) + ',' + 'plan_id=' + str(plan_id) + ",config_id=" + requested_config
        else:
            general_info = 'project_id=' + str(project_id) + ',' + 'plan_id=' + str(plan_id) + ",config_id=" + requested_config + ",asconf=" + requested_asconf
        file_object  = open(file_name, 'a') 
        for section_result in list_of_section_details:
            section_id = section_result['section_id']
            suite_id = section_result['suite_id']
            depth = section_result['depth']
            run_id = section_result['run_id']
            plan_folder = "P" + str(project_id)
            section_name = "G" + str(section_id)
            suite_plus_section = "S" + str(suite_id) +  "/" + section_name
            name = plan_folder + "_" + suite_plus_section
            scm_path = qa_root + '/' + plan_folder + '/' + suite_plus_section
            line_list = []
            line_list.append("name=" + name)
            line_list.append(',')
            line_list.append(qa_key + "=" + scm_path)
            line_list.append(',')     
            line_list.append("id=" + str(section_id))
            line_list.append(',')
            line_list.append('suite_id=' + str(suite_id))
            line_list.append(',') 
            line_list.append('depth=' + str(depth))
            line_list.append(',')
            line_list.append('folder='+ plan_folder)
            line_list.append(',')     
            line_list.append('subfolder='+ suite_plus_section)
            line_list.append(',')
            line_list.append('subsection='+ section_name)
            line_list.append(',')
            line_list.append(general_info)
            line_list.append(',')
            line_list.append('run_id='+ str(run_id))
            
            full_line = "".join(line_list)       
            file_object.write(full_line)
            file_object.write('\n')
        file_object.close()