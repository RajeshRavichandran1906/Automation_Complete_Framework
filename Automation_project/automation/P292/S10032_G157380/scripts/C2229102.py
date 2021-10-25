'''
Created on Jan 04, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229102
TestCase Name = Verify "Filter"/"Exclude" options on ESRI maps
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229102_TestClass(BaseTestCase):

    def test_C2229102(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229102'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
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
        Step 03: Double click "Cost of Goods", "Store,Country"
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Store,Country", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
          
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 34, 'Step03.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '98M', '196M', '294M', '392M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step03:b(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 03.c(i) Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start', x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step03.e: verify the default tooltip values",default_move=True)       
          
          
        """
        Step 04: Click "Insert" button
        Step 05: Click "Change" dropdown > "ESRI Bubble"
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
        chart_type_css="#TableChart_2 svg>g>text.title"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
          
        """
        Step 06: Right click "Store,State,Province" > "Map As" > "US State (Name)"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Store,State,Province',1, 1, 'Map As', 'US State (Name)')
        time.sleep(6)
          
        """
        Step 07: Double click "Store,State,Province", "Revenue"
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
          
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 36, 'Step 07.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g25!mmarker!", "bar_blue", "Step 07.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '164M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step07:d(i) Verify legend Title")
          
          
        """
        Step 08: Hover over "Idaho, United States" bubble
        Step 09: Verify the tooltip is displayed
        """ 
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g25!mmarker!",expected_tooltip, "Step 09.e: verify the default tooltip values") 
        time.sleep(5) 
          
        """
        Step 10: Select "Exclude from Chart"
        """ 
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody2")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 [class*='riser!s0!g25!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody2", "riser!s0!g25!mmarker!",'Exclude from Chart',wait_time=1)
         
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_esrimap_2',mrid='mrid',mrpass='mrpass')
#         time.sleep(10)
        
        """
        Step 11: Verify the maps are filtered
        """ 
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 34, 'Step11.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '39.1M', '78.2M', '117.4M', '156.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11.b Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 11.c Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step11.d: verify the default tooltip values",default_move=True) 
         
        time.sleep(5)      
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 35)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 35, 'Step 11.e: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g66!mmarker!", "bar_blue", "Step 11.f Verify first bar color")
        legend=['Revenue', 'Revenue', '31.8M', '15.9M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step11.g Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Texas', 'Revenue:$30,157,666.35', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g66!mmarker!",expected_tooltip, "Step 11.h: verify the default tooltip values") 
        metaobj.verify_filter_pane_field('Store,State,Province', 1, "Step 11.i")
        
        """
        Step 12: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 13: Verify the map is run in a new window
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 34, 'Step13.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '39.1M', '78.2M', '117.4M', '156.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13.b Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 13.c Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start', x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip= ['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step13.d: verify the default tooltip values",default_move=True) 
        
        time.sleep(5)      
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 35)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 35, 'Step 13.e: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g66!mmarker!", "bar_blue", "Step 13.f Verify first bar color")
        legend=['Revenue', 'Revenue', '31.8M', '15.9M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step13.g Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Texas', 'Revenue:$30,157,666.35', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g66!mmarker!",expected_tooltip, "Step 13.h: verify the default tooltip values")      
        
        """
        Step 14: Hover over the United States in the Choropleth Map
        Step 15: Select "Filter Chart" in the tooltip
        """
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',mouse_duration=2.5,x_offset=-20, y_offset=10)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mregion",'Filter Chart',wait_time=1,default_move=True)
        
        """
        Step 16: Verify both maps are filtered
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step16.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '153.3M', '155M', '156.5M', '158M', '159.6M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:b Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion", "Cumulus1", "Step 16.c Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start', x_offset=90, y_offset=40)
        time.sleep(1)
#         expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step16.e: verify the default tooltip values",default_move=True) 
              
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 35)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 35, 'Step 16.e: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g25!mmarker!", "bar_blue", "Step 16.f Verify first bar color")
        legend=['Revenue', 'Revenue', '30.2M', '15.6M', '1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step16:g Verify legend Title")
        time.sleep(5)
        expected_tooltip= ['Store State Province:Texas', 'Revenue:$30,157,666.35', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g28!mmarker!",expected_tooltip, "Step 16.h: verify the default tooltip values")  
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229102_Actual_Step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 17: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 18: Click "Save" icon
        Step 19: Enter Title "C2229102"
        Step 20: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 21: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2229102.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 22: Verify the visualization is restored
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 34)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 34, 'Step22.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '39.1M', '78.2M', '117.4M', '156.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step22.b Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 22.c Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start', x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Cost of Goods:$898,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step22.d: verify the default tooltip values",default_move=True) 
        
        time.sleep(5)      
        parent_css="#MAINTABLE_wbody2 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 35)
        parent_css="#MAINTABLE_wbody2 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", 35, 'Step 22.e: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g66!mmarker!", "bar_blue", "Step 22.f Verify first bar color")
        legend=['Revenue', 'Revenue', '31.8M', '15.9M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody2", legend, "Step22.g Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Texas', 'Revenue:$30,157,666.35', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g66!mmarker!",expected_tooltip, "Step 22.h: verify the default tooltip values") 
        metaobj.verify_filter_pane_field('Store,State,Province', 1, "Step 22.i")
        
        """
        Step 23: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
                
if __name__ == '__main__':
    unittest.main()