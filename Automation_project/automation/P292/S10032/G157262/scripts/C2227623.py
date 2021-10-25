'''
Created on Jun 6, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227623
TestCase Name = Drill down using ESRI Bubble map 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227623_TestClass(BaseTestCase):

    def test_C2227623(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227623'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Change" dropdown > select ESRI Proportional (Bubble) map
        """
        ribbonobj.change_chart_type("bubble_map")
        
        """
        Step 03: Right click "Store,State,Province" > "Map As" > "US State (Name)"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Store,State,Province',1, 1, 'Map As', 'US State (Name)')
        time.sleep(4)
        
        """
        Step 04: Double click "Store,State,Province", "Revenue"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 51)
#         parent_css="#MAINTABLE_wbody1 .legend text"
#         resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        
        """
        Step 05: Hover over bubble for "San Francisco" > verify menu with "Drill down to Store City" and 'Store State Province: California" is displayed
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g12!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(2)
        expected_tooltip=['Store State Province:California', 'Revenue:$15,282,788.72', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g12!mmarker!",expected_tooltip, "Step 05: verify the default tooltip values")       
        time.sleep(5)
         
        """
        Step 06: Select "Drill down to Store City" > Verify Preview
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g12!mmarker!", "Drill down to Store City", wait_time=1)
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step06.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 06.a: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mmarker!", "bar_blue", "Step 06.b Verify first bar color")
        legend=['Revenue', 'Revenue', '6.4M', '4.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06.d Verify legend Title")
        
        """
        Step 07: Hover over bubble for "San Francisco" > Verify menu
        """
        time.sleep(5)
        expected_tooltip=['Store City:San Francisco', 'Revenue:$4,403,592.44', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mmarker!",expected_tooltip, "Step 07: verify the default tooltip values")       
         
        """
        Step 08: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step 09: Hover over bubble for "San Francisco" > Verify menu
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g2!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(2)
        expected_tooltip=['Store City:San Francisco', 'Revenue:$4,403,592.44', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mmarker!",expected_tooltip, "Step 09: verify the default tooltip values")       
        time.sleep(5)
         
        """
        Step 10: Select "Drill up to Store State Province"
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g2!mmarker!", "Drill up to Store State Province", wait_time=1)
        time.sleep(5)
        
        """
        Step 11: Hover over bubble > Verify menu
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(2)
        expected_tooltip=['Store State Province:California', 'Revenue:$15,282,788.72', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 11: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227623_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 13: Click "Save" > "C2166442" > click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 16: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step16.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 16.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mmarker!", "bar_blue", "Step 16.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '6.4M', '4.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store City:San Francisco', 'Revenue:$4,403,592.44', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mmarker!",expected_tooltip, "Step 16.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()