import time
from common.lib.base import BasePage
from selenium.webdriver.support.color import Color
from common.lib.utillity import UtillityMethods as utillityobject
from selenium.common.exceptions import NoSuchElementException
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.core_utility import CoreUtillityMethods as core_utilobj

class InfoGraphic(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(InfoGraphic, self).__init__(driver)
        self.browser = utillityobject.parseinitfile(self, 'browser').lower()
         
    def create_setup_url(self):
        '''
        Desc: This function will return the set up URL.
        @author: Aftab
        '''
        node = core_utilobj.parseinitfile(self, 'nodeid')
        port = core_utilobj.parseinitfile(self, 'httpport')
        context = core_utilobj.parseinitfile(self, 'wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
        return(setup_url)
        
    def wait_for_object(self, element_css, option='text', visble_element_text=None, expected_number=None, time_out=25):
        '''
        This function is handle synchronization with visible text or expected visible element count in IA tool.
        '''
        if option == 'text':
            utillityobject.synchronize_with_visble_text(self, element_css, visble_element_text, time_out)
        elif option == 'number':
            utillityobject.synchronize_with_number_of_element(self, element_css, expected_number, time_out)
    
    def scrolled_into_view(self, object_to_view):
        '''
        This function bring the hidden DOM object to View
        '''
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollIntoView(true);',object_to_view)
        time.sleep(2)
          
    def verify_message_in_html_body(self, msg="/bipgqashare/qaauto_lnx_apps/smoketest/wf_retail_lite.mas"):
        '''
        Desc: This function is used to verify message from html>body 
        :Param :msg="/bipgqashare/qaauto_lnx_apps/smoketest/wf_retail_lite.mas"
        @Usage :verify_message_in_html_body() 
        '''
        access_folder_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if msg in access_folder_response_text:
            raise UserWarning("wf_retail_lite.mas is pointing to -" +access_folder_response_text)
    
    def run_infographic_using_api(self, folder_name, subfolder_name, fex_name, oUser):
        '''
        Desc: This function used to run fex
        :Param : folder_name='Reports'
        :Param :subfolder_name='Auto_Link'
        :Param :fex_name='Report_Store_Product_Metrics'
        @Usage : run_retailsamples_using_api(folder_name='Reports', subfolder_name='Reports', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass' 
        '''
        project_id=utillityobject.parseinitfile(self, 'project_id')
        user_id=utillityobject.parseinitfile(self, oUser)
        environment_url=InfoGraphic.create_setup_url(self)
        product = folder_name + '%252F' + subfolder_name
        run_api_url = environment_url + 'run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder' + '=IBFS%3A%2FWFC%2FRepository%252F' + product + '%252F&BIP_item='+fex_name+'.fex'
        self.driver.get(run_api_url)
        time.sleep(10)
        error_hint="Itemdoesnotexist"
        resource_not_found_err_msg="Received - Item Does not Exist. Verify " +  product + " Repository folder OR the required fex " + fex_name + ".fex are added in the set up - {0} - user: {1}".format(environment_url, user_id)
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if error_hint in api_url_response_text:
            raise LookupError(resource_not_found_err_msg)
        access_to_item_denied_msg = "Accesstoitemdenied"
        project_not_found_err_msg="Received Access to item denied Means"+ project_id + "is not available in setup - {0} - user: {1}".format(environment_url, user_id)
        if access_to_item_denied_msg in api_url_response_text:
            raise LookupError(project_not_found_err_msg)
        time.sleep(5)
        
    def restore_infographic_using_api(self, folder_name,  subfolder_name, fex_name, oUser):
        '''
        Desc: This function will edit fex in tool
        :Param : folder_name='Reports'
        :Param :subfolder_name='Auto_Link'
        :Param :fex_name='Report_Store_Product_Metrics'
        @Usage : edit_retailsamples_using_api(tool='Report', folder_name='Reports', subfolder_name='Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid',mrpass='mrpass')
        
        '''
        user_id=utillityobject.parseinitfile(self, oUser)
        environment_url=InfoGraphic.create_setup_url(self)
        product = folder_name + '/' + subfolder_name
        edit_api_url = environment_url + 'ia?item=IBFS:/WFC/Repository/' + product + '/'+fex_name+'.fex'
        self.driver.get(edit_api_url)
        time.sleep(30)
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down - user: {1}.".format(environment_url, user_id))
        time.sleep(2)
        
    
    def invoke_ia_tool_using_api(self, tool='report', master='baseapp', mrid=None, mrpass=None):
        '''
        Desc: This function will invoke the info assist for tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        project = utillityobject.parseinitfile(self, 'project_id')
        suite = utillityobject.parseinitfile(self, 'suite_id')
        folder = project + '/' + suite
        api_url = setup_url + 'ia?tool=' + tool + '&master=' + master + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass)
        time.sleep(30)
        self.driver.implicitly_wait=1
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False
        
    def invoke_ia_tool_using_api_(self, tool='report', master='baseapp', mrid=None, mrpass=None):
        '''
        Desc: This function will invoke the info assist for tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        project = utillityobject.parseinitfile(self, 'project_id')
        suite = utillityobject.parseinitfile(self, 'suite_id')
        group_id=utillityobject.parseinitfile(self,'group_id')
        folder = project + '_' + suite + '_' + group_id
        api_url = setup_url + 'ia?tool=' + tool + '&master=' + master + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass)
        time.sleep(30)
        self.driver.implicitly_wait=1
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False    
    
    def invoke_ia_tool_in_edit_mode_using_api(self, fex, tool='report', mrid=None, mrpass=None):
        '''
        Desc: This function will invoke the info assist tools in edit mode for a particular fex in tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        project_id=utillityobject.parseinitfile(self, 'project_id')
        folder = utillityobject.parseinitfile(self, 'suite_id')
        api_url = setup_url+ 'ia?&item=IBFS%3A%2FWFC%2FRepository/'+project_id+'/'+folder+'/'+fex+'.fex&tool='+tool
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass)
        time.sleep(30)
        
    def logout_ia_using_api(self):
        '''
        Desc: This function will invoke the visualization tools in run mode.
        '''
        utillityobject.wf_logout(self)
                
    def ibfs_save_as(self, file_name, file_type=None, folder_location_to_save=None):
        utillityobject.ibfs_save_as(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
        
    def verify_chart_color(self, parent_css, riser_css, color_name, method, attribute, msg):
        '''
        Desc: This function will verify the chart color using using method = 'get_attribute' OR 'get_css_property'.
        method='get_attribute' OR 'get_css_property'.
        attribute='fill' OR 'stroke'
        '''
        absolute_raiser_css = parent_css + " " + riser_css
        elem=self.driver.find_element_by_css_selector(absolute_raiser_css)
        if method.lower() == 'get_attribute':
            if self.browser.lower() == 'ie':
                temp_obj=((utillityobject.get_element_attribute(self, elem, attribute))[:-9]+")")[4:]
            else:
                temp_obj=((utillityobject.get_element_attribute(self, elem, attribute))[:-10]+")")[4:]
            actual_color = "rgb" + temp_obj
            expected_color=utillityobject.color_picker(self, color_name, 'rgb')
        elif method == 'get_css_property':
            actual_color = Color.from_string(utillityobject.get_element_css_propery(self, elem, attribute)).rgba
            expected_color=utillityobject.color_picker(self, color_name, 'rgba')
        utillityobject.asequal(self, actual_color, expected_color, msg)