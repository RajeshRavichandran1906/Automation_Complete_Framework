'''
Created on Mar 23, 2018

@author: Aftab
'''
import time
from common.lib import html_controls as HtmlControls
from selenium.common.exceptions import NoSuchElementException
from common.lib.utillity import UtillityMethods as util_method
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.core_utility import CoreUtillityMethods as core_utils
from common.locators.loginpage_locators import LoginPage as Locators

class Login():
    
    def __init__(self, driver):
        self.driver=driver 
    
    def create_setup_url(self):
        '''
        Desc: This function will return the set up URL.
        @author: Aftab
        '''
        node = core_utils.parseinitfile(self, 'nodeid')
        port = core_utils.parseinitfile(self, 'httpport').strip()
        context = core_utils.parseinitfile(self, 'wfcontext')
        port = '' if port == '' else ':' + port 
        setup_url = "http://{0}{1}{2}/home8206".format(node, port, context)
        return(setup_url)
        
    def login_page(self, user_name, password, add_home_path=True):
        '''
        Desc: This function type user name and password in login page and click to login button.
        :Usage login_page('admin','admin')
        @author: Aftab
        '''
        util_method.wf_login(self, mrid=user_name, mrpass=password, add_home_path=add_home_path)
    
    def invoke_home_page(self, user_name, password):
        '''
        Desc: This function call for login to Home|welcome page.
        :Usage invoke_home_page('admin','admin')
        @author: Aftab
        '''
        environment_url=Login.create_setup_url(self)
        self.driver.get(environment_url)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(environment_url))
        Login.login_page(self,user_name, password)
        util_method.synchronize_until_element_is_visible(self, LoginPageLocators.loader_css, 350)
    
    def invoke_paris_home_page(self, user_name, password):
        '''
        Desc: This function invoke paris home page
        :Usage invoke_paris_home_page('admin','admin')
        '''
        environment_url=Login.create_setup_url(self).replace("home8206", "")
        self.driver.get(environment_url)
        util_method.wait_for_page_loads(self, 10, pause_time=1)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(environment_url))
        Login.login_page(self,user_name, password, add_home_path=False)
        util_method.synchronize_until_element_is_visible(self, LoginPageLocators.loader_css, 350)
        util_method.wait_for_page_loads(self, 80, pause_time=5)
        
    def invoke_new_tool_using_api(self, master_file_name, tool_name, user_name, password):
        '''
        Desc: This function call to invoke new tool using api.
        :Usage invoke_new_tool_using_api('car', 'report', 'admin','admin')
        @author: Aftab
        '''
        environment_url=Login.create_setup_url(self)
        core_utils_obj=core_utils(self.driver)
        project = core_utils_obj.parseinitfile('project_id')
        suite = core_utils_obj.parseinitfile('suite_id')
        folder = project + '/' + suite
        api_url = environment_url.replace('home','') + 'ia?tool=' + tool_name + '&master=' + master_file_name + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(environment_url))
        Login.login_page(self, user_name, password)
        time.sleep(1)
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                core_utils_obj.left_click(continue_to_login)
        except NoSuchElementException:
            return False
    
    def invoke_tool_in_edit_mode_using_api(self, fex_name, tool_name, user_name=None, password=None):
        '''
        Desc: This function call to invoke tool in edit mode using api.
        :Usage infoassist_tool_using_api_edit('test', 'report', user_name='admin', password='admin')
        @author: Aftab
        '''
        environment_url=Login.create_setup_url(self)
        project_id=self.parseinitfile('project_id')
        folder = self.parseinitfile('suite_id')
        api_url = environment_url.replace('home','')+ 'ia?&item=IBFS%3A%2FWFC%2FRepository/'+project_id+'/'+folder+'/'+fex_name+'.fex&tool='+tool_name
        self.driver.get(api_url)
        if 'user_name'!= None:
            Login.login_page(self, user_name, password)
        time.sleep(1)
        error_hint="Itemdoesnotexist"
        resource_not_found_err_msg="Received Item Does not Exist. Means Either " +  folder + " Repository folder OR the required fex " + fex_name + ".fex is not available in the set up."
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if error_hint in api_url_response_text:
            raise LookupError(resource_not_found_err_msg)
        access_to_item_denied_msg = "Accesstoitemdenied"
        project_not_found_err_msg="Received Access to item denied Means"+ project_id + "is not available"
        if access_to_item_denied_msg in api_url_response_text:
            raise LookupError(project_not_found_err_msg)
        time.sleep(15)
        
    def invoke_home_page_with_public_access(self):
        '''
        Desc: This function will nvoke home page by clicking on Public access in login page
        :Usage invoke_home_page_with_public_access()
        @author: Kiruthika
        '''
        core_utils_obj=core_utils(self.driver)
        environment_url=Login.create_setup_url(self)
        self.driver.get(environment_url)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(environment_url))
        public_access_css = "div[class*='public-access']>label"
        util_method.synchronize_with_number_of_element(self, public_access_css, 1, 120)
        core_utils.update_current_working_area_browser_specification(self)
        public_access_elem =self.driver.find_element_by_css_selector(public_access_css)
        core_utils_obj.left_click(public_access_elem)
    
    def invoke_homepage_with_portal(self,user_name, password):
        '''
        Description:This function used invoke homepage directly by accessing portals
        @param user_name:key from config file
        @param password : key from config file
        usage invoke_homepage_with_portal('mrid','mrpass')
        '''
        set_up_url=Login.create_setup_url(self).replace("home8206", "")
        portal_context = 'portals'
        environment_url = set_up_url+portal_context
        self.driver.get(environment_url)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(environment_url))
        Login.login_page(self,user_name, password)
        util_method.synchronize_until_element_is_visible(self, LoginPageLocators.loader_css, 350)
        
class LoginPage:
    
    def __init__(self, driver):
        
        self._locators_   =  Locators
        self._utils_      =  util_method(driver)
        self._core_utils  =  core_utils(driver)
        self.driver = driver
        
    def invoke(self):
        """
        Description : Invoke the login page
        """
        self._core_utils.update_current_working_area_browser_specification()
        url = self._utils_.get_setup_url().replace("home8206", "")
        self.driver.get(url)
        self._utils_.synchronize_until_element_is_visible("#" + self._locators_.sign_in[1], 60)
        
    def click_tour_webfocus(self):
        """
        Description : Click on Tour WebFOCUS link
        """
        link = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.tour_wf, "Tour WebFOCUS")
        link.click()
    
    def click_visit_knowledge_base(self):
        """
        Description : Click on Tour WebFOCUS link
        """
        link = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.visit_kb, "Visit the Knowledge Base")
        link.click()
        
    @property
    def UserName(self): 
        username_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.user_name, 'Login Page user name text')
        return HtmlControls.TextBox(username_obj, 'Login Page User Name TextBox')
    
    @property
    def Password(self): 
        username_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.password, 'Login Page password text')
        return HtmlControls.TextBox(username_obj, 'Login Page Password TextBox') 
    
    @property
    def ErrorMessage(self): 
        username_obj = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.error_msg, 'Login Page Error Message')
        return HtmlControls.Label(username_obj, 'Login Page Error Message Label')  
    
    @property
    def SignInButton(self): 
        sign_in = self._utils_.validate_and_get_webdriver_object_using_locator(self._locators_.sign_in, 'Login Page Sign In Button')
        return HtmlControls.Button(sign_in, 'Login Page SignIn Button')