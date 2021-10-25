'''
Created on June 27, 2017
Status: re-automate for AS 8202
@author: Jesmin 
@modified date: 01/31/18
@modified by: Jesmin A
Test Suite = http://lnxtestrail/testrail/index.php?/cases/view/2224509
Test Case =     Local Data Server - Verify Geographic Role 'Continent' with 'Color' use & Equal Breaks 
'''

import time, unittest
from common.lib.as_basetestcase import AS_BaseTestCase
from common.lib import as_utility, utillity
from common.pages import as_panels, as_wizard, as_ribbon, as_html_canvas_area, as_esri_map_run

from selenium.webdriver.common.by import By
from common.pages import as_esri_map_run



class C2224509_TestClass(AS_BaseTestCase):

    def test_C2224509(self):

        '''Variable and object instantiation for both drivers'''
        driver = self.driver
        asutilobj = as_utility.AS_Utillity_Methods(driver)
        aspanelsobj = as_panels.AS_Panels(driver)
        aswizardobj = as_wizard.AS_Wizard_Windows(driver)
        asribbonobj = as_ribbon.AS_Ribbon(driver)
        as_html_canvas_area_obj=as_html_canvas_area.AS_Html_Canvas(driver)
        
        
        '''Local variables'''
        server = asutilobj.parseinitfile('clientid')
        node = asutilobj.parseinitfile('data_server_path')
        folder=asutilobj.parseinitfile('data_server_app_folder')
        tree_pane = server+"->"+node +"->"+folder
        layer_name = "Continents"
        esri_css = "#" + layer_name + "_layer > path:nth-child(7)"
        test_case = "C2224509"
        legend_css = "#Continent_Legend_Continent"        
        
        
        
        

        '''________________________________   Runtime Test Script   ________________________________''' 
        
        se_driver=asutilobj.get_dataserver_se_driver(test_case + ".htm")
        as_esri_map_runobj = as_esri_map_run.AS_Esri_Map_Run(se_driver)
        utillobj=utillity.UtillityMethods(se_driver)      
        
        
        """  wait for map finish loading polygon """ 
        as_esri_map_runobj._validate_page((By.CSS_SELECTOR, esri_css), wait_time=4800)  
        bol=se_driver.find_element_by_css_selector(esri_css).is_displayed()
        utillobj.asequal(True, bol, "Step 0: Map Painted data. ")
       
               
        """Step 05: Verify: users see the colors represent in the color scheme scale"""     
        as_esri_map_runobj.verify_esri_map_fill_color(esri_css,"dull_green2", "Step 05: ")       
        time.sleep(2)
                              
        """Step 06: Click on TOC widget; Expand Legend; Verify legend appears"""  
        as_esri_map_runobj.esri_select_main_menu_map_widget("toc")
        time.sleep(2) 
        as_esri_map_runobj.esri_select_map_toc_tools("Continents", "show_tool") 
        time.sleep(2)
        
        as_esri_map_runobj.esri_select_map_toc_tools("Continents", "toggle_layer_legend")                    
        time.sleep(2)
        
        obj_css="div[id='Continents_Legend_Continents_0'] svg path" 
        expected_fill_color="dull_green2";
        expected_stroke_color="light_gray1"
        as_esri_map_runobj.verify_esri_map_toc_widget_legend_color(obj_css,expected_fill_color, expected_stroke_color, "Step 06: ")
      
        # Take screenshot   (Step 08- shape & default extent will be verified via screenshot)    
        #utillity.UtillityMethods.take_screenshot(driver.find_element_by_css_selector("#emfobject1_gc"),'C2224509_Base_step06', image_type='base')
        time.sleep(2)
        
        '''close browser'''   
        asutilobj.close_se_driver(se_driver)
        
if __name__ == '__main__':
    unittest.main() 
