'''
Created on Nov 14, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229097
TestCase Name = Verify "Clear" option on esri map components 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229097_TestClass(BaseTestCase):

    def test_C2229097(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229097'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
          
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
        
        """
        Step 03: Double click "Cost of Goods", "Store,Country"
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Store,Country", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
         
        """
        Step 04: Click "Clear" button
        """
        ribbonobj.select_ribbon_item('Home', 'Clear')
        time.sleep(5)
        
        """Verify "Warning" prompt appears."""
        cap_css="div[id^='BiDialog']>div[class*='window-active'] [class*='caption'] [class*='bi-label']"
        cap_text='Warning'
        popup_css="div[id^='BiDialog']>div[class*='window-active'] [class='bi-component'] [class*='bi-label']"
        pop_text="Are you sure you would like to CLEAR the selected Component?"
        utillobj.verify_popup("div[id^='BiDialog']>div[class*='active']", "Step04: Verify 'Warning' prompt appears", caption_css=cap_css, caption_text=cap_text, popup_text_css=popup_css, popup_text=pop_text)
        
        """
        Step 05: Click OK
        """
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(2) 
         
        """
        Step 06: Verify the map is cleared
        """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 06: Verify the map is cleared on Preview")
        time.sleep(1)
        
        """
        Step 07: Click "Undo" button
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(8)
        
        """
        Step 08: Verify the fields are restored
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step08.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '98M', '196M', '294M', '392M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 08.c(i) Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step08.e: verify the default tooltip values",default_move=True)       
        
        """
        Step 09: Click "Insert" button
        Step 10: Click "Change" dropdown > "ESRI Bubble"
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
        chart_type_css="#TableChart_2 svg>g>text.title"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
        
        """
        Step 11: Right click "Store,State,Province" > "Map As" > "US State (Name)"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Store,State,Province',1, 1, 'Map As', 'US State (Name)')
        time.sleep(6)
        
        """
        Step 12: Double click "Store,State,Province", "Revenue"
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 51)
        
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 36, 'Step 12.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g25!mmarker!", "bar_blue", "Step 12.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '164M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step12:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g25!mmarker!",expected_tooltip, "Step 12.e: verify the default tooltip values")       
        
        """
        Step 13: Click "Clear" dropdown > "Visualization"
        """
        ribbonobj.select_ribbon_item('Home','clear_dropdown',opt='Visualization')
        
        """
        Step 14: Click OK
        """
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(5) 
        chart_type_css="#TableChart_2 svg>g>text.title"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
         
        """
        Step 15: Verify both components are cleared
        """
        def_chart=driver.find_element_by_css_selector("#TableChart_1 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 15.a: Verify the choropleth map1 is cleared on Preview")
        time.sleep(1)
        def_chart=driver.find_element_by_css_selector("#TableChart_2 svg>g>text.title").text.strip()
        utillobj.asequal("Drop Measures or Sorts into the Query Pane", def_chart, "Step 15.b: Verify the bubble map1 is cleared on Preview")
        time.sleep(1)
        
        """
        Step 16: Click "Undo" button
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(8)
        
        """
        Step 17: Verify both components are restored
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step17.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '98M', '196M', '294M', '392M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 17.c(i) Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step17.e: verify the default tooltip values",default_move=True) 
              
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 36, 'Step 17.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g25!mmarker!", "bar_blue", "Step 17.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '164M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step17:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g25!mmarker!",expected_tooltip, "Step 17.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2229097_Actual_Step17', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 18: Click "Save" icon
        Step 19: Enter Title "C2229097"
        Step 20: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
if __name__ == '__main__':
    unittest.main()