from configparser import ConfigParser
import sys, subprocess, os
from testrail import testrail as tr

CASE_RUNNER_FILE = 'singlerunner.py'

class HealthChecker(object):
    
    def __init__(self):
        
        self.project_id = sys.argv[1][1:]
        self.suite_id = sys.argv[2][1:]
        self.group_id = sys.argv[3][1:]
        self.user_case_list = sys.argv[4]
        self.workdir = sys.argv[3]

    def __get_case_list_to_run(self) :
        """
        Description : This method used to get cases for run. If user not pass case list from jenkins then case list will get from test rail suite section
        """
        if self.user_case_list.upper() == 'NONE' :
            run_case_list = self.__get_case_list_from_testrail_suite_section()
        else :
            run_case_list = eval(self.user_case_list.replace('\n', '').replace(' ', ''))
            type_error = "CaseListToRun parameter value should be list. Example : ['C5831836','C5831836']"
            if type(run_case_list) != type([]) :
                raise TypeError(type_error)
        return run_case_list
    
    def __get_case_list_from_testrail_suite_section(self):
        """
        Description : This method used to get all test cases from suite section
        """
        automation_status_index = 4
        testrail = self.__get_testrail_object()
        url='get_cases/' + self.project_id + '&suite_id=' + self.suite_id + '&section_id=' + self.group_id
        section_cases = testrail.send_get(url)
        case_list = ['C' + str(case['id']) for case in section_cases if case['custom_automation_status'] == automation_status_index]
        return case_list
        
    def __get_testrail_object(self):
        """
        Description : This method used to get tetrail properties from config file andcreate testrail object
        """
        testrail_conf_file= os.path.join(os.getcwd() , 'driver', 'config.ini')
        parser = ConfigParser()
        parser.read(testrail_conf_file)
        section='testrail'
        client = tr.APIClient(parser[section]['tr_link'])
        client.user = parser[section]['tr_uid']
        client.password = parser[section]['tr_pwd']
        return client
        
    def Start_Runner(self):
        """
        Description : This method used torun all cases
        """
        run_case_list = self.__get_case_list_to_run()
        os.chdir(self.workdir) #Changing working directory
        for case in run_case_list :
            case_run_command = 'python' + ' ' + CASE_RUNNER_FILE + ' ' + case.strip()
            try:
                msg = " Case " + case + " could not be run with " + case_run_command
                resp = subprocess.call(case_run_command)
            except Exception as e:
                print(msg + str(e)) 
            if resp != 0:
                print(msg) 
            msg = ''        

HealthChecker().Start_Runner()