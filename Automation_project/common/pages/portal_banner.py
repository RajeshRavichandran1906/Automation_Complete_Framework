from common.lib.base import BasePage
from common.lib.utillity import UtillityMethods as utill_obj
from common.lib.core_utility import CoreUtillityMethods as core_utill_obj
from common.pages.wf_mainpage import Wf_Mainpage as home_page
import time

class Portal_banner(BasePage):
    
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(Portal_banner, self).__init__(driver)
    
    def select_username_dropdown_menu(self, navigate_path=None):
        '''
        Desc: This will select the menu or submenu items from username dropdown.
        usage: banner_obj.select_username_dropdown_menu(navigate_path='Administration->Security Center')
        '''
        pop_up_css="div[class*='pop-top'][data-ibx-type='ibxMenu']"
        username_dropdown_css="[class^='pvd-canvas-area ibx-widget'] [class^='pvd-portal-banner ibx-widget'] [class^='pvd-right-menu-banner'] [class^='ibx-widget']"
        username_dropdown_object=self.driver.find_element_by_css_selector(username_dropdown_css)
        core_utill_obj.left_click(self, username_dropdown_object)
        utill_obj.synchronize_with_number_of_element(self, pop_up_css, 1, 90)
        if navigate_path != None:
            home_page.select_context_menu_item(self, navigate_path)
        time.sleep(1)
    
    
    def verify_portal_title(self, expected_title, msg):
        '''
        Desc: This will select the menu or submenu items from username dropdown.
        usage: banner_obj.verify_portal_title('Portal for Context Menu Testing', Step x:...)
        '''
        portal_title_css=".pvd-portal-title .ibx-label-text"
        actual_title=self.driver.find_element_by_css_selector(portal_title_css).text
        utill_obj.asequal(self, expected_title, actual_title, msg)
        
       
        