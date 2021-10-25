#import testrail as tr
from testrail import testrail as tr
import time, os
from configparser import ConfigParser

MIN_SLEEP_TIME=300
MIN_LOOP_COUNT=20
QUERY_INTERRUPTED = "Query execution was interrupted"
        
class Tr_Exception_Check(object):
    
    '''
    Constructor function
    '''
    def __init__(self,sleep_time=MIN_SLEEP_TIME,upper_limit=MIN_LOOP_COUNT,config_file='config.ini'):
        '''
        Private variables
        '''
        self.__current_file_path=os.path.abspath(os.path.dirname(__file__))  # read current file (tr_exception_check.py) path
        if sleep_time>=MIN_SLEEP_TIME:
            self.__sleep_time=sleep_time
        else :
            raise ValueError("Sleep time should be more than "+MIN_SLEEP_TIME+" seconds.")
    
        if upper_limit>=MIN_LOOP_COUNT:
            self.__upper_limit=upper_limit
        else :
            raise ValueError("Upper limit should be more than "+MIN_LOOP_COUNT) 
        self.__tr_link=None
        self.__tr_user=None
        self.__tr_password=None
        self.__config_file=config_file
        self.__read_tr_client_properties()
        
    '''
        Private method
    '''
    def __read_tr_client_properties(self):
        
        '''
        Description : Read tr client properties from config.ini file
        '''
        section='testrail'
        config_file_path=os.path.join(self.__current_file_path,self.__config_file) # Join path
        if os.path.exists(config_file_path) :
            parser=ConfigParser()
            parser.read(config_file_path)
            self.__tr_link=parser[section]['tr_link']
            self.__tr_user=parser[section]['tr_uid']
            self.__tr_password=parser[section]['tr_pwd']
        else :
            raise ResourceWarning("The given config file path not exists in file system [" + config_file_path + "].")
        tr_client = tr.APIClient(self.__tr_link)
        tr_client.user =self.__tr_user
        tr_client.password=self.__tr_password
        self.tr_client = tr_client
    '''
        Private method
    '''
    def __check_tr_client_exception(self):
        count=0
        no_reponse_yet=True
        while no_reponse_yet and count< self.__upper_limit:
            try:
                tr_result_fields=self.tr_client.send_get('get_result_fields')
                no_reponse_yet=False
                break
            except tr.APIError:
                time.sleep(self.__sleep_time)
                count=count+1
                print('Sleep iteration : ',count)
        msg = "End Test Rail wait:" + " sleep iterations completed: " + str(count) + " out of maximum iterations: " + str(self.__upper_limit);
        if (no_reponse_yet == True):
            msg += "\nWarning: testrail has failed to return. Further tests are not guaranteed to be processed.";
            raise ConnectionError(msg)
        print(msg)
    '''
    Public method
    '''  
    def testrail_get(self, cmd):
        response_from_testrail = None
        try:
            response_from_testrail=self.tr_client.send_get(cmd)
        except tr.APIError as e:            
            self.__check_tr_client_exception()
            # two chances at sleep only, after that, fail
            # testrail.APIError: TestRail API returned HTTP 500 ("Query execution was interrupted")
            try:
                response_from_testrail=self.tr_client.send_get(cmd)
            except tr.APIError as e2:
                error_msg = str(e2)
                if QUERY_INTERRUPTED in error_msg:
                    self.__check_tr_client_exception()
                    response_from_testrail=self.tr_client.send_get(cmd)
                else:
                    raise e
        return(response_from_testrail)

    def testrail_post(self, cmd, data_dictionary):
        response_from_testrail = None
        print('cmd : ',cmd)
        print('data_dictionary : ',data_dictionary)
        try:
            response_from_testrail=self.tr_client.send_post(cmd, data_dictionary)
        except tr.APIError as e:
            self.__check_tr_client_exception()
            # two chances at sleep only, after that, fail
            # testrail.APIError: TestRail API returned HTTP 500 ("Query execution was interrupted")
            try:
                response_from_testrail=self.tr_client.send_post(cmd, data_dictionary)
            except tr.APIError as e2:
                error_msg = str(e2)
                if QUERY_INTERRUPTED in error_msg:
                    self.__check_tr_client_exception()
                    response_from_testrail=self.tr_client.send_post(cmd, data_dictionary)
                else:
                    raise e2   
        return(response_from_testrail)
        
    def start_tr_exception_check_process(self):
        self.__check_tr_client_exception()

Tr_Exception_Check().start_tr_exception_check_process()
