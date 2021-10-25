import xml.etree.ElementTree as ET
from configparser import ConfigParser
from configobj import ConfigObj
from testrail import testrail as tr
import sys, datetime
#pkgname=sys.argv[1]
#conf_id=sys.argv[2]
#rel_id=sys.argv[3].lower()

conf_id='wf1'#To get it from jenkin
pkgname='wf010101a'#To get it from jenkin
rel_id='8202m'#To get it from jenkin
now = datetime.datetime.now()

#conf_file=os.getcwd() + "\\qa\\selenium\\driver\\config.ini"
conf_file="D:\\config.ini"
conf_pair = {}
parser = ConfigParser()
parser.read(conf_file)
section='testrail'
client = tr.APIClient(parser[section]['tr_link'])
client.user = parser[section]['tr_uid']
client.password = parser[section]['tr_pwd']
section='day'
today_browser=parser[section][now.strftime("%A").lower()]
print(today_browser)
plan_file="D:\\" + rel_id + "plan.ini"
config = ConfigObj(plan_file)

for section in config.sections:
    for key in config[section].keys():
        print("Project: ", key)
        planid=config[section][key][today_browser]
        print("Plan ID: ", planid)
        all_job_entry=[]
        plan_description=client.send_get('get_plan/'+planid)['description']
        xml_string=plan_description.replace('\r','').replace('\t','').replace('\n','')
        root = ET.fromstring(xml_string)
        root_summary=root.attrib
        job_names=[job.get('name') for job in root.findall('job')]
        for job_name in job_names:
            for a in root.findall('job')[job_names.index(job_name)].findall('suite')[0].findall('entry'):
                all_job_entry.append(a.attrib)
        for suite_entry in all_job_entry:
            suite_list=suite_entry['name'].split(',')
            for suite_id in suite_list:
                if conf_id == suite_entry['setup_id']: 
                    print("python qa/selenium/driver/seleniumrunner.py "+root_summary['product']+" "+root_summary['release']+" "+suite_entry['setup_id']+" " + pkgname + " " +root_summary['projectID']+" " + suite_id +" " + suite_entry['runID'] +" "+root_summary['browser']+"")