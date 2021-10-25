'''
Created on May 22, 2019

@author: TD13786
This script will run a part of TestComplete automation based on the installation parameters passed in 
'''

import sys
import os
from configparser import ConfigParser



class TC_Plan_Distributor():
    
    def __init__(self, prod, rel, pkg, conf, inst_id, config_file='qa/automation/utilities/config.ini', jenkins='', track='branch82xx'):
        self.prod = prod
        self.rel = rel
        self.pkg = pkg
        self.conf = conf
        self.inst_id = int(str(inst_id).strip())
        self.config_file = config_file
        self.plan_list = []
        self.jenkins = "jenkins" + jenkins
        self.track = track

            
    def get_plan_list(self):
        parser=ConfigParser()
        section = 'schedule'
        try:
            parser.read(self.config_file)
            set_num = self.inst_id % 3
            self.plan_list=parser[section]['set'+str(set_num)].split(',')
        except Exception as e:
            print("Error reading config.ini file or the schedule section within it\n")
            print("current working directory is " + os.getcwd())
            print(str(e))
            raise
    
    def set_wgets(self):
        cmd_list = []
        for plan in self.plan_list:
            cmd = 'wget --auth-no-challenge --delete-after --http-user=guest --http-password=guest "http://{jenkins}:8080/job/TCPlanRunner/buildWithParameters?token=run&plan={plan}&rel={rel}&pkg={pkg}&track={track}&confid={conf}"'.format(jenkins=self.jenkins, plan=plan, rel=self.rel, pkg=self.pkg, track=self.track, conf=self.conf)
            cmd_list.append(cmd)        
        
        commands = '\n'.join(cmd_list)
        print("All wget calls are listed as follows\n" + commands)
        with open('tc_plans.bat', 'w') as f:
            f.write(commands)
        
        
if __name__ == '__main__':
#     prod = 'wf'#sys.argv[0]
#     rel = '8206'#sys.argv[1]
#     pkg = 'wf052119a'#sys.argv[2]
#     conf = '721'#sys.argv[3]
#     inst_id = '749'#sys.argv[4]
    prod = sys.argv[1]
    rel = sys.argv[2]
    pkg = sys.argv[3]
    conf = sys.argv[4]
    inst_id = sys.argv[5]
    plan_distributor = TC_Plan_Distributor(prod, rel, pkg, conf, inst_id)
    plan_distributor.get_plan_list()
    plan_distributor.set_wgets()
    