'''
Created on Nov 28, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348793
TestCase Name = Verify mapping State/Province with User Defined parent
'''

import unittest,time, pyautogui
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, wf_map, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

class C2348793_TestClass(BaseTestCase):

    def test_C2348793(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348793'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=places/NO_PLACESXY
        """
        utillobj.infoassist_api_login('idis','places/places_xy_new','P292/S10660_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
                  
        """
        Step 02: Click "Change" dropdown > "Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_esrimap_2',mrid='mrid',mrpass='mrpass')
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)
               
        """
        Step 03: Go to Format tab
        Step 04: Click "Background" dropdown > "Oceans basemap"
        """
        ribbonobj.select_ribbon_item('Format','Background')
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='oceans_map']"
        chart_elem = driver.find_element_by_css_selector(chart_type_css)
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 60)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(10)
                
        """
        Step 05: Verify the map canvas is changed
        """
        chart_type_css="[id*='pfjTableChart_1_com-esri-map'][id*='layers']"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 150)
        ocean_tile_css="[id*='pfjTableChart_1_com-esri-map'][id*='layers']"
        layer=driver.find_elements_by_css_selector(ocean_tile_css)
        utillobj.asequal(len(layer), 1, "Step 05: Verify the map canvas is changed to Ocean")
        time.sleep(6)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,'C2348793_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
                
        """
        Step 06: Right click "STATE" > "Map As" > "State/Province"
        """
        time.sleep(6)
        metaobj.datatree_field_click('STATE',1, 1, 'Map As', 'State/Province...')
                
        """
        Step 07. Verify the georole dialog is populated
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#geoRoleCancelBtn')
        resultobj._validate_page(elem)
        cap_css="div[id^='QbDialog']  div[class^='bi-window-caption window-caption'] div[class^='bi-label'][style*='left']"
        cap_text='Map STATE'
        utillobj.verify_popup("div[id^='QbDialog']>div[class*='active']", "Step 07: Verify the georole dialog appears", caption_css=cap_css, caption_text=cap_text)
                
        """ 
        Step 08. Click "Cancel"
        """
        wfmapobj.set_geo_role( btn_click='Cancel')
               
        """
        Step 09: Right click "STATE" > "Map As" > "State/Province"
        """
        time.sleep(6)
        metaobj.datatree_field_click('STATE',1, 1, 'Map As', 'State/Province...')
               
        """ 
        Step 10. Click "User Defined" radio button
        Step 11: Verify "Stored As" > "Name" disabled.
        Step 12: Click "Get Values"
        Step 13: Select "United States" > Ok.
        Step 14: Click OK
        """
        time.sleep(3)
        parent_css="#geoRoleCancelBtn"
        resultobj.wait_for_property(parent_css, 1)
        wfmapobj.set_geo_role(user_defined=['United States'])
        time.sleep(20)
        wfmapobj.set_geo_role(btn_click='Ok')
               
        """
        Step 15: Double click "POPULATION"
        """
        time.sleep(4)
        metaobj.datatree_field_click("POPULATION",2,1)
        time.sleep(4)
              
        """
        Step 16: Drag "STATE" into Layer
        """
        time.sleep(2)
        metaobj.drag_drop_data_tree_items_to_query_tree("STATE", 1, "Layer", 0)
        time.sleep(6)
              
        """
        Step 17: Verify the map is updated
        """ 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 39)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 39, 'Step17.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1279!mregion!", "persian_red3", "Step 17.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['STATE:Montana', 'POPULATION:47445', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1279!mregion!",expected_tooltip, "Step17.e: verify the default tooltip values")       
              
        """
        Step 18: Click "Demographic Layers" > "USA Labor Force Participation Rate 2010" > OK
        """
        ribbonobj.select_ribbon_item('Format','Demographiclayers')
        Demographic_css="[id^='QbDemographicLayersDlg'] [id^='DemographicLayerGrid']"
        resultobj.wait_for_property(Demographic_css, 2)
        lifestyle_list=[]
        population_list=[('USA Labor Force Participation Rate 2010',0)]
        wfmapobj.select_demographic_layer(lifestyle_list, population_list, btn_click='Ok')
        time.sleep(5)
             
        """
        Step 19: Verify the map is updated
        """ 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 39)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 39, 'Step19.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step19:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1279!mregion!", "persian_red3", "Step 19.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['STATE:Montana', 'POPULATION:47445', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1279!mregion!",expected_tooltip, "Step19.e: verify the default tooltip values")       
           
        """
        Step 20: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step 21: Verify the maps are displayed correctly
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 39)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 39, 'Step21.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step21:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1279!mregion!", "persian_red3", "Step 21.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['STATE:Montana', 'POPULATION:47445', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1279!mregion!",expected_tooltip, "Step21.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2348793_Actual_step21', image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """
        Step 22: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        """
        Step 23: Click "Save" icon
        Step 24: Enter Title "C2348793"
        Step 25: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        
        """
        Step 26: Locate the saved fex > right mouse click > "Run"
        """ 
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10660_esrimap_2','mrid','mrpass')
        time.sleep(10)
        
        """
        Step 27: Hover over "Florida" state
        Step 28: Verify the tooltip is displayed correctly
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 39)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 39, 'Step28.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step28:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g624!mregion!", "chardonnay", "Step 28.c(i) Verify first bar color")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g624!mregion!']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=15, y_offset=7)
        time.sleep(1)
        expected_tooltip=['STATE:Florida', 'POPULATION:12119819', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g624!mregion!",expected_tooltip, "Step28.e: verify the default tooltip values",default_move=True)    
        time.sleep(5)
        
        """
        Step 29: Click "Pan" button
        Step 30: Lasso the south east region (approx 25 points)
        Step 31: Select "Exclude from Chart"
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem) 
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1 div[class^='SelectionButton UIButton toggleModePan']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle')
        time.sleep(1)
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(6)
        action1 = ActionChains(self.driver)
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g924!mregion!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        source=driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g924!mregion!']")
        get_source = utillobj.get_object_screen_coordinate(source, x_offset=-20, y_offset=-20)
        target=driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g624!mregion!']")
        get_target = utillobj.get_object_screen_coordinate(target, coordinate_type='bottom_right', x_offset=10, y_offset=10)
        utillobj.drag_drop_on_screen(sx_offset=get_source['x'],sy_offset=get_source['y'],tx_offset=get_target['x'],ty_offset=get_target['y'])
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(5)
        
        """
        Step 32: Verify the states are removed from the map
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g1267!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 15)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 15, 'Step32.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step32:b(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1267!mregion!", "persian_red3", "Step 32.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['STATE:Montana', 'POPULATION:47445', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1267!mregion!",expected_tooltip, "Step32.d: verify the default tooltip values")  
        time.sleep(5)
        
        """
        Step 33: Dismiss the map window
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 34: Reopen the fex using the API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2348793.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 35: Verify IA is launched, preserving the map
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 39)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 39, 'Step35.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['POPULATION', '0M', '9.1M', '18.2M', '27.3M', '36.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step35:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1279!mregion!", "persian_red3", "Step 35.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['STATE:Montana', 'POPULATION:47445', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1279!mregion!",expected_tooltip, "Step35.e: verify the default tooltip values")  
        time.sleep(5)
        
        """
        Step 36: Dismiss IA window
        """
                   
if __name__ == '__main__':
    unittest.main()