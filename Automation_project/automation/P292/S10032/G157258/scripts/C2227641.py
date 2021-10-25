'''
Created on 28-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227641
TestCase Name = Numeric Filter format D20.2
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227641_TestClass(BaseTestCase):

    def test_C2227641(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227641'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
             
        """
        Step 02: Double-click "Revenue,Local Currency", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click('Revenue,Local Currency', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(8)
             
        """
        Step 04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Quarter" into the Columns bucket (Matrix in Query pane)
        """
        metaobj.datatree_field_click('Sale,Quarter', 1, 1, 'Add To Query', 'Columns')
        time.sleep(5)
             
        """
        Step 05: Drag and drop "Revenue,Local Currency" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Revenue,Local Currency', 1)
        time.sleep(5)
             
        """
        Step 06: Verify Filter dialog
        Step 07: Click OK
        """
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),11.38,"Step06: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),5114060.62,"Step06: Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
               
        """
        Step 08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step08: Verify 'Revenue,Local Currency' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',11.38,'float',msg="Step08: Verify filter prompt range values -min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step08: Verify filter prompt range values -max")
        time.sleep(2)
               
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28, 'Step8a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 08.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 08:d(ii) Verify Y Axis Title") 
        time.sleep(2)
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 08: Verify column header")
        expected_tooltip=['Sale Quarter:1', 'Product Category:Stereo Systems', 'Revenue Local Currency:319,705,081.32', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar!r0!c0",expected_tooltip, "Step 08e: verify the default tooltip values")      
        elem1=(By.CSS_SELECTOR, "#ar_Prompt_1")
        resultobj._validate_page(elem1)
        
        """
        Step09: Edit Prompt value > Drag slider handle to the right at value 2083.01 (or approximate)
        """
        time.sleep(2)
        browser=utillobj.parseinitfile('browser')
        if browser =='Firefox':
            propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 1,'float')
        if browser in ['IE', 'Chrome']:
            propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 1,'float')
         
        """
        Step10: Verify Canvas and Prompt 
        """
        if browser == 'Firefox':
            ran=1052211
            riser=13
        if browser in ['IE', 'Chrome']:
            ran=1022821
            riser=14
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',ran,'float',msg="Step10: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step10: Verify filter prompt range values-max")
        time.sleep(2)
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, riser, 'Step10a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "Step10.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10:d(ii) Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 10: Verify column header")
        expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 10e: verify the default tooltip values")      
            
        """
        Step11: Right click "Revenue,Local Currency" filter in the Filter pane > Edit
        """
        time.sleep(2)
        metaobj.filter_tree_field_click('Revenue,Local Currency',1,1, 'Edit...')
        time.sleep(2)
          
        """
        Step12: Verify Filter dialog
        Step13: Click Ok
        """
        if browser == 'Firefox':
            ran={'From':'1052212.33','To':'5114060.62'}
        if browser in ['IE', 'Chrome']:
            ran={'From':'1022821.24','To':'5114060.62'}
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(int(float(d['float_value'])),int(float(ran['From'])),"Step12: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(int(float(d['float_value'])),int(float(ran['To'])),"Step12: Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
            
        """
        step14: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
              
        """
        Step15: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)       
        elem1=(By.CSS_SELECTOR, "div[id*='ibi$container$inner$HBOX_1']")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227641_Actual_step15_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        elem1=(By.CSS_SELECTOR, "#sliderPROMPT_1")
        resultobj._validate_page(elem1)

        if browser == 'Firefox':
            ran=1052211
            riser=13
        if browser in ['IE', 'Chrome']:
            ran=1022821
            riser=14       
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',ran,'float',msg="Step15: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',5114060.62,'float',msg="Step15: Verify filter prompt range values-max") 
        time.sleep(2)
            
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, riser, 'step15a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "step15c.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 15:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 15:d(ii) Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 15b: Verify column header")
        expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 15e: verify the default tooltip values")      
              
        """
        Step16: Close output window
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
          
        """
        Step17: Click Save in the toolbar
        Step18: Save as "C2227641" > Click Save
        Step19: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
            
        """
        Step 20: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227641.fex&tool=idis
        Step21: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        elem1=(By.CSS_SELECTOR, "#ar_Prompt_1")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step21: Verify 'Revenue Local Currency' appears in filter pane")        
        if browser == 'Firefox':
            ran=1052211
            riser=13
        if browser in ['IE', 'Chrome']:
            ran=1022821
            riser=14
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',ran,'float',msg="Step21: Verify filter prompt range values -min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step21: Verify filter prompt range values -max")
         
        time.sleep(2)
            
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, riser, 'Step21a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 21b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "Step21.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 21:d(ii) Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 21: Verify column header")
        expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 21e: verify the default tooltip values")      
          
        """
        Step22: Logout
        """

if __name__ == '__main__':
    unittest.main()
    