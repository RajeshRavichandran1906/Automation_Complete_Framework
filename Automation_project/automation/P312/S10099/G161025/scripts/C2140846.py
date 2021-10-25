"""
Created on Jun 28, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140846
TestCase Name : IA-4557:Vis: Exclude From Chart in vis with same field in color and Filter prompt working wrongly in preview
"""

import unittest, time 
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea
from common.wftools.visualization import Visualization

class C2140846_TestClass(BaseTestCase):

    def test_C2140846(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140846'
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Double click Product Category and Revenue.
        """
        visual.double_click_on_datetree_item("Product,Category", 1)
        visual.wait_for_visible_text(element_css, "Product,Category")
        visual.double_click_on_datetree_item("Revenue", 1)
        visual.wait_for_visible_text(element_css, "Revenue")

        """
        Step 03: Verify label values
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class*='riser']", 7)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03.01: verify X axis title Product Category")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03.02: verify Y axis title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.04: X annd Y axis Scales Values has changed or NOT')
                
        """
        Step 04: Hover over "Camcorder" bar.
        Verify the tool tip:
        """
        bar_riser=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g1!mbar", bar_riser, "Step 04.01: Verify bar riser values.")
        
        """
        Step 05: Add Sale Year to Color.
        """
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Add To Query","Color")
        time.sleep(5)
        
        """
        Step 06: Verify query pane
        """
        metaobj.verify_query_pane_field("Vertical Axis","Revenue",1,"Step 06.01: Verify query pane")
        
        """
        Step 07: Add Sale Year to Filter Prompt, change to Equal to and Choose 2011 and 2012 and click Ok 
        """
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        time.sleep(3)
        l=["[All]","2011","2012"]
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'],['GridItems',l])
        """
        Step 08: Verify query added to filter pane
        """
        time.sleep(6)
        metaobj.verify_filter_pane_field("Sale,Year",1,"Step 08.01: Verify query added to filter pane")
        
        time.sleep(15)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step 08.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.03: X annd Y axis Scales Values has changed or NOT')
        
        
        """
        Step 09: Choose Accessories 2011 and click "Exclude From Chart".
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)   
        time.sleep(10)   
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar","Exclude from Chart")
        time.sleep(8)
        
        """
        Step 10: Verify query added to filter pane
        """
        
        metaobj.verify_filter_pane_field("TIME_YEAR and PRODUCT_CATEGORY",2, "Step 10.01: Verify query added to filter pane")
        
        """
        Step 11: Verify filtered bar values.
        """
        time.sleep(8)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s1!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)   
        time.sleep(10)
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 11.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.02: X annd Y axis Scales Values has changed or NOT')
        
        bar_values=['Product Category:Accessories', 'Revenue:$7,860,068.93', 'Sale Year:2012', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar", bar_values, "Step 11.03: Verify filtered bar values.")
        
        """
        Step 12: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
         
        """
        Step 13: Verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)  
        time.sleep(15)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 13.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 13.02: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 13.03: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 13.04: verify Y axis title")
        
        """
        Step 14: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 15: Click "Save" in the toolbar > Type C2140846 > Click "Save" in the Save As dialog
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 16: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()