"""
Created on Jun 21, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110389
TestCase Name : IA-3966:Exclude from Chart not working properly in Preview
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


class C2110389_TestClass(BaseTestCase):

    def test_C2110389(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110389'
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
        Step 02: Add fields 'Cost of Goods' and 'Product,Category'
        """
        time.sleep(6)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(3)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(3)
        
        """
        Step 03: verify label values
        """
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']"))
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03: verify X axis title")
        
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class='yaxis-title']"))
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Cost of Goods", "Step 03: verify Y axis title")
        
        """
        Step 04: verify query pane
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Cost of Goods", 1, "Step 04: verify Cost of Goods added to query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category",1, "Step 04: verify Product,Category  added to query pane")
        
        """
        Step 05: Verify all bar riser values
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        bar_riser=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        time.sleep(5)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step05: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step05: Verify the total number of risers displayed')
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar",bar_riser,"Step 05: Verify all bar riser values")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step05: Verify bar color")
                
        """
        Step 06: Drag and drop 'Product,Category' into Filter bucket and click OK.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        metaobj.create_visualization_filters('alpha')
        
        """
        Step 07: Verify query added to filter pane
        """
        time.sleep(4)
        utillobj._validate_page((By.CSS_SELECTOR,"#qbFilterBox table>tbody>tr>td>img"))
        metaobj.verify_filter_pane_field("Product,Category",1, "Step 07: Verify Product,Category added to filter pane")
        
        """
        Step 08: Check 'Computers', 'Media Player', 'Stereo Systems', 'Televisions' in filter prompt pane.
        """
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', False)
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player', False)
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', False)
        
        time.sleep(10)
        propertyobj.select_or_verify_show_prompt_item(1, 'Televisions', False)
        time.sleep(10)
        """
        Step 09: Verify filtered bar values.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step09: Verify the total number of risers displayed on Run Chart')
        bar_riser_filter=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar",bar_riser_filter,"Step 09: Verify filtered bar values.")
        
        """
        Step 10: Hover over the 'Televisions', click Exclude from Chart.
        """
        time.sleep(10)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g3!mbar", "Exclude from Chart")
        
        """
        Step 11: Verify televisions got excluded.
        """
        time.sleep(8)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        xaxis_value = "Televisions"
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, "Step11a:Televisions is excluded from X Label")
        metaobj.verify_filter_pane_field("Product,Category",1, "Step 11: Verify Product,Category added to filter pane")
        
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step11b: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step11b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11b: Verify bar color")
                
        """
        Step 12: Click Run in the toolbar
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            time.sleep(50)        
        
        """
        Step 13: Verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(10)
        xaxis_value = "Televisions"
        xaxis = self.driver.find_element_by_xpath(VisualizationResultareaLocators.bar_xlabel)
        utillity.UtillityMethods.as_notin(self,xaxis.text, xaxis_value, "Step13a:Televisions is excluded from X Label")
        #metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and BUSINESS_REGION',1, 'Step 09:  Verify Query added to filter pane')
        
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step13b: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step12b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13b: Verify bar color")
                
        bar_riser_runtime =['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar",bar_riser_runtime,"Step 13: Verify output")
        time.sleep(30)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2110389_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 15: Click "Save" in the toolbar > Type C2110389 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main()
                
