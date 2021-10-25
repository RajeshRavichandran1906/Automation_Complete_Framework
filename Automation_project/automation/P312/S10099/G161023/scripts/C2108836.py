'''
Created on May'31, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108836
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
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2108836_TestClass(BaseTestCase):
    def test_C2108836(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108836'

        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid02', 'mrpass02')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P141/S8357', 'mrid', 'mrpass')
        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click on "Revenue", "Sale,Year"
        """
        time.sleep(6)
        metaobj.datatree_field_click("Revenue", 2, 1)
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        
        """
        Step 03: Verify x and y axis labels
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year",'Step 03: Verify X title Sale Year')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue",'Step 03: Verify Y title Revenue')
        
        """
        Step 04: verify bar riser values
        """
        a=['Sale Year:2011', 'Revenue:$48,965,069.21', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", a, "Step 04: verify bar riser values")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 04: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 04: Verify first bar color")
        time.sleep(8)
        
        """
        Step 05: Add "Sale,Year" to the Filter pane > "OK".
        """
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        time.sleep(3)
        metaobj.create_visualization_filters('numeric')
        
        """
        Step 06: Verify query added to filter pane
        """
        parent_css="#qbFilterWindow #qbFilterBox img"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.verify_filter_pane_field("Sale,Year",1,"Step 06: Verify Sale,Year added to filter pane")
        time.sleep(15)
        
        """
        Step 07: verify slider prompt display properly
        """
        parent_css="#Prompt_1 #ar_Prompt_1 [id*='slider'] [class*='ui-slider-range']"
        resultobj.wait_for_property(parent_css, 1)
        range_val = ['2011', '2017']
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2011,'int',msg="Step 07: Verify Slider prompt min value 2011")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step 07: Verify Slider prompt max value 2017")
        time.sleep(5)

        """
        Step 08: Click "Run" in the toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 09: Verify output
        """
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2011,'int',msg="Step 09.1: Verify Slider prompt min value 2011")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step 09.1: Verify Slider prompt max value 2017")
        time.sleep(5)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Sale Year",'Step 09.2: Verify X title Sale Year')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue",'Step 09.3: Verify Y title Revenue')
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09.4: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 09.5: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 09.6: Verify first bar color")
        b = ['Sale Year:2011', 'Revenue:$48,965,069.21', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", b, "Step 09.7: Verify output")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108836_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
        Step 10: close the output window
        """
        self.driver.close()
        time.sleep(7)
        utillobj.switch_to_window(0)
        time.sleep(9)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        """
        Step 11: Click "Save" in the toolbar > Type C2108836 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()