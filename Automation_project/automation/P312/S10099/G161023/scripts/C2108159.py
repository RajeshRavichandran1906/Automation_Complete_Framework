'''
Created on May'21, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108159
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity


class C2108159_TestClass(BaseTestCase):

    def test_C2108159(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108159'
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
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4','mrid','mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """
        Step 02: Double click "Revenue" and "Customer,Business Region"
        """
        metaobj.datatree_field_click("Revenue",2,1)
        metaobj.datatree_field_click("Customer,Business,Region",2,1)
        time.sleep(12)
        
        """
        Step 03: Verify x and y axis labels
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(4)
        expected_xval_list=['EMEA', 'North America', 'Oceania', 'South America']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 03c Verify the total number of risers displayed on Run Chart')

        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        
        xaxis_value="Customer Business Region"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        
        """
        Step 04: verify all bar riser values
        """
        time.sleep(4)
        bar = ['Customer Business Region:EMEA', 'Revenue:$562,316,133.90', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Sub Region']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar, "Step 04: verify all bar riser values")
        
        """
        Step 05: Add Sale, Year to Horizontal axis.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Year",1,1,"Add To Query","Horizontal Axis")
        
        """
        Step 06: Verify label values.
        """
        time.sleep(12)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 23)
        time.sleep(4)
        expected_xval_list=['EMEA : 2011', 'EMEA : 2012', 'EMEA : 2013', 'EMEA : 2014', 'EMEA : 2015', 'EMEA : 2016', 'North America : 2011', 'North America : 2012', 'North America : 2013', 'North America : 2014', 'North America : 2015', 'North America : 2016', 'Oceania : 2012', 'Oceania : 2013', 'Oceania : 2014', 'Oceania : 2015', 'Oceania : 2016', 'South America : 2011', 'South America : 2012', 'South America : 2013', 'South America : 2014', 'South America : 2015', 'South America : 2016']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 06.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 23, 'Step 06.b Verify the total number of risers displayed on Run Chart')

        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c(i) Verify first bar color")

        xaxis_value="Customer Business Region : Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 06:d(ii) Verify Y-Axis Title")
        
        """
        Step 07: Add Sale, Year to Filter, change the operator to "Equal to", select only 2012 and click Ok.
        """
        metaobj.datatree_field_click("Sale,Year",1,1,"Filter")
        time.sleep(12)
        l= ['[All]','2012']
        metaobj.create_visualization_filters('numeric', ['Operator','Equal to'], ['GridItems',l])
        time.sleep(12)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        expected_xval_list=['EMEA : 2012', 'North America : 2012', 'Oceania : 2012', 'South America : 2012']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 07b Verify the total number of risers displayed on Run Chart')

        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        
        xaxis_value="Customer Business Region : Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:d(ii) Verify Y-Axis Title")

    
        """
        Step 08: verify Sale,Year query added to fitler pane.
        """
        time.sleep(3)
        metaobj.verify_filter_pane_field("Sale,Year",1,'Step 08: Sale Year added to filter pane')

        """
        Step 09: Add Customer, Business Region to Filter, accept default and click Ok.
        """
        time.sleep(3)
        metaobj.datatree_field_click("Customer,Business,Region",1,1,"Filter")
        time.sleep(12)
        metaobj.create_visualization_filters("alpha")

        """
        Step 10: verify Customer,Business Region query added to filter pane.
        """
        time.sleep(12)
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.verify_filter_pane_field("Customer,Business,Region",2,'Step 10: Customer Businees Region added to filter pane')
        time.sleep(6)
        expected_xval_list=['EMEA : 2012', 'North America : 2012', 'Oceania : 2012', 'South America : 2012']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 10.b Verify the total number of risers displayed on Run Chart')

        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c(i) Verify first bar color")
        
        xaxis_value="Customer Business Region : Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:d(ii) Verify Y-Axis Title")

        """
        Step 11 : Change "Equal to" to DropDown Single Select in Customer, Business Region filter prompt.
        """
        time.sleep(3)
        propertyobj.change_prompt_options("2","Dropdown (Single Select)")
        
        """
        Step 12 : Verify EMEA is the default value in dropdown.
        """
        time.sleep(12)
        css ="select[id*='combobox'] option[value='EMEA']"
        elem=(By.CSS_SELECTOR,css)
        resultobj._validate_page(elem)
        try:
            em=driver.find_element_by_css_selector(css).is_displayed()
            
        except:
            em = False
        utillobj.asequal(True,em, "Step 12 : Verify EMEA is the default value in dropdown."  )
        time.sleep(15)
        
        """
        Step 13 : Verify EMEA region values display in preview.
        """
        parent_css="#MAINTABLE_wbody1 svg > g text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css, 1)
        bar_runtim = ['Customer Business Region:EMEA', 'Sale Year:2012', 'Revenue:$39,630,841.14', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_runtim, "Step 13 : Verify EMEA region values display in preview.")
        expected_xval_list = ['EMEA : 2012']
        expected_yval_list = ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M', '45M']
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13.a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 13.b Verify the total number of risers displayed on Run Chart')

        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.c(i) Verify first bar color")
        
        xaxis_value="Customer Business Region : Sale Year"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 13:d(ii) Verify Y-Axis Title")
        time.sleep(30)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2108159_Actual_step13', image_type='actual')
        
        
        """
        Step 14 : Click "Save" in the toolbar > Type C2108159 > Click "Save" in the Save As dialog
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()
