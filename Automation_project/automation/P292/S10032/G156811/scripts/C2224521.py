'''
Created on June 6th, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224521&group_by=cases:section_id&group_id=156811&group_order=asc
Test Case = Local Domains - Default Extent - Verify zoom Local Domains - TOC Widget - Verify users can turn On/Off heatmap on a point layer
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility


class C2224521_TestClass(AS_BaseTestCase):

    def test_C2224521(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        layer_name = "Customers"
        poly_css='#Zip3_layer > path:nth-child(4)'  
        layer_name_css="#"+layer_name+ "Djt > div > ul.optionsBox > li.BoxLi > ul > li.optsIcon.optsActive"
        
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
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name, opt="cluster", val="")
        time.sleep(2)
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name, opt="heatmap", val="")
        time.sleep(2)
        """  take screenshot  """ 
        #utillobj.take_screenshot(driver.find_element_by_css_selector("#emfobject1_gc"),'C2021878_Actual_step03', image_type='actual')
        
        """ 4: un check Customer layer """
        se_driver.find_element_by_css_selector(layer_name_css).click() #closing toolbox, layer otherwise doesn't get recognized    
        as_esri_map_runobj.esri_check_uncheck_layer(layer_name)
        time.sleep(2)
        
        """ Verify Layer is off """ 
        as_esri_map_runobj.verify_esri_map_layer_on_off(layer_name,False,"Step 04: "+layer_name+" Layer is OFF ")           
        """  Verify Cluster  OFF """ 
        as_esri_map_runobj.verify_esri_map_layer_cluster_on_off(layer_name,0,"Step 04 : ")
        
        """ 5: Check Layer back to ON >> Toggle heatmap OFF   """
        as_esri_map_runobj.esri_check_uncheck_layer(layer_name)
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools(layer_name, "toggle_options")       
        time.sleep(2)
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name, opt="heatmap") 
        time.sleep(2) 
        
            
        """  Verify Layer is ON """ 
        se_driver.find_element_by_css_selector(layer_name_css).click() #closing toolbox, layer otherwise doesn't get recognized   
        as_esri_map_runobj.verify_esri_map_layer_on_off(layer_name,True,"Step 05: "+layer_name+" Layer is ON ")
        
        """  Verify Cluster  OFF """ 
        as_esri_map_runobj.verify_esri_map_layer_cluster_on_off(layer_name,0,"Step 04 : ") 
        
        """  take screenshot  """ 
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021878_Base_step05', image_type='base')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)             
      

      
   
        
if __name__ == '__main__':
    unittest.main() 
