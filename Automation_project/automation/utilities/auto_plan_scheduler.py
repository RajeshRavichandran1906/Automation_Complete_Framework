'''
Created on Jul 29, 2019

@author: td13786

how to handle a complete re-run?

'''

import os
import sys
import json
import math
import datetime
from configparser import ConfigParser
from auto_sched_parser import Auto_Sched
from run_control import Run, Run_Controller

prod = sys.argv[1].strip() #'wf'
rel = sys.argv[2].strip() #'8206'
pkg = sys.argv[3].strip() #"wf070319a"
conf = sys.argv[4].strip() # 756
run_mode = sys.argv[5].strip()
date_to_run = sys.argv[6].strip() if len(sys.argv) > 6 else None
csv_dir = "\\\\qaops\\qaops\\schedules\\csv"
data_folder = os.path.join(csv_dir, 'data\\')

# Updating schedule - should only be run at the beginning of a testing cycle 
# when this code is run, assume a new cycle 
#*******************************************************************************************************
sched_parser = Auto_Sched(rel)
file = sched_parser.get_csv_by_rel(csv_dir)
sched_dict = sched_parser.generate_dict(file, ['validation', 'regression', 'testcomplete'])    
if not sched_dict:
    print("no dictionary was generated - check if the csv file exists")
    sys.exit(0)

hist_log_path = os.path.join(data_folder, rel + '_auto_hist.log')

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

if not os.path.exists(hist_log_path):
    with open(hist_log_path, 'w') as hist_log:
        hist_log.write("[install]\npackage = \nrelease = \n\n[schedule]\nnext_day = 2\nlast_run =\n")

#******************************************************************************************************

#******************************************************************************************************
# added -6 hours offset to handle invocations that happen after 12 am
base_day = datetime.datetime.today() + datetime.timedelta(hours = -6) if date_to_run is None or date_to_run == '' else datetime.datetime.strptime(date_to_run, '%Y-%m-%d')
today = base_day.strftime('%Y-%m-%d')
print(today)
today_day = base_day.strftime('%A').lower()
#******************************************************************************************************

day_in_cycle = 1    
update = False
rerun = True if run_mode == "2" else False
parser = ConfigParser()
parser.read(hist_log_path)
config_package = parser["install"]["package"]
is_new_hist = False

# new package or new schedule (new testing cycle) - reset history and JSON
if config_package != pkg:
    parser["install"]["package"] = pkg
    parser["install"]["release"] = rel
    parser["schedule"]["next_day"] = '1'
    parser["schedule"]["last_run"] = ''
    with open(hist_log_path, 'w') as configfile:
        parser.write(configfile)
    with open(os.path.join(data_folder, rel + '.json'), 'w') as dict_writer:
        json.dump(sched_dict, dict_writer)
        
if run_mode in ['1', '2']: 
    # 1 means regular scheduled run, can be called multiple times a day (multiple configs)
    # 2 means a rerun of all the plans for this config for today - also checking if last run is today in case of user input error or history is incorrectly modified 
    if parser["schedule"]["last_run"] is None or parser["schedule"]["last_run"] < today: #only update next_day when last_run is before today
        day_in_cycle = int(parser["schedule"]["next_day"]) # No error handling so that automation will not run if next_day throws format exception
        parser["schedule"]["next_day"] = str(day_in_cycle + 1)
        parser["schedule"]["last_run"] = today
        is_new_hist = True
    else:
        day_in_cycle = int(parser["schedule"]["next_day"]) - 1 # No error handling so that automation will not run if next_day throws format exception  

# No error handling so that in case of failure, automation will not be run
if is_new_hist:
    with open(hist_log_path, 'w') as configfile:
        parser.write(configfile)

# Find out week number of year. Sunday is treated as last day of week by strftime("%V"). Add 1 to week number if Sunday.
#week_number = int(base_day.strftime("%V")) if int(base_day.strftime("%w")) > 0 else int(base_day.strftime("%V")) + 1
#week = 'even' if week_number % 2 != 0 else 'odd'

first_day = datetime.datetime(2021, 1, 3)
day_diff = (base_day - first_day).days + 1
week_number = math.ceil(day_diff/7)
week = 'even' if week_number % 2 == 0 else 'odd'
if day_diff < 0:
    week = 'even' if week_number % 2 != 0 else 'odd'


run_mode_str = ""
if run_mode == '1':
    run_mode_str = "regular scheduled run" 
elif run_mode == '2':
    run_mode_str = "rerun"
else:
    run_mode_str = 'other'
    
print("run mode is {}".format(run_mode_str))
print(str(day_in_cycle) + " days into the testing cycle")
print("This week is " + week) 

run = Run(prod, rel, pkg, conf, week = week, day = today_day) 
controller = Run_Controller(run, data_folder, update=update, rerun=rerun)
sched = controller.get_sched_json()
plans = controller.get_plan_list_from_json(sched)
print("The following plans will be run ")
print(plans)
controller.set_plan_list(plans)
controller.clear_bat()
controller.set_wgets()
controller.update_hist(sched)
controller.update_json_file(sched)
print('\n')
    
