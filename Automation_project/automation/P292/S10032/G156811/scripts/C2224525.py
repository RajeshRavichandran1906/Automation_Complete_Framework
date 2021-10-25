'''
Created on June 12th, 2017
Status: re-automate for AS 8202
@author: Jesmin 

Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224525&group_by=cases:section_id&group_order=asc&group_id=156813s
Test Case = Local Domains - Selection Widget - Verify Select features within a polygon 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from selenium.webdriver import ActionChains


class C2224525_TestClass(AS_BaseTestCase):

    def test_C2224525(self):

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
        as_esri_map_runobj.esri_move_map_widget("selection", 600,10,x_off_set=100, y_off_set=20) 
        time.sleep(2)
                    
        """ click on 3 location to make selection """
        se_driver.find_element_by_css_selector("li.selectByPolygon").click()
        time.sleep(5)
        
        browser=utillobj.parseinitfile('browser')        
        if browser=='Firefox':
            as_esri_map_runobj.esri_selection_widget_polygon_tool("#Customers_layer > circle:nth-child(61)", "#Customers_layer > circle:nth-child(61)")
            time.sleep(10)
            as_esri_map_runobj.esri_selection_widget_polygon_tool("#Customers_layer > circle:nth-child(71)", "#Customers_layer > circle:nth-child(71)")
            time.sleep(5)
            as_esri_map_runobj.esri_selection_widget_polygon_tool("#Customers_layer > circle:nth-child(330)", "#Customers_layer > circle:nth-child(330)")
            time.sleep(5)
            as_esri_map_runobj.pynput_double_click("#Customers_layer > circle:nth-child(61)")        
        else:      
            as_esri_map_runobj.click("#Customers_layer > circle:nth-child(61)")
            as_esri_map_runobj.click("#Customers_layer > circle:nth-child(71)")
            as_esri_map_runobj.click("#Customers_layer > circle:nth-child(330)")
            action1=ActionChains(se_driver)
            source=se_driver.find_element_by_css_selector("#Customers_layer > circle:nth-child(61)")
            action1.double_click(source).perform()       
        time.sleep(10) 
        """ Verify selected point image and total count"""
        as_esri_map_runobj.verify_esri_map_selected_point_image_text("Step 04: ")
           
        """ Step 06: Click on Select Feature to Delete""" 
        se_driver.find_element_by_css_selector("li.clearSelection2").click()
        time.sleep(2)
        as_esri_map_runobj.esri_selection_widget_polygon_tool("#Customers_layer > circle:nth-child(61)", "#Customers_layer > circle:nth-child(71)")
        time.sleep(10)
        """ take screenshot  """
        #utillobj.take_screenshot(se_driver.find_element_by_css_selector("emfobject1_gc"),'C2224525_Base_step06', image_type='base')
        time.sleep(2) 
        """Verify total number of selected point is less"""
        as_esri_map_runobj.verify_esri_map_selected_point_image_text("Step 04: ")                
               
        """ Step 06b: Click on the icon shows total marker selected """
        as_esri_map_runobj.esri_selection_widget_click_tools("zoom_to_selection")
        time.sleep(2)
        """ get current zoom level """
        zoom_to_selection = se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")          
        utillobj.as_GE(zoom_to_selection,initial_zoom,"Step 07b: Verify map zoomed using zoom to selection button.")
            
        """ Step 08 : Click on "Clear Selection" button """
        as_esri_map_runobj.esri_selection_widget_click_tools("clear_selection")
        time.sleep(2)     
        
        """Verify all selections are removed"""
        as_esri_map_runobj.verify_esri_map_selected_unselected_points( "Step 07: all points are deselected")
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)  
        
if __name__ == '__main__':
    unittest.main() 
