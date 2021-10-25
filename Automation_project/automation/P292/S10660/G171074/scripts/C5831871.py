'''
Created on Jun 26, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831871
TestCase Name = Numeric Filter format D20.2
'''
import unittest,time
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run, metadata

class C5831871_TestClass(BaseTestCase):

    def test_C5831871(self):
        
        """
        CLASS OBJECTS
        """
        driver = self.driver #Driver reference object created
        metadataobj = metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831871'
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)
        utillobj.wait_for_page_loads(metaobj.chart_long_timesleep)
        """
        Step 02: Double-click "Revenue,Local Currency", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click('Revenue,Local Currency', 2, 1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='mbar']", 1, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='mbar']", 7, metaobj.chart_long_timesleep)
             
        """
        Step 04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Quarter" into the Columns bucket (Matrix in Query pane)
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Columns', 0)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class*='colLabel!c0!']", '1', metaobj.chart_long_timesleep)
        metadataobj.collapse_data_field_section('Sales_Related')
             
        """
        Step 05: Drag and drop "Revenue,Local Currency" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Revenue,Local Currency', 1)
        utillobj.synchronize_until_element_is_visible("#avfFromValue input", metaobj.chart_long_timesleep)
     
        """
        Step 06: Verify Filter dialog
        Step 07: Click OK
        """
        utillobj.synchronize_with_number_of_element("#avfFromValue input", 1, 20)
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),11.38,"Step 06.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),5114060.62,"Step 06.02: Verify range to value")  
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
        
        """
        Step 08: Verify Canvas
        """
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step 08.01: ")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',11.38,'float',msg="Step 08.02: Verify filter prompt range values -min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step 08.03: Verify filter prompt range values -max")
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 rect[class*='riser']", 28, metaobj.chart_long_timesleep)
        time.sleep(8) # giving time for the riser to show up properly
        utillobj.wait_for_page_loads(100)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 28, 'Step 08.04: Verify the total number of risers displayed on Run Chart')
        
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.05: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step 08.06: Verify first bar color")
#         xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 08.07: Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Category', expected,"Step 08.08: Verify column header")
#         expected_tooltip=['Sale Quarter:1', 'Product Category:Stereo Systems', 'Revenue Local Currency:319,705,081.32', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar!r0!c0",expected_tooltip, "Step 08.09: verify the default tooltip values")      
        utillobj.synchronize_until_element_is_visible("#ar_Prompt_1", metaobj.chart_long_timesleep)
        
        """
        Step09: Edit Prompt value > Drag slider handle to the right at value 2083 (or approximate)
        """
        propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 1,'float')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='riser']", 14, metaobj.chart_long_timesleep)
        
        """
        Step10: Verify Canvas
        """
        if Global_variables.browser_name == 'firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',120000,'float',msg="Step 10.01: Verify filter prompt range values-min")
            riser=14
        if Global_variables.browser_name in ['ie', 'Chrome','edge']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',1022821,'float',msg="Step 10.01: Verify filter prompt range values-min")
            riser=14
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step 10.02: Verify filter prompt range values-max")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step 10.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.05: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "Step 10.06: Verify first bar color")
#         xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10.07: Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Category', expected,"Step 10.08: Verify column header")
#         expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 10.09: verify the default tooltip values")      
            
        """
        Step11: Right click "Revenue,Local Currency" filter in the Filter pane > Edit
        """
        time.sleep(2)
        metaobj.filter_tree_field_click('Revenue,Local Currency',1,1, 'Edit...')
        utillobj.synchronize_until_element_is_visible("#avfFromValue input", metaobj.chart_long_timesleep)
          
        """
        Step12: Verify Filter dialog
        Step13: Click OK
        """
        if Global_variables.browser_name == 'firefox':
            ran={'From':'1020000','To':'5114060.62'}
        if Global_variables.browser_name in ['ie', 'chrome','edge']:
            ran={'From':'1022821.24','To':'5114060.62'}
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.as_GE(int(float(d['float_value'])),int(float(ran['From'])), "Step 13.01: Verify From value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(int(float(d['float_value'])),int(float(ran['To'])),"Step 13.02: Verify range to value")  
        metaobj.create_visualization_filters('numeric')
        utillobj.synchronize_until_element_disappear("#avFilterOkBtn", metaobj.chart_long_timesleep)
            
        """
        step14: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
              
        """
        Step15: Verify output
        """
        utillobj.synchronize_until_element_is_visible("#sliderPROMPT_1 span[id$='s_min']", metaobj.chart_long_timesleep)
        if Global_variables.browser_name == 'firefox':
            ran=1020000
            riser=14
        if Global_variables.browser_name in ['ie', 'chrome','edge']:
            ran=1022821
            riser=14       
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',ran,'float',msg="Step 15.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',5114060.62,'float',msg="Step 15.02: Verify filter prompt range values-max") 
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, riser, 'step 15.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "step 15.05: Verify first bar color")
#         xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 15.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 15.06: Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Category', expected,"Step 15.07: Verify column header")
#         expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 15.08: verify the default tooltip values")      
              
        """
        Step16: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible('#applicationButton', metaobj.chart_long_timesleep)
          
        """
        Step17: Click Save in the toolbar > Save as "C5831871" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step18: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        utillobj.infoassist_api_logout()
            
        """
        Step 19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2227671.fex&tool=idis
        Step 20: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", metaobj.chart_long_timesleep)
        
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step 20.01: Verify 'Revenue Local Currency' appears in filter pane")        
        if Global_variables.browser_name == 'firefox':
            ran=1020000
            riser=14
        if Global_variables.browser_name in ['ie', 'chrome','edge']:
            ran=1022821
            riser=14
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',ran,'float',msg="Step 20.02: Verify filter prompt range values -min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',5114060.62,'float',msg="Step 20.03: Verify filter prompt range values -max")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, riser, 'Step 20.04: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Camcorder', 'Stereo Systems', 'Televisions', 'Accessories', 'Camcorder']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 20.05: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!r0!c0", "bar_blue", "Step 20.06: Verify first bar color")
#         xaxis_value="Product Category"
        yaxis_value="Revenue Local Currency"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 20.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 20.07: Verify Y Axis Title") 
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Category', expected,"Step 20.08: Verify column header")
#         expected_tooltip=['Sale Quarter:1', 'Product Category:Camcorder', 'Revenue Local Currency:18,822,808.58', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar!r0!c0",expected_tooltip, "Step 20.09: verify the default tooltip values")      
          
        """
        Step 21: Logout
        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()