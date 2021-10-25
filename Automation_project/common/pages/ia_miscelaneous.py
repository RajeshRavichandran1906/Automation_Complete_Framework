import time
from common.lib.base import BasePage
from selenium.webdriver.support.color import Color
from common.lib.utillity import UtillityMethods as utillityobject
from selenium.common.exceptions import NoSuchElementException
from common.locators.loginpage_locators import LoginPageLocators
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class IA_Miscelaneous(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(IA_Miscelaneous, self).__init__(driver)
        self.browser = utillityobject.parseinitfile(self, 'browser').lower()
        
    def wait_for_object(self, element_css, option='text', visble_element_text=None, expected_number=None, time_out=25):
        '''
        This function is handle synchronization with visible text or expected visible element count in IA tool.
        '''
        if option == 'text':
            utillityobject.synchronize_with_visble_text(self, element_css, visble_element_text, time_out)
        elif option == 'number':
            utillityobject.synchronize_with_number_of_element(self, element_css, expected_number, time_out)
            
    def verify_message_in_html_body(self, message="/bipgqashare/qaauto_lnx_apps/smoke_retailsamples_alphaformat/wf_retail_lite.mas", msg="Step X"):
        '''
        Desc: This function is used to verify message from html>body 
        :Param :msg="/bipgqashare/qaauto_lnx_apps/smoketest/wf_retail_lite.mas"
        @Usage :verify_message_in_html_body(msg="Step X: Verify body of the message shows smoketest app folder) 
        '''
        access_folder_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if message in access_folder_response_text:
            utillityobject.asin(self, message, access_folder_response_text, msg)
        else:
            raise UserWarning("wf_retail_lite.mas is not pointing to {0}".format(message))
    
    def run_fex_using_api(self, folder_name, fex_name=None, mrid=None, mrpass=None, home_page='New'):
        '''
        Desc: This function used to invoke run fex
        @Usage : run_fex_using_api(folder_name='Reports', folder_name='Retail_Samples/Reports/Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass' 
        '''
        setup_url = utillityobject.get_setup_url(self)
        self.driver.get(setup_url)
        if home_page== 'New':
            page_css = WfMainPageLocators.CONTENT_ICON_CSS
        else:
            page_css = "[id*='treeView'] table[class*='bi-tree-view-table']"
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(setup_url))
        utillityobject.login_wf(self, mrid, mrpass)
        utillityobject.synchronize_with_number_of_element(self, page_css, 1, 90)
        run_api_url = setup_url.replace('home8206', '') + 'run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder' + '=IBFS%3A%2FWFC%2FRepository%2F' + folder_name + '&BIP_item='+fex_name+'.fex'
        self.driver.get(run_api_url)
        time.sleep(5)

    def run_htmlfex_using_api(self, folder_name, fex_name=None, mrid=None, mrpass=None, home_page='New'):
        '''
        Desc: This function used to invoke run html fex
        @Usage : run_fex_using_api(folder_name='Reports', folder_name='Retail_Samples/Reports/Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid', mrpass='mrpass' 
        '''
        setup_url = utillityobject.get_setup_url(self)
        self.driver.get(setup_url)
        if home_page== 'New':
            page_css = WfMainPageLocators.CONTENT_ICON_CSS
        else:
            page_css = "[id*='treeView'] table[class*='bi-tree-view-table']"
        refused_to_connect_msg = "refusedtoconnect"
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if refused_to_connect_msg in api_url_response_text:
            raise EnvironmentError("WebFOCUS Client {0} is down.".format(setup_url))
        utillityobject.login_wf(self, mrid, mrpass)
        utillityobject.synchronize_with_number_of_element(self, page_css, 1, 90)
        run_api_url = setup_url.replace('home8206', '') + 'run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder' + '=IBFS%3A%2FWFC%2FRepository%2F' + folder_name + '&BIP_item='+fex_name+'.htm'
        self.driver.get(run_api_url)
        time.sleep(5)
            
    def edit_fex_using_api(self, folder_name, tool='Report', fex_name=None, mrid=None, mrpass=None):
        '''
        Desc: This function will edit fex in tool
        @Usage : edit_retailsamples_using_api( folder_name='Reports/Auto_Link', fex_name='Report_Store_Product_Metrics', mrid='mrid',mrpass='mrpass')
        '''
        if folder_name == None :
            project = utillityobject.parseinitfile(self, 'project_id')
            suite = utillityobject.parseinitfile(self, 'suite_id')
            group_id=utillityobject.parseinitfile(self,'group_id')
            folder = project + '_' + suite + '/' + group_id
        else :
            folder = folder_name
        setup_url = utillityobject.get_setup_url(self)
        edit_api_url = setup_url.replace('home8206', '') + 'ia?&item=IBFS%3A%2FWFC%2FRepository/'+ folder + '/' + fex_name+ '.fex&tool='+tool
        self.driver.get(edit_api_url)
        utillityobject.login_wf(self, mrid, mrpass, add_home_path=False)
        time.sleep(5)
            
    def invoke_ia_tool_using_api(self, tool='report', master='baseapp', mrid=None, mrpass=None):#deprecated [please don't use this one]
        '''
        Desc: This function will invoke the info assist for tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        project = utillityobject.parseinitfile(self, 'project_id')
        suite = utillityobject.parseinitfile(self, 'suite_id')
        folder = project + '/' + suite
        api_url = setup_url.replace('home8206', '') + 'ia?tool=' + tool + '&master=' + master + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)
        time.sleep(30)
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False
        
    def invoke_ia_tool_using_api_(self, tool='report', master='baseapp', mrid=None, mrpass=None, folder_path=None):
        '''
        Desc: This function will invoke the info assist for tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        if folder_path:
            folder=folder_path
        else:
            project = utillityobject.parseinitfile(self, 'project_id')
            suite = utillityobject.parseinitfile(self, 'suite_id')
            group_id=utillityobject.parseinitfile(self,'group_id')
            folder = project + '_' + suite + '/' + group_id
        api_url = setup_url.replace('home8206', '') + 'ia?tool=' + tool + '&master=' + master + '&item=IBFS%3A%2FWFC%2FRepository%2F' + folder
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)
        time.sleep(30)
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False    
    
    def invoke_ia_tool_in_edit_mode_using_api(self, fex, tool='report', mrid=None, mrpass=None, folder_path=None):
        '''
        Desc: This function will invoke the info assist tools in edit mode for a particular fex in tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        if folder_path:
            folder=folder_path
        else:
            project_id=utillityobject.parseinitfile(self, 'project_id')
            suite_id = utillityobject.parseinitfile(self, 'suite_id')
            folder = project_id+'/'+suite_id
        api_url = setup_url.replace('home8206', '')+ 'ia?&item=IBFS%3A%2FWFC%2FRepository/'+folder+'/'+fex+'.fex&tool='+tool
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)
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
            if Global_variables.browser_name in ['ie', 'edge']:
                temp_obj=((utillityobject.get_element_attribute(self, elem, attribute))[:-9]+")")[4:]
            else:
                temp_obj=((utillityobject.get_element_attribute(self, elem, attribute))[:-10]+")")[4:]
            actual_color = "rgb" + temp_obj
            expected_color=utillityobject.color_picker(self, color_name, 'rgb')
        elif method == 'get_css_property':
            actual_color = Color.from_string(utillityobject.get_element_css_propery(self, elem, attribute)).rgba
            expected_color=utillityobject.color_picker(self, color_name, 'rgba')
        utillityobject.asequal(self, actual_color, expected_color, msg)