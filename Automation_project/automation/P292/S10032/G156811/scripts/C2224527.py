'''
Created on June 12th, 2017
Status: re-automate for AS 8202
@author: Jesmin 
Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224527&group_by=cases:section_id&group_order=asc&group_id=156813s
Test Case = Local Domains - TOC & Selection widget - Verify zoom to layer extent  
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver import ActionChains


class C2224527_TestClass(AS_BaseTestCase):

    def test_C2224527(self):

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
       
        """ Get initial Zoom to verify zoom level later   """     
        initial_zoom =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")       
        time.sleep(2) 
        
        """ 2 : Click on TOC widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')  
        time.sleep(2)
                 
        """ 3:  zoom 4 times using + button  & Click on Layer extent icon"""
        as_esri_map_runobj.esri_zoom_in_out('in',5)
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools("Customers", "zoom_to_layer")
        time.sleep(2)
         
        """ get the value of current zoom level """
        toc_zoom_to_layer_extent =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")
        utillobj.as_LE(initial_zoom,toc_zoom_to_layer_extent,"Step 3: Verify map zoomed using TOC widget zoom to layer extent button")
            
        """ take screenshot  """
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021880_Bases_step05', image_type='baase')
        time.sleep(2)
        
        """ Close TOC widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')  
        
        """ Click on Selection widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('selection')
        time.sleep(2)
        
        """ 4:  zoom out 4 times using + button  & Click on Layer extent icon"""
        as_esri_map_runobj.esri_zoom_in_out('out', 4)
        time.sleep(2)       
       
        as_esri_map_runobj.esri_selection_widget_click_tools("zoom_to_layer")
        time.sleep(2)
         
        """ get the value of current zoom level """
        selection_zoom_to_layer_extent= se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")
        utillobj.asequal(toc_zoom_to_layer_extent,selection_zoom_to_layer_extent,"Step 4: Verify map zoomed using Selection widget zoom to layer extent button")
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  

        
if __name__ == '__main__':
    unittest.main() 
