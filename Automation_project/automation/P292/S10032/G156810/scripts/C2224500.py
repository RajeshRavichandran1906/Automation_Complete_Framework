'''
@Created on June 26th, 2017
@Status: re-automate for AS 8201m
@author: Jesmin 
@Test Suite  = http://lnxtestrail/testrail/index.php?/cases/view/2224500&group_by=cases:section_id&group_order=asc&group_id=156810
@Test Case = Local Domains - Verify Geographic Role 'US County' with 'Unique' use & Label
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


class C2224500_TestClass(AS_BaseTestCase):

    def test_C2224500(self):
        
        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)     
        
        """Local variables"""
        server = asutilobj.parseinitfile('clientid')
        node = asutilobj.parseinitfile('node')
        project = asutilobj.parseinitfile('project_id')        
        sub_folder = asutilobj.parseinitfile('suite_id')
        tree_pane = server + node + project + "->" + sub_folder
        test_case = "C2224500"
        fex="us_county"
        req_panel_menu= "Requests->Parameters..."
        
        '''===================================== AS side code ================================='''  
        asutilobj.select_tree_view_pane_item(tree_pane) 
        aswizardobj.Html_Document_Wizard("Home", "html_document")
        
        '''Step 1-2: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 

        '''Step 2: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown(fex,req_panel_menu )   
        
        '''Step 3: Settings'''
        aspanelsobj.expand_panel('Settings') 
        time.sleep(1)
        aspanelsobj.settings_layer_name("US_County", 14, 5)      
        aspanelsobj.settings_geo_role("us_county", "US county (Name)", Columns=[{"row": "1", "value": "CNTYNAME"}]) 
        
            
        aspanelsobj.set_html_esri_map_layer_attributes(["STNAME"])              
        aspanelsobj.set_html_esri_map_layer_visulization(Enable_Popups="On", Transparency="100")        
        
        
        
        aspanelsobj.symbol_settings_using_field(Use_Name = "Unique", Field_Name="STNAME")  
                  
        aspanelsobj.symbol_settings_unique_move_visible_labels("left", ["ARKANSAS","COLORADO","ILLINOIS"])            
    
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.unique_symbol_settings(aspanelsobj, "ARKANSAS", "AK", "Named Colors", ("basic", 110, 5, "#0000ff"), ("basic", 290, 5, "#000000"), "5", "Solid")      

        aspanelsobj.expand_panel("Settings")
        aspanelsobj.unique_symbol_settings(aspanelsobj, "COLORADO", "CL", "Named Colors", ("basic", 120, 5, "#800080"), ("basic", 290, 5, "#000000"), "3", "Dash")
   
        aspanelsobj.expand_panel("Settings")
        aspanelsobj.unique_symbol_settings(aspanelsobj, "ILLINOIS", "IL", "Named Colors", ("basic", 50, 5, "#008080"), ("basic", 290, 5, "#000000"), "3", "Dash")
        time.sleep(1)
      
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        """Test Locators""" 
        loc1 = "div[class='IBI_EMFObject internal_default claro map']"  
        poly_css="#US_County_layer > path:nth-child(94)"
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)
        asutilobj.click_html_webpage(se_driver.title, se_driver.name)    
       
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 1: Map Painted data.")
        time.sleep(2)        
        
        """Step 11: Verify: TOC widget shows the label ; Color matches from design-time & runtime""" 
        as_esri_map_runobj.verify_esri_map_fill_color(poly_css,"red", "Step 11: ")  
        time.sleep(2)              
               
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools("US_County", "show_tool")
        time.sleep(2)
                
        """Step 13: """
        as_esri_map_runobj.esri_select_map_toc_tools("US_County", "toggle_layer_legend")
        time.sleep(2)    
        obj_css="#US_County_layer > path:nth-child(88)" 
        expected_fill_color="teal_2"
        expected_stroke_color="black"   
        msg="Step 13: "     
        as_esri_map_runobj.verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color,expected_stroke_color,msg)  
        
        """Step 14: Click on "Toggle Option"; Draw the opacity slider back & forth; Verify:transparency increases & decreases"""        
        as_esri_map_runobj.esri_select_map_toc_tools("US_County","toggle_options")
        time.sleep(2)   
        as_esri_map_runobj.toggle_cluster_heatmap_transparency_button("US_County",'transparency' ,value= 0.2)
        time.sleep(2) 
           
        """Take screenshot """
        utillobj.take_screenshot(se_driver.find_element_by_css_selector(loc1),'C2224500_Base_step14', image_type='base')
        time.sleep(2)
        asutilobj.close_se_driver(se_driver)
        
if __name__ == '__main__':
    unittest.main() 
