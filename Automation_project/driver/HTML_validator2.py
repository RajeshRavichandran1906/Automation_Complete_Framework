'''
Created on May 18 2019

'''
import os, shutil
from glob import glob
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from testrail import testrail as tr
import time
from selenium import webdriver
import uiautomation as automation
from datetime import datetime

def getFieldsDictionary(fields_str):
    """
    Description : Return the field info as dic from test rail database 
    """
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

def enable_ie_protected_mode():
    """ 
    Description : Enables the Protected mode setting for all zones in IE browser
    """
    if browser=='ie':
        for zone in range(1,5):
            cmd = ('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet" "Settings\\Zones\\'+str(zone)+' /v 2500 /t REG_DWORD /d 0 /f')
            os.system(cmd)
    print(browser + "'s Protected Mode checked")

def validate_and_project_id(project_id):
    # permit either numeric project number or 'p' prefix project number
    index_of_p = project_id.lower().find('p')
    if (index_of_p == 0):
       project_id = project_id[1:]
    if (not project_id.isdigit()):
        msg = "Project provided is not numeric: " + project_id
        raise RuntimeError(msg)

def get_fields_as_dictionary(fields_str):
        """
        Description : This function used to return field options as dictionary
        """
        theDictionary = {}
        for item in fields_str.split('\n'):
                pair = item.split(',')
                if len(pair) > 1:
                    if bool(re.match('.*:.*', pair[1])):
                        reobj=re.match('(.*):.*', pair[1])
                        theDictionary.update({reobj.group(1).lower(): pair[0].strip().lower()})
                    else:
                        theDictionary.update({re.sub(' ','', pair[1].lower()): pair[0].strip().lower()})            
        return theDictionary

def get_case_field_option_index(field_name, field_option):
        """
        Description : This function used to check whether given field_name and field_option are available in test rail database and 
        return result field option index value. For field_list parameter, should be pass testrail field list values
        :param : field_name='browsers'
        :param : field_option='ie11'
        :usage : __request_to_get_result_field_index('browsers', 'ie11)
        """
        field_list = client.send_get('get_case_fields')
        return get_field_option_index(field_list, field_name, field_option)

def get_test_result_field_option_index(field_name, field_option):
        """
        Description : This function used to check whether given field_name and field_option are available in test rail database and 
        return result field option index value. For field_list parameter, should be pass testrail field list values
        :param : field_name='browsers'
        :param : field_option='ie11'
        :usage : __request_to_get_result_field_index('browsers', 'ie11)
        """
        field_list = client.send_get('get_result_fields')
        return get_field_option_index(field_list, field_name, field_option)

def get_field_option_index(field_list, field_name, field_option):
        """
        Description : This function used to check whether given field_name and field_option are available in test rail database and 
        return result field option index value. For field_list parameter, should be pass testrail field list values
        :param : field_name='browsers'
        :param : field_option='ie11'
        :usage : __request_to_get_result_field_index('browsers', 'ie11)
        """
        for i in range(len(field_list)) :
            if field_list[i]['name'].lower().replace(' ', '')==field_name.lower().replace(' ', '') :
                result_field_options=field_list[i]['configs'][0]['options']['items']
                field_option_index=get_fields_as_dictionary(result_field_options).get(field_option.lower().replace(' ', ''))
                if field_option_index==None:
                    raise KeyError('The requested ' + field_name + ' [ ' + field_option + ' ] is not present in the testrail database')
                else :
                    return int(field_option_index)
                break
        else :
            raise KeyError('The requested result field [ ' + field_name + ' ] is not present in the testrail')
        
def get_test_status_index(status):
    """
    """
    test_fields = client.send_get('get_statuses')
    for index in range(len(test_fields)):
        if test_fields[index]['name'].lower() == status.lower() :
            return test_fields[index]['id']
    else :
        pass

def filter_cases_by_test_status_to_run(run_id, status=None):
    """
    """
    automated_index = get_case_field_option_index('automation_status', 'automated')
    scripts_path_reg = os.getcwd()+'/qa2/sikuli/'+suite + "/*.sikuli"
    print(scripts_path_reg)
    case_path = glob(scripts_path_reg)
    case_list = [int(re.findall("(\d+)\.sikuli$", path)[0]) for path in case_path if len(re.findall("(C\d+)\.sikuli$", path))>0]
    run = client.send_get("get_tests/" + str(run_id))
    status_index = get_test_status_index(status) if status!=None else None
    run_case_list = []
    if status_index == None :
        for index in range(len(run)) :
            if run[index]['custom_automation_status'] == automated_index :
                run_case_list.append(run[index]['case_id'])
    else :
        for index in range(len(run)) :
            if run[index]['custom_automation_status'] == automated_index :
                if run[index]['status_id'] == status_index :
                    run_case_list.append(run[index]['case_id'])
    filter_case_list = list(set(case_list) & set(run_case_list))
    return filter_case_list

def run_sikulix_cmd():
    test_status = None if test_result_status_name.lower() == 'none' else test_result_status_name
    actual_cases_to_run=filter_cases_by_test_status_to_run(runid, test_status)
    suiteDir = os.getcwd()+'/qa2/sikuli/'+suite
    os.chdir(suiteDir)
    for test in actual_cases_to_run :
        test = str(test)
        cmd='get_results_for_case/'+runid+'/'+test+'&limit=1'
        defects = ""
        runtest=True
        if client.send_get(cmd):
            output=client.send_get(cmd)
            if output[0]['defects']:
                defects=output[0]['defects']
                status='6' 
                runtest= False
        if runtest:
            test_file = "C" + test
            resp=subprocess.call('C:/Sikuli/runsikulix.cmd -r ' + test_file)
            if resp != 0:
                continue
            for name in glob(suiteDir+'/reports/*'+test_file+'*.xml'):
                tree = ET.parse(name)
                root = tree.getroot()
                fail=root.attrib.get('failures')
                err=root.attrib.get('errors')
                if fail != '0' or err != '0':
                    status='5'
                else:
                    status='1'
                break
        #try:
        cmd='add_result_for_case/'+runid+'/'+test
        print("test= C", test, "status= ", status)
        resp=client.send_post(cmd,{'status_id':status,'custom_pkgname':pkgname,'custom_browsers':browser_index,
        'custom_configurations':confid_index,'custom_run_mode':tool_index,'custom_release':release_index,
        'custom_prodid':product_index,'custom_atm_issues':1,'defects':defects})
        print(resp)
        #except:
        #    print("Error occurred while posting result")

""" Setting AS tool and environment"""

def config_wfscom_and_invoke_appstudio():
    root=os.getcwd()
    new_suiteDir=root+'/qa2/sikuli'
    print('new_suiteDir_path: ', new_suiteDir)
    # The below script moves the sikuli folder from qa2 to qa
    #shutil.move(new_suiteDir, root)
    
    suiteDir=root+'/qa2/sikuli/'+suite
    print("actual_suite_dir",suiteDir)
    #rename existing wfscom to new name
    wfscom_path='C:/Users/qaauto/AppData/Roaming/Information Builders/'
    filename='wfscom.xml'
    new_filename='wfscom_old.xml'
    print('existing_path: ', wfscom_path+filename)
    print('new_path: ', suiteDir+'/'+filename)
    try:
        if os.path.isfile(wfscom_path+new_filename):
            os.remove(wfscom_path+new_filename)
    except:
        pass
    try:
        if os.path.isfile(wfscom_path+filename):
            os.rename(wfscom_path+filename, wfscom_path+new_filename)
        else:  
            print("Could not find %s file." % filename)
    except:
        pass
    #moving the wfscom from suite location to its appstudio path location
    try:
        if os.path.isfile(suiteDir+'/'+filename):
            shutil.move(suiteDir+'/'+filename, wfscom_path)
        else:
            print("Pass")
    except:
        pass    
    #aspath='D:/'+confid+'/ibi/AppStudio82/bin/Focshell.exe'
    aspath='D:/'+confid+'/ibi/AppStudio82/bin/AppStudio.exe'
    f=open(suiteDir + '/reports/aspath','w')
    f.write('')
    f.write(aspath)
    f.close()
    time.sleep(30)
    os.system('start /min c:/Winium.Desktop.Driver.exe')
    time.sleep(60)
    if os.path.isfile(aspath):
        driver = webdriver.Remote(
        command_executor='http://localhost:9999',
        desired_capabilities={'debugConnectToRunningApp': 'false',
            'app': aspath
        })
        automation.WindowControl(ClassName="#32770").Exists(maxSearchSeconds=250)
        try:
            if driver.find_element_by_name('Cancel').is_displayed():
                driver.find_element_by_name('Cancel').click()
        except:pass
        time.sleep(15)
        help_dialog_object=driver.find_element_by_class_name('#32770')
        if help_dialog_object.find_element_by_name('Close').is_displayed():
            help_dialog_object.find_element_by_name('Close').click()
        time.sleep(2)
    else:
        print("appstudio_path",aspath)
        exit()


'''------------------------- Arguments from Jenkins -------------------------------------'''
product=sys.argv[1]
release=sys.argv[2]
confid=sys.argv[3]
pkgname=sys.argv[4]
project_id=sys.argv[5]
suite=sys.argv[6]
runid=sys.argv[7]
browser=sys.argv[8]
test_result_status_name=sys.argv[9]
'''-------------------------------------------------------------------------------------'''

"""code to to print start time of the testcase"""
print("\n\n") 
startTime=datetime.now()
print("Test run started : "+ startTime.strftime('%y/%m/%d %H:%M:%S'))

""" Testrail functions"""
client = tr.APIClient('http://lnxtestrail.ibi.com/testrail/')
client.user = 'bigscm@ibi.com'
client.password = 'Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR'

browser_index = get_test_result_field_option_index("browsers", browser)
product_index = get_test_result_field_option_index("prodid", product)
confid_index = get_test_result_field_option_index("configurations", confid)
release_index = get_test_result_field_option_index("release", release)
tool_index = get_test_result_field_option_index("run_mode", "sk")

validate_and_project_id(project_id)
enable_ie_protected_mode()
config_wfscom_and_invoke_appstudio()
run_sikulix_cmd()

""" end time of the case"""           
endTime= datetime.now()
print("Test run ended : "+endTime.strftime('%y/%m/%d %H:%M:%S'))
runDuration=(endTime - startTime)
print("Duration of test run : " + str(runDuration))

""" Clean UP process"""
os.system("taskkill /f /im  Winium.Desktop.Driver.exe")