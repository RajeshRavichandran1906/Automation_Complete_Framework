'''
@Created on June 27, 2017
@Status: re-automate for AS 8201M
@author: Jesmin 
@Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224502&group_by=cases:section_id&group_id=156810&group_order=asc
'''

import time, unittest
from common.lib.as_basetestcase import AS_BaseTestCase
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from common.lib import as_utility, utillity
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area, as_esri_map_run
from selenium.webdriver.common.by import By
import uiautomation as automation
import pyautogui
from pynput.keyboard import Controller


class C2224502_TestClass(AS_BaseTestCase):

    def test_C2224502(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)        
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)
        as_wizard_obj= as_wizard.AS_Wizard_Windows(driver)
        
        '''Local Variables'''       
        server = asutilobj.parseinitfile('clientid')
        node = asutilobj.parseinitfile('node')
        project = asutilobj.parseinitfile('project_id')        
        sub_folder = asutilobj.parseinitfile('suite_id')
        tree_pane = server+ node+project + "->" + sub_folder 
        layer_name = "Country"
        esri_css = "#Country_layer > path:nth-child(66)" #Country_layer > path:nth-child(66)
        test_case = "C2224502"
        tooltip_data="COUNTRY: Greenland"
        
       
        '''===================================== AS side code ================================='''  
        asutilobj.select_tree_view_pane_item(tree_pane)
        time.sleep(3) 
        as_wizard_obj.Html_Document_Wizard("Home", "html_document")
        time.sleep(3)
        
        '''Step 1: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        
        '''Step 2: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown("country_layer", "Requests->Parameters...")
        
        '''Step 3: Geographic role settings'''
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.settings_layer_name(layer_name, 14, 5)
        aspanelsobj.settings_geo_role("country_layer", "Country (Name)", Columns =  [{"row": "1", "value": "COUNTRY"}])
        
        '''Step 4: Layer visualization settings'''      
        aspanelsobj.set_html_esri_map_layer_attributes(["COUNTRY", "ISO2", "ISO3", "AREA_KM2", "COUNTRY_CODE", "GDP_USD", "GD_USD_BILLIONS", "COLOR_NAMED", "COLOR_RGB", "COLOR_HEX", "LABELS"])
        aspanelsobj.set_html_esri_map_layer_visulization(Enable_Popups = "On")
        
        ac_la = ActionChains(driver)
        ac_la.move_to_element_with_offset(driver.find_element_by_name('Layer Attributes'), 280, -10).click().perform()
        layer_elem = driver.find_element_by_name("COLOR_HEX")
        ac = ActionChains(driver)
        ac.key_down(Keys.CONTROL)
        ac.click(layer_elem)
        layer_elem = driver.find_element_by_name("LABELS")
        ac.click(layer_elem)
        ac.key_up(Keys.CONTROL)
        ac.perform()
        driver.find_element_by_name("Button1").click()
        #aspanelsobj.set_html_esri_map_layer_visulization(Enable_Popups = "On", Default_Visibility = "On")
        
        '''Step 5: Symbol Settings'''
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.symbol_settings_using_field(Use_Name = "Dynamic")
        aspanelsobj.symbol_settings_dynamic(Dynamic_Label = "COUNTRY", Dynamic_Color = "COLOR_HEX")
        time.sleep(1)
   
        
        '''Step 6: Save and Run '''
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
                 
        '''________________________________   Runtime Test Script   ________________________________'''     
            
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        try:
            driver.find_element_by_name("OK").click()
        except: 
            print("no alert")
        time.sleep(3)
        
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, "#Country_layer > path:nth-child(66)"), wait_time=4800)    
        as_esri_map_runobj.verify_esri_map_fill_color("#Country_layer > path:nth-child(66)", "teal", "Teal ")
        
        se_driver.find_element_by_css_selector(esri_css).click()
        time.sleep(1)
        as_esri_map_runobj.verify_esri_map_feature_tooltip(esri_css,tooltip_data,"Step 11: ")
        
        '''Close driver'''  
        asutilobj.close_se_driver(se_driver)
          
        
if __name__ == '__main__':
    unittest.main() 
