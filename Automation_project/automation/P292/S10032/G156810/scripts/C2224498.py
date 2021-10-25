'''
Created on June 21, 2017
Status: re-automate for AS 8202
@author: Jesmin 
@modification_date: 1/29/2018
@modifier: Lawrence

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224498&group_by=cases:section_id&group_id=156810&group_order=asc
Test Case = Local Domains - Verify Geographic Role 'US Cities' with 'Single' Use & Size
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
from selenium.webdriver import ActionChains

class C2224498_TestClass(AS_BaseTestCase):

    def test_C2224498(self):

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
        test_case = "C2224498"
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
        aspanelsobj.select_new_request_from_split_dropdown("us_city", "Requests->Parameters...")   
   
        '''Step 3: Settings'''
        aspanelsobj.expand_panel('Settings') 
        time.sleep(1)
        aspanelsobj.settings_layer_name("US_City", 14, 5)      
        aspanelsobj.settings_geo_role("us_city", "US city (Name)", Columns=[{"row": "1", "value": "CITY_NAME"}]) 
        aspanelsobj.set_html_esri_map_layer_visualization_generic((2, "100"), (4, "On"), (5, "On"), (6, "On"))#
               
        aspanelsobj.set_html_esri_map_layer_attributes(["STNAME","STALPHCR"])
        
        driver.find_element_by_id("23705").click()
        aspanelsobj.color_picker_web_palette(10, 12, "color")
        aspanelsobj.expand_panel('Settings')
        driver.find_element_by_id("23602").click()
        driver.find_element_by_id("23602").send_keys("18")
        asutilobj.select_item_from_dropdown_menu((By.NAME,"Image Source"), "left", "Diamond", "no offset") 
        time.sleep(1)
        
      
        
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
          
    
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""  
        point_css="g[id^='US'] > path:nth-child(1110)"   
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)    
       
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, point_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(point_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data.")
        time.sleep(2)        
        
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2)
        
        action = ActionChains(driver)
        layer_name_tooltip=se_driver.find_element_by_css_selector('ul.lyrItems > li.lyrName')
        action.move_to_element(layer_name_tooltip) 
        del action 
        time.sleep(5)
        
        """Step 08: Verify:selected shape appear on the map; Color matches; view is Default extent"""     
        as_esri_map_runobj.verify_esri_map_fill_color(point_css,"outrageous_orange", "Step 08: ")  
        time.sleep(2)
                      
        """Step 09: Click on a point; Verify info window appears"""
        se_driver.find_element_by_css_selector(point_css).click()
        time.sleep(2)
        as_esri_map_runobj.verify_esri_map_feature_tooltip(point_css, "STALPHCR: MS", "Step 09: ")
    
        # Take screenshot   (Step 08- shape & default extent will be verified via screenshot)    
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("div.IBI_DesktopContainer.IBI_temp_unselect"),'C2022159_Actual_step09', image_type='')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)
        
if __name__ == '__main__':
    unittest.main() 
