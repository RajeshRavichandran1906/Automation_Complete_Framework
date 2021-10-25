"""
Created on Jun 28, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140689
TestCase Name : IA-4578:Vis: Filter Prompt doesn't work after Drilldown, Remove filter and Reset if same field in Horizontal and Filter
"""

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_run, metadata
from common.lib import utillity
from common.wftools.visualization import Visualization

class C2140689_TestClass(BaseTestCase):

    def test_C2140689(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140689'
        element_css = '#queryTreeWindow'
        
        """
        CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite 
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS404%2F
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
                
        """
        Step 2: Double click Product Category and Revenue.
        """
        metadataobj.collapse_data_field_section('Filters and Variables')
        visual.double_click_on_datetree_item("Product,Category", 1)
        visual.wait_for_visible_text(element_css, "Product,Category")
        visual.double_click_on_datetree_item("Revenue", 1)
        visual.wait_for_visible_text(element_css, "Revenue")
        
        """
        Step 03: Verify label values
        """
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class*='riser']", 7)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Category", "Step 03.01: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 03.02: verify Y axis title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03.04: X and Y axis Scales Values has changed or NOT')
                
        """
        Step 04: Verify query pane
        """
        metaobj.verify_query_pane_field("Vertical Axis", "Revenue", 1, "Step 04.01: verify Revenue added to query pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "Product,Category", 1, "Step 04.02: verify Product,Category added to query pane")
        
        """
        Step 05: Hover over "Camcorder" bar.
        Verify the tool tip:
        """
        bar_riser=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g1!mbar", bar_riser, "Step 05.01: Verify bar riser values.")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 05.02: Verify first bar color")
        
        """
        Step 06: Add Product Category to Filter, accept default and click ok.
        """
        time.sleep(8)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        time.sleep(2)
        metaobj.create_visualization_filters('alpha')
        time.sleep(4)
       
        """
        Step 07: Verify query added to filter pane
        """
        metaobj.verify_filter_pane_field("Product,Category",1,"Step 07.01: Verify query added to filter pane")
        
        """
        Step 08: Change the Filter to List (Single Select) using the drop down.
        """
        time.sleep(5)
        propertyobj.change_prompt_options("1", "List (Single Select)")
        time.sleep(8)
        x=['Accessories']
        time.sleep(10)
        y=['0', '30M', '60M', '90M', '120M', '150M']
        time.sleep(10)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 08.01: X and Y axis Scales Values has changed or NOT')
        time.sleep(5)
        bar_riser=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', "riser!s0!g0!mbar", bar_riser, "Step 08.02: Verify bar riser values in preview")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.03: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 1, "Step 08.04: Verify number of risers")
        
        """
        Step 09: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 10: Select Accessories and click Drilldown.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)   
        time.sleep(10)
        x=['Accessories']
        y=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 10.01: X and Y axis Scales Values has changed or NOT')
        time.sleep(5)
        bar_riser=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Drill down to Product Subcategory']
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.02: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 1, "Step 10.03: Verify number of risers")
        time.sleep(5)
        
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar","Drill down to Product Subcategory", 1)
         
        """
        Step 11: verify label values
        """
        loc="[id^='MAINTABLE_1'] [class*='riser!s0!g2!mbar']"
        elem1=(By.CSS_SELECTOR, loc)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory", "Step 11.01: verify X axis title product Subcategory")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 11.02: verify Y axis title Revenue")
         
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 11.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Charger', 'Headphones', 'Universal Remote Controls']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.04: X and Y axis Scales Values has changed or NOT')
         
        """
        Step 12: Verify bar riser values (product subcategory:revenue)
        """
        time.sleep(10)
        bar_rise_runtime=['Product Subcategory:Charger', 'Revenue:$4,022,834.91', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_rise_runtime, "Step 12.01: Verify bar riser values (product subcategory:revenue)",x_offset=0,y_offset=-7)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.02: Verify bar color")
        time.sleep(5)
        
        """
        Step 13: Select Reset from the Run menu option.
        """
        runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        time.sleep(15)
          
        """
        Step 14: Hover Over on Accessories and choose DrillDown.
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(10)
        x=['Accessories']
        y=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x, y, 'Step 14.01: X and Y axis Scales Values has changed or NOT')
        time.sleep(5)
        bar_riser=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Drill down to Product Subcategory']
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.02: Verify first bar color")
        resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, 1, "Step 14.03: Verify number of risers")
        time.sleep(5)
         
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar","Drill down to Product Subcategory")
         
        """
        Step 15: Verify x-axis label title and values (product subcategory)
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(15)         
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory", "Step 15.01: verify X axis title Product Subcategory")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 15.02: verify Y axis title")        
         
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 15.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Charger', 'Headphones', 'Universal Remote Controls']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.05: Verify bar color")
                 
        """
        Step 16: Hover over on any bar and choose Remove Filter.
        """
        time.sleep(5)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g0!mbar","Remove Filter")
        time.sleep(5)
         
        """
        Step 17: Verify output
        """
        expected_xval_list=['Charger', 'Headphones', 'Universal Remote Controls']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M', '80M']
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 17.01: Verify the total number of risers displayed on Run Chart')
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 17.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 17.03: Verify bar color")
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory", "Step 17.04: verify X axis title Product Subcategory")
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue", "Step 17.05: verify Y axis title")  
        
        """
        Step 18: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 19: Click "Save" in the toolbar > Type C2140689 > Click "Save" in the Save As dialog. Save the fex with the same name as this test case.
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 20: Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()