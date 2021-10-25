'''
Created on May'24, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108831
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_run, ia_run, metadata
from common.locators import visualization_resultarea_locators
from selenium.webdriver.common.by import By
from common.lib import utillity, core_utility

class C2108831_TestClass(BaseTestCase):

    def test_C2108831(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108831'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ia_resarea = ia_run.IA_Run(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        time.sleep(2)
         
        """
        Step 02: Double click "Revenue" and "Product,Category"
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 2, 1)
        metaobj.datatree_field_click("Dimensions->Product->Product->Product,Category", 2, 1)
        
        """
        Step 03: Verify x and Y axis labels
        """
        
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 90, 1)
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.b Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar", "bar_blue", "Step 03.e Verify second bar color")
        
        """
        Step 04: Verify all bar riser values
        """
        bar= ['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, " Step 04: Verify all bar riser values")
         
        """
        Step 05: Run the Visualization.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        core_utilobj.switch_to_new_window()
        
        """
        Step 06: Verify output.
        """
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 90, 1)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 06.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 06.b Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c(i) Verify first bar color")
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 06:d(ii) Verify Y-Axis Title")    
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar", "bar_blue", "Step 06.e Verify second bar color")    
        
        bar_runtime= ['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_runtime, "Step 06: Verify output.")
        
        """
        Step 07: From the Run menu option choose show data (grid icon).
        """
        time.sleep(4)
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        time.sleep(8)
        
        """
        Step 08: Verify revenue and product category data values
        """
        parent_css='table.arPivot'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
        ia_resarea.verify_table_data_set("table.arPivot", "C2108831_Ds01.xlsx", "Step 08: Verify revenue and product category data values")
        
        """
        Step 09: Again Click Show Data to revert back to chart.
        """
        time.sleep(5)
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report", toggle='no')
        time.sleep(5)
        
        """
        Step 10: Hover on Media Player and select filter chart.
        """
        parent_css='#MAINTABLE_wbody1'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
        
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g3!mbar","Filter Chart")
        
        """
        Step 11: Verify media player value alone is filtered.
        """
        time.sleep(12)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 1)
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 11.b Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c(i) Verify first bar color")
        
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:d(ii) Verify Y-Axis Title")    
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.e Verify second bar color")    
        
        bar_value=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Remove Filter', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_value, "Step 11.f: Verify media player value alone is filtered.")
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']"),'C2108831_Actual_step11', image_type='actual')
        
        time.sleep(1)
        core_utilobj.switch_to_previous_window()
        time.sleep(3)

        """
        Step 12: Click "Save" in the toolbar > Type C2108831 > Click "Save" in the Save As dialog
        """        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
