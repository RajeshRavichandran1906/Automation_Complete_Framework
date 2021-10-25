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


class C2224519_TestClass(AS_BaseTestCase):

    def test_C2224519(self):


        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)             

         
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        poly_css='#Zip3_layer > path:nth-child(4)' 
        layer_name="Customers" 
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
       
        """ 2: HOVER OVER & VERIFY TOOLTIPS FOR ALL MAIN MENU WIDGETS """
        as_esri_map_runobj.verify_esri_main_menu_tooltips(msg="Step 02: ")
        driver.implicitly_wait(2)
        
        """ 3: Click on TOC Widget & turn cluster & heatmap on """
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc") 
        time.sleep(2)        
        as_esri_map_runobj.esri_select_map_toc_tools("Customers", "toggle_options") 
        time.sleep(2) 
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name,"cluster",btn_color="sea_green",btn_css="#CustomersDjt .lyrInfo label[for='Customers_tgg']")
        time.sleep(2)
        
        se_driver.find_element_by_css_selector(layer_name_css).click() #closing toggle opion button, layer otherwise doesn't get recognized  
        as_esri_map_runobj.esri_select_map_toc_tools("Customers", "toggle_options") 
        time.sleep(2)
         
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button(layer_name,"heatmap",btn_color="sea_green",btn_css="#CustomersDjt .lyrInfo label[for='Customers_hm']")
        time.sleep(2) 
        
        """Verify Cluster appears """  
        se_driver.find_element_by_css_selector(layer_name_css).click() #closing toggle opion button, layer otherwise doesn't get recognized             
        as_esri_map_runobj.verify_esri_map_cluster_image_text(layer_name, 10, 1,"81","Step 03: ")
               
        """ Take screenshot """
        #utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021879_Base_step03', image_type='base')
  
        """ 4: HOVER OVER & VERIFY TOOLTIPS FOR ALL MAIN MENU WIDGETS """ 
        as_esri_map_runobj.esri_select_map_toc_tools("Customers", "toggle_options") 
        time.sleep(2)   
        as_esri_map_runobj.verify_esri_toc_widget_tooltips(layer_name, "point","Step 04: ")
        time.sleep(2)  

        """ 6:  Minimize TOC widget widget  """
        as_esri_map_runobj.esri_minimize_maximize_widget("toc")   
        time.sleep(1)    
              
        """ 6:  Click on the TOC widget icon & Verify widget is minimized """
        as_esri_map_runobj.verify_esri_map_widget_minimize_maximize("minimize",'Step 06: ')
        time.sleep(2) 
        asutilobj.close_se_driver(se_driver)  
   
        
if __name__ == '__main__':
    unittest.main() 
