'''
Created on Jul 10, 2019

@author: td13786

This class provides methods to read and write to the history data file
'''

import os
import json
import datetime


class Run(object):
    
    def __init__(self, prod, rel, pkg, conf, is_scheduled = True, tool = None, browser = None, week = 'even', day = None, track= None):
        self.tool = tool.upper() if tool is not None else None
        self.prod = prod
        self.rel = rel
        self.pkg = pkg
        self.conf = conf
        self.is_scheduled = is_scheduled
        self.browser = browser.lower() if browser is not None else None 
        self.day = day.lower() if day is not None else Run.set_day_of_week()
        self.week = week.lower() #needs to be passed in, cannot be both
        self.track = track #should be handled by Jenkins
        self.plan_list = []        
                                
        
    '''
    returns lower case day string such as wednesday, monday for look up
    '''
    @classmethod
    def set_day_of_week(self):
        day = datetime.datetime.today().strftime('%A').lower()
        if int(datetime.datetime.now().strftime('%H')) <= 6:
            day = (datetime.date.today() - datetime.timedelta(days = 1)).strftime('%A').lower()
            
        return day
        
    
class Run_Controller(object):

    TC_BAT_NAME = "tc_plans"
    SEL_BAT_NAME = "sel_plans"
    TEST_TYPES = {"val":"validation", "reg":"regression", "tc":"testcomplete"}
    
    def __init__(self, run, data_dir='qa/automation/utilities/data/', update=False, rerun=False):
        self.run = run
        self.data_dir = data_dir
        self.update = False if rerun else update #to ensure reruns do not update history
        self.rerun = rerun
        
    
    '''utility function to read in json schedule with error handling'''
    def get_sched_json(self):
        sched = None
        try:
            with open(os.path.join(self.data_dir, self.run.rel + '.json')) as schedule_json:
                sched = json.load(schedule_json)
        except Exception as e:
            print("Error loading schedule json file")
            print(str(e))    
        return sched 
    
    '''utility function to create a plan object (dictionary) which contains tool, browser and plan_id'''
    def create_plan_object(self, tool, browser, plan_id):
        plan_obj = {}
        plan_obj["tool"] = tool
        plan_obj["browser"] = browser
        plan_obj["id"] = plan_id
        return plan_obj
    
    '''read schedule json file to get a list of plans that have not been run'''        
    def get_plan_list_from_json(self, sched):
        sections = []
        plans = []
        if self.run.tool == 'TC':
            sections.append(Run_Controller.TEST_TYPES["tc"])        
        elif self.run.tool == 'SEL':
            sections.append(Run_Controller.TEST_TYPES["val"])
            sections.append(Run_Controller.TEST_TYPES["reg"])
        elif self.run.tool is None:
            sections.append(Run_Controller.TEST_TYPES["tc"])
            sections.append(Run_Controller.TEST_TYPES["val"])
            sections.append(Run_Controller.TEST_TYPES["reg"])
            
        for section in sections:
            if section in sched: #check if json has plan types specified by the tool
                tool = "SEL"
                if section == Run_Controller.TEST_TYPES["tc"]:
                    tool = "TC"
                possible_browsers = []
                if self.run.browser is not None:
                    if self.run.browser in sched[section]:
                        possible_browsers.append(self.run.browser)
                    else:
                        print("Browser {} not found".format(str(self.run.browser)))
                else:
                    possible_browsers = sched[section] #check and make sure browsers are correct
                
                for browser in possible_browsers: 
                    if self.run.week in sched[section][browser] and self.run.day in sched[section][browser][self.run.week]:
                        if self.run.conf in sched[section][browser][self.run.week][self.run.day]:
                            for plan in sched[section][browser][self.run.week][self.run.day][self.run.conf]["plans"]:
                                if not self.day_exists_in_hist(sched) or self.rerun:
                                    plan_obj = self.create_plan_object(tool, browser, plan[1:])
                                    plans.append(plan_obj)
        
        return plans
    
    
    '''
    Setting plan_list at instance level.  
    This method should only be called when it is a scheduled run
    '''
    def set_plan_list(self, plans):
        if self.run.is_scheduled:
            self.run.plan_list = plans
    
    
    '''
    takes an ad-hoc list, and runs plans that exist in schedule
    ad-hoc list needs to have 'R' in plan number
    in this use case, self.run is being constructed with default values and populated on the fly
    this method should return a list of Run objects with plan_list populated
    each Run objects will then create -wgets in bat files
    '''
    def get_run_obj_list_from_list(self, prod, rel, pkg, conf, sched, ad_hoc_list, track=None):
        run_object_list = []
        
        for test_type in Run_Controller.TEST_TYPES.values():
            for browser in sched[test_type]:
                for week in sched[test_type][browser]:
                    for day in sched[test_type][browser][week]:
                        for config in sched[test_type][browser][week][day]:
                            if config.isdigit():#config id format check
                                tool = 'SEL'
                                if test_type == 'testcomplete':
                                    tool = 'TC'
                                run_object = self.get_run_obj_for_conf(prod, rel, pkg, conf, browser, week, day, track, sched[test_type][browser][week][day][config]["plans"], ad_hoc_list, tool)                           
                                if run_object is not None:
                                    run_object_list.append(run_object)
        return run_object_list
    
    '''
    only used if it is a unscheduled run
    is_scheduled must be False
    ad_hoc_list must be provided
    this method cleanses ad_hoc_list format
    '''
    def get_run_obj_for_conf(self, prod, rel, pkg, conf, browser, week, day, track, plan_list, ad_hoc_list, tool):
        run_object = None
        clean_plan_list = []
        
        for plan in ad_hoc_list:
            formatted_plan = None
            if plan.isdigit():
                formatted_plan = "R" + str(plan).rstrip()
            elif(plan[0].upper() == "R"):
                formatted_plan = "R" + str(plan[1:]).rstrip()
            if formatted_plan is not None:
                clean_plan_list.append(formatted_plan) 
                
        intersection = list(set(plan_list) & set(clean_plan_list))
        if len(intersection) > 0:
            run_object = Run(prod, rel, pkg, conf, is_scheduled = False, tool = tool, browser = browser, week = week, day = day, track = track)#, iteration = iteration)
            for plan in intersection:
                run_object.plan_list.append(plan + "_" + tool)
        return run_object
    
    '''
    checks if a given plan has been run for this package
    '''
    def day_exists_in_hist(self, sched):
        for test_type in Run_Controller.TEST_TYPES.values():
            for browser in sched[test_type]:
                if self.run.day in sched[test_type][browser][self.run.week]:
                    if self.run.conf in sched[test_type][browser][self.run.week][self.run.day]:
                        return True if sched[test_type][browser][self.run.week][self.run.day][self.run.conf]["executed"] == "true" else False
        return True #if self.day or browser does not exist, nothing will be run. It is effectively same as if the "executed" flag were "true".   
    
    
    '''
    update history dictionary with plans
    '''
    def update_hist(self, sched):
        if self.update and self.run.is_scheduled:
            for test_type in Run_Controller.TEST_TYPES.values():
                for browser in sched[test_type]:
                    if self.run.day in sched[test_type][browser][self.run.week] and self.run.conf in sched[test_type][browser][self.run.week][self.run.day]:
                        sched[test_type][browser][self.run.week][self.run.day][self.run.conf]["executed"] = "true"
    
    '''
    create wget calls based on plans to run
    '''
    def set_wgets(self, run_obj=None): 
        run = self.run if run_obj is None else run_obj
        sel_cmd_list = []
        tc_cmd_list = []

        sel_output_name = Run_Controller.SEL_BAT_NAME
        tc_output_name = Run_Controller.TC_BAT_NAME
        
        for plan in run.plan_list:
            plan_tool = plan["tool"]
            plan_name = plan["id"]
            plan_browser = "cr_current"
            
            if plan["browser"] == "firefox":
                plan_browser = "ff_current"
            elif plan["browser"] == "edge":
                plan_browser = "eg_current"
            elif "ie" in plan["browser"]:
                plan_browser = "ie_current"
                
            jenkins_machine = "jenkins-prod"
            job_name = "PlanRunner"
            cmd_list = sel_cmd_list

            if plan_tool == "TC":
                job_name = "TCPlanRunner"
                jenkins_machine = "jenkins"  
                cmd_list = tc_cmd_list
                
            cmd = 'wget --auth-no-challenge --delete-after --http-user=guest --http-password=guest "http://{jenkins}:8080/job/{job}/buildWithParameters?token=run&plan={plan}&rel={rel}&pkg={pkg}&confid={conf}&browser_id={br}"'\
            .format(jenkins=jenkins_machine, job=job_name, plan=plan_name, rel=run.rel, pkg=run.pkg, conf=run.conf, br=plan_browser)
            
            if run.track is not None:
                cmd = cmd[:-1] + '&track={}"'.format(run.track)
            
            print(cmd + '\n')
            cmd_list.append(cmd)        
        
        sel_commands = '\n'.join(sel_cmd_list) + '\n'
        tc_commands = '\n'.join(tc_cmd_list) + '\n'
        
        for output_name in [sel_output_name, tc_output_name]: 
            if output_name == sel_output_name:
                commands = sel_commands
                cmd_list = sel_cmd_list
            else:
                commands = tc_commands
                cmd_list = tc_cmd_list
                
            if len(cmd_list) > 0: 
                try:
                    if run_obj is None: 
                        with open('{name}.bat'.format(name=output_name), 'w') as f:
                            f.write(commands)
                            self.update = True
                    else: # called multiple times during Ad-hoc run
                        with open('{name}.bat'.format(name=output_name), 'a') as f:
                            f.write(commands)
                            self.update = False 
                except:
                    print("Could not create batch file - no plans were run!!!")    
            
    
    '''
    empties the content of tc_plans.bat and sel_plans.bat
    should only be called once, at the very beginning of script
    '''
    def clear_bat(self):
        for bat_name in (Run_Controller.TC_BAT_NAME, Run_Controller.SEL_BAT_NAME):
            bat_file_name = bat_name + ".bat"
            try:
                with open(bat_file_name, 'w') as f:
                    f.write('')
            except FileNotFoundError:
                print("No file found. Nothing to delete.")
        
    
    '''
    writes updated json file back to disk
    only called when self.update flag is True
    build logic to handle concurrent writing to the same file
    '''
    def update_json_file(self, sched):
        if self.update and self.run.is_scheduled:
            try:
                with open(os.path.join(self.data_dir, self.run.rel + '.json'), 'w') as new_schedule_json:
                    json.dump(sched, new_schedule_json, sort_keys = True)
            except Exception as e:
                print("Error updating schedule file on disk")
                print(str(e))
            
    
    
if __name__ == '__main__':
    '''Use case 1: kicked off by installation - is_scheduled, explicit conf id and week, no day or track or tool'''
    run = Run('wf', 'head_git', 'wf070819a', '812', day = 'Tuesday', week = 'even')
    print(run.is_scheduled)
    controller = Run_Controller(run, r'C:\Users\td13786\eclipse-workspace\automation\utilities\data')
    sched = controller.get_sched_json()
    print(sched)
    plans = controller.get_plan_list_from_json(sched)
    print(plans)
    controller.set_plan_list(plans)
    controller.set_wgets()
    controller.update_hist(sched)
    print(sched)
    controller.update_json_file(sched)
    plans = controller.get_plan_list_from_json(sched)
    print(plans)
    controller.set_plan_list(plans)
    controller.set_wgets()
    
    '''Use case 2: run manually - is scheduled needs to be False, no conf, day, week or browser'''
    '''what to do when a plan exists in multiple run objects?'''
#     run_objects = controller.get_run_obj_list_from_list('wf', '8206', 'wf070819a', '698', sched, ['93332', '92486', '92171', 'R93389', 'R92810 '], iteration='0')
#     print(run_objects)
#     controller.clear_bat()
#     for r in run_objects:
#         print(r.plan_list)
#         controller.set_wgets(r)
     
    
    
    
    
    
    
    
    
    
    
    
    
    