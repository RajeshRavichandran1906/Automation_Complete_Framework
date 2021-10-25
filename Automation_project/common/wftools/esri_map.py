from common.lib import utillity
from common.lib.base import BasePage
from common.locators.visualization_run_locators import VisualizationRunLocators
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, StaleElementReferenceException
import re
import time
from selenium.webdriver.support.ui import Select
from pynput.mouse import Button, Controller
from selenium.webdriver.support.color import Color
from common.pages import as_ribbon
from common.lib import as_utility

class AS_Html_Canvas(BasePage):     
        
    def __init__(self, driver):
        super(AS_Html_Canvas, self).__init__(driver)
        
    
    def drag_drop_on_canvas(self,tab_name,ribbon_button_name,start_x,start_y,end_x,end_y):
        '''call as_riboon to click on object'''
        as_ribbon_obj= as_ribbon.AS_Ribbon(self.driver)
        as_ribbon_obj.click_ribbon_item(tab_name, ribbon_button_name)        

        time.sleep(3)
        ac = ActionChains(self.driver)
        html = self.driver.find_element_by_name("HtmlPage")
        ac.move_to_element_with_offset(html,start_x, start_y)
        ac.click_and_hold()
        time.sleep(1)
        ac.move_to_element_with_offset(html, end_x, end_y)
        ac.release().perform()        
        time.sleep(1)
        del ac
        
    def drag_drop_elements(self, source, *args):
        '''
        Usage: drag_drop_elements(driver.find_element_by_name("embedded"), driver.find_element_by_name("Zip3"))
               drag_drop_elements(driver.find_element_by_name("embedded"), 500, 600)
        Params: source - starting element, target - ending element location , or use coordinates instead of the target
        Description: click and drag element to another element (location), use when connecting elements or moving an object to a folder
        Author: Lawrence
        Date: 4/27/17
        '''
        driver = self.driver
        targets = {1: "drag_and_drop", 2: "drag_and_drop_by_offset"}
        target_inputs = len(args)
        ac = ActionChains(driver)
        getattr(ac, targets[target_inputs])(source, *args).release().perform()
        del ac
        time.sleep(1)
        
    def drag_drop_by_coordinate_offsets(self, source, target, start_x,start_y,end_x,end_y): 
        '''
        Usage: drag_drop_elements(driver.find_element_by_name("embedded"), driver.find_element_by_name("Zip3"), 100, 10, 500, 600)
        Params: source - starting element, target - ending element location , coordinates offset from the parent objects
        Description: click and drag element to another element (location) - by offsets from objects
        Author: Lawrence
        Date: 4/27/17
        ''' 
        driver = self.driver 
        ac = ActionChains(driver)
        ac.move_to_element_with_offset(source, start_x, start_y)
        ac.click_and_hold()
        time.sleep(1)
        ac.move_to_element_with_offset(target, end_x, end_y)
        ac.release().perform()        
        time.sleep(1)
        del ac

    def select_design_param_js_css_canvas(self, option):
        '''
        Usage: drag_drop_elements(driver.find_element_by_name("embedded"), driver.find_element_by_name("Zip3"))
        Params: source - starting element, target - ending element location 
        Description: click and drag element to another element (location), use when connecting elements or moving an object to a folder
        Author: Lawrence
        Date: 4/27/17
        '''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        options = {'design': 90, 'parameters': 150, 'embedded javascript': 270, 'embedded css': 350}
        lower_case = option.lower()
        if lower_case in options:
            asutilobj.element_clicker(driver.find_elements_by_id("1")[5], (By.CLASS_NAME, "Button"), "left", "offset", options[lower_case], 5)
        else: 
            print("Canvas option not found")
        time.sleep(1)
  
    
        
        
  
    
        
        