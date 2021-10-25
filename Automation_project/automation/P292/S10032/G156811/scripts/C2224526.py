'''
Created on June 12th, 2017
Status: re-automate for AS 8202
@author: Jesmin 
Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224526&group_by=cases:section_id&group_order=asc&group_id=156813s
Test Case = Local Domains - Selection Widget - Verify Select features within a distant 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver import ActionChains


class C2224526_TestClass(AS_BaseTestCase):

    def test_C2224526(self):

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
        
        """ Step 02: Turn of Zip3 layer"""
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(1)
        as_esri_map_runobj.esri_check_uncheck_layer("Zip3")
        time.sleep(1) 
        as_esri_map_runobj.esri_select_main_menu_map_widget('toc')
        time.sleep(1)
   
        """ AStep 03: Click on Selection widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('selection')
        time.sleep(2) 
        as_esri_map_runobj.esri_move_map_widget("selection",600,10,x_off_set=100, y_off_set=20) 
        time.sleep(2) 
        as_esri_map_runobj.esri_selection_widget_click_tools("zoom_to_layer") 
        time.sleep(2) 
        
        """ verify zoom level  """     
        zoom_to_layer =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom") 
        se_driver.implicitly_wait(5)
        utillobj.as_GE(zoom_to_layer,initial_zoom,"Step 3: Verify map zoomed using  zoom_to_layer button")
        
        """ Step 04a: distance = 10 ;leave default ml selected; click on a marker """
        as_esri_map_runobj.esri_selection_widget_distance_tool("distance_select",10,"ml","#Customers_layer > circle:nth-child(93)")        
        time.sleep(2)
        
        """ Verify selected point image and total count"""
        as_esri_map_runobj.verify_esri_map_selected_point_image_text("Step 04a: ")        
               
        """ Steo 04b: Click on Select Feature to Delete  """  
        as_esri_map_runobj.esri_selection_widget_extent_unselect_tools("unselect","#SelectedGraphics_layer > image:nth-child(5)", "#SelectedGraphics_layer > image:nth-child(9)")                  
        time.sleep(3) 
        """Verify total number of selected point is less than original"""
        as_esri_map_runobj.verify_esri_map_selected_point_image_text("Step 04b: ")
    
        """ Step 05: Click on the icon shows total marker selected  """
        as_esri_map_runobj.esri_selection_widget_click_tools("zoom_to_selection")
        time.sleep(2)  
             
        """ verify zoom level  """     
        zoom_to_selection =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")                
        utillobj.as_GE(initial_zoom,zoom_to_selection,"Step 05: Verify map zoomed using zoom_to_selection button")
        
       
        """ Step 07: Click on "Clear Selection" button"""
        as_esri_map_runobj.esri_selection_widget_click_tools("clear_selection")
        time.sleep(1)  
        
        """ Verify there is no selected points """
        as_esri_map_runobj.verify_esri_map_selected_unselected_points("Step 07: Selection has been removed")
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
        
if __name__ == '__main__':
    unittest.main() 
