'''
Created on May'17, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108155
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2108155_TestClass(BaseTestCase):

    def test_C2108155(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108155'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01: Launch the IA API with wf_retail_lite
            http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
            Step 02 : Double click Gross Profit & Product,Category
        """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(2)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        """
            Step 03 : Verify x and y axis labels

        """
        time.sleep(5)        
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03:c(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.d: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 03.d Verify second bar color")
        
        """
        Step 04 : Verify all bar riser values
        """
        bar=['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar, " Step 04 : Verify all bar riser values")

        """
        Step 05 : Drag Sale,Year (YYMDy) to filter pane
        """
        time.sleep(1)
        #metaobj.datatree_field_click("Sale,Year", 1, 2,"Filter")
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Year',0)
        time.sleep(2)
        metaobj.create_visualization_filters('alpha')
        
        
        """
        Step 06 : Verify query added to filter pane.
        """
        time.sleep(15)
        metaobj.verify_filter_pane_field("Sale,Year",1,'Step 06: Sale Year added to filter pane')
        time.sleep(6)
        """
        Step 07 : verify slider range values.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2011,'int',msg="Step07: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step07: Verify filter prompt range values- max")
        time.sleep(2)
        """
        Step 08 : Run visualization.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 09 : verify output.
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 09a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09b: X annd Y axis Scales Values has changed or NOT')
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09:c(ii) Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 09.d Verify second bar color")
        
        bar_runtime=['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar_runtime, "Step 09.e : verify output.")
        time.sleep(8)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2011,'int',msg="Step09: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step09: Verify filter prompt range values- max")
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2108155_Actual_step09', image_type='actual')
        time.sleep(5)
        
        
        """
        Step 10 : Close browser.
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(9)
        
        """
        Step 11 : Click "Save" in the toolbar > Type C2108155 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(6)
        
        
if __name__ == '__main__':
    unittest.main()