'''
Created on June16, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109129
TestCase Name : IA-4303:Remove 'tooltip' filter vis w/filter prompt at run time is not working if hierarchical data
'''
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

class C2109129_TestClass(BaseTestCase):

    def test_C2109129(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109129'
        """
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Add Product Category and Cost of Goods to Canvas
        """
        time.sleep(10)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        
        """
        Step 03: Verify labels
        """
        time.sleep(12)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 03a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 03b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        
        
        """
        Step 04: verify query pane.
        """
        
        
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category",1, "Step 04: verify Product,Categor query pane")
        metaobj.verify_query_pane_field("Vertical Axis", "Cost of Goods", 1,"Step 04: verify Cost of Goods query pane")
        
        
        """
        Step 05: Add Product Category to Filter accept default and click Ok
        """
        time.sleep(3)
        
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        
        time.sleep(5)
        
        metaobj.create_visualization_filters('alpha')
        
        """
        Step 06: Verify query added to filter.
        """
        
        time.sleep(5)
        parent_css="#qbFilterBox table>tbody>tr img"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field("Product,Category",1, "Step 06: Verify query added to filter.")
        
        """
        Step 07: Verify all bar riser values
        """
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 07a: Verify the total number of risers displayed on Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        time.sleep(5)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 07b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:d(ii) Verify Y-Axis Title")
        bar_value = ['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_value, "Step 07:e(i) Verify bar riser")
         
        
        """
        Step 08: Click Run in the toolbar.
        """
        time.sleep(1) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)   #to switch to run window
        time.sleep(15)
        
        """
        Step 09: Hover 'Media Player' and click Filter chart.
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(10)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 09a: Verify the total number of risers displayed on Run Chart')
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mbar","Filter Chart")
        
        """
        Step 10: Verify Tooltip values.
        """
        
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1,'Step 10a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step10: X and Y axis Scales Values has changed or NOT')
        
        filter_values=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Remove Filter', 'Drill down to Product Subcategory']
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10b: Verify bar color")
        time.sleep(3)
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", filter_values, "Step 10c:Verify Tooltip values.")
         
        """
        Step 11: Hover on 'Media Player' and select Remove filter.
        """
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mbar","Remove Filter")
       
        
        """
        Step 12: Verify output.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7,'Step 12a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12: X and Y axis Scales Values has changed or NOT')
       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12b: Verify bar color")
        output_value = ['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", output_value, "Step 12c: Verify output")
        """
        Step 13: Close the output window
        """
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2109129_Actual_step13', image_type='actual')
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)   # switch back to main window
        time.sleep(15)
        """
        Step 14: Click "Save" in the toolbar > Type C2109129 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
        
