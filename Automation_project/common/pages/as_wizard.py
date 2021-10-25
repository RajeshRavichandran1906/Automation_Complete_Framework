import time
from common.lib.base import BasePage
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.pages import as_ribbon
from common.lib import as_utility
import uiautomation as automation

class AS_Wizard_Windows(BasePage):
    def __init__(self, driver):
        super(AS_Wizard_Windows, self).__init__(driver)
    
    def Html_Document_Wizard(self,tab_name,ribbon_button_name,file_type="HTML Page",**kwargs):                
        ribbon_obj = as_ribbon.AS_Ribbon(self.driver) 
        as_util_obj= as_utility.AS_Utillity_Methods(self.driver)     
          
        ribbon_obj.click_ribbon_item(tab_name, ribbon_button_name)   
        time.sleep(5)
          
        if file_type!="HTML Page":
            self.driver.find_element_by_name("HTML / Document Wizard").find_element_by_name(file_type).click()
            time.sleep(2)
        else:
            pass
        
        if 'tree_path' in kwargs:
            as_util_obj.select_tree_view_pane_item(kwargs['parent_obj'], kwargs['tree_path'])
            
        if 'recent_doc' in kwargs:
            #TODO:
            self.recent_html_doc_pane()  
        button_control=automation.ButtonControl(Name='Next >')
        button_control.Click()
        time.sleep(3) 
        button_control=automation.ButtonControl(Name='Finish')
        button_control.Click()
        time.sleep(3)
#         self.driver.find_element_by_name("Next >").click()
#         time.sleep(1)
#         self.driver.find_element_by_name("Finish").click()
#         time.sleep(1) 
#         
        ''' need too add steps from responsive and document'''
        ''' use default value defined in parameter'''
        #TODO: crate 1 function for 2nd page and import here        
        #TODO:  create 1 function for doc PDF for 2nd page 
        
    
    def recent_html_doc_pane(self):
        #TODO: NEED to test it
        self.driver.find_element_by_name("HTML / Document Wizard").find_element_by_id("ScrollbarThumb")[1].click()
        
    def new_parameters_wizard(self, **kwargs):
        '''
        Usage: new_parameters_wizard(Grouping_Options = "New single layer form", Default_Selection = True, Edit_Box_Controls = True, Controls_All_Parameters = True)
        Params: kwargs options -> Grouping_Options takes in the combobox element name as a string, the checkbox controls accept True or False as their values (True = click, False = don't)
        Description:
        Author: Lawrence
        Date: 4/26/17
        '''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        parent_obj = driver.find_element_by_name("New Parameters")
        #TODO: ID 1 - control box containing checkboxes (can't find internal elements without offset)
        #Parameter grouping options
        if 'Grouping_Options' in kwargs:
            asutilobj.select_item_from_dropdown_menu((By.ID, "23076"), "left", kwargs['Grouping_Options'], "no offset")
        #Clickable checkboxes
        if 'Default_Selection' in kwargs and kwargs['Default_Selection'] == True:
            driver.find_element_by_name('Don\'t show again and use default selection').click()
        if 'Edit_Box_Controls' in kwargs and kwargs['Edit_Box_Controls'] == True:
            driver.find_element_by_name('Create edit box controls').click()
        if 'Controls_All_Parameters' in kwargs and kwargs['Cobtrols_All_Parameters'] == True:
            driver.find_element_by_name('Create controls for all Parameters').click()
        if 'No_Run_Button' in kwargs and kwargs['No_Run_Button'] == True:
            driver.find_element_by_name('Don\t create run button').click()
        if 'Confirm' in kwargs and kwargs['Confirm'] == False:
            parent_obj.find_element_by_name("Cancel").click()
        else:
            parent_obj.find_element_by_name("OK").click()
        
                   

            