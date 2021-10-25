import time
from common.lib.base import BasePage
from selenium.webdriver.support.color import Color
from common.lib.utillity import UtillityMethods as utillityobject
from selenium.common.exceptions import NoSuchElementException
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.global_variables import Global_variables


class Visualization_Miscelaneous(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Visualization_Miscelaneous, self).__init__(driver)
        self.browser = utillityobject.parseinitfile(self, 'browser').lower()
        
    def wait_for_object(self, element_css, option, visble_element_text=None, expected_number=None, time_out=120):
        '''
        :Desc: This function is handle synchronization with visible text or expected visible element count in IA tool.
        :Param: option = 'text' or 'number'
        '''
        if option == 'text':
            utillityobject.synchronize_with_visble_text(self, element_css, visble_element_text, time_out)
        elif option == 'number':
            utillityobject.synchronize_with_number_of_element(self, element_css, expected_number, time_out)
        time.sleep(3)
    
    def invoke_visualization_tool_using_api(self, tool='idis', master='baseapp', mrid=None, mrpass=None):
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
        time.sleep(3)
        try:
            continue_to_login = self.driver.find_element(*LoginPageLocators.continue_login)
            if continue_to_login.is_displayed():
                continue_to_login.click()
        except NoSuchElementException:
            return False
    
    def invoke_visualization_tool_in_edit_mode_using_api(self, fex, tool, mrid=None, mrpass=None):
        '''
        Desc: This function will invoke the visualization tools in edit mode for a particular fex in tools like report, chart, visualization.
        '''
        setup_url = utillityobject.get_setup_url(self)
        project_id=utillityobject.parseinitfile(self, 'project_id')
        folder = utillityobject.parseinitfile(self, 'suite_id')
        api_url = setup_url.replace('home8206', '')+ 'ia?&item=IBFS%3A%2FWFC%2FRepository/'+project_id+'/'+folder+'/'+fex+'.fex&tool='+tool
        self.driver.get(api_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)
        time.sleep(10)   
        error_hint="Itemdoesnotexist"
        resource_not_found_err_msg="Received Item Does not Exist. Means Either " +  folder + " Repository folder OR the required fex " + fex + " is not available in the set up."
        api_url_response_text= self.driver.find_element_by_css_selector("html body").text.replace(' ', '')
        if error_hint in api_url_response_text:
            raise LookupError(resource_not_found_err_msg)
        access_to_item_denied_msg = "Accesstoitemdenied"
        project_not_found_err_msg="Received Access to item denied Means"+ project_id + "is not available"
        if access_to_item_denied_msg in api_url_response_text:
            raise LookupError(project_not_found_err_msg)
        time.sleep(15) 
    
    def invoke_visualization_tool_in_run_mode_using_api(self, fex, mrid=None, mrpass=None):
        '''
        Desc: This function will invoke the visualization tools in run mode. For fex parameter we should pass the fex name with extension(eg:- abc.fex)
        '''  
        fex = fex.replace('.fex','')  #replaced because create, edit function usage is without .fex, whereas run we need to send testcase with.fex. This willnot affect existing usage with .fex          
        setup_url = utillityobject.get_setup_url(self)
        project_folder=utillityobject.parseinitfile(self, 'project_id')
        suite_folder = utillityobject.parseinitfile(self, 'suite_id')
        api_url = setup_url.replace('home8206', '') + 'run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252F' + project_folder + "/" + suite_folder + '&BIP_item=' + fex+'.fex'
        self.driver.get(setup_url)
        utillityobject.wf_login(self, mrid=mrid, mrpass=mrpass, add_home_path=False)        
        self.driver.get(api_url)
        time.sleep(10)
    
    def logout_visualization_using_api(self):
        '''
        Desc: This function will invoke the visualization tools in run mode.
        '''
        utillityobject.wf_logout(self)
                
    def ibfs_save_as_visualization(self, file_name, file_type=None, folder_location_to_save=None):
        utillityobject.ibfs_save_as(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
    
    def ibfs_save_visualization(self, file_name, file_type=None, folder_location_to_save=None):
        utillityobject.ibfs_save(self, file_name, file_type=file_type, folder_location_to_save=folder_location_to_save)
            
    def verify_chart_color(self, parent_css, riser_css, color_name, method, attribute, msg):
        '''
        Desc: This function will verify the chart color using using method = 'get_attribute' OR 'get_css_property'.
        method='get_attribute' OR 'get_css_property'.
        attribute='fill' OR 'stroke'
        '''
        absolute_raiser_css = parent_css + " " + riser_css
        elem=self.driver.find_element_by_css_selector(absolute_raiser_css)
        if method == 'get_attribute':
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
