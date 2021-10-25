"""
Created on Jun 21, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110388
TestCase Name : IA-3993:WF BUE:Vis:Runtime:Filter chart, reset to default and apply drilldown display loading icon
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2110388_TestClass(BaseTestCase):

    def test_C2110388(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110388'
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F    
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add revenue(Vertical axis),Product category(horizontal-axis).
        """
        time.sleep(10)
        metaobj.datatree_field_click("Revenue", 1, 1, "Add To Query","Vertical Axis")
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Add To Query","Horizontal Axis")
       
        """
        Step 03: verify label values
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03: verify Y axis title")
        
        """
        Step 04: verify query pane
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Revenue", 1, "Step 04: verify Revenue added to query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 04: verify Product,Category added to query pane")
        
        """
        Step 05: Verify all bar riser values
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(6)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step05: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step05: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step05: Verify bar color")
        
        bar_riser = ['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar",bar_riser,"Step05: Verify all bar riser values ")
        
        """
        Step 06: Click Run in the toolbar.
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        
        """
        Step 07: Hover on Media player and select filter chart.
        """     
        time.sleep(8)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(10)        
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g3!mbar", "Filter Chart")
        time.sleep(5)
        
        """
        Step 08: Verify filtered tooltip values.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step08: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step08: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08: Verify bar color")
        
        bar_riser_runtime =['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1',"riser!s0!g0!mbar",bar_riser_runtime,"Step 08: Verify filtered tooltip values.")
 
        """
        Step 09: Click on the run-time toolbar options icon and select reset to default.
        """
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, '#MAINTABLE_menuContainer1')
        resultobj._validate_page(elem1)
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        time.sleep(15)
        
        """
        Step 10: Verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step10: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step10: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10: Verify bar color")
        
        bar_riser1 =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar",bar_riser1,"Step 10: Verify output")
        
        """
        Step 11: Hover on Stereo systems and select drilldown
        """        
        time.sleep(5)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g4!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g4!mbar",'Drill down to Product Subcategory')        
        time.sleep(8)
        
        """
        Step 12: Verify label values
        """
        time.sleep(3)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory", "Step 12: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 12: verify Y axis title")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 5, 'Step 12a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12b: X annd Y axis Scales Values has changed or NOT')
        time.sleep(20)
        raiser="div[id*='ibi$container$inner$HBOX_1']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2110388_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 13: Close the output window.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 14: Click "Save" in the toolbar > Type C2110388 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        
if __name__ == '__main__':
    unittest.main()
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         