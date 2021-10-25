'''
Created on June 6th, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224523&group_by=cases:section_id&group_id=156811&group_order=asc
Test Case = Local Domains - Selection Widget - Verify tooltips for all icon 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver.support.ui import Select

class C2224523_TestClass(AS_BaseTestCase):

    def test_C2224523(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        poly_css='#Zip3_layer > path:nth-child(3)'          
        test_case = "C2224518"
        
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)  
        
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ") 
        time.sleep(1) 
       
        """ Step 02: Turn off Zip3 layer"""
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(5) 
        as_esri_map_runobj.esri_check_uncheck_layer("Zip3")
        time.sleep(2)  
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        #as_esri_map_runobj.esri_move_map_widget("toc", 600,10,x_off_set=100, y_off_set=20) 
        time.sleep(3)         
        
   
        """ Step 03: Click on Selection widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('selection')
        time.sleep(1) 
        """ Step 04a: draw a selection """ 
        se_driver.find_element_by_class_name("selectByExtent").click()
        time.sleep(3)  
          
        as_esri_map_runobj.esri_selection_widget_extent_unselect_tools("extent_select","#Customers_layer > circle:nth-child(61)", "#Customers_layer > circle:nth-child(329)")    
        time.sleep(3)  
        """ Step 04b:Verify selected point image and total count"""        
        as_esri_map_runobj.verify_esri_map_selected_point_image_text("Step 04b: ")           
         
                    
        """Step 4c: Hover Over all tools """
        as_esri_map_runobj.verify_esri_selection_widget_tooltips("point", "Step 4c: ")
        time.sleep(2)
        as_esri_map_runobj.esri_close_widget('selection')
 
        """ take screenshot  """
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021882_Base_step03', image_type='base')
        time.sleep(2)
        
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        as_esri_map_runobj.esri_check_uncheck_layer("Zip3") 
        as_esri_map_runobj.esri_select_main_menu_map_widget('selection')
        layer_dropdown=Select(se_driver.find_element_by_css_selector("select[id='select:opLayer']"))
        layer_dropdown.select_by_visible_text("Zip3")
        time.sleep(1)
 
        """ Step 4b: lasso on polygon to make selection """
        as_esri_map_runobj.esri_selection_widget_extent_unselect_tools("extent_select","#Zip3_layer > path:nth-child(2)", "#Zip3_layer > path:nth-child(7)")
        time.sleep(5)
     
        """Step 4b: Hover Over all tools """
        as_esri_map_runobj.verify_esri_selection_widget_tooltips("polygon","Step 4b: ")
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
        
if __name__ == '__main__':
    unittest.main() 
