"""
Created on Jun 24, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140683
TestCase Name : IA-4485:Vis: Groups on dimension and Filter prompt are disconnected at run time
"""

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility
from common.wftools import report
from common.wftools import visualization

class C2140683_TestClass(BaseTestCase):

    def test_C2140683(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        report_obj=report.Report(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140683'
        """
        Step 01: Launch the IA API with wf_retail_lite http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS404%2F

        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')

        """
        Step 02: Double click "Revenue" and "Product,Category"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        parent_css="#queryTreeWindow"
        visual.wait_for_visible_text(parent_css, 'Revenue')
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text(parent_css, 'Product,Category')
        
        """
        Step 03: Verify label values
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03.01: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03.02: verify Y axis title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 03.03: X annd Y axis Scales Values has changed or NOT')
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.04: Verify first bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.05: Verify the total number of risers displayed on Run Chart')
        time.sleep(8)
        
        """
        Step 04: Verify all bar riser data values.
        """
        bar_riser=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar_riser, "Step 04.01: Verify bar riser data values.")
        time.sleep(8)
        
        """
        Step 05: Right click on Product, Category in Query Pane and Choose Create Groups.
        """
        visual.right_click_on_field_under_query_tree("Product,Category", 1, "Create Group...")

        """
        Step 06: Select Accessories and Camcorder and create Group, click ok to save group and exit group window.
        """
        visual.wait_for_visible_text('#dynaGrpsOkBtn', 'OK')
        value=["Accessories","Camcorder"]
        visual.slect_group_grid_values(value)
        visual.create_group_options('Group')
        time.sleep(3)
        visual.exit_group_dialog('ok')
                
        """
        Step 07: Verify group added to data pane
        """
        report_obj.collapse_datatree_field_section('Filters and Variables')
        utillobj.wait_for_page_loads(5) 
        metaobj.verify_data_pane_field('Dimensions', 'PRODUCT_CATEGORY_1',9, "Step 07.01")
        
        """
        Step 08: Add newly created Group to filter, accept default and click Ok.
        """
        metaobj.datatree_field_click("Dimensions->PRODUCT_CATEGORY_1",1,1,"Filter")
        utillobj.synchronize_until_element_is_visible("#avFilterOkBtn", 90)
        time.sleep(2)
        utillobj.wait_for_page_loads(20)
        metaobj.create_visualization_filters('alpha')
        time.sleep(5)
        utillobj.wait_for_page_loads(20)
        
        """
        Step 09: Verify query added to filter pane
        """
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(3)
        metaobj.verify_filter_pane_field("PRODUCT_CATEGORY_1",1,"Step 09.01: Verify query added to filter pane")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "PRODUCT_CATEGORY_1", "Step 09.02: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 09.03: verify Y axis title")
        expected_xval_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.05: Verify first bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 09.06: Verify the total number of risers displayed on Run Chart')
                
        """
        Step 10: Click Run in the toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(20)
        core_utilobj.switch_to_new_window()
        
        """
        Step 11: Lasso Media Player and Stereo systems and Filter Chart.
        """
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", 90)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g2!mbar', target_tag='rect', target_riser='riser!s0!g3!mbar')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        
        """
        Step 12: Verify filtered bar values
        """
        time.sleep(2)
        bar_riser_runtime=['PRODUCT_CATEGORY_1:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar_riser_runtime, "Step 12.01: Verify filtered bar values")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "PRODUCT_CATEGORY_1", "Step 12.02: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 12.03: verify Y axis title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list,'Step 12.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.05: Verify first bar color")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 12.06: Verify the total number of risers displayed on Run Chart')
        
        """
        Step 13: Verify values in filter prompt
        """
        propertyobj.select_or_verify_show_prompt_item(1, "Media Player", True,verify_type=True,msg="Step 13.01: Verify Media Player in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, "Stereo Systems", True,verify_type=True,msg="Step 13.02: Verify Stereo Systems in filter prompt")
        
        """
        Step 14: Close the output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#applicationButton img", 90)
        
        """
        Step 15: Click "Save" in the toolbar > Type C2140683 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main()