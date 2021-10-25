'''
Created on Jul 26, 2019

@author: ml12793

@description: CICD-111: create methods to update case level attributes 
'''

try:
    from testrail import testrail
except ImportError:
    import testrail
    
from configparser import ConfigParser
import sys
import traceback
import os
import mysql.connector as mysql
import json

class TR_DAO(object):
    
    def __init__(self):
        parser = ConfigParser()
        parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
        section = 'testrail'
        self.client = testrail.APIClient(parser[section]['tr_link'])
        self.client.user = parser[section]['tr_uid']
        self.client.password = parser[section]['tr_pwd']
        self.db_host = parser[section]['db_host']
        self.db_user = parser[section]['db_user']
        self.db_passwd = parser[section]['db_passwd']
        self.db_name = parser[section]['db_name']

    @staticmethod    
    def retrieve_id(s):
        if type(s) == int:
            return str(s)
        if type(s) == str:
            return s.strip()[1:]
        
    @staticmethod
    def raise_api_error(call, err):
        raise testrail.APIError('{0} API error: {1}'.format(call, err))
        
    @staticmethod
    def print_error(call):
        print('Unexpected {0} error: '.format(call))
        print(*traceback.format_exception(*sys.exc_info()))
        
    def get_case(self, case_id):
        '''return case detail json'''
        call = 'get_case/' + TR_DAO.retrieve_id(case_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_case', e)
        except:
            TR_DAO.print_error(call)
            raise 
    
    def get_plan(self, plan_id):
        '''return plan detail json'''
        call = 'get_plan/' + TR_DAO.retrieve_id(plan_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_plan', e)
        except:
            TR_DAO.print_error(call)
            raise 
        
    def get_run(self, run_id):
        '''return run detail json'''
        call = 'get_run/' + TR_DAO.retrieve_id(run_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_run', e)
        except:
            TR_DAO.print_error(call)
            raise     
        
    def get_suite(self, suite_id):
        '''return suite detail json'''
        call = 'get_suite/' + TR_DAO.retrieve_id(suite_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_suite', e)
        except:
            TR_DAO.print_error(call)
            raise 
    
    def get_tests(self, run_id):
        '''return list of cases in a run'''
        call = 'get_tests/' + TR_DAO.retrieve_id(run_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_tests', e)
        except:
            TR_DAO.print_error(call)
            raise 
        
    def get_suites(self, project_id):
        '''return list of suites in a project'''
        call = 'get_suites/' + TR_DAO.retrieve_id(project_id)
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_suites', e)
        except:
            TR_DAO.print_error(call)
            raise
        
    def get_sections(self, project_id, suite_id):
        '''return list of sections in a suite'''
        call = 'get_sections/{0}&suite_id={1}'.format(TR_DAO.retrieve_id(project_id), TR_DAO.retrieve_id(suite_id))
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_sections', e)
        except:
            TR_DAO.print_error(call)
            raise
            
    def get_cases(self, project_id, suite_id, section_id=None):
        '''return list of cases in a suite'''
        if section_id == None:
            call = 'get_cases/{0}&suite_id={1}'.format(TR_DAO.retrieve_id(project_id), TR_DAO.retrieve_id(suite_id)) 
        else:
            call = 'get_cases/{0}&suite_id={1}&section_id={2}'.format(TR_DAO.retrieve_id(project_id), TR_DAO.retrieve_id(suite_id), TR_DAO.retrieve_id(section_id))
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_cases', e)
        except:
            TR_DAO.print_error(call)
            raise 

    def get_case_fields(self):
        '''return list of case level attributes'''
        call = 'get_case_fields'
        try:
            return self.client.send_get(call)
        except testrail.APIError as e:
            TR_DAO.raise_api_error('get_case_fields', e)
        except:
            TR_DAO.print_error(call)
            raise 
        
    def get_case_field_options_dict(self, field_label):
        '''return field system name, dict of case field options
           sample call: get_case_field_options_dict(self, 'Automation Type')
           sample call return: {'None': 0, 'se': 1, 'tc': 2}
        '''
        case_fields = self.get_case_fields()
        case_options = {}
        for case_field in case_fields:
            if case_field['label'] == field_label:
                field_system_name = case_field['system_name']
                try:
                    status_items = case_field['configs'][0]['options']['items'].split('\n')
                except KeyError:
                    return field_system_name, None
                if '' in status_items:
                    status_items.remove('')
                for status_item in status_items:
                    case_options[status_item.split(',')[1].strip()] = int(status_item.split(',')[0].strip())
        return field_system_name, case_options
    
    def get_cases_for_plan(self, plan_id):
        '''return dict of run cases in a plan'''
        plan_entries = self.get_plan(plan_id)['entries']
        runs = [entry['runs'][0]['id'] for entry in plan_entries]
        plan_cases = {}
        for run in runs:
            run_tests = self.get_tests(run)
            run_cases = [run_test['case_id'] for run_test in run_tests]
            plan_cases['R' + str(run)] = run_cases
        return plan_cases  
    
    def get_section_cases_for_plan(self, plan_id):
        '''return dict of section cases in a plan
        Sample return:{ 'P400':
                            {
                            'S10995': {'G193418': [2512008], 'G193420': [2512078, 2512079, 2512082, 2512088, 2512089], 'G433141': []},
                            'S19631': {'G491027': [5824592]}, 
                            'S19632': {'G491031': [6272964, 6272965]}
                            }
                        }
        '''
        plan_entries = self.get_plan(plan_id)['entries']
        runs = [entry['runs'][0] for entry in plan_entries]
        section_cases_for_plan = {}
        section_cases_for_runs = {}
        for run in runs:
            project_id = run['project_id']
            suite_id = run['suite_id']
            section_cases_for_run = self.get_section_cases_for_run(run['id'])
            section_cases_for_runs['S' + str(suite_id)] = section_cases_for_run['S' + str(suite_id)]
        section_cases_for_plan['P' + str(project_id)] = section_cases_for_runs
        return section_cases_for_plan
    
    def get_section_cases_for_run(self, run_id):
        ''''return dict of section cases in a run
        Sample return:{'S10995': 
                            {'G193418': [2512008], 'G193420': [2512078, 2512079, 2512082, 2512088, 2512089], 'G433141': []}
                        }
        '''
        run_tests = self.get_tests(run_id)
        run_cases = [run_test['case_id'] for run_test in run_tests]
        run = self.get_run(run_id)
        project_id = run['project_id']
        suite_id = run['suite_id']
        suite_sections = self.get_sections(project_id, suite_id)
        section_cases_for_run = {}
        subsection_cases = {}
        for suite_section in suite_sections:
            section_id = suite_section['id']
            section_cases = self.get_cases(project_id, suite_id, section_id)
            suite_section_cases = [section_case['id'] for section_case in section_cases if section_case['id'] in run_cases]
            subsection_cases['G' + str(section_id)] = suite_section_cases
        section_cases_for_run['S' + str(suite_id)] = subsection_cases
        return section_cases_for_run
                   
    def get_cases_for_suite(self, suite_id, project_id=None, field_dict=None):
        '''return dict of cases of suites in a suite
        field_dict example: 
        {
        'Automation Status': 'Automated',
        'Automation Type': 'se'     
        }
        '''        
        field_system_dict = {}
        if field_dict != None:
            for key in field_dict.keys():
                field_system_name, case_options = self.get_case_field_options_dict(key)
                field_system_dict[field_system_name] = case_options[field_dict[key]]
        suite = self.get_suite(suite_id)
        if project_id == None:
            project_id = suite['project_id']
        suite_cases = self.get_cases(project_id, suite_id)
        cases = []
        for suite_case in suite_cases:
            filter = []
            for key in field_system_dict.keys():
                filter.append(suite_case[key] == field_system_dict[key])
            if all(filter):
                cases.append(suite_case['id'])
        return cases
 
    def get_cases_for_project(self, project_id, field_dict=None):
        '''return dict of cases of suites in a project
        field_dict example: 
        {
        'Automation Status': 'Automated',
        'Automation Type': 'se'     
        }
        '''
        project_suites = self.get_suites(project_id)          
        suites = [project_suite['id'] for project_suite in project_suites]
        project_cases = {}
        for suite in suites:
            cases = self.get_cases_for_suite(suite, project_id, field_dict)
            project_cases['S' + str(suite)] = cases
        return project_cases
        
    def update_plan_entry(self, plan_id, entry_id, data_dict):
        '''function to update test plan entry
        data_dict example:
        {
        'case_ids': [123456, 234567, 345678]
        }
        '''
        call = 'update_plan_entry/{0}/{1}'.format(TR_DAO.retrieve_id(plan_id), entry_id)
        try:
            self.client.send_post(call, data_dict)
            print('Plan entry {0} was updated successfully.'.format(entry_id))
        except testrail.APIError as e:
            TR_DAO.raise_api_error('update_plan_entry', e)
        except:
            TR_DAO.print_error(call)
            raise        
 
    def refresh_plan(self, plan_id, field_dict):
        '''refresh existing plan based on case attribute values
        field_dict example:
        {
        'Automation Status': 'Automated',
        'Automation Type': 'se'
        }
        
        Note: in order to use this function, please do not use "include all" to select cases for test runs
        '''   
        plan = self.get_plan(plan_id)
        project_id = plan['project_id']
        plan_entries = plan['entries']   
        for plan_entry in plan_entries:
            entry_id = plan_entry['id']
            suite_id = plan_entry['suite_id']
            cases = self.get_cases_for_suite(suite_id, project_id, field_dict)
            data_dict = {}
            data_dict['case_ids'] = cases
            self.update_plan_entry(plan_id, entry_id, data_dict)   
                                  
    def update_case(self, case_id, data_dict):
        '''
        function to update test case attribute(s)
        supported data_dict keys:   Automation Status
                                    Automation Type
                                    Comment
                                    Description
                                    Preconditions
                                    Release Begin
                                    Release End
        data_dict example: 
        {
        'Automation Status': 'Automated',
        'Automation Type': 'se',
        'Comment': 'Dummy Comment',
        'Description': 'Dummy Description', 
        'Preconditions': 'Dummy Preconditions',
        'Release Begin': '8201',
        'Release End': '8205.08',      
        }
        '''
        case_fields = self.get_case_fields()
        case_field_label_set = set([field['label'] for field in case_fields])
        to_update_case_field_label_set = set(data_dict.keys())
        to_update_case_field_label_set.difference_update(case_field_label_set)
        if(len(to_update_case_field_label_set)) != 0:
            raise KeyError('Please check following data_dict keys: {}'.format(', '.join(to_update_case_field_label_set)))  
        mapped_data_dict = {}
        for key in data_dict.keys():
            field_system_name, field_option_dict = self.get_case_field_options_dict(key)
            if field_option_dict != None:
                try:
                    mapped_data_dict[field_system_name] = field_option_dict[data_dict[key]]
                except KeyError:
                    raise ValueError('Please check the value of {}.'.format(key))
            else:
                mapped_data_dict[field_system_name] = data_dict[key]
        #check if the values of case attributes to update are the same as current ones
        case_dict = self.get_case(case_id)
        compare = []
        for key in mapped_data_dict.keys():
            compare.append(mapped_data_dict[key] == case_dict[key])
        if all(compare):
            print('The values of case attributes to update are the same as current ones, no case update call was made for C{}.'.format(case_id))
        else:
            call = 'update_case/' + TR_DAO.retrieve_id(case_id)
            try:
                self.client.send_post(call, mapped_data_dict)
                print('Test case C{0} was updated successfully.'.format(case_id))
            except testrail.APIError as e:
                TR_DAO.raise_api_error('update_case', e)
            except:
                TR_DAO.print_error(call)
                raise

#*******************************Database queries***********************            
    def get_project_id_by_plan_id(self, plan_id):
        query = "select project_id from runs where plan_id = {plan_id}".format(plan_id = str(plan_id).strip())
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return str(result_set[0][0])
        else:
            return None  
        
    def get_run_id_by_plan_id(self, plan_id):
        query = "select id from runs where plan_id = {plan_id} and is_plan = 'false'".format(plan_id = plan_id)
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return self.detuple_list(result_set)
        else:
            return []        
        
    def get_suite_id_by_plan_id(self, plan_id):
        query = "select suite_id from runs where plan_id = {plan_id}".format(plan_id = plan_id)
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return self.detuple_list(result_set)
        else:
            return []    
          
    def get_run_id_by_plan_suite(self, plan_id, suite_id):
        query = "select id from runs where plan_id = {plan_id} and suite_id = {suite_id}".format(plan_id = str(plan_id).strip(), suite_id = str(suite_id).strip())
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return str(result_set[0][0])
        else:
            return None          

    def get_status_id_by_label(self, status_labels):
        status_label_string = "\'{status_labels}\'".format(status_labels = status_labels.strip())

        if ',' in status_labels:
            status_label_string = ','.join(["\'{}\'".format(label.strip()) for label in status_labels.split(',')])

        query = "select id, label from statuses where label in ({status_labels}) and is_active = true".format(status_labels = status_label_string)
        
        if status_labels == 'None':
            query = "select id, label from statuses"
        
        result_set = self.exec_sql_select_query(query)

        if len(result_set) > 0:
            return self.format_list(result_set)
        else:
            return []        

    def get_test_status_for_case(self, case_id, run_id):
        query = "select statuses.name from tests join statuses on tests.status_id = statuses.id where tests.case_id = {case_id} and tests.run_id = {run_id}".format(case_id = str(case_id).strip(), run_id = str(run_id).strip())
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return str(result_set[0][0])
        else:
            return None

    def get_section_run_cases(self, section_id, run_id, **field_dict):
        '''Get cases belonging to runs and sections. Extra arguments can be passed in as key-value pairs. Returns a list of id, name dictionaries.
        When a single section_id is passed in (how suite_runner4.py calls this method), results are sorted by display_order (the order in which cases appear in a specific section in TR GUI)
        But when multiple section_ids are passed in (there hasn't been such a case), sort order defaults back to case_id.
        '''
        
        table1 = "cases"
        table2 = "tests"
        db_column_group = []
        db_column_group.append(self.get_table_columns(table1))
        db_column_group.append(self.get_table_columns(table2))
        
        for key in field_dict.keys():
            table_name = str(key).split('_', 1)[0].strip()
            table_num = 1
            try:
                table_num = [table1, table2].index(table_name)
            except ValueError:
                raise ValueError("table {table} is not cases or runs".format(table = table_name))
             
            column_name = str(key).split('_', 1)[1].strip()
            if column_name not in db_column_group[table_num]:
                raise  ValueError("Column {col} does not exist in table {table}".format(col = column_name, table = table_name))
         
        query = "select cases.id, cases.title from cases join tests on cases.id = tests.case_id where cases.section_id in ({section_id}) and tests.run_id in ({run_id}) and tests.is_selected = true".format(section_id = section_id.strip(), run_id = run_id.strip())
         
        if len(field_dict) > 0:   
            where_clause = " and " + " and ".join([str(key).split('_', 1)[1].strip() + " in (" + str(value).strip() + ")" for key, value in field_dict.items()])
            query += where_clause
            
        # when there's only one section id, sort by display_order to match TR GUI case order     
        if section_id.isdigit():
            query += " order by cases.display_order"   
  
        result_set = self.exec_sql_select_query(query)

        if len(result_set) > 0:
            return self.format_list(result_set)
        else:
            return []           
    
    def get_section_cases(self, section_id, **field_dict):
        '''Get cases belonging sections. Extra arguments can be passed in as key-value pairs. Returns a list of id, name dictionaries.'''
        table_name = 'cases'
        db_cols = self.get_table_columns(table_name)
        for column_name in field_dict.keys():
            if column_name not in db_cols:
                raise ValueError("Column {col} does not exist in table {table}".format(col = column_name, table = table_name))
        
        query = "select id, title from cases where section_id in ({section_id})".format(section_id = section_id) 
        
        if len(field_dict) > 0:   
            where_clause = " and " + " and ".join([str(key).strip() + " in (" + str(value).strip() + ")" for key, value in field_dict.items()])
            query += where_clause
          
        result_set = self.exec_sql_select_query(query)

        if len(result_set) > 0:
            return self.format_list(result_set)
        else:
            return []        
     
    def get_table_columns(self, table_name):
        '''Returns a list of column names of a given table'''
        query = "select column_name from information_schema.columns where table_schema = 'testrail' and table_name = '{table_name}'".format(table_name = str(table_name).strip())
        result_set = self.exec_sql_select_query(query)
        
        if len(result_set) > 0:
            return self.detuple_list(result_set)
        else:
            return []
        
    def get_project_attr(self, project_id, attrs):
        '''attrs: comma separated attributes string, example: 'name, is_completed' '''
        return self.get_psgc_attr('project', project_id, attrs)
    
    def get_suite_attr(self, suite_id, attrs):
        '''attrs: comma separated attributes string, example: 'name, peoject_id' '''
        return self.get_psgc_attr('suite', suite_id, attrs)
    
    def get_group_attr(self, group_id, attrs):
        '''attrs: comma separated attributes string, example: 'name, suite_id' '''
        return self.get_psgc_attr('group', group_id, attrs)
    
    def get_case_attr(self, case_id, attrs):
        '''attrs: comma separated attributes string, example: 'title, custom_automation_type' '''
        return self.get_psgc_attr('case', case_id, attrs)
    
    def get_psgc_attr(self, psg, psg_id, attrs):
        if psg.strip() == 'group':
            table_name = 'sections'
        else:
            table_name = psg.strip() + 's'
        db_cols = self.get_table_columns(table_name)
        attr_lst = [attr.strip() for attr in attrs.split(',')]
        for attr in attr_lst:
            if attr not in db_cols:
                raise ValueError("Column {} does not exist in table {}".format(attr, table_name))
        query = 'select {} from {} where id = {}'.format(attrs, table_name, TR_DAO.retrieve_id(psg_id)) 
        result_set = self.exec_sql_select_query(query)
        attr_dict = dict(zip(attr_lst, result_set[0]))
        #retrieve name for nested group
        if psg.strip() == 'group' and 'name' in attr_lst:
            group_name = ''
            group_id = TR_DAO.retrieve_id(psg_id)
            while True:
                query = 'select name, parent_id from sections where id = {}'.format(group_id)
                result_set = self.exec_sql_select_query(query)
                group_name = result_set[0][0] + '->' + group_name
                if result_set[0][1] != None:
                    group_id = result_set[0][1]
                else:
                    break
            attr_dict['name'] = group_name[:-2]
        return attr_dict
    
    def get_case_field(self, case_field_label):  
        return self.get_field('case', case_field_label)
    
    def get_result_field(self, result_field_label):
        return self.get_field('result', result_field_label)
        
    def get_field(self, field_type, field_label):
        if field_type == 'case':
            entity_id = 1
        elif field_type == 'result':
            entity_id = 2
        else:
            raise ValueError('{} is not a valid field type.'.format(field_type))
        query = 'select label from fields'
        result_set = self.exec_sql_select_query(query)
        field_label_list = self.detuple_list(result_set)
        if field_label.strip() not in field_label_list:
            raise ValueError('{} is not a valie field label.'.format(field_label))
        query = 'select configs from fields where entity_id = {} and is_system = False and label = \'{}\''.format(entity_id, field_label.strip())
        result_set = self.exec_sql_select_query(query)
        field_dict = {}
        field_options = json.loads(result_set[0][0])[0]['options']
        try:
            field_option_items = field_options['items']
        except KeyError:
            return field_dict
        field_option_items_lst = field_option_items.split('\n')
        if '' in field_option_items_lst:
            field_option_items_lst.remove('')
        for field_option_item in field_option_items_lst:
            item_value, item_key = field_option_item.split(',')
            field_dict[item_key.strip()] = item_value.strip()
        return field_dict
     
    def get_sql_connection(self):
        db_conn = None        
        try:
            db_conn = mysql.connect(
                host = self.db_host,
                user = self.db_user,
                passwd = self.db_passwd,
                database = self.db_name
                )
        except Exception as e:
            print("db connection error")
            print(str(e))
        
        return db_conn
    
    def exec_sql_select_query(self, query): 
        db_conn = self.get_sql_connection()
        records = []
        if db_conn is not None:
            cursor = db_conn.cursor()
            try:
                cursor.execute(query)
                records = cursor.fetchall()
            except Exception as e:
                print(str(e))
            db_conn.close()
        
        return records
    
    def detuple_list(self, result_list):
        return [result[0] for result in result_list]

    def format_list(self, result_list):
        dict_list = []
        for result in result_list:
            id_name_dict = {}
            id_name_dict['id'] = str(result[0])
            id_name_dict['name'] = str(result[1])
            dict_list.append(id_name_dict)
        return dict_list
            
if __name__ == '__main__':
    tr = TR_DAO()
    plan_id = '96723'
#     project_id = tr.get_project_id_by_plan_id(plan_id)
#     print(project_id)
#     suite_ids = tr.get_suite_id_by_plan_id(plan_id)
#     print(suite_ids)
#     run_ids = tr.get_run_id_by_plan_id(plan_id)
#     print(run_ids)
#     status = tr.get_test_status_for_case('2272909', '92811')
#     print(status)
#     cases = tr.get_section_cases('163887, 157809')
#     print(cases)
#     cases = tr.get_section_cases(section_id='157809, 163887', custom_automation_status='3,4')
#     print(cases)
    cases = tr.get_section_run_cases('169813', '97147')
    print(cases)
    cases = tr.get_section_run_cases('157809', '92811', tests_status_id='1,2', tests_case_id='2272874,2272877')
    print(cases)
    cases = tr.get_section_run_cases('169813', '97147', tests_status_id='4')
    print(cases)
#     run_id = tr.get_run_id_by_plan_suite('92810', '10050')
#     print(run_id)
#     status_ids = tr.get_status_id_by_label('Passed, Failed, Retest')
#     print(status_ids)
#     status_ids = tr.get_status_id_by_label('None')
#     print(status_ids)
#     print(','.join([status['id'] for status in status_ids]))
#     cols = tr.get_table_columns('runs')
#     print(cols)
#     print(tr.get_project_attr(400, 'name, is_completed'))
#     print(tr.get_suite_attr(10995, 'name, project_id'))
#     print(tr.get_group_attr(731125, 'name, suite_id'))
#     print(tr.get_case_attr(2235439, 'title'))
#     automation_status_dict = tr.get_case_field('Automation Status ')
#     print(automation_status_dict)
#     print(automation_status_dict['Automated'])
#     print(tr.get_case_field('Comment'))
#     print(tr.get_result_field('Configurations'))
#     print(tr.get_result_field('Release'))
#     print(tr.get_result_field('Prodid'))
#     print(tr.get_result_field('Browsers'))
#     print(tr.get_result_field('Run Mode'))
#     print(tr.get_case(2512091))
#     print(tr.get_tests(91766))
#     print(tr.get_tests('R91766'))
#     print(tr.get_suites(400))
#     print(tr.get_suites('P400'))
#     print(tr.get_plan(76476))
#     print(tr.get_plan('R76476'))
#    print(tr.get_run(93290))
#    print(tr.get_cases_for_plan(91765))
#     print(tr.get_cases_for_plan('R91765'))     
#    print(tr.get_cases(400, 10995))
#     print(tr.get_cases('P400', 'S10995'))
#     print(tr.get_case_fields())  
#     print(tr.get_sections(400, 10995))
#     print(tr.get_cases_for_plan(93289))
#     print(tr.get_section_cases_for_run(97147))
#     print(tr.get_section_cases_for_plan(93289))
#    print(tr.get_cases_for_project('P400', {'Automation Type': 'se', 'Automation Status': 'Automated'}))
#    print(tr.get_cases_for_project('P400', {'Automation Status': 'Automated'}))
#     print(tr.get_cases_for_project('P400'))
#     print(tr.get_case_field_options_dict('Release End'))
#     tr.update_case(2512091,{
#                             'Automation Status11': 'Ready for automation',
#                             'Automation Type': 'tc',
#                             'Comment': 'Dummy Comment',
#                             'Description': 'Dummy Description', 
#                             'Preconditions': 'Dummy Preconditions',
#                             'Release Begin11': '8205',
#                             'Release End11': '8207',  
#                             })
#     tr.update_case('C2241290',{
#                             'Automation Status': 'Automated',
#                             'Automation Type': 'se',
#                             'Comment': 'Dummy Comment',
#                             'Description': 'Dummy Description', 
#                             'Preconditions': 'Dummy Preconditions',
#                             'Release Begin': '8203',
#                             'Release End': '8207',  
#                             })
#     tr.refresh_plan(93289, {'Automation Status': 'Ready for automation', 'Automation Type': 'se'})
#     tr.refresh_plan(93289, {'Automation Status': 'Comment'})