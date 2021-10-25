'''
Author: Lawrence Yu
Date: 7/22/19
Description: Post a new test result to TestRail for a case in a run and associate it with the user posting it. This can be to update statuses, comments, and/or tickets (Jira).
How to use: Sample input from a command line:
python add_new_test_result.py case_id=C2512010 browser_id=cR prodid=wf relid=8206 pkgname=wf072219a confid=698 run_id=R63124 user=Lawrence_Yu status=failed
Dependencies: tr_users_exception_check.py, config.ini, testrail.py
'''

import sys
import re
import pickle
import time
import json
import shutil
from configparser import ConfigParser
import requests
import subprocess
import os

#arg_dict = {'browser_id': 'CR', 'case_id': 'C2228180', 'confid': '873', 'pkgname': 'wf080119a', 'prodid': 'wf', 'relid': '82xx', 'run_id': 'R93613', 'status': 'fail', 'user': 'Lawrence_Yu@ibi.com'}
SUCCESS = "SUCCESS"
FAIL = "FAIL:"
EXIT_MESSAGE = "Exiting program."

if sys.platform == 'linux':
    tr_data_dir = "/bigshare/tr_data/temp"
    base_tr_dir = None
    testrail_config_path = "/usr/local/share_data/config.ini"
else:
    tr_data_dir = "\\\\bigscmstr\\bigshare\\tr_data\\temp"
    base_tr_dir = "\\\\jarunner002\\C$"
    testrail_config_path = base_tr_dir + "\\Users\\qaauto\\data\\config.ini"

def getFieldsDictionary( fields_str ) :
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
    
class Add_New_Test_Result:
    
    def __init__(self):
        missing = ""
        if 'browser_id' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'browser_id')
        if 'prodid' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'prodid')
        if 'relid' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'relid')
        if 'pkgname' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'pkgname')
        if 'confid' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'confid')
        if 'run_id' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'run_id')
        if 'user' not in arg_dict.keys():
            missing = Add_New_Test_Result._comma_delimited_list(missing, 'user')
        if missing != "":
            print(FAIL, "Missing required parameter(s):", missing + ".")
            sys.exit(0)
        if 'status' not in arg_dict.keys():
            #!(C || T) = neither remaining option were found
            if not ('user_comment' in arg_dict.keys() or 'ticket' in arg_dict.keys()):
                print(FAIL, "Missing a field to edit (at least one of: status, user_comment, or ticket).")
                sys.exit(0)
            #!C && T = normally invalid but we will post a default comment to allow it
            if ('user_comment' not in arg_dict.keys()) and ('ticket' in arg_dict.keys()):
                arg_dict['user_comment'] = 'Jira ticket(s): ' + arg_dict['ticket']
        if 'user_comment' in arg_dict.keys():
            arg_dict['user_comment'] = arg_dict['user_comment'].strip("'")
            arg_dict['user_comment'] = arg_dict['user_comment'].strip('"')
        gid = 'qaauto'
        gpwd = os.environ.get(gid)
        Add_New_Test_Result.check_tr_api_key(arg_dict['user'].lower(), gid, gpwd, base_tr_dir)
        Add_New_Test_Result.check_config_parameters(arg_dict['prodid'], arg_dict['relid'], arg_dict['pkgname'], arg_dict['confid'])
        self.get_tr_fields()
        self.test_tool_name = 'manual'
        
    @staticmethod
    def check_tr_api_key(user, gid, gpwd, dir_path=None):
        if dir_path != None:
            try:
                winCMD = 'NET USE ' + dir_path + ' /User:' + gid + ' ' + gpwd
                subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)
            except:
                print(FAIL, "Unable to access TestRail configuration directory.")
                sys.exit(0)
            
        config = ConfigParser()
        config.read(testrail_config_path)
        try:
            api_key = config['users'][user]
        except:
            print(FAIL, "TestRail API key lookup failed for user: [" + user + "].")
            sys.exit(0)
        
    @staticmethod
    def check_config_parameters(prodid, relid, pkgname, confid):
        url = 'http://bigops.ibi.com:3007/pkg_cgi/checkInstall.pl?prodid=' + prodid + '&relid=' + relid + '&pkgname=' + pkgname + '&confid=' + confid
        try:
            res = requests.get(url)
        except:
            sys.exit(0)
        if not (('CURRENT' in res.text) or ('YES' in res.text)):
            print(FAIL, 'Product, release, package, and configuration id combination does not match. ')
            sys.exit(0)
        return True
            
    @staticmethod
    def _comma_delimited_list(previous, current):
        if previous == "" or previous == None:
            compiled = current
        else: 
            compiled = previous + ',' + current
        return compiled
        
    def tr_post(self):
        run_id = Add_New_Test_Result.strip_prefix('R', arg_dict['run_id'])
        case_id = Add_New_Test_Result.strip_prefix('C', arg_dict['case_id'])
        cmd = 'add_result_for_case/' + run_id + '/' + case_id
        post_body = self.compile_post_body(run_id, case_id)
        
        ts = time.localtime()
        time_pattern = "%Y%m%d%H%M%S"
        timestamp = time.strftime(time_pattern, ts)
        file_name = 'manual_update_R' + run_id + '_C' + case_id + '_' + timestamp + '.manualresult'
        Add_New_Test_Result.write_json_to_file(file_name, post_body, tr_data_dir)
        print(SUCCESS)
        
    @staticmethod
    def write_json_to_file(file_name, data_dict, tr_data_dir):
        if bool(data_dict) == False:
            print(FAIL, "No data being moved.")
            sys.exit(0)
        with open(file_name, 'w') as file:
            file.write(json.dumps(data_dict))
        try:
            shutil.move(file_name, tr_data_dir)
        except:
            print(FAIL, 'Unable to move file [' + file_name + '] to [' + tr_data_dir + ']')
            sys.exit(0)
    
    @staticmethod
    def write_pickle_file(output_name, data):
        with open(output_name, 'wb') as fp: 
            pickle.dump(data, fp, protocol=2)
    
    @staticmethod
    def get_tr_data(tr_file):
        try:
            with open (tr_file, 'rb') as fp:
                itemlist = pickle.load(fp)
                return itemlist
        except IOError:
            print(FAIL, "Didn't find a file with the name: [" + tr_file + "]")
            sys.exit(0)
    
    def get_tr_fields(self):
        res_file_name = 'tr_result_fields'
        stat_file_name = 'tr_statuses'
        try:
            import testrail
            parser = ConfigParser()
            parser.read(testrail_config_path)
            url = parser['testrail']['tr_link']
            user = 'bigscm@ibi.com'
            pwd = parser['users'][user]
            client = testrail.APIClient(url)
            client.user = user
            client.password = pwd
            self.result_fields = client.send_get('get_result_fields')
            self.statuses = client.send_get('get_statuses')
        except:
            self.result_fields = Add_New_Test_Result.get_tr_data(res_file_name)
            self.statuses = Add_New_Test_Result.get_tr_data(stat_file_name)
            
        if self.result_fields == None or self.statuses == None:
            print(FAIL, "Could not obtain TestRail configuration data.")
            sys.exit(0)
            
    def format_browser(self):
        browser = arg_dict['browser_id'].lower() 
        if '_current' not in browser: 
            browser = browser + '_current'
        return browser
    
    def compile_post_body(self, run_id, case_id):
        post_body = {}
        result_fields_dict = self.result_fields_lookup(self.format_browser(), arg_dict['relid'], arg_dict['prodid'].lower(), arg_dict['confid'], self.test_tool_name.lower())
        post_body['run_id'] = run_id
        post_body['case_id'] = case_id
        post_body['user'] = arg_dict['user']
        post_body['custom_browsers'] = result_fields_dict['browser_key']
        post_body['custom_pkgname'] = arg_dict['pkgname']
        post_body['custom_prodid'] = result_fields_dict['product_key']
        post_body['custom_configurations'] = result_fields_dict['configuration_key']
        post_body['custom_release'] = result_fields_dict['release_key']
        post_body['custom_run_mode'] = result_fields_dict['run_mode_key']
        post_body['custom_atm_issues'] = 1
        post_body['defects'] = ""
        post_body['comment'] = ""
        post_body['status_id'] = ""
        if 'status' in arg_dict.keys():
            arg_status = arg_dict['status'].lower()
            status_mapping = {'pass': 'passed', 'fail': 'failed', 'known': 'custom_status1', 'retest': 'retest', 'blocked': 'blocked'}
            if arg_status in status_mapping.keys():
                post_body['status_id'] = self.statuses_lookup(status_mapping[arg_status])
            else:
                print(FAIL, "Unrecognized database status provided.")
                sys.exit(0)
        if 'user_comment' in arg_dict.keys():
            post_body['comment'] = arg_dict['user_comment']
        if 'ticket' in arg_dict.keys():
            post_body['defects'] = arg_dict['ticket']
        return post_body
        
    def result_fields_lookup(self, browser, release, product, confid, test_tool_name, **kwargs):
        data_dict = {}
        result_fields = self.result_fields
        for i in range(len(result_fields)):
            #print(result_fields[i]['name'])
            if result_fields[i]['name'] == 'release':
                data_dict['release_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.lower())
                if data_dict['release_key'] == None:
                    data_dict['release_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(release.upper())
            if result_fields[i]['name'] == 'prodid':  
                data_dict['product_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(product)
            if result_fields[i]['name'] == 'configurations':
                data_dict['configuration_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(confid)
            if result_fields[i]['name'] == 'browsers':
                data_dict['browser_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(browser)  
            if result_fields[i]['name'] == 'run_mode':
                data_dict['run_mode_key'] = getFieldsDictionary(result_fields[i]['configs'][0]['options']['items']).get(test_tool_name) 
        if data_dict['release_key'] is None:
            print('The requested release ' + release + ' is not currently a valid release choice in TestRail.')
            sys.exit(0)
        if data_dict['product_key'] is None:
            print('The requested product ' + product + ' is not currently a valid product choice in TestRail.')
            sys.exit(0)
        if data_dict['configuration_key'] is None:
            print('The requested configuration ' + confid + ' is not currently a valid configuration choice in TestRail.')
            sys.exit(0)
        if data_dict['browser_key'] is None:
            print('The requested browser [' + browser + '] is not currently a valid browser choice in TestRail.')
            sys.exit(0)
        if data_dict['run_mode_key'] is None:
            print('The requested run mode [' + test_tool_name + '] is not currently a valid run mode choice in TestRail.')
            sys.exit(0)
        return data_dict
    
    def statuses_lookup(self, status):
        statuses = self.statuses
        for item in statuses:
            if status == item['name']:    
                status_key = item['id']
                return status_key
        print(FAIL, "Could not find status to set.")
        sys.exit(0)
    
    @staticmethod
    def strip_prefix(prefix, value):
        if str(value)[0].lower() == prefix.lower():
            value = value[1:]
        return str(value)
        
    @staticmethod
    def add_prefix(prefix, value):
        if str(value)[0].lower() != prefix.lower():
            value = prefix.upper() + str(value)
        return value
    
if __name__ == "__main__":
    post_obj = Add_New_Test_Result()
    post_obj.tr_post()
       