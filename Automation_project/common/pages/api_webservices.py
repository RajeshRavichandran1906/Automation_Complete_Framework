import time, os, re
import keyboard
from common.lib import utillity
from common.lib.base import BasePage
import xml.etree.ElementTree as ET
from configparser import ConfigParser
from common.locators.loginpage_locators import LoginPageLocators
from selenium.webdriver.common.by import By

class API_Web_Services(BasePage):
    
    '''
    Global variables
    '''
    bitmap_value=''
    authentication_xml_string=''
    bitmap_value_xml_string=''
    
    def get_setup_url(self):
        '''
        Description : This function read setup name, port number and context from config.init file and return full ULR to invoke page 
        '''
        node = utillity.UtillityMethods.parseinitfile(self, 'nodeid')
        port = utillity.UtillityMethods.parseinitfile(self, 'httpport')
        context = utillity.UtillityMethods.parseinitfile(self, 'wfcontext')
        return('http://' + node + ':' + port + context + '/')
    
    def open_view_source(self):
        '''
        Description : It will invoke new window using Ctr+u to read XMl text 
        '''
        winow_number_before_view_source=len(self.driver.window_handles)
        keyboard.send('ctrl+u')
        count=0
        upper_limit=30
        while True:
            if count == upper_limit:
                break
            winow_number_after_view_source=len(self.driver.window_handles)
            if winow_number_after_view_source == winow_number_before_view_source+1:
                time.sleep(2)
                utillity.UtillityMethods.switch_to_window(self, 1, pause=5)
                break
            else:
                time.sleep(1)
                count += 1
        
    def get_full_xml_string(self):
        '''
        Description : Read XML text and return 
        '''
        API_Web_Services.open_view_source(self)
        full_xml_content = self.driver.find_element_by_css_selector("html body table").text.strip()
        self.driver.close()
        utillity.UtillityMethods.switch_to_window(self, 0, pause=5)
        return (full_xml_content)

    def get_authentication_xml_dict(self, section_name):
        '''
        Description : Return XMl authentication sections values as dictionary 
        section_name ='authentication_rootObject' OR 'authentication_properties' OR 'authentication_status' OR 'authentication_groups' OR 'authentication_pSetList'
        '''
        if self.authentication_xml_string != '':
            result_str=self.authentication_xml_string
        else:
            result_str = API_Web_Services.get_full_xml_string(self)
            self.authentication_xml_string = result_str
        root = ET.fromstring(result_str)
        return_dict={}
        if section_name=='authentication_rootObject':
            return_dict = root.findall('rootObject')[0].attrib
        if section_name=='authentication_properties':    
            for vat in root.findall('rootObject')[0].findall('properties')[0].findall('entry'):
                return_dict[vat.get('key')] = vat.get('value')
        if section_name=='authentication_status':
            return_dict = root.findall('rootObject')[0].findall('status')[0].attrib
        if section_name=='authentication_groups':    
            return_dict = root.findall('rootObject')[0].findall('groups')[0].attrib
        if section_name=='authentication_pSetList':    
            return_dict = root.findall('rootObject')[0].findall('pSetList')[0].attrib
        return(return_dict)    
    
    def get_bitmap_value_xml_dict(self, case_id, section_name):
        '''
        Description: Return XMl bitmap values as dictionary
        '''
        if self.bitmap_value_xml_string != '':
            result_str=self.bitmap_value_xml_string
        else:
            result_str = API_Web_Services.get_full_xml_string(self)
            self.bitmap_value_xml_string = result_str
        root = ET.fromstring(result_str)
        return_dict={}
        ini_file=os.getcwd() + "\data\\" + case_id + ".ini"
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(ini_file)
        root_index=int(parser['bitmap_rootObject']['index'])
        if section_name=='bitmap_rootObject':
            return_dict = root.findall('rootObject')[root_index].findall('item')[0].attrib
            API_Web_Services.bitmap_value=return_dict['menuActionBitMap']
            return (return_dict)
        
        elif section_name=='bitmap_properties':
            return_dict=root.findall('rootObject')[root_index].findall('item')[0].findall('properties')[0].attrib    
            for vat in root.findall('rootObject')[root_index].findall('item')[0].findall('properties')[0].findall('entry'):
                return_dict[vat.get('key')] = vat.get('value')
            return (return_dict)
        else:
            which_node=re.match('bitmap_(.*)', section_name).group(1)
            return_dict=root.findall('rootObject')[root_index].findall('item')[0].findall(which_node)[0].attrib    
            return (return_dict)
        
    def get_bitmap_value_list_xml_dict(self):
        '''
        Description : Return XMl bitmap_list  values as dictionary
        '''
        result_str = API_Web_Services.get_full_xml_string(self)
        root = ET.fromstring(result_str)
        return_dict={}
        for item in root.findall('rootObject')[0].findall('item'):
            return_dict[item.get('index')] = item.get('value')
        return (return_dict)
    
    def get_verification_status(self, case_id, act_dict, section):
        '''
        Description : Read test case init file and compare with actual XML section value
        :param : case_id ='C2348457'
        :param : act_dict= authentication_rootObject_actual_dict
        :param : section='authentication_rootObject' or 'authentication_properties' or 'bitmap_value'
        '''
        ini_file=os.getcwd() + "\data\\" + case_id + ".ini"
        parser = ConfigParser()
        parser.optionxform=str
        parser.read(ini_file)
        exp_dict=dict(parser.items(section))
        status={'status':'pass'}
        for dict_key in exp_dict:
            if exp_dict[dict_key]!=act_dict[dict_key]:
                status['status']=dict_key
                break
        return(status)
    
    def get_message(self, section_name, status):
        '''
        Description : Return verification message with section key
        '''
        if status['status']=='pass':
            msg="Step X: Verify " + section_name + " section."
        else:
            msg="Step X: Verify " + section_name + " section for " + status['status'] + " Key Value."
        return(msg)
    
    def verify_xml_value(self, case_id, section_name):
        '''
        Description : Verify all XML section values 
        '''
        if section_name=='authentication':
            section_name_list=['authentication_rootObject','authentication_properties','authentication_status','authentication_groups','authentication_pSetList']
            for section in section_name_list :
                act_dict=API_Web_Services.get_authentication_xml_dict(self, section)
                status=API_Web_Services.get_verification_status(self, case_id, act_dict, section)
                msg=API_Web_Services.get_message(self, section_name, status)
                utillity.UtillityMethods.asequal(self, 'pass', status['status'], msg)
        if section_name=='bitmap_rootObject':
            section_name_list=['bitmap_rootObject','bitmap_properties' ,'bitmap_casterObjects', 'bitmap_pageDataBean', 'bitmap_portalPaths', 'bitmap_pathMappingTypes', 'bitmap_portalPageOrder']
            ini_file=os.getcwd() + "\data\\" + case_id + ".ini"
            parser = ConfigParser()
            parser.optionxform=str
            parser.read(ini_file)
            for section in section_name_list:
                if parser.has_section(section):
                    act_dict=API_Web_Services.get_bitmap_value_xml_dict(self, case_id, section)
                    status=API_Web_Services.get_verification_status(self, case_id, act_dict, section)
                    msg=API_Web_Services.get_message(self, section, status)
                    utillity.UtillityMethods.asequal(self, 'pass', status['status'], msg)
        if section_name=='bitmap_value_list':
            act_dict=API_Web_Services.get_bitmap_value_list_xml_dict(self)    
            status=API_Web_Services.get_verification_status(self, case_id, act_dict,section_name)
            msg=API_Web_Services.get_message(self, section_name, status)
            utillity.UtillityMethods.asequal(self, 'pass', status['status'], msg)
            
    def login_wf(self):
        '''
        Description : To login WF set up, before 
        '''
        loginid = utillity.UtillityMethods.parseinitfile(self, 'mrid')
        loginpwd = utillity.UtillityMethods.parseinitfile(self, 'mrpass')
        uname1=(By.CSS_SELECTOR, 'input[id=SignonUserName]')
        self._validate_page(uname1)
        usename= self.driver.find_element(*LoginPageLocators.uname)
        usename.click()
        time.sleep(2)
        usename.send_keys(loginid)
        time.sleep(1)
        if loginpwd!=None:
            passwd =self.driver.find_element(*LoginPageLocators.pword)
            passwd.send_keys(loginpwd)
            time.sleep(1)
        sign_in =self.driver.find_element(*LoginPageLocators.submit)
        sign_in.click()
        time.sleep(5)
            
    def invoke_and_verify_authentication(self, case_id):
        '''
        Description : Invoke authentication URL and verify all authentication sections
        '''
        setup_url = API_Web_Services.get_setup_url(self)
        self.driver.get(setup_url)
        API_Web_Services.login_wf(self)
        loginid = utillity.UtillityMethods.parseinitfile(self, 'mrid')
        loginpwd = utillity.UtillityMethods.parseinitfile(self, 'mrpass')
        api_url=setup_url + "rs/ibfs?IBIRS_action=signOn&IBIRS_userName="+loginid+"&IBIRS_password="+loginpwd
        self.driver.get(api_url)
        time.sleep(4)
        API_Web_Services.verify_xml_value(self, case_id, 'authentication')
        
    def invoke_and_verify_bitmap_value(self, case_id):
        '''
        Description : Invoke bitmap URL and verify all bitmap_value
        '''
        setup_url = API_Web_Services.get_setup_url(self)
        try:
            ini_file=os.getcwd() + "\data\\" + case_id + ".ini"
            parser = ConfigParser()
            parser.optionxform=str
            parser.read(ini_file)
            item_name=parser['bitmap_url']['item_name']
            api_url=setup_url + "wfirs/ibfs?IBFS_path=/WFC/Repository/P242_S10674_G171304"+item_name+"&IBFS_action=list"
        except KeyError:
            api_url=setup_url + "wfirs/ibfs?IBFS_path=/WFC/Repository/P242_S10674_G171304&IBFS_action=list"
        print(api_url)
        self.driver.get(api_url)
        time.sleep(4)
        API_Web_Services.verify_xml_value(self, case_id, 'bitmap_rootObject')
        
    def get_bitmap_value(self):
        return(API_Web_Services.bitmap_value.replace('+', '%2b'))
        
    def invoke_and_verify_bitmap_value_list(self, case_id):
        '''
        Description : Invoke bitmap_list URL and verify all bitmap list value
        '''
        setup_url = API_Web_Services.get_setup_url(self)
        bitmap_value=API_Web_Services.get_bitmap_value(self)
        api_url=setup_url + "wfirs/utils?IBFS_action=expandMenuActions&IBFS_base64content=" + bitmap_value
        self.driver.get(api_url)
        time.sleep(4)
        API_Web_Services.verify_xml_value(self, case_id, 'bitmap_value_list')        
    
    def run_test(self, case_id):
        '''
        Description : Invoke authentication, bitmap and bitmap_list URL and verify all section values
        '''
        API_Web_Services.invoke_and_verify_authentication(self, case_id)
        API_Web_Services.invoke_and_verify_bitmap_value(self, case_id)
        API_Web_Services.invoke_and_verify_bitmap_value_list(self, case_id)