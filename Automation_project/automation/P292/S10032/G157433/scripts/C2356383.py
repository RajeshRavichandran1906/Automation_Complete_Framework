'''
Created on Jun 7, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2356383
TestCase Name = Change Choropleth to Proportional and Vice Versa
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase

class C2356383_TestClass(BaseTestCase):

    def test_C2356383(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2356383'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10332&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02: Home > Change > Esri Choropleth
        """
        ribbonobj.change_chart_type("choropleth_map")
        time.sleep(5)
        parent_css="[class*='esriScalebarSecondNumber']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 30)
        
        """
        Step 03: Double click Store,State,Province and Cost of Goods
        """
        metaobj.datatree_field_click("Store,State,Province", 2,1)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 144, 45)
        
        """
        Step 04: Hover over Idaho
        """
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g25!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle', x_offset=0, y_offset=-8)
        time.sleep(1)
        expected_tooltip=['Store State Province:Idaho, United States', 'Cost of Goods:$235,572,893.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mregion",expected_tooltip, "Step04.a: verify the default tooltip values",default_move=True)
        
        """
        Step 05: Home > Change > Esri Proportional
        """
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
        
        """
        Step 06: Hover over Idaho
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 60, 35)
        expected_tooltip=['Store State Province:Idaho, United States', 'Cost of Goods:$235,572,893.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mmarker!",expected_tooltip, "Step 06.a: verify the default tooltip values")       
        
        """
        Step 07: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 08: Hover over Idaho in the outpout window
        """
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 60, 35)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 60, 'Step 08.a: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mmarker!", "bar_blue", "Step 08.b(i) Verify first bar color")
        legend=['Cost of Goods', 'Cost of Goods', '235.6M', '117.8M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:c(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho, United States', 'Cost of Goods:$235,572,893.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mmarker!",expected_tooltip, "Step 08.d: verify the default tooltip values")       
        
        """
        Step 09: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        parent_css="#applicationButton img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)

        """
        Step 10: In design window Home > Change > Esri Choropleth
        """
        ribbonobj.change_chart_type("choropleth_map")
        parent_css="[class*='esriScalebarSecondNumber']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 30)
        
        """
        Step 11: Hover over Idaho
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 144, 45)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 144, 'Step11.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '59M', '117.8M', '176.6M', '235.6M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:b(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mregion", "elf_green", "Step 11.c(i) Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g25!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle', x_offset=0, y_offset=-8)
        time.sleep(1)
        expected_tooltip=['Store State Province:Idaho, United States', 'Cost of Goods:$235,572,893.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mregion",expected_tooltip, "Step11.e: verify the default tooltip values",default_move=True)
        
        """
        Step 12: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 13: Hover over Idaho in the outpout window
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 144, 45)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 144, 'Step13.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Cost of Goods', '0M', '59M', '117.8M', '176.6M', '235.6M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:b(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mregion", "elf_green", "Step 13.c(i) Verify first bar color")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g25!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle', x_offset=0, y_offset=-8)
        time.sleep(1)
        expected_tooltip=['Store State Province:Idaho, United States', 'Cost of Goods:$235,572,893.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mregion",expected_tooltip, "Step13.e: verify the default tooltip values",default_move=True)
        
        """
        Step 14: Close output window,
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1="#applicationButton img"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
         
        """
        Step 15: Logout using API(without saving fex)
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()