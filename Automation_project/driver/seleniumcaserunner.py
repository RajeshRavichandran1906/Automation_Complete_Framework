'''
Created on Aug 24, 2018

@author: LY14557
@description: Runs a single case without any connection to TestRail. This is to emulate an official test without posting results.
@input(s): case id
'''

import sys, os, shutil
from configparser import ConfigParser
from testrail import testrail as tr

class seleniumcaserunner():
    def __init__(self):
        self.case_id = sys.argv[1]
        self.release = sys.argv[2]
        self.group_id = sys.argv[3]
        self.suite_id = sys.argv[4]
        self.project_id = sys.argv[5]
        self.project_dir = sys.argv[6]

        self.root=os.getcwd()
 
        #seleniumDir="qa/selenium/"
        #suiteDir=root+'/'+seleniumDir+group_id
        
        '''conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
        parser = ConfigParser()
        parser.read(conf_file)
        
        section='testrail'
        client = tr.APIClient(parser[section]['tr_link'])
        client.user = parser[section]['tr_uid']
        client.password = parser[section]['tr_pwd']
        self.client = client'''
        
    def get_case_details_from_tr(self):
        cmd = "get_case/"
        '''result=self.client.send_get(cmd+self.caseid)
        print(result)'''
    
    def get_case_from_cvs(self):
        pass
    
    def run_case(self):
        group_id = self.group_id
        project_dir = self.project_dir
        root = self.root
        
        if os.path.isdir(root + '/' + project_dir + '/' + group_id + '/common'):
            print("[" + root + '/' + project_dir + group_id + '/common' + "] exists. Moving into proper folder structure location.")
            os.system('rm -r '+ root + '/' +project_dir + group_id + '/common')
        else:
            print("[" + root + '/' + project_dir + group_id + '/common' + "] does not exist. Cannot move nonexistent folder.")
            exit(1)
            
        shutil.move(root + 'qa/selenium/common', root+'/qa/selenium/' + group_id + '/')
        shutil.move(root + 'qa/selenium/driver/singlerunner.py', root + '/qa/selenium/' + group_id + '/')
    
def __main__():
    scr_obj = seleniumcaserunner()
    scr_obj.run_case()
    pass
    
if __name__ == '__main__':
    __main__()