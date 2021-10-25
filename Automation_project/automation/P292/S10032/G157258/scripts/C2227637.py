'''
Created on 23-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227637
TestCase Name = Alphanumeric Filter with Geometry field
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227637_TestClass(BaseTestCase):

    def test_C2227637(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227637'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 02: Double-click "Revenue Local Per SQ. M.", located under Sales Measures
        Step 03: Expand Dimension "Customer" > Double click "Customer,Country"
        """
        metaobj.datatree_field_click('Revenue Local Per SQ. M.', 2, 1)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
        metadataobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(5)
        
        metaobj.datatree_field_click('Customer,Country', 2, 1)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 42)
        
        """
        Step 04: Expand Dimension "Customer" > "Customer,Country" > "Attributes" > Drag and drop "Customer,Continent" into the Filter pane
        """
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_filter('Dimensions->Customer->Customer->Customer,Country->Attributes->Customer,Continent',1)
        time.sleep(5)
        
        """
        Step 05: Verify Filter dialog
        Step 06: Uncheck "[All]"
        Step 07: Select "North America" and "South America"
        Step 08: Click OK
        """
        item_list=['[All]', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true')
        time.sleep(2)
        l=['[All]', 'North America', 'South America']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 09: Verify Canvas
        """
        metaobj.verify_filter_pane_field('Customer,Continent',1,"Step09: Verify 'Customer,Continent' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, 'North America', verify=True, verify_type="true", msg="Step09: Verify North America is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'South America', verify=True, verify_type="true", msg="Step09: Verify South America is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 09a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Argentina', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Mexico', 'United States']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 09.c(i) Verify first bar color")
        xaxis_value="Customer Country"
        yaxis_value="Revenue Local Per SQ. M."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09:d(ii) Verify Y-Axis Title")  
#         expected_tooltip=['Customer Country:Brazil', 'Revenue Local Per SQ. M.:186,547.23', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 09e: verify the default tooltip values")      
                
        """
        Step10: Click Run
        """
        time.sleep(3)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
        
        """
        Step11: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(10) 
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227637_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        propertyobj.select_or_verify_show_prompt_item(1, 'North America', verify=True, verify_type="true", msg="Step11: Verify North America is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'South America', verify=True, verify_type="true", msg="Step11: Verify South America is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 11a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Argentina', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Mexico', 'United States']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 11.c(i) Verify first bar color")
        xaxis_value="Customer Country"
        yaxis_value="Revenue Local Per SQ. M."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11:d(ii) Verify Y-Axis Title")  
#         expected_tooltip=['Customer Country:Brazil', 'Revenue Local Per SQ. M.:186,547.23', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 11e: verify the default tooltip values")
        
        """
        Step12: Close output window
        Step13: Click Save in the toolbar
        Step14: Save as "C2227637" > Click Save
        Step15: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227637.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        
        """
        Step17: Verify Canvas
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.verify_filter_pane_field('Customer,Continent',1,"Step17: Verify 'Customer,Continent' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, 'North America', verify=True, verify_type="true", msg="Step17: Verify North America is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'South America', verify=True, verify_type="true", msg="Step17: Verify South America is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 17a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Argentina', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Mexico', 'United States']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 17b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 17.c(i) Verify first bar color")
        xaxis_value="Customer Country"
        yaxis_value="Revenue Local Per SQ. M."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 17:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 17:d(ii) Verify Y-Axis Title")  
#         expected_tooltip=['Customer Country:Brazil', 'Revenue Local Per SQ. M.:186,547.23', 'Filter Chart', 'Exclude from Chart', 'Drill up to Customer Business Sub Region', 'Drill down to Customer State Province']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 17e: verify the default tooltip values")                
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()
    