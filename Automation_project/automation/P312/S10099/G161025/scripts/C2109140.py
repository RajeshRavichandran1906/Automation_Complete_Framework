"""
Created on Jun 20, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109140
TestCase Name : IA-4072:Add Query Variable to Filter panel in visualization yields unrecoverable error
"""

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

class C2109140_TestClass(BaseTestCase):

    def test_C2109140(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109140'
        """
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add Revenue and Product Category
        """
        time.sleep(3)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category',2, 1)
        time.sleep(4)
        
        """
        Step 03: Verify label values
        """
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class^='xaxis'][class$='title']"))
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 03: Verify X title')
        utillobj._validate_page((By.CSS_SELECTOR,"#MAINTABLE_wbody1_f text[class='yaxis-title']"))
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Revenue",'Step 03: Verify Y title')
        parent_css1="#MAINTABLE_wbody1_f text[class^='xaxis'][class*='labels']"
        resultobj.wait_for_property(parent_css1,7)
        parent_css2="#MAINTABLE_wbody1_f text[class^='yaxis-labels']"
        resultobj.wait_for_property(parent_css2,8)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step03: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step03: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step03: Verify bar color")
         
        """
        Step 04: Verify bar riser values
        """
        time.sleep(2)
        a =['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 04: Verify bar riser values")
  
        """
        Step 05: Verify query pane
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue', 1, "Step 05: Verify Revenue added to query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 05: Verify Product,Category added to query pane")
         
        """
        Step 06: Drag the 'Store Front' filter from the Query Variables in the data pane to the filter section of the Query pane.
        """
        metaobj.datatree_field_click("Query Variables->Store Front",2,1)
        time.sleep(15)
        
        """
        Step 07: verify query added to filter pane
        """
        utillobj._validate_page((By.CSS_SELECTOR,"#qbFilterBox table>tbody>tr>td>img"))
        metaobj.verify_filter_pane_field("Store Front", 1, "Step 07: verify Store Front added to filter pane")
        time.sleep(15)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 07: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Revenue",'Step 07: Verify Y title')
        time.sleep(2)
        a =['Product Category:Accessories', 'Revenue:$90,051,223.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 07: Verify bar riser values")
        parent_css="#MAINTABLE_wbody1_f text[class^='yaxis-labels']"
        resultobj.wait_for_property(parent_css,7)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step07: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step07: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07: Verify bar color")
        
        """
        Step 08: Click Run in the toolbar.
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')   
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        
        """
        Step 09: Verify output.
        """
        elem1=(By.CSS_SELECTOR, '[class*="riser!s"]')
        resultobj._validate_page(elem1)
        time.sleep(10)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1_f', "Product Category",'Step 09: Verify X title')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1_f', "Revenue",'Step 09: Verify Y title')
        time.sleep(2)
        a =['Product Category:Accessories', 'Revenue:$90,051,223.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1",'riser!s0!g0!mbar', a,"Step 09: Verify bar riser values")
        time.sleep(6)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step09: X and Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step09: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09: Verify bar color")
        time.sleep(20)
        ele=driver.find_element_by_css_selector(" #orgdiv0")
        utillobj.take_screenshot(ele,'C2109140_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 10: Close the output window
        """
        time.sleep(2)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Stop 11: Click "Save" in the toolbar > Type C2109140 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()
        
