'''
Created on Nov 22, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348854
TestCase Name = Verify Visualization with filters
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2348854_TestClass(BaseTestCase):

    def test_C2348854(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348854'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
            
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)
          
        """
        Step 03: Double click "Store,Country", "Revenue"
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(4) 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
            
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
            
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step03.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 03.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step03:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step 03.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
          
        """
        Step 04: Click "Insert"
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
        chart_type_css="#TableChart_2 svg>g>text.title"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
          
        """
        Step 05: Click "Change" dropdown > "Map"
        Step 06: Select "Leaflet Bubble" > OK (Keep "United States of America" Territory)
        """
        ribbonobj.change_chart_type('map')
        time.sleep(3)
        ribbonobj.select_map('bubble',teritory='United States of America')
        time.sleep(3)
        combo_btn=driver.find_element_by_css_selector("div[id^='QbDialog'] #mapTerrCombo div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn, 'United States of America', msg='Step 06: Verify popup menu')
        time.sleep(2)
        driver.find_element_by_css_selector("div[id^='QbDialog'] #mapTypesOkBtn").click()
        time.sleep(2)
        parent_css="div.leaflet-control-scale-line"
        resultobj.wait_for_property(parent_css,2)
        
        """
        Step 07: Double click "Gross Profit"
        """
        metaobj.datatree_field_click("Gross Profit", 2,1)
        time.sleep(8)
         
        """
        Step 08: Double click "Store,State,Province"
        """
        metaobj.datatree_field_click("Store,State,Province", 2,1)
        time.sleep(3)
         
        """
        Step 09: Select "state_name" as Geographic Role > OK
        """
        time.sleep(5)
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"state_name (Alabama, Alaska, Arizona)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(5)
         
        """
        Step 10: Verify the map
        """ 
        parent_css="#MAINTABLE_wbody2 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 36, 'Step10.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step10:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g25!mstate!", "bar_blue", "Step 10.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g25!mstate!",expected_tooltip, "Step10.e: verify the default tooltip values")       
         
        """
        Step 11: Drag "Store,Country" into Filter pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter("Store,Country", 1)       
        time.sleep(6)
                 
        """
        Step 12: Uncheck "[All]"
        Step 13: Check "Canada", "Mexico", "United States" > OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        metaobj._validate_page(elem)            
        time.sleep(2)
        l=['[All]', 'Canada', 'Mexico', 'United States']               
        metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['GridItems',l])
        time.sleep(3)
         
        """
        Step 14: Verify the map is filtered
        """ 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step14.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mregion", "elf_green", "Step 14.c(i) Verify first bar color")
        legend=['Revenue', '13M', '146.2M', '279.4M', '412.6M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',mouse_duration=2.5,x_offset=-10, y_offset=-10)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.41', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step 14.e: verify the default tooltip values",default_move=True)       
                
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 36, 'Step14i.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step14i:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g11!mstate!", "bar_blue", "Step 14i.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip= ['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g11!mstate!",expected_tooltip, "Step14i.e: verify the default tooltip values")  
        metaobj.verify_filter_pane_field('Store,Country',1,"Step14:")  
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step14:Verify prompt Canada is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Mexico',verify=True, verify_type=True, scroll_down=True, msg="Step14:Verify prompt Mexico is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'United States',verify=True, verify_type=True, scroll_down=True, msg="Step14:Verify prompt United States is checked")
        time.sleep(5)   
         
        """
        Step 15: In the Bubble map component, click "Pan"
        Step 16: Lasso all bubble except "Alaska", "Hawaii"
        Step 17: Select "Filter Chart"
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem) 
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody2 [class^='data-selection-button leaflet-control']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle')
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(6)
        action1 = ActionChains(self.driver)
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody2")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        raiser="#MAINTABLE_wbody2 [class*='riser!s0!g35!mstate!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        source=driver.find_element_by_css_selector("#MAINTABLE_wbody2 path[class*='riser!s0!g35!mstate!']")
        get_source = utillobj.get_object_screen_coordinate(source, x_offset=-20, y_offset=-20)
        target=driver.find_element_by_css_selector("#MAINTABLE_wbody2 path[class*='riser!s0!g8!mstate!']")
        get_target = utillobj.get_object_screen_coordinate(target, coordinate_type='bottom_right', x_offset=80, y_offset=20)
        utillobj.drag_drop_on_screen(sx_offset=get_source['x'],sy_offset=get_source['y'],tx_offset=get_target['x'],ty_offset=get_target['y'])
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
        
        """
        Step 18: Verify the map is filtered
        """ 
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step18.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "Cumulus1", "Step 18.c(i) Verify first bar color")
        legend=['Revenue', '528.3M', '533.7M', '539M', '544.4M', '549.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=50, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$539,051,293.73']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step 18.e: verify the default tooltip values",default_move=True)       
               
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 34, 'Step18i.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step18i:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g7!mstate!", "bar_blue", "Step 18i.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g7!mstate!",expected_tooltip, "Step18i.e: verify the default tooltip values")       
        metaobj.verify_filter_pane_field('Store,Country',1,"Step11:")
        metaobj.verify_filter_pane_field('Store,State,Province',2,"Step11:")
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step18:Verify prompt Canada is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Mexico',verify=True, verify_type=True, scroll_down=True, msg="Step18:Verify prompt Mexico is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'United States',verify=True, verify_type=True, scroll_down=True, msg="Step18:Verify prompt United States is checked")
        time.sleep(5)   
        
        """
        Step 19: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 20: Verify the maps are displayed correctly
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step20.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "Cumulus1", "Step 20.c(i) Verify first bar color")
        legend=['Revenue', '528.3M', '533.7M', '539M', '544.4M', '549.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20:d(i) Verify legend Title")
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 34, 'Step20i.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step20i:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g7!mstate!", "bar_blue", "Step 20i.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g7!mstate!",expected_tooltip, "Step20i.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2348854_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step20:Verify prompt Canada is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Mexico',verify=True, verify_type=True, scroll_down=True, msg="Step20:Verify prompt Mexico is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'United States',verify=True, verify_type=True, scroll_down=True, msg="Step20:Verify prompt United States is checked")
        time.sleep(5) 
        
        """
        Step 21: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 22: Click "Save" icon
        Step 23: Enter Title "C2348854"
        Step 24: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
        
        """
        Step 25: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2348854.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 26: Verify the visualization is restored
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step26.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "Cumulus1", "Step 26.c(i) Verify first bar color")
        legend=['Revenue', '528.3M', '533.7M', '539M', '544.4M', '549.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step26:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=50, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$539,051,293.73']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step 26.e: verify the default tooltip values",default_move=True)       
               
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 34, 'Step26i.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step26i:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g7!mstate!", "bar_blue", "Step 26i.c(i) Verify first bar color")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g7!mstate!",expected_tooltip, "Step26i.e: verify the default tooltip values")       
        metaobj.verify_filter_pane_field('Store,Country',1,"Step26:")
        metaobj.verify_filter_pane_field('Store,State,Province',2,"Step26:")
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step26:Verify prompt Canada is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Mexico',verify=True, verify_type=True, scroll_down=True, msg="Step26:Verify prompt Mexico is checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'United States',verify=True, verify_type=True, scroll_down=True, msg="Step26:Verify prompt United States is checked")
        time.sleep(5)        
        
        """
        Step 27: Dismiss IA
        """
                
if __name__ == '__main__':
    unittest.main()