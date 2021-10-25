'''
Created on June 27, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224501
Test Case = Local Domains - Verify Geographic Role "US Zip3" using 'Color' use
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility


class C2224501_TestClass(AS_BaseTestCase):

    def test_C2224501(self):


        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)      
        test_case = "C2224518"

            
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""     
        poly_css = "#Zip3_layer > path:nth-child(3)" 
        

        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)    
       
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector('#Zip3_layer > path:nth-child(3)').is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ")
        
        'Turn off Customer layer'
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(2)
        as_esri_map_runobj.esri_check_uncheck_layer("Customers")
        time.sleep(2)
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(2)
            
        # Verify zip3 color   
        as_esri_map_runobj.verify_esri_map_fill_color('#Zip3_layer > path:nth-child(4)', "drak_green", "Step 08: ")
        
        
        
        """ Step 09: Click on TOC widget"""
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools('Zip3','toggle_layer_legend')
        time.sleep(10)
        as_esri_map_runobj.esri_move_map_widget("toc", 600,10,x_off_set=100, y_off_set=20)
        time.sleep(3) 
        
        
        obj_css="#Zip3_Legend_Zip3_0  div svg path" 
        expected_fill_color="drak_green"
        expected_stroke_color="light_gray1"                  
        as_esri_map_runobj.verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color, expected_stroke_color,"Step 09: ")       
        
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2224501_Base_step09', image_type='base')
        time.sleep(2) 
        
        
if __name__ == '__main__':
    unittest.main() 
