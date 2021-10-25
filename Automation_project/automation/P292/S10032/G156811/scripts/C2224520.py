'''
Created on June 5th, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157398
Test Case = Local Domains - Default Extent - Verify zoom 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility


class C2224520_TestClass(AS_BaseTestCase):

    def test_C2224520(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        poly_css='#Zip3_layer > path:nth-child(4)' 
        layers=["Customers","Zip3"] 
        test_case = "C2224518"
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)  
        
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ")  
       
        """  Step 3: Un-check Customer & Zip3 layer """ 
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc") 
        time.sleep(2)

        for i in layers:
            as_esri_map_runobj.esri_check_uncheck_layer(i) 
            time.sleep(2)   
    
        """  take screenshot  """ 
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021876_Base_step03', image_type='base')
        
        """  Step 3: verify points & polygons are not visible in the map  """         
        for i in layers:
            as_esri_map_runobj.verify_esri_map_layer_on_off(i, False,"Step 3: "+i+ " Layer is unchecked.")
                     
        """ Step 4: Check Customers & Zip3 layers """ 
        for i in layers:
            as_esri_map_runobj.esri_check_uncheck_layer(i) 
            time.sleep(2)  
                     
        """ Step 6: verify points & polygons are  visible in the map """  
        for i in layers:
            as_esri_map_runobj.verify_esri_map_layer_on_off(i,True,"Step 6: "+i+" Layer is checked")
        
        """ take screenshot """ 
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021876_Base_step06', image_type='base')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
   
        
if __name__ == '__main__':
    unittest.main() 
