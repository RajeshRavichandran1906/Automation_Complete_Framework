'''
@Created on May 30, 2017
@Status: re-automate for AS 8201m
@author: Jesmin 
@modification_date: 1/25/17
@Test_Suite = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224518&group_by=cases:section_id&group_order=asc&group_id=156811
@Test_Case = Local Domains - Default Extent - Verify zoom 
'''

import unittest
import time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area, as_environment_tree


class C2224518_TestClass(AS_BaseTestCase):

    def test_C2224518(self):

        '''class object instantiation for both drivers'''
        driver = self.driver      
        as_util_obj = as_utility.AS_Utillity_Methods(driver)
        as_panels_obj = as_panels.AS_Panels(driver)
        as_wizard_obj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj= as_html_canvas_area.AS_Html_Canvas(driver)     
        
        
        '''Local variables'''
        test_case = "C2224518" 
        server = as_util_obj.parseinitfile('clientid')
        node = as_util_obj.parseinitfile('node')
        project = "P292_S10032_G157398"      
        sub_folder = as_util_obj.parseinitfile('suite_id')
        tree_pane = server + node + project + "->" + sub_folder        
        fexes = ["customer_layer", "zip3_baselayer"]  
        labels= ["Standard","Valued","Elite"] 
        custom_labels=["Repeated Customer","Valued Customer","Hi-Valued Customer"]
        
        '''===================================== AS side code ================================='''    
    
        as_util_obj.select_tree_view_pane_item(tree_pane) 
        as_wizard_obj.Html_Document_Wizard("Home", "html_document")
        time.sleep(3)
        
        '''Step 1-2: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        time.sleep(3)
        
        '''Step 3: Add fex'''
        for i in fexes:
            as_panels_obj.select_new_request_from_split_dropdown(i, "Requests->Parameters...")    
            
        '''Step 4: Settings'''
        as_panels_obj.expand_panel('Settings') 
        time.sleep(1)
        as_panels_obj.settings_layer_name("Customers", 14, 5)      
        as_panels_obj.settings_geo_role("customer_layer", "Point Of Interest") 
        driver.find_element_by_id("15081").click()
        as_util_obj.select_item_from_dropdown_menu((By.NAME,"CUST_ID"), "left", "CUST_ID", "no offset") 
        time.sleep(1)
        driver.find_element_by_id("23509").click()
        
        as_panels_obj.symbol_settings_using_field(Use_Name = "Unique", Field_Name="CUST_TYPE")  
        driver.find_element_by_id("23602").click()
        driver.find_element_by_id("23602").send_keys("15")
              
        as_panels_obj.symbol_settings_unique_move_visible_labels("left",labels ) 
        as_panels_obj.symbol_settings_unique_label_names(labels, custom_labels)
        
        driver.find_element_by_name("Standard").click()
        driver.find_element_by_id("23706").click()
        as_panels_obj.color_picker_web_palette(1, 3, "color")
        as_panels_obj.expand_panel('Settings')
        driver.find_element_by_name("Valued").click()
        driver.find_element_by_id("23706").click()
        as_panels_obj.color_picker_web_palette(1, 7, "color")
        as_panels_obj.expand_panel('Settings')
        '''Click on new layer button'''
        as_util_obj.element_clicker(driver, (By.ID, "12345"), "left", "offset", 240, 40) 
        as_panels_obj.settings_layer_name("Zip3", 14, 25)      
        as_panels_obj.settings_geo_role("zip3_baselayer", "US postal code (3 digits)", Columns =  [{"row": "1", "value": "ZIP3"}])
        as_panels_obj.symbol_settings_using_field(Use_Name = "Color", Field_Name = "POP2010")
        as_panels_obj.symbol_settings_color(By = "Natural Jenks")
        time.sleep(1) 
        
        asribbonobj.as_menu('save_as')
        try:
            as_util_obj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
           

               
        
  
        
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""
        loc1 = "div[class='IBI_EMFObject internal_default claro map']"       
        esri_css = "#Zip3_layer > path:nth-child(3)" 
        
        
        se_driver=as_util_obj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        as_util_obj.click_html_webpage(se_driver.title, se_driver.name)    
       
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, esri_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector('#Zip3_layer > path:nth-child(3)').is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data. ")
        
        """ verify initial Zoom to verify zoom level later   """     
        initial_zoom =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")
        time.sleep(5)
        print(initial_zoom)
                 
        """ zoom 2 times using + button """       
        as_esri_map_runobj.esri_zoom_in_out('in', 3)
        time.sleep(5)
         
        """ get the value of current zoom level """
        plus_button_zoom =se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")        
        print(plus_button_zoom)
        utillobj.as_GE(int(plus_button_zoom),int(initial_zoom),"Step 3: Verify map zoomed using Plus zoom button")
 
        """ take screenshot  """
        #utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2021875_Base_step05', image_type='base')        
         
        """ Step 4 Click on Default Extent widget """
        as_esri_map_runobj.esri_select_main_menu_map_widget('home')
        time.sleep(2)
           
        """ get current zoom level """
        default_extent_widget_zoom = se_driver.find_element_by_css_selector(loc1).get_attribute("data-zoom")    
        print(default_extent_widget_zoom)
        utillobj.as_LE(int(default_extent_widget_zoom),int(plus_button_zoom),"Step 4: Verify map zoomed using Default extent widget.")  
        time.sleep(2)
        as_util_obj.close_se_driver(se_driver)         
        
if __name__ == '__main__':
    unittest.main() 
