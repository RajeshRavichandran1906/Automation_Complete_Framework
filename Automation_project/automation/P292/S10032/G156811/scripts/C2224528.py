'''
Created on June 13th, 2017
Status: re-automate for AS 8202
@author: Jesmin 
Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224528&group_by=cases:section_id&group_order=asc&group_id=156813s
Test Case = Local Domains - Basemap Widget - Verify users can change basemap 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver import ActionChains


class C2224528_TestClass(AS_BaseTestCase):

    def test_C2224528(self):

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
       
        """ Step 02: Verify default basemap is Light Gray """
        as_esri_map_runobj.esri_select_main_menu_map_widget("basemap")
        time.sleep(1)
                
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021873_Base_step02', image_type='base')
        time.sleep(2)
        
        """ Step 03:  verify the list of basemaps """   
        exptd_basemap_list=['Imagery', 'Imagery with Labels', 'Streets', 'Topographic', 'Dark Gray Canvas', 'Light Gray Canvas', 'National Geographic', 
                            'Oceans', 'Terrain with Labels', 'OpenStreetMap', 'USA Topo Maps', 'USGS National Map']      
        print(exptd_basemap_list)
        as_esri_map_runobj.verify_esri_basemap_list(exptd_basemap_list,"Step 03: ")   
        
        """ Step 04:  Change the default basemap to Imagery """        
        as_esri_map_runobj.esri_select_basemap("Imagery","Step 04: ")
        
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021873_Base_step03', image_type='base')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
        
if __name__ == '__main__':
    unittest.main() 
