"""
Created on Jun 29, 2016
@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140850
TestCase Name : IA-4786:Lasso filter with dimension in rows adds grayed out filter to pane.
"""

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2140850_TestClass(BaseTestCase):

    def test_C2140850(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140850'
        """
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
#         utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8404', 'mrid04', 'mrpass04')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Drag "Product,Category" to Matrix - Rows.
        """
        time.sleep(6)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Add To Query","Rows")
        """
        Step 03: Drag "Revenue" to Vertical Axis.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 1, 1,"Add To Query","Vertical Axis")
        """
        Step 04: Drag "Sale,Year" to Horizontal Axis.
        """
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Add To Query","Horizontal Axis")
        time.sleep(8)
        """
        Step 05: Verify label values
        """
        time.sleep(8)
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 5a: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r4!c0!", "bar_blue", "Step 5b(i): Verify fourth row bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r3!c0!", "bar_blue", "Step 5b(ii): Verify third row bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r1!c0!", "bar_blue", "Step 5b(iii): Verify first row bar color")
        xaxis_value="Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 5c(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 5c(ii): Verify Y-Axis Title")
        labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(10)
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1_f", "Rows", "Product Category", labels, "Step 5d:")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 42, "Step 05: Verify filtered values (2011 to 2013)")
    
        """
        Step 06: Verify query pane
        """
        metaobj.verify_query_pane_field('Rows', "Product,Category", 1, "Step 06a: Verify Query panel Rows ")
        metaobj.verify_query_pane_field("Horizontal Axis", "Sale,Year", 1, "Step 06b: Verify Horizontal Axis ")
        metaobj.verify_query_pane_field('Vertical Axis', "Revenue", 1, "Step 06c: Verify Vertical Axis")
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g5!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """
        Step 07: Verify 'Accessories and Video production' bar values (Product Category:SaleYear:Revenue)
        """   
        time.sleep(10)     
        expected_tooltip=['Product Category:Accessories', 'Sale Year:2015', 'Revenue:$35,619,872.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar!r0!c0!",expected_tooltip, "Step 07a: verify the default tooltip values on a bar in first row")
        time.sleep(15)
        expected_tooltip=['Product Category:Computers', 'Sale Year:2016', 'Revenue:$63,190,001.88', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g5!mbar!r2!c0!",expected_tooltip, "Step 07b: verify the default tooltip values on a bar in middle row")
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g3!mbar!r4!c0']")
        resultobj._validate_page(elem1)
        expected_tooltip=['Product Category:Stereo Systems', 'Sale Year:2014', 'Revenue:$36,604,611.32', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g3!mbar!r4!c0!",expected_tooltip, "Step 07c: verify the default tooltip values on a bar in lower row")
        
        """
        Step 08: Drag "Product,Category" to Filter pane. Click OK.
        """
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        time.sleep(8)
        metaobj.create_visualization_filters('alpha')
        time.sleep(8)
        
        """
        Step 09: Verify query added to filter pane
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 09: Verify query added to filter pane")
        time.sleep(8)
        
        """
        Step 10: Lasso 3 data points pertinent 2011-2013 for Accessories.
        Step 11: Select "Filter Chart".
        """
        time.sleep(5)
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!r0!c0', target_tag='rect', target_riser='riser!s0!g2!mbar!r0!c0',x_offset=-10,y_offset=-10)
        else:
            resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!r0!c0', target_tag='rect', target_riser='riser!s0!g2!mbar!r0!c0')
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
        
        """
        Step 12: Verify query added to filter pane
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and TIME_YEAR',2,"Step 12a: Verify query added to filter pane")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, "Step 12b: Verify filtered values (2011 to 2013)")
    
        
        """
        Step 13: Verify filtered bar values (ProductCategory:SaleYear:Revenue) 
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        elem1=(By.CSS_SELECTOR, "#iaCanvasPanel")
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        expected_xval_list=['2011', '2012', '2013']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step13: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step13: Verify fourth row bar color")
        time.sleep(5)
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, "Step 13: Verify filtered values (2011 to 2013)")
    
        a =['Product Category:Accessories', 'Sale Year:2011', 'Revenue:$5,039,297.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar!r0!c0',a,"Step 13: Verify Accessories:2011 values")
        
        """
        Step 14: Click Run in the toolbar
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        
        """
        Step 15: verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        expected_xval_list=['2011', '2012', '2013']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        time.sleep(10)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step15: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step15: Verify fourth row bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, "Step 15: Verify filtered values (2011 to 2013)")
    
        a =['Product Category:Accessories', 'Sale Year:2011', 'Revenue:$5,039,297.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar!r0!c0',a,"Step 15: Verify Accessories:2011 values")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140850_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 16: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 17: Click "Save" in the toolbar > Type C2140850 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        