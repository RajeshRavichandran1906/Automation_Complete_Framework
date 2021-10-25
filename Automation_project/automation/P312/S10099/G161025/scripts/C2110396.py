'''
Created on June23, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=147037&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110396
TestCase Name : IA-2897:Filter the field in DMYYq and DMYYm formats returns FOC006 and FOC009 errors
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
class C2110396_TestClass(BaseTestCase):

    def test_C2110396(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2110396'
        """
        Step 01: Launch the IA API with CENTURYMASTER (Folder - S8404 and Master - CENTURYMASTER) and login as "autodevuser03"
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/CENTURYMASTER&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/centurymaster','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        defobj = define_compute.Define_Compute(self.driver)
        time.sleep(10)
        
        """
        Step 02: Select Calculation\Define
        Step 03: Type name DMYYM, type Format DMYYm
        Step 04: Expand 'Order Date,Compound', add field "Order Date,Y-M" for expression, click ok
        """
        defobj.calculate_define_compute('Define','DMYYM','DMYYm','Dimensions->Centurymaster->Order Date,Compound->Order Date,Y-M', 1, 'ok')
        
        """
        Step 05: Verify DMYYM is added to data pane
        """
        metaobj.verify_data_pane_field("Measures", "DMYYM", 6, "Step 05: Verify DMYYM is added to data pane")
        
        """
        Step 06: Add "Revenue" and "DMYYM" fields to Query Pane
        """
        time.sleep(5)
        metaobj.datatree_field_click('Measures->DMYYM', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Measures->Revenue', 2, 1)
        time.sleep(5)
        
        """
        Step 07: Verify label values
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s0!g16!mbar']")
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 24, 'Step 07a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['01/2008', '03/2008', '05/2008', '07/2008', '11/2008', '02/2009', '04/2009', '06/2009', '10/2009', '12/2009']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g16!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        xaxis_value="DMYYM"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07:d(ii) Verify Y-Axis Title")
        
        """
        Step 08: verify query pane
        """
        metaobj.verify_query_pane_field("Horizontal Axis", "DMYYM", 1, "Step 08a: ")
        metaobj.verify_query_pane_field('Vertical Axis', "Revenue", 1, "Step 08b: ")
        time.sleep(5)
        
        """
        Step 09: Verify first and last 3 bar riser values
        """
        expected_tooltip=['DMYYM:01/2008', 'Revenue:33,409,279.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 09a: verify the default tooltip values for the first bar")
        time.sleep(5)
        expected_tooltip=['DMYYM:12/2008', 'Revenue:21,527,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g11!mbar",expected_tooltip, "Step 09b: verify the default tooltip values for the middle bar")
        time.sleep(5)
        expected_tooltip=['DMYYM:11/2009', 'Revenue:57,279,893.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g22!mbar",expected_tooltip, "Step 09c: verify the default tooltip values for the last bar")
        
        """
        Step 10: Drag/drop Define field DMYYM to Filter Pane, click ok to create filter
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_filter('Measures->DMYYM', 1)
        time.sleep(8)
        self.driver.find_element_by_id("avFilterOkBtn").click()
        time.sleep(8)
        
        """
        Step 11: verify query added to filter pane with out errors
        """
        metaobj.verify_filter_pane_field("DMYYM", 1, "Step 11a. ")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 24, 'Step 11a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['01/2008', '03/2008', '05/2008', '07/2008', '11/2008', '02/2009', '04/2009', '06/2009', '10/2009', '12/2009']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 11.c(i) Verify first bar color")
        xaxis_value="DMYYM"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11:d(ii) Verify Y-Axis Title")
        expected_tooltip=['DMYYM:12/2008', 'Revenue:21,527,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g11!mbar",expected_tooltip, "Step 11e: verify the default tooltip values")
        
        """
        Step 12: Click Run in the toolbar
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        
        
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """
        Step 13: Verify output
        """
        time.sleep(5)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 24, 'Step 13a: Verify the total number of risers displayed on Run Chart')
        x_val_list=['01/2008', '03/2008', '05/2008', '07/2008', '11/2008', '02/2009', '04/2009', '06/2009', '10/2009', '12/2009']
        y_val_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 13b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 13c(i): Verify first bar color")
        xaxis_value="DMYYM"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 13d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 13d(ii) Verify Y-Axis Title")
        expected_tooltip=['DMYYM:12/2008', 'Revenue:21,527,749.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g11!mbar",expected_tooltip, "Step 13e: verify the default tooltip values")
        time.sleep(15)
        utillobj.take_screenshot(driver.find_element_by_css_selector(" #orgdiv0"),'C2110396_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Close the output window.
        """
        time.sleep(6)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        
        """
        Step 13: Click "Save" in the toolbar > Type C2110396 > Click "Save" in the Save As dialog
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
