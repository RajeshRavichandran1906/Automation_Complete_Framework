from common.lib import utillity
from common.lib.base import BasePage
from common.pages.rc_misc import RC_Misc
from common.locators.rc_basic_locators import RCBasicLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time, re, os


class RC_Basic(BasePage):
    """ Inherit attributes of the parent class = Baseclass """

    def __init__(self, driver):
        super(RC_Basic, self).__init__(driver)

    def _validate_page(self, locator):
        self.longwait.until(EC.visibility_of_element_located(locator))
    
    def select_rc_ribbon_button(self, ribbon_button_name): 
        """
        param ribbon_button_name: 'save_and_close' OR 'properties'.... (Refer to the locator file to understand the ribbon object naming convention)
        Syntax: select_rc_ribbon_button('properties')
        @author = Niranjan
        """
        button_name = "ribbon_" + ribbon_button_name.lower()
        self.driver.find_element(*RCBasicLocators.__dict__[button_name]).click()
        time.sleep(2)
    
    def select_rc_menu_item(self, menu_item_name):
        """
        param menu_item_name: 'Save', 'Save As..'.... (any item to be clicked from the RC menu)
        Syntax: select_rc_menu_item('Save')
        @author = Niranjan
        """
        self.driver.find_element(*RCBasicLocators.rc_menu_btn).click()
        time.sleep(2)
        utillity.UtillityMethods.select_or_verify_bipop_menu(self, menu_item_name)  
        time.sleep(2)  
    def create_email_task(self, **kwargs):
        user_id=self.driver.find_element(*RCBasicLocators.__dict__["task_execution_id"])
        passwd_btn=self.driver.find_element(*RCBasicLocators.__dict__["task_password_btn"])
        RC_Misc.set_task_password(self, user_id, "srvadmin", passwd_btn, "srvadmin")
        time.sleep(2)
        
    def create_email_distribution(self, **kwargs): 
        """
        param type: 'Distribution List' OR 'Distribution File', OR 'Email Address(s)', OR 'Dynamic Distribution List'
        param to: To address
        param from: From Address
        param reply_address: Reply Address
        param subject: Subject of the email
        Syntax: create_email_distribution(type='Distribution List', to='xxx', from='xxx', reply_address='xxx', subject='xxx')
        @author = Niranjan
        """
        if 'type' in kwargs:
            type_elem=self.driver.find_element(*RCBasicLocators.email_type)
            utillity.UtillityMethods.select_any_combobox_item(self, type_elem, kwargs['type'])
            time.sleep(2)
        if 'to_addr' in kwargs:
            to_elem=self.driver.find_element(*RCBasicLocators.email_to)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, to_elem, kwargs['to_addr'])
            time.sleep(1)
        if 'from_addr' in kwargs:
            from_elem=self.driver.find_element(*RCBasicLocators.email_from)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, from_elem, kwargs['from_addr'])
            time.sleep(1)
        if 'reply_addr' in kwargs:
            reply_elem=self.driver.find_element(*RCBasicLocators.email_reply_address)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, reply_elem, kwargs['reply_addr'])
            time.sleep(1)
        if 'subject' in kwargs:
            subject_elem=self.driver.find_element(*RCBasicLocators.email_subject)
            utillity.UtillityMethods.set_text_field_using_actionchains(self, subject_elem, kwargs['subject'])
            time.sleep(1)
    
    
    
    
    
    
    