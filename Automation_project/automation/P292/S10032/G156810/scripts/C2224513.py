'''
@Created on June 27, 2017
@Status: re-automate for AS 8201m
@author: Jesmin 
@modification_date: 1/25/17

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2224513&group_by=cases:section_id&group_order=asc&group_id=156810
Test Case = Local Domains - Verify Geographic Role "US Zip3" using 'Color' use
'''

import time, unittest
from common.lib.as_basetestcase import AS_BaseTestCase
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area, as_esri_map_run
from common.lib import as_utility, utillity




class C2224513_TestClass(AS_BaseTestCase):

    def test_C2224513(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        utility_obj= utillity.UtillityMethods(driver)
        as_util_obj = as_utility.AS_Utillity_Methods(driver)       
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)
        esri_css = "#WorldCity_layer > circle:nth-child(558)" 
        esri_css2 = "#WorldCity_layer > circle:nth-child(605)"
        
        
        ''' Local Variables'''
        server = as_util_obj.parseinitfile('clientid')
        node = as_util_obj.parseinitfile('node')
        project = as_util_obj.parseinitfile('project_id')        
        sub_folder = as_util_obj.parseinitfile('suite_id')
        domain_folder = "P292_S10032_G157398"
        tree_pane = server + node + domain_folder + "->" + sub_folder
        print(tree_pane)
        fexe = "world_city_pop"
        req_panel_menu= "Requests->Parameters..."
        panel_name='Settings'
        layer_attribute_list=["PLACE_NAME", "COUNTRY", "COUNTRY_CODE", "STATE", "LATITUDE", "LONGITUDE", "POPULATION", "LABEL", "COLOR_NAMED"]
        layer_name = "WorldCity"       
        test_case = "C2224513"
    
               
        '''===================================== AS side code ================================='''  
        as_util_obj.select_tree_view_pane_item(tree_pane) 
        aswizardobj.Html_Document_Wizard("Home", "html_document")
        '''Step 1: Draw map'''
        as_html_canvas_area_obj.drag_drop_on_canvas("Components", "esri_map", 80, 120, 650, 690) 
        '''Step 2: Add fex'''
        aspanelsobj.select_new_request_from_split_dropdown(fexe,req_panel_menu )

        '''Step 3: Geographic role settings'''
        aspanelsobj.expand_panel(panel_name)
        aspanelsobj.settings_layer_name(layer_name, 14, 5)
        aspanelsobj.settings_geo_role("world_city_pop", "City", Columns =  [{"row": "1", "value": "PLACE_NAME"}, {"row": "3", "value": "COUNTRY"}])
        '''Step 4: Layer visualization settings'''
        aspanelsobj.set_html_esri_map_layer_attributes(layer_attribute_list)
        layer_attribute_list=["COLOR_RGB", "COLOR_HEX", "SIZES"]
        aspanelsobj.set_html_esri_map_layer_attributes(layer_attribute_list)
        aspanelsobj.set_html_esri_map_layer_visualization_generic((1, "Off"), (2, "100"), (3, "Off"), (4, "On"), (5, "On"), (1, "Off"))
        
        '''Step 5: Symbol Settings'''
        #aspanelsobj.expand_panel('Settings')
        aspanelsobj.symbol_settings_using_field(Use_Name = "Color", Field_Name = "POPULATION")
        aspanelsobj.symbol_settings_color(By = "Natural Jenks", Number_Of_Classes = "5")
        time.sleep(1)
        #aspanelsobj.symbol_settings_color(By = "natural jenks")
        '''Step 6: Save and Run'''
        asribbonobj.as_menu('save_as') 
        try:
            as_util_obj.save_as_dialog(driver.find_element_by_name("Save As"), test_case)
        except:
            print("No Save As dialog")
        
        '''________________________________   Runtime Test Script   ________________________________''' 
        se_driver=as_util_obj.get_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        
        bol= True if se_driver.switch_to.alert else False
        se_driver.switch_to.alert.accept()
        time.sleep(5)
        utility_obj.asequal(True, bol, "Step 13: First JS alert appeared")
          
        bol= True if se_driver.switch_to.alert else False
        se_driver.switch_to.alert.accept()
        time.sleep(5)
        utility_obj.asequal(True, bol, "Step 13: 2nd JS alert appeared")   
        
        
        bol= True if se_driver.find_element_by_css_selector(esri_css).is_displayed() else False        
        utility_obj.asequal(True, bol, "Step 01: Map Painted data. ")
        
        '''Step  14: verify color'''
        as_esri_map_runobj.verify_esri_map_fill_color(esri_css, "cream", "Step 14: ")
        as_esri_map_runobj.verify_esri_map_fill_color(esri_css2, "dull_green", "Step 14: ")      
        
        as_util_obj.close_se_driver(se_driver)
        
if __name__ == '__main__':
    unittest.main() 
