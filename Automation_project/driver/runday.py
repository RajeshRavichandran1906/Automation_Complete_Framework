from datetime import date
from configparser import ConfigParser
import re
import os, calendar,sys, subprocess
from testrail import testrail as tr
import tr_exception_check as trchecker

rel=sys.argv[1]
conf=sys.argv[2]
pkg=sys.argv[3]
prod=sys.argv[4]



cvs_branch = rel if rel == 'HEAD' else 'branch'+rel
trcheck = trchecker.Tr_Exception_Check()

def get_configparser_object(file_path):
        """
        This method used to read given file path using ConfigParser package and return object 
        """
        Error_Msg="[{0}] path not exists in file system".format(file_path)
        if os.path.exists(file_path) :
            parser=ConfigParser()
            parser.optionxform = str
            parser.read(file_path)
            return parser
        else :
            raise FileNotFoundError(Error_Msg)
    
def get_scheduled_browser_section():
    weekNumber = date.today().isocalendar()[1]
    cr_start_week=1
    ff_start_week=2
    eg_start_week=3
    ie_start_week=4
    cr_week_list=[]
    ff_week_list=[]
    eg_week_list=[]
    ie_week_list=[]
    
    for i in range(0, 15):
        cr_week_list.append(cr_start_week + 4 * i)
        ff_week_list.append(ff_start_week + 4 * i)
        eg_week_list.append(eg_start_week + 4 * i)
        ie_week_list.append(ie_start_week + 4 * i)
    scheduled_browser_section = 'Chrome' if weekNumber in cr_week_list else 'Firefox' if weekNumber in ff_week_list else 'Edge' if weekNumber in eg_week_list else 'IE' if weekNumber in ie_week_list else None
    if scheduled_browser_section == None:
        raise ValueError("This week there is no schedule for automation run.")
    print('This is the ', weekNumber, ' week number of the Year. The scheduled browser for this week is ', scheduled_browser_section, '.')
    return scheduled_browser_section

wget_cmd='wget --auth-no-challenge --delete-after --http-user=guest --http-password=guest '
url='http://jenkins-prod:8080/job/PlanRunner/buildWithParameters?'
targetJob = 'SuiteSectionRunner'
tool = 'se' if prod == 'wf' else None
jenkinsuser = 'guest'
jenkinspassword = 'guest'
teststatustotest = 'None'
milestone_id = ''
plan_id = ''

if tool == None:
    raise ValueError('Sorry this system is implemented only for selenium suite run for WF product at this moment.')

scheduled_browser = get_scheduled_browser_section()
my_date = date.today()
current_day_name = calendar.day_name[my_date.weekday()].capitalize()
schedule_data_file=os.getcwd() + '\\qa\\selenium\\driver\\runschedule\\schedule.data'
parser_obj=get_configparser_object(schedule_data_file)
config_section = current_day_name.upper()
if config_section not in ('SATURDAY', 'SUNDAY'):
    for project_id in parser_obj[config_section].keys():
        schedule_release_dict = [item.strip() for item in parser_obj[config_section][project_id].split(',')]
        if rel not in schedule_release_dict:
            print('Sorry this automation run is not scheduled for the provided [' + rel + '] release.')
            continue
        for milestonedetail in trcheck.testrail_get('get_milestones/'+project_id.lstrip('P')+'&is_completed=0'):
            if milestonedetail['name'].startswith(rel) and 'WebFOCUS' in milestonedetail['name']:
                milestone_id = milestonedetail['id']
            
        for plandetail in trcheck.testrail_get('get_plans/' + str(project_id.lstrip('P')) + '&is_completed=0&milestone_id=' + str(milestone_id)):
            if plandetail['name'].startswith('SEL') and scheduled_browser in plandetail['name']:
                if re.match(r'.*CID\s+(\d+).*', plandetail['name']).group(1) != conf:
                    print('Today [{0}] there is no automation schedule run for conf ID : {1}.'.format(config_section, conf))
                    break
                if rel == 'HEAD' and project_id == 'P292':
                    if current_day_name in plandetail['name']:
                        plan_id = plandetail['id']
                        call_job=wget_cmd + '"{0}token=run&product={1}&plan={2}&rel={3}&targetJob={4}&tool={5}&pkg={6}&jenkinsUser={7}&jenkinsPassword={8}&testStatusToTest={9}"'.format(url, prod, plan_id, cvs_branch, targetJob, tool, pkg, jenkinsuser, jenkinspassword, teststatustotest)
                        print(call_job)
                        subprocess.call(call_job)
                        break
                else:
                    plan_id = plandetail['id']
                    call_job=wget_cmd + '"{0}token=run&product={1}&plan={2}&rel={3}&targetJob={4}&tool={5}&pkg={6}&jenkinsUser={7}&jenkinsPassword={8}&testStatusToTest={9}"'.format(url, prod, plan_id, cvs_branch, targetJob, tool, pkg, jenkinsuser, jenkinspassword, teststatustotest)
                    print(call_job)
                    subprocess.call(call_job)
                    break
                #subprocess.call(call_job)
else:
    print('Automation will not run on ' + config_section + ' are not supported at this moment.')