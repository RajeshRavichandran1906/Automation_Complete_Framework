'''
Created on June 13th, 2017
Status: re-automate for AS 8202
@author: Jesmin 
Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224529&group_by=cases:section_id&group_order=asc&group_id=156813s
Test Case = Local Domains - Geo-Location Widget - Verify map zoom to users current location 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver import ActionChains


class C2224529_TestClass(AS_BaseTestCase):

    def test_C2224529(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        poly_css='#Zip3_layer > path:nth-child(3)'  
        loc1 = "div[class='IBI_EMFObject internal_default claro map']"        
        test_case = "C2224518"
        
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)  
        
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ") 
        time.sleep(10) 
       
        """ verify initial Zoom to verify zoom level later   """     
        initial_zoom =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")
        
                
        """ Step 02: Click on Find My Location widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget("my_location")
        time.sleep(25)
        
        
        """ Click OK """
        expected_alert_msg="This browser is preventing users from getting the current position."
        utillobj.verify_js_alert(expected_alert_msg,'Step 03: Verify Alert')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)        
        
if __name__ == '__main__':
    unittest.main() 
