from common.lib import utillity
from common.lib.base import BasePage
from common.locators.wf_alert_assist_locators import WfAlertAssistLocators
from selenium.webdriver.support import expected_conditions as EC
import time

class Wf_Alert_Assist(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Wf_Alert_Assist, self).__init__(driver)
        
    
    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    
    def api_login(self):
        utliobj=utillity.UtillityMethods(self.driver)
        node = utliobj.parseinitfile('nodeid')
        port = utliobj.parseinitfile('httpport')
        context = utliobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context 
        project = utliobj.parseinitfile('project_id')
        suite = utliobj.parseinitfile('suite_id')
        folder = project + '/' + suite
        api_url = setup_url + "/ia?item=IBFS%3A%2FWFC%2FRepository%2F"+folder+"&tool=Alert"
        self.driver.get(api_url)
        utliobj.login_wf("mrid","mrpass")
        time.sleep(30)
            
    def select_aa_tree_item(self, aa_tool_name, click_type = 0, *args):
        """
        :param field_name:'Sale, Year' 
        :param position:1,2...  
        :param click_type: 0 -> left click, 1 -> right click, 2 -> double click.
        :param args: after right click --> selection menu option.
        """
        aa_tool_elems=self.driver.find_elements_by_css_selector("#aaTree table span")
        required_aa_tool_elem=aa_tool_elems[[el.text.strip() for el in aa_tool_elems].index(aa_tool_name)]
        utillity.UtillityMethods.click_on_screen(self, required_aa_tool_elem, coordinate_type='middle',click_type=click_type)
        time.sleep(2)
        if len(args)>0:
            for arg in args:
                utillity.UtillityMethods.select_or_verify_bipop_menu(self, arg)
                
    
    def verify_aa_tree_item(self, aa_tool_name, msg):
        """
        :param field_name:'Sale, Year' 
        :param position:1,2...  
        :param click_type: 0 -> left click, 1 -> right click, 2 -> double click.
        :param args: after right click --> selection menu option.
        """
        aa_tool_elems=self.driver.find_elements_by_css_selector("#aaTree table span")
        aa_tool_values=[el.text.strip() for el in aa_tool_elems]
        utillity.UtillityMethods.asin(self, aa_tool_name, aa_tool_values, msg)
        
                    
    def select_aa_tool_menu_item(self, item_name, **kwargs):
        """
        param: item_name: 'menu_save_as' OR 'menu_run' - these need to be get it from Wf_Alert_Assist_Locators.
        """
        aa_btn=self.driver.find_element(*WfAlertAssistLocators.Appbtn)
        utillity.UtillityMethods.click_on_screen(self, aa_btn, coordinate_type='middle',click_type=0)
        time.sleep(2)
        elem1=WfAlertAssistLocators.__dict__[item_name]
        self._validate_page(elem1)
        aa_tool_menu=self.driver.find_element(*WfAlertAssistLocators.__dict__[item_name])
        utillity.UtillityMethods.click_on_screen(self, aa_tool_menu, coordinate_type='middle',click_type=0)
        time.sleep(8)
   
    def select_top_toolbar_item(self, item_name, **kwargs):
        """
        param: item_name: 'toptoolbar_new' OR 'toptoolbar_run' - these need to be get it from Wf_Alert_Assist_Locators.
        This function is specific to click on toolbar buttons - new, run, undo, redo, run
        """
    
        top_toolbar_obj=self.driver.find_element(*WfAlertAssistLocators.__dict__[item_name])
        utillity.UtillityMethods.click_on_screen(self, top_toolbar_obj, coordinate_type='middle',click_type=0)
        time.sleep(8)
