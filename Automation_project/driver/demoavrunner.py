from runnerfactory import RunnerFactory
# import glob
# import os
# import re
# import subprocess
# import sys
# import xml.etree.ElementTree as ET
# from configparser import ConfigParser
# import shutil
# import testrail as tr
# 
# product=sys.argv[1]
# release=sys.argv[2]
# confid=sys.argv[3]
# pkgname=sys.argv[4]
# project_id=sys.argv[5]
# suite=sys.argv[6]
# runid=sys.argv[7]
# browser=sys.argv[8]
# status_to_test=sys.argv[9]
# status_to_assign=sys.argv[10]
# author_credit=sys.argv[11]
# 
# run_mode_name = "se"
# test_result_status_name = "retest"
# 
# root=os.getcwd()
# seleniumDir="qa/selenium/"
# suiteDir=root+'/'+seleniumDir+suite
# 
# def getFieldsDictionary( fields_str ) :
#     theDictionary = {}
#     for item in fields_str.split('\n'):
#             pair = item.split(',')
#             if len(pair) > 1:
#                 if bool(re.match('.*:.*', pair[1])):
#                     reobj=re.match('(.*):.*', pair[1])
#                     theDictionary.update({reobj.group(1): pair[0].strip()})
#                 else:
#                     theDictionary.update({re.sub(' ','', pair[1]): pair[0].strip()})
#     return theDictionary
# conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
# conf_pair = {}
# parser = ConfigParser()
# parser.read(conf_file)
# 
# section='testrail'
# client = tr.APIClient(parser[section]['tr_link'])
# client.user = parser[section]['tr_uid']
# client.password = parser[section]['tr_pwd']
# 
# section='browser'
# browser=browser+parser[section][browser]
# 
# result_fields=client.send_get('get_result_fields')
# for i in range(len(result_fields)):
#     if result_fields[i]['name'] == 'release':
#         release_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release)
#     if result_fields[i]['name'] == 'prodid':  
#         product_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(product)
#     if result_fields[i]['name'] == 'configurations':
#         configuration_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(confid)
#     if result_fields[i]['name'] == 'browsers':
#         browser_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(browser)  
#     if result_fields[i]['name'] == 'run_mode':
#         run_mode_key = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(run_mode_name)       
# 
# if release_key is None:
#     raise KeyError('The requested release ' + release + ' is not currently a valid release choice in TestRail.')
# if product_key is None:
#     raise KeyError('The requested product ' + product + ' is not currently a valid product choice in TestRail.')
# if configuration_key is None:
#     raise KeyError('The requested configuration ' + confid + ' is not currently a valid configuration choice in TestRail.')
# if browser_key is None:
#     raise KeyError('The requested browser [' + browser + '] is not currently a valid browser choice in TestRail.')
# if run_mode_key is None:
#     raise KeyError('The requested run mode [' + run_mode_name + '] is not currently a valid run mode choice in TestRail.')
# 
# result_fields=client.send_get('get_case_fields')
# current_value = result_fields[0]['configs'][0]['options']['items']
# if current_value.find(status_to_test) == -1:
#     msg = "Requested status to test [" + status_to_test + "] is not present in the testrail database."
#     raise ValueError(msg)
# case_status_dictionary = getFieldsDictionary(current_value)
# 
# status_test_key = case_status_dictionary.get(status_to_test.replace(" ", ""))
# if status_test_key is None:
#     msg = "Requested status to test [" + status_to_test + "] is not present in the testrail database."
#     raise ValueError(msg)
# status_assignment_key = case_status_dictionary.get(status_to_assign.replace(" ", ""))
# if status_assignment_key is None:
#     msg = "Requested status to assign [" + status_to_assign + "] is not present in the testrail database."
#     raise ValueError(msg)
# 
# result_fields=client.send_get('get_statuses')
# for i in range(len(result_fields)):
#     if result_fields[i]['name'] == test_result_status_name:
#         test_result_status = result_fields[i]['id']
# if test_result_status is None:
#     msg = "Requested test status to assign [" + test_result_status_name + "] is not present in the testrail database."
#     raise ValueError(msg)    
# 
# result_comment="[" + author_credit + "] has modified a case promoted from " + status_to_test + " to " +  status_to_assign + " by the automation infrastructure."
# case_update_info={"custom_automation_status": status_assignment_key}
# 
# suitename=re.sub(r'_.*','',suite)
# suiteid=re.sub(r'S','',suitename)
# 
# if os.path.isdir(root+'/qa/selenium/'+suite+'/common'):
#     os.system('rm -r '+root+'/qa/selenium/'+suite+'/common')
# shutil.move(root+'/qa/selenium/common', root+'/qa/selenium/'+suite+'/')
# shutil.move(root+'/qa/selenium/driver/singlerunner.py', root+'/qa/selenium/'+suite+'/')
# 
# #running tests
# os.chdir(suiteDir)
# 
# result=client.send_get('get_cases/'+project_id+'&suite_id='+suiteid)
# for i in range(len(result)):
#     if result[i]['custom_automation_status'] == int(status_test_key.strip()):
#         testid=str(result[i]['id'])
#         test='C'+testid
#         resp=subprocess.call('python singlerunner.py '+test)
#         if resp != 0:
#             print("failing case [" + test + "], case status will not be changed")
#             continue
#         found_in_folder = False
#         for name in glob.glob(suiteDir+'/results/*'+test+'*.xml'):
#             tree = ET.parse(name)
#             root = tree.getroot()
#             fail=root.attrib.get('failures')
#             err=root.attrib.get('errors')
#             if fail == '0' and err == '0': 
#                 cmd='update_case/'+testid
#                 resp=client.send_post(cmd,case_update_info)
#             break
# 
#         try:
#             cmd='add_result_for_case/'+runid+'/'+testid
#             resp=client.send_post(cmd,{ 'status_id':test_result_status,'custom_pkgname':pkgname,'custom_browsers':browser_key,
#                 'custom_configurations':configuration_key,'custom_run_mode':run_mode_key,'custom_release':release_key,
#                 'custom_prodid':product_key,'custom_atm_issues':1,'defects':'','comment': result_comment})
#             
#         except:
#             continue
#             #print(sys.exc_info())