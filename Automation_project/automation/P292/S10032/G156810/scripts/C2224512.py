'''
@Created on June 27, 2017
@Status: re-automate for AS 8202
@Status: re-automate for AS 8202
@author: Jesmin 
@modification_date: 1/25/17
@Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224512
@Test Case = Remote Domains - Verify Geographic Role 'States' with 'Unique' USE & COLOR - rgb
'''

import time, unittest
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility, utillity
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area, as_esri_map_run
from selenium.webdriver.common.by import By



class C2224512_TestClass(AS_BaseTestCase):

    def test_C2224512(self):

        '''Object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)
        as_wizard_obj = as_wizard.AS_Wizard_Windows(driver)
        
        
        '''Local Variables'''
        server = asutilobj.parseinitfile('clientid')
        node = asutilobj.parseinitfile('node')
        project = asutilobj.parseinitfile('project_id')        
        sub_folder = asutilobj.parseinitfile('suite_id')
        tree_pane = server + node + project + "->" + sub_folder        
        layer_name = "World State"
        esri_css = "#" + layer_name + "_layer > path:nth-child(3)"
        test_case = "C2224512"
        legend_css = "#WorldStates_Legend_WorldStates" #"div[id='USCity_Legend_USCity'] svg path"
        other_css = "#" + layer_name + "_layer > path:nth-child(9)"
        
        '''________________________________   Designtime Test Script   ________________________________''' 
        asutilobj.select_tree_view_pane_item(tree_pane) 
        as_wizard_obj.Html_Document_Wizard("Home", "html_document")
        time.sleep(3)
        
        '''Step 1: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        '''Step 2: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown("world_states", "Requests->Parameters...")
        '''Step 3: Geographic role settings'''
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.settings_layer_name(layer_name, 14, 5)
        aspanelsobj.settings_geo_role("world_states", "State (Name)", Columns =  [{"row": "1", "value": "STATE"}, {"row": "2", "value": "COUNTRY"}, {"row": "3", "value": "COUNTRY_CODE"}])
        '''Step 4: Layer visualization settings'''
        aspanelsobj.set_html_esri_map_layer_visulization(Transparency = "100", Enable_Popups = "On", Default_Visibility = "On", Default_Extent = "On")
        '''Step 5: Symbol settings - names and move labels'''
        aspanelsobj.expand_panel('Settings')
        aspanelsobj.symbol_settings_using_field(Use_Name = "Unique", Field_Name = "COLOR_RGB")
        aspanelsobj.symbol_settings_unique_move_visible_labels("left", ["255,0,0", "0,49,148", "0,0,0"])
        self.unique_symbol_settings(aspanelsobj, "255,0,0", "MIDDLE CLASS", "Named Colors", ("basic", 180, 5, "#ff0000"), ("basic", 290, 5, "#000000"))
        self.unique_symbol_settings(aspanelsobj, "0,49,148", "UPPER CLASS", "Named Colors", ("basic", 100, 5, "#0000ff"), ("basic", 290, 5, "#000000"))
        self.unique_symbol_settings(aspanelsobj, "0,0,0", "LOWER CLASS", "Named Colors", ("basic", 290, 5, "#000000"), ("basic", 290, 5, "#000000"))
        '''Step 6: Save and Run'''
        asribbonobj.as_menu('save_as')
        try:
            asutilobj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
           
            
        """________________________________  Runtime  Test Script   ________________________________"""   
        poly_css="g[id^='World'] > path:nth-child(2)" 
        
        se_driver=asutilobj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)  
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, poly_css), wait_time=4800)         
                            
        bol=se_driver.find_element_by_css_selector(poly_css).is_displayed()
        utillobj.asequal(True, bol, "Step 0: Map Painted data. ")
        time.sleep(10)              
        
        """Step 06: Verify polygon color""" 
        as_esri_map_runobj.verify_esri_map_fill_color(poly_css,"blue", "Step 11: ")  
        time.sleep(2)              
        
        """Step 13: """
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools("World State", "show_tool")
        time.sleep(2)
        as_esri_map_runobj.esri_select_map_toc_tools("World State", "toggle_layer_legend")
        time.sleep(2)
        
        obj_css="div[id='World State_Legend_World State_0'] svg path"   
        expected_fill_color="blue"
        expected_stroke_color="black"   
        msg="Step 13: "     
        as_esri_map_runobj.verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color, expected_stroke_color,msg)      
               
        
        """Take screenshot """
        utillobj.take_screenshot(se_driver.find_element_by_css_selector("div.IBI_DesktopContainer.IBI_temp_unselect"),'C2224512_Base_step09', image_type='base')
        time.sleep(2)

        time.sleep(2)   
        asutilobj.close_se_driver(se_driver)
        
    def unique_symbol_settings(self, panels_obj, label_id, label_name, color_method, color, outline):
        panels_obj.expand_panel("Settings")
        color_functions = {"named colors": "color_picker_named_colors", "system colors": "color_picker_system_colors", "custom color": "color_picker_custom_color"}
        panels_obj.symbol_settings_unique_label_names([label_id], [label_name])
        panels_obj.color_picker_select_tab("color", Tab = color_method, Use = "unique")
        getattr(panels_obj, color_functions[color_method.lower()])(*color)
        panels_obj.expand_panel("Settings")
        panels_obj.color_picker_select_tab("outline", Tab = color_method, Use = "unique")
        getattr(panels_obj, color_functions[color_method.lower()])(*outline)
        


if __name__ == '__main__':
    unittest.main() 
