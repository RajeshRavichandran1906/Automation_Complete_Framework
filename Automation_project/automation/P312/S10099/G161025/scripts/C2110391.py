'''
Created on June21, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110391
TestCase Name : IA-3762:Lasso (filter) visualization yields (FOC003)
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, core_metadata
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators


class C2110391_TestClass(BaseTestCase):

    def test_C2110391(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110391'
        """
        Step 01: Launch the IA API with wf_retail_lite (Folder - S8404 and Master - wf_retail_lite) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_metaobj = core_metadata.CoreMetaData(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add Revenue to Vertical axis, Sale Year to Horizontal axis and Product Category to Rows
        """
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(10)
        metaobj.datatree_field_click('Sale,Year', 2, 1)
        time.sleep(10)
        core_metaobj.expand_data_field_section('Dimensions->Product->Product')
        time.sleep(9)
        metaobj.datatree_field_click('Product,Category',1,1,'Add To Query','Rows')
        time.sleep(10)
        
        """
        Step 03: Verify label values
        """
        raiser="[class*='riser!s0!g5!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year", "Step 03: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03: verify Y axis title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step03: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 42, 'Step03: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar", "bar_blue", "Step03: Verify bar color") 
        time.sleep(8)

        """
        Step 04: verify query pane
        """
        time.sleep(5)
        metaobj.verify_query_pane_field('Rows', 'Product,Category',1, "Step 04: Verify query pane")
        
        """
        Step 05: Verify Accesories and Video production bar riser values
        """
        raiser="[class*='riser!s0!g5!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        a =['Product Category:Accessories', 'Sale Year:2016', 'Revenue:$53,208,007.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g5!mbar!r0!c0', a, "Step 05: Verify Accessories:2016 values")
        
        """
        Step 06: Add Product Category to filter, leave default and click ok.
        """
        core_metaobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category',1,1,'Filter')
        vis_filter="#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']"
        elem1=(By.CSS_SELECTOR, vis_filter)
        resultobj._validate_page(elem1)
        metaobj.create_visualization_filters('alpha')
        
        """
        Step 07: Verify query added to filter pane
        """
        raiser="[class*='riser!s0!g0!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step 07: Verify query added to filter pane")
        
        """
        Step 08: Lasso on Accessories 2011 to 2013 and click on Filter Chart
        """
        time.sleep(10)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!r0!c0', target_tag='rect', target_riser='riser!s0!g2!mbar!r0!c0', x_offset=0, y_offset=-50)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(8)
        metaobj.verify_filter_pane_field('PRODUCT_CATEGORY and TIME_YEAR',2,"Step 08: Verify query added to filter pane")
        
        """
        Step 09: Verify filtered values (2011 to 2013)
        """
        raiser="[class*='riser!s0!g0!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        elem1=(By.CSS_SELECTOR, '#iaCanvasPanel')
        resultobj._validate_page(elem1)
        time.sleep(5)
        elem = "#MAINTABLE_wbody1 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 300).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        a =['Product Category:Accessories', 'Sale Year:2011', 'Revenue:$5,039,297.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar!r0!c0',a,"Step 09: Verify Accessories:2011 values")
        time.sleep(10)
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 3, "Step 09: Verify filtered values (2011 to 2013)")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year", "Step 09: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 09: verify Y axis title")
        expected_xval_list=['2011', '2012', '2013']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09: Verify bar color") 
        time.sleep(8)
        """
        Step 10: Click Run in the toolbar
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        
        
        """
        Step 11:  Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g0!mbar!r0!c0']")
        resultobj._validate_page(elem1)
        a =['Product Category:Accessories', 'Sale Year:2011', 'Revenue:$5,039,297.57', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'riser!s0!g0!mbar!r0!c0',a,"Step 11: Verify Accessories:2011 values")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 11: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2011', '2012', '2013']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c(i) Verify first bar color")
        xaxis_value="Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:d(ii) Verify Y-Axis Title")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2110391_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Close the output window.
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        
        """
        Step 13: Click "Save" in the toolbar > Type C2110391 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 14: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == '__main__':
    unittest.main()
