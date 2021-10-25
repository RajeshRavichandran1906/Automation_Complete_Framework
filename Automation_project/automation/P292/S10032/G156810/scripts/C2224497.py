'''
Created on May 30, 2017
Status: re-automate for AS 8202
@author: Jesmin 
@modification_date: 1/29/2018
@modifier: Lawrence

Test Suite =http://lnxtestrail/testrail/index.php?/cases/view/2224497&group_by=cases:section_id&group_id=156810&group_order=asc
Test Case = ocal Domains - Verify Geographic Role "Point of Interest" by 'Single' use - Projected Coordinate System
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area
import pyautogui

class C2224497_TestClass(AS_BaseTestCase):

    def test_C2224497(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)     
        server = asutilobj.parseinitfile('clientid')
        folder = asutilobj.parseinitfile('suite_id')
        project = asutilobj.parseinitfile('project_id') 
        test_case = "C2224497"
        domain = "->Domains->"
        domain_folder = "P292_S10032_G157398"
        sub_folder = folder
        tree_pane = server + domain + domain_folder + "->" + sub_folder
        
        '''AS side code'''
        asutilobj.select_tree_view_pane_item(tree_pane)
        aswizardobj.Html_Document_Wizard("Home", "html_document")
        
        '''Step 1-2: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        
        '''Step 3: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown("incidents_date_param_500rec", "Requests->Parameters...")   
        
        '''Step 4: Settings'''
        aspanelsobj.expand_panel('Settings') 
        time.sleep(1)
        aspanelsobj.settings_layer_name("Customers", 14, 5)      
        aspanelsobj.settings_geo_role("incidents_date_param_500rec", "Point Of Interest") 
        driver.find_element_by_id("15081").click()
        asutilobj.select_item_from_dropdown_menu((By.NAME,"COMPLAINT_NO"), "left", "COMPLAINT_NO", "no offset") 
        time.sleep(1)
        driver.find_element_by_id("23509").click()
        aspanelsobj.expand_panel('Settings') 
        asutilobj.element_clicker(driver, (By.ID, "23736"), "left", "offset", 100, 110)
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("tab")
        time.sleep(1)
        elem = driver.find_element_by_id("3")      
        elem_name = elem.get_attribute("Name")
        print(elem_name)
        pyautogui.typewrite("2264")
        time.sleep(2)
        
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
          
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""  
        point_css = '#Customers_layer > circle:nth-child(296)'  
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)    
       
        '''  wait for map finish loading polygon ''' 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, point_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(point_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data.")
                
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2)           
        as_esri_map_runobj.verify_esri_map_fill_color(point_css,"demo_color", "Step 09: ")  
        time.sleep(2)  
             
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2224497Base_step02', image_type='base')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)
        
        
if __name__ == '__main__':
    unittest.main() 
