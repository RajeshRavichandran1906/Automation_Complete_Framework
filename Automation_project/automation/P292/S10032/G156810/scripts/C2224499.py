'''
Created on June 20th, 2017
Status: re-automate for AS 8202
@author: Jesmin 
@modification_date: 1/29/2018
@modifier: Lawrence
Test Suite =http://lnxtestrail/testrail/index.php?/cases/view/2224499&group_by=cases:section_id&group_id=156810&group_order=asc
Test Case = Local Domains - Local Domains - Verify Geographic Role 'US State(Name)' with 'Unique' use
'''

import unittest
import time
from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility
from common.lib import utillity
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area
import pyautogui
from selenium.webdriver import ActionChains


class C2224499_TestClass(AS_BaseTestCase):

    def test_C2224499(self):
        
        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)     
        server = asutilobj.parseinitfile('clientid')
        folder = asutilobj.parseinitfile('suite_id')
        project = asutilobj.parseinitfile('project_id') 
        test_case = "C2224499"
        poly_css="#US_States_layer > path:nth-child(37)"
        domain = "->Domains->"
        domain_folder = "P292_S10032_G157398"
        sub_folder = folder
        tree_pane = server + domain + domain_folder + "->" + sub_folder
        
        '''AS side code'''
        asutilobj.select_tree_view_pane_item(tree_pane)
        aswizardobj.Html_Document_Wizard("Home", "html_document")
        
        '''Step 1-2: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        '''Step 3: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown("world_states", "Requests->Parameters...")   
        
        '''Step 4: Settings'''
        #aspanelsobj.expand_pane_using_id("Settings")
        aspanelsobj.expand_panel('Settings') 
        time.sleep(1)
        aspanelsobj.settings_layer_name("US_States", 14, 5)      
        aspanelsobj.settings_geo_role("world_states", "US state (Name)", Columns=[{"row": "1", "value": "STATE"}]) 
        '''Step 5: Layer attributes'''
        aspanelsobj.set_html_esri_map_layer_attributes(["STATE","COUNTRY","COUNTRY_CODE", "POPULATION", "COLOR", "COLOR_RGB", "COLOR_HEX", "LABELS", "IMAGE"])
        aspanelsobj.set_html_esri_map_layer_attributes(["SIZE"])
        aspanelsobj.set_html_esri_map_layer_visulization(Transparency = "80", Enable_Popups = "On", Default_Extent = "On")
        aspanelsobj.symbol_settings_using_field(Use_Name = "Unique", Field_Name="LABELS")        
        aspanelsobj.symbol_settings_unique_move_visible_labels("left", ["Low Density","High Density","Mid Density"])           
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.unique_symbol_settings(aspanelsobj, "Low Density", "Low", "Named Colors", ("basic", 120, 5, "#800080"), ("basic", 290, 5, "#000000"), "5", "Solid")      

        aspanelsobj.expand_panel("Settings")
        aspanelsobj.unique_symbol_settings(aspanelsobj, "High Density", "High", "Custom Color", (0, 128, 0), (0, 0, 0), "3", "Dot")
   
        aspanelsobj.expand_panel("Settings")
        aspanelsobj.unique_symbol_settings(aspanelsobj, "Mid Density", "Mid", "System Colors", ("Highlight",), ("Background",), "3", "Dash")
        time.sleep(2)
        #aspanelsobj.collapse_pane_using_id("Settings")
        #time.sleep(2)
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators"""  
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)    
       
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800) 
        #time.sleep(4) 
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data.")
        time.sleep(2)        
        
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2)        
    
        get_layer_name_tooltip=se_driver.find_element_by_css_selector('ul.lyrItems > li.lyrName').get_attribute("title")
        print(get_layer_name_tooltip) 
        utillity.UtillityMethods.asequal(driver,"US_States", get_layer_name_tooltip,"Step 08a: verify layer tooltip") 
        
        """Step 08: Verify:selected shape appear on the map; Color matches; view is Default extent"""     
        as_esri_map_runobj.verify_esri_map_fill_color(poly_css,"green", "Step 08b: ")  
        time.sleep(2)   
        
        """Step 12: """
        as_esri_map_runobj.esri_select_map_toc_tools("US_States", "show_tool")
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools("US_States", "toggle_layer_legend")
        time.sleep(2)
        obj_css="#US_States_Legend_US_States  svg path"    
        expected_fill_color="highlight"
        expected_stroke_color="black"   
        msg="Step 12: "     
        as_esri_map_runobj.verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color, expected_stroke_color,msg)     
        
        
        """Step 13: """ 
        se_driver.find_element_by_css_selector("li[id='US_StatesDjt'] li[class='optsIcon']").click()
        time.sleep(2) 
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button("US_States", "transparency",value=0.9)
        
        # Take screenshot   (Step 08- shape & default extent will be verified via screenshot)    
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("#emfobject1_gc"),'C2224499_Base_step09', image_type='base')
       
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)   
            
        
if __name__ == '__main__':
    unittest.main() 
