"""
Created on Jun 24, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140682
TestCase Name : IA-373:Prompts are bigger in Chrome and Firefox, Title text and Prompt content
"""

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2140682_TestClass(BaseTestCase):

    def test_C2140682(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140682'
        """
        Step 01: Launch the IA API with CAR http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','ibisamp/car','P312/S10099_5', 'mrid', 'mrpass')
#         utillobj.infoassist_api_login('idis','baseapp/CAR','S8404', 'mrid04', 'mrpass04')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add fields country, sales
        """
        
        time.sleep(4)
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(2)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(8)
        """
        Step 03: Verify label titles
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        xaxis_value="COUNTRY"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step03: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step03: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step03: Verify bar color") 
        time.sleep(8)
        
        """
        Step 04: Verify query pane
        """
       
        metaobj.verify_query_pane_field("Vertical Axis", "SALES",1, "Step 04: Verify query pane")
        
        """
        
        
        Step 05: Verify all bar riser values
        """
        time.sleep(4)
        bar_values=['COUNTRY:ENGLAND', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar",bar_values, "Step 05: Verify bar riser values")
        
        """
        Step 06: Drag and drop Country into filter pane
        """
        
        metaobj.datatree_field_click("COUNTRY", 1, 1,"Filter")
        time.sleep(10)
        btn="#avFilterOkBtn"
        elem1=(By.CSS_SELECTOR, btn)
        resultobj._validate_page(elem1)
        time.sleep(4)
        metaobj.create_visualization_filters('alpha')
        time.sleep(20)
        """
        Step 07: Verify query added to filter pane
        
        """
        time.sleep(6)
        metaobj.verify_filter_pane_field("COUNTRY", 1,"Step 07: Verify query added to filter pane")
        
        
        """
        Step 08: Drag and drop Sales to filter pane
        """
        
        metaobj.datatree_field_click("SALES", 1, 1,"Filter")
        time.sleep(10)
        btn="#avFilterOkBtn"
        elem1=(By.CSS_SELECTOR, btn)
        resultobj._validate_page(elem1)
        time.sleep(4)
        metaobj.create_visualization_filters('numeric')
        time.sleep(20)
        """
        Step 09: Verify query added to filter pane
        """
        
        time.sleep(6)
        metaobj.verify_filter_pane_field("SALES", 2,"Step 09: Verify query added to filter pane")
        time.sleep(6)
        xaxis_value="COUNTRY"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step09: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09: Verify bar color") 
        time.sleep(20)
        
        """
        Step 10: Verify text and titles of filter prompts
        """
        
        propertyobj.select_or_verify_show_prompt_item(1, "[All]",  verify=False, verify_type=True, msg="Step 10a: Verify title of 1st filter prompt")
        
        """
        Step 11: Click Run in the toolbar
        """
        
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(15)
#         window_after = driver.window_handles[1]  # to switch to run window
#         driver.switch_to.window(window_after)
#         time.sleep(3)
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        
        """
        Step 12: Verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        xaxis_value="COUNTRY"
        yaxis_value="SALES"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step12: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step12: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step12: Verify bar color") 
        bar_values_runtime=['COUNTRY:ENGLAND', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar",bar_values_runtime, "Step 12: Verify output")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140682_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
        Step 13: Close the output window
        """
        self.driver.close()
        time.sleep(10)
#         window_before = driver.window_handles[0]  # switch back to main window
#         driver.switch_to.window(window_before)
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        """
        Step 14: Click "Save" in the toolbar > Type C2140682 > Click "Save" in the Save As dialog
        """
        time.sleep(5)
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        