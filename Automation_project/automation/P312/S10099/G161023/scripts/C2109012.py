'''
Created on June7, 2016
@author: Kiruthika

Test Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109012&group_by=cases:section_id&group_id=146864&group_order=asc
TestCase Name : IA-4362:Vis: Exclude from chart is not working if the Filter Prompt and Chart dimension are of same field
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2109012_TestClass(BaseTestCase):

    def test_C2109012(self):
        driver = self.driver #Driver reference object created
        """    TESTCASE VARIABLES    """
        Test_Case_ID = 'C2109012'
        
        """    Step 01: Launch API (Folder - S8357 and Master - wf_retail_lite) and login as "autodevuser03"    """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    Step 02: Add Product Category and Cost of Goods to Canvas    """
        metaobj.datatree_field_click('Product,Category',2,1)
        time.sleep(8)
        metaobj.datatree_field_click('Cost of Goods',2,1)
        time.sleep(8)
        
        """    Step 03: Verify x and y axis labels    """
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03:a(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03b: Verify the total number of risers displayed on Preview Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 03c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 03.d(i) Verify first bar color")
        expected_tooltip=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar",expected_tooltip, "Step 03.e: verify the default tooltip values")
        
        """    Step 04: Verify query pane dialog.  Vertical Axis > Cost of Goods, Horizontal Axis> Product,Category """
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category', 1, "Step 04: Verify query pane dialog Horizontal Axis> Product,Category")
        metaobj.verify_query_pane_field('Vertical Axis', 'Cost of Goods', 1, "Step 04: Verify query pane dialog Vertical Axis > Cost of Goods")
        
        """    Step 05: Add Product Category to Filter, accept default and click Ok.    """
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category',1,1,'Filter')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#avFilterOkBtn")
        resultobj._validate_page(elem1)
        time.sleep(5)
        metaobj.create_visualization_filters('alpha')
        time.sleep(10)
        
        """    Step 06: verify query added to filter pane.    """
        metaobj.verify_filter_pane_field('Product,Category', 1, "Step 06: verify query added to filter pane.")
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=True, msg='Step 06a: verify the ALL is checked under Show prompt')
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 06b: Verify the total number of risers displayed on Preview Chart')
        
        """    Step 07: Hover over on 'Media player' and choose Exclude from Chart.    """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g3!mbar', 'Exclude from Chart')
        time.sleep(10)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(5)
        
        """    Step 08: verify Media player is unchecked in filter prompt    """
        propertyobj.select_or_verify_show_prompt_item(1,'Media Player', True, verify_type=False, msg='Step 08a: verify "Media Player" is unchecked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=False, msg='Step 08a: verify the ALL is checked under Show prompt')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 08b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers','Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        time.sleep(5)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list,'Step 08: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 08:d(ii) Verify Y-Axis Title")
        
        
        """    Step 09: Click "Run" in the toolbar.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    Step 10: Verify 'Media Player' is unchecked in output and verify 'Media Player' not displayed in chart.     """
        propertyobj.select_or_verify_show_prompt_item(1,'Media Player', True, verify_type=False, msg='Step 10a: verify "Media Player" is unchecked under Show prompt')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 10b: Verify the total number of risers displayed on Run Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 10c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 10d(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10e(ii) Verify Y-Axis Title")
        expected_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 10f: verify the default tooltip values")
        
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2109012_Actual_step10', image_type='actual')
        time.sleep(5)
        
        """    Step 11: Close the output window    """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """    Step 12: Click "Save" in the toolbar > Type C2109012 > Click "Save" in the Save As dialog    """
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
    

