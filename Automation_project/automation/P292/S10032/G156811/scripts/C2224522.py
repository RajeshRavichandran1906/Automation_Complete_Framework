'''
Created on June 6th, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224522&group_by=cases:section_id&group_id=156811&group_order=asc
Test Case = Local Domains - Selection Widget - Verify Users cannot make selection on Heat & Cluster layers
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import alert

class C2224522_TestClass(AS_BaseTestCase):

    def test_C2224522(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        layer_name = "Customers"
        poly_css='#Zip3_layer > path:nth-child(4)'          
        test_case = "C2224518"
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)  
        
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ")  
       
        """ STEP 2: Click on TOC Widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")   
        time.sleep(2)
        
        """ Step 3 :  Show Tools >> Toggle heatmap ON    """   
        as_esri_map_runobj.esri_select_map_toc_tools(layer_name, "toggle_options")
        time.sleep(2)
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name,"cluster",btn_color="sea_green",btn_css="#CustomersDjt .lyrInfo label[for='Customers_tgg']")
        time.sleep(2) 
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name,"heatmap",btn_color="sea_green",btn_css="#CustomersDjt .lyrInfo label[for='Customers_hm']")
        time.sleep(2) 
        
        """ 5: Un-Check Zip3 layer """
        layer_name = "Zip3"
        as_esri_map_runobj.esri_check_uncheck_layer(layer_name)
        time.sleep(2)
        
        """ Verify Layer is OFF """
        as_esri_map_runobj.verify_esri_map_layer_on_off(layer_name, False, "Step 05: ") 
        
        """ Screenshot TESTING BEFORE JS ALERT works """     
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021881_Base_step05', image_type='base')        
        
        """ Click on Selection widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc") 
        time.sleep(2)
        as_esri_map_runobj.esri_select_main_menu_map_widget("selection") 
        time.sleep(5)
       
        """ Click OK """
        expected_alert_msg="Selection Tools (message): Selection tool can not start at this moment. Either there are no layers on this map or they are not selectable. Make sure to turn On your layers and/or disable clusters"
        utillobj.verify_js_alert(expected_alert_msg,'Step 08: Verify Alert')
 
        
             
      
        """ Logout from BIP  """
        utillobj.infoassist_api_logout()
        se_driver.implicitly_wait(2)  
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
   
        
if __name__ == '__main__':
    unittest.main() 
