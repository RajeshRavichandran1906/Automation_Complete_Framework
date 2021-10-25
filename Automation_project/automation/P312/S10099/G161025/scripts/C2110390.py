'''
Created on June21, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110390&group_by=cases:section_id&group_id=147037&group_order=asc
TestCase Name : IA-3770:Exclude,Reset and again Exclude from chart does not work.
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_metadata_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2110390_TestClass(BaseTestCase):

    def test_C2110390(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110390'
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
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
        Step 02: Add Revenue and Product category
        """
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        
        """
        Step 03: Verify label values
        """
        time.sleep(5)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03: verify Y axis title")
        
        """
        Step 04: verify query pane
        """
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category',1, "Step 04: Verify query pane Horizontal Axis")
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue',1, "Step 04: Verify query pane Vertical Axis")
        
        """
        Step 05: Verify riser values
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        a =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar', a, "Step 05: Verify riser values")
        
        """
        Step 06: Click Run in the toolbar
        """
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            time.sleep(50) 
        
        
        """
        Step 07:  Hover on a Camcorder and select exclude from chart.
        """
        time.sleep(8)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g1!mbar", "Exclude from Chart")
        time.sleep(4)
        """
        Step 08: Verify Camcorder value excluded
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        xaxis_value = "Camcorder"
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, "Step08:Camcorder is excluded from X Label")
        #metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and BUSINESS_REGION',1, 'Step 09:  Verify Query added to filter pane')
        
        expected_xval_list=['Accessories', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 08b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 8b(i): Verify bar color")
        a=['Product Category:Computers', 'Revenue:$103,316,482.12', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g1!mbar',a,"Step 08c: Hover 2nd bar and verify Camcorder is not there ")
        
        """
        Step 09: Click on the arrow icon at right-bottom corner and select reset.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        time.sleep(2)
         
        """
        Step 10: verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10: Verify bar color")
        a =['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g1!mbar', a, "Step 10: Verify Camcorder Tooltip")
         
        """
        Step 11: Hover on Computers and select exclude from chart.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g2!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(5)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g2!mbar", "Exclude from Chart")
        time.sleep(4)
         
        """
        Step 12: Verify Computers value excluded
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g2!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)        
         
        time.sleep(8)     
        xaxis_value = "Computers"
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, "Step12a:Computers is excluded from X Label")
        #metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and BUSINESS_REGION',1, 'Step 09:  Verify Query added to filter pane')
        
        expected_xval_list=['Accessories', 'Camcorder', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step12b: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step12b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12b: Verify bar color")
           
        a =['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g2!mbar', a, "Step 12: Hover 3rd bar and verify Computers is not there ")
        
        elem1=(By.CSS_SELECTOR, "div[id*='ibi$container$inner$HBOX_1']")
        resultobj._validate_page(elem1) 
        time.sleep(5)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2110390_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
                 
        """
        Step 13: Close the output window.
        """
        self.driver.close()
        window_before = driver.window_handles[0]  # switch back to main window
        driver.switch_to.window(window_before)
         
        """
        Step 14: Click "Save" in the toolbar > Type C2110390 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """
        Step 15: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()
