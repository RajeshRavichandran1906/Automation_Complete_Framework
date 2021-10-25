'''
Created on Sept 12, 2019

@author: ml12793

'''   
from configparser import ConfigParser
import os
import psycopg2

class RES_DAO(object):
    
    def __init__(self):
        parser = ConfigParser()
        parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
        section = 'caserun'
        self.db_host = parser[section]['db_host']
        self.db_user = parser[section]['db_user']
        self.db_passwd = parser[section]['db_passwd']
        self.db_name = parser[section]['db_name']
        
    def get_known_cases(self, release_id, conf_id, browser):
        '''return list of known issue test case id, comment, ticket and latest pkgname dictionary for certain release, config and browser'''
        query = '''
                    select distinct(case_id), comment, ticket_id, max(pkgname) over(partition by case_id) from caserun  
                    left join runticket on caserun.caserun_id = runticket.caserun_id 
                    join install on caserun.instid = install.instid 
                    join package on install.pkgid = package.pkgid 
                    where status = 'known' and relid = '{}' and confid = '{}' and browser_id = '{}' 
                ''' .format(release_id.strip(), conf_id.strip(), browser.strip())
        result_set = self.exec_sql_select_query(query)
        keys = ['id', 'comment', 'ticket', 'pkgname_latest']        
        return [dict(zip(keys, case)) for case in result_set]
    
    def is_known(self, release_id, conf_id, browser, case_id):
        '''return type: boolean,
           if case is found and is known: return True
           if case is found and is not known: return False
           if case is not found: return False
        '''
        query = '''
                    select status from caserun 
                    join install on caserun.instid = install.instid
                    join package on install.pkgid = package.pkgid
                    where relid = '{}' and confid = '{}' and browser_id = '{}' and case_id = 'C{}'
                    order by pkgname desc
                    limit 1
                '''.format(release_id.strip(), conf_id.strip(), browser.strip(), case_id.strip())
        result_set = self.exec_sql_select_query(query)
        if len(result_set) == 0:
            return False
        return 'known' == result_set[0][0]
    
    def get_known_case_info(self, release_id, conf_id, browser, case_id):
        '''return known issue test case id, comment, ticket and latest pkgname dictionary for certain release, config and browser'''
        if self.is_known(release_id, conf_id, browser, case_id):
            query = '''
                    select distinct(case_id), comment, ticket_id, max(pkgname) over(partition by case_id) from caserun  
                    left join runticket on caserun.caserun_id = runticket.caserun_id 
                    join install on caserun.instid = install.instid 
                    join package on install.pkgid = package.pkgid 
                    where status = 'known' and relid = '{}' and confid = '{}' and browser_id = '{}' and case_id = 'C{}'
                    '''.format(release_id.strip(), conf_id.strip(), browser.strip(), case_id.strip())
            result_set = self.exec_sql_select_query(query)
            keys = ['id', 'comment', 'ticket', 'pkgname_latest'] 
            return dict(zip(keys, result_set[0]))
        return None
            
    def get_sql_connection(self):
        db_conn = None        
        try:
            db_conn = psycopg2.connect(
                host = self.db_host,
                user = self.db_user,
                password = self.db_passwd,
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
            
if __name__ == '__main__':
    res = RES_DAO()
#     print(res.get_known_cases('82xx', '698', 'CR'))
#     print(res.get_known_cases('head_git', '784', 'CR'))
    print(res.is_known('head_git', '784', 'CR', '2511590'))
    print(res.get_known_case_info('head_git', '784', 'CR', '2511590'))