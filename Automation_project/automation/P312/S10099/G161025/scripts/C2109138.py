"""
Created on Jun 23, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109138
TestCase Name : IA-4110:(FOC280) is thrown for filter with aggregation(Count)
"""

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2109138_TestClass(BaseTestCase):

    def test_C2109138(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109138'
        
        """
        Step 01: http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add field "Cost of Goods" from Sales
        """
        metaobj.datatree_field_click("Cost of Goods",2,1)
        
        """
        Step 03: Add field "Product,SubCategory" from Product Dimension
        """
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(8)
        
        """
        Step 04: Verify label values
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step04a: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.b(i) Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 04:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 04:c(ii) Verify Y-Axis Title")
        
        """
        Step 05: verify all bar riser values
        """
        time.sleep(5)
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step05: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step05: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step05: Verify bar color")
        bar_riser=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_riser, "Step 05: Verify  bar riser values", x_offset=0, y_offset=-7)
        
        """
        Step 06: Drag/drop "Product,Category" to Filter Pane
        """
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        time.sleep(13)
       
        """
        Step 07: Select Aggregation COUNT, select Operator EQUAL TO
        Step 08: De-select "All"
        Step 09: Check off values 2, 4, 5.
        Step 10: Verify filter dialog.
        Step 11: Click Ok.
        """
        l = ['[All]','2', '4','5']
        metaobj.create_visualization_filters('alpha',['Aggregation','Count'],['Operator','Equal to'], ['GridItems',l])
        time.sleep(8)
        
        """
        Step 12: verify query added to filter pane
        """
        time.sleep(5)
        parent_css="#qbFilterBox table>tbody>tr img"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field("CNT (Product,Category)", 1,"Step 12: verify query added to filter pane")
        
        """
        Step 13: Verify query pane
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Cost of Goods",1, "Step 13: Verify query pane")
        
        """
        Step 14: Verify all bar riser values
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step14: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Charger', 'DVD Players - Portable', 'Handheld', 'Portable TV', 'Professional', 'Streaming', 'Universal Remote Controls']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M','40M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step14.a: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step14.b: Verify bar color")
        time.sleep(5)
        bar_riser=['Product Subcategory:Charger', 'Cost of Goods:$2,052,711.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",  "riser!s0!g0!mbar", bar_riser, "Step 14.c: Verify bar riser values", x_offset=0, y_offset=-9)
        
        """
        Step 15: Click Run in the toolbar
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)        # to switch to run window
        time.sleep(15)
        
        """
        Step 16: Verify output
        """        
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, '//*[contains(@class,"riser!s0!g0!mbar")]')))
        raiser="div[id*='ibi$container$inner$HBOX_1']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 16: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Charger', 'DVD Players - Portable', 'Handheld', 'Portable TV', 'Professional', 'Streaming', 'Universal Remote Controls']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M','40M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16.a: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.b: Verify bar color")
        time.sleep(5)
        bar_riser=['Product Subcategory:Charger', 'Cost of Goods:$2,052,711.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_riser, "Step 16.c: Verify bar riser values")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2109138_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 17: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)            # switch back to main window
        time.sleep(15)
        
        """
        Step 18: Click "Save" in the toolbar > Type C2109138 > Click "Save" in the Save As dialog
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item("menu_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
                
                