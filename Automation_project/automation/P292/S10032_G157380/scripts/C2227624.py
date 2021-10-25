'''
Created on Jun 7, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227624
TestCase Name = Drill down using ESRI Choropleth Map
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2227624_TestClass(BaseTestCase):

    def test_C2227624(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227624'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type("choropleth_map")
          
        """
        Step 03: Double click "Store,Country", "Revenue"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Store,Country', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        time.sleep(4)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        
        """
        Step 04: Hover over United States > Verify menu
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step 04.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mregion!", "Vermilion", "Step 04.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step04:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mregion!']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',x_offset=-5, y_offset=-10)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.41', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g3!mregion!",expected_tooltip, "Step 04.e: verify the default tooltip values", default_move=True)
        time.sleep(5)
        
        """
        Step 05: Select "Drill down to Store State Province"
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g3!mregion!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(6)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mregion!']")
        utillobj.click_on_screen(parent_elem,'bottom_middle',x_offset=-5, y_offset=-10)    
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g3!mregion!", "Drill down to Store State Province", wait_time=1, default_move=True)
        time.sleep(5)
        
        """
        Step 06: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 78)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",78, 'Step 06.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,Country',1,"Step11:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g9!mregion!", "elf_green", "Step 06.c(i) Verify first bar color")
        legend=['Revenue', '1M', '82.7M', '164.4M', '246.1M', '327.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 06:d(i) Verify legend Title")
        time.sleep(5)
        
        """
        Step 07: Hover over green area (Idaho) > Verify menu
        """
        expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g9!mregion!",expected_tooltip, "Step 07.e: verify the default tooltip values", y_offset=5)       
        time.sleep(5)
        
        """
        Step 08: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 09: Hover over green area (Idaho) > Verify menu
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g9!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 78)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g9!mregion!",expected_tooltip, "Step 09: verify the default tooltip values", y_offset=5)       
        time.sleep(5)
         
        """
        Step 10: Select "Drill up to Store Country" > Verify output
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g9!mregion!", "Drill up to Store Country", wait_time=1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step 10.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 10.c(i) Verify first bar color")
        legend=['Revenue', '545,792,165.4', '545,792,165.9', '545,792,166.4', '545,792,166.9', '545,792,167.4']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion!']")
        utillobj.click_on_screen(parent_elem, 'start', x_offset=85, y_offset=40)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 10.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
        
        """
        Step 11: Close output window
        """
        time.sleep(5)
        driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 12: Click Run in IA
        """
        time.sleep(10)
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 13: Hover over green area (Idaho) > Select "Drill down to Store City."
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g9!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 78)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g9!mregion!",expected_tooltip, "Step 13: verify the default tooltip values", y_offset=5)       
        time.sleep(5)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g9!mregion!", "Drill down to Store City", wait_time=1, y_offset=5)
        
        """
        Step 14: Verify output
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step 14.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mregion!", "persian_red", "Step 14.c(i) Verify first bar color")
        legend=['Revenue', '327,810,679.5', '327,810,680', '327,810,680.5', '327,810,681', '327,810,681.5']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify legend Title")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227624_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 15: Hover over bubble > Verify menu
        """
        expected_tooltip=['Store City:Boise, Idaho, United States', 'Revenue:$327,810,680.45', 'Remove Filter', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion!",expected_tooltip, "Step 15: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 16: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 17: Click "Save" icon > "C2166443" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 19: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 20: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="path[class*='riser!s0!g9!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 78)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",78, 'Step 20.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,Country',1,"Step11:")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g9!mregion!", "elf_green", "Step 20.c(i) Verify first bar color")
        legend=['Revenue', '1M', '82.7M', '164.4M', '246.1M', '327.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g9!mregion!",expected_tooltip, "Step 20.e: verify the default tooltip values", y_offset=5)       
        time.sleep(5)
        
        """
        Step 21: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()