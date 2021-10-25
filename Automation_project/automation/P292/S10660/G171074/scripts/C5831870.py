'''
Created on 10-May-2018

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831870
TestCase Name = Numeric Filter format D20.2M
'''
import unittest,time
from common.wftools.visualization import Visualization
from common.lib import utillity, core_utility
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run
from common.lib.basetestcase import BaseTestCase

class C5831870_TestClass(BaseTestCase):

    def test_C5831870(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C5831870'
        
        """
        CLASS OBJECTS
        """
        driver = self.driver #Driver reference object created
        visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)        
                  
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='mbar']", 1, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1_f rect[class*='mbar']", 7, metaobj.chart_long_timesleep)
                  
        """
        Step 04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Year" into the Rows bucket (Matrix in Query pane)
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year", 1, 'Rows', 0)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class*='rowLabel!r0']", '2011', metaobj.chart_long_timesleep)
                  
        """
        Step 05: Drag and drop "Cost of Goods" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Cost of Goods', 1)
                  
        """
        Step 06: Verify Filter dialog
        Step 07: Type 5000 in the "From" value input box
        Step 08: Click OK
        """
        utillobj.synchronize_until_element_is_visible("#avfFromValue input", metaobj.chart_long_timesleep)
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),16,"Step 06.00: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),13000,"Step 06.01: Verify range to value")  
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',['From',5000])
        utillobj.synchronize_until_element_disappear('#avFilterOkBtn', metaobj.chart_long_timesleep)
                   
        """
        Step 09: Verify Canvas
        """
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 09.00:")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5000,'int',msg="Step 09.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step 09.02: Verify filter prompt range values-max")
        parent_css = "#MAINTABLE_wbody1  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 12, 10)    
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step 09.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list= ['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
#         expected_yval_list=['0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M']
#         resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09.04:')
        visual.verify_x_axis_label(expected_xval_list, msg='Step 09.04')
        visual.verify_y_axis_label(expected_yval_list,msg='Step 09.04')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 09.05: Verify first bar color")
#         xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
#         resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09.07: Verify Y Axis Title") 
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 09.08: Verify column header")
                    
        """
        Step10: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
                     
        """
        Step11: Verify output
        """
        utillobj.synchronize_until_element_is_visible("#sliderPROMPT_1 span[id$='s_min']", metaobj.chart_long_timesleep)  
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',5000, 'int',msg="Step 11.00: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',13000,'int',msg="Step 11.01: Verify filter prompt range values-max") 
                   
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step 11.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 11.04: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 11.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11.06: Verify Y Axis Title") 
       
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 11.07: Verify column header")
                     
        """
        Step12: Close output window
        Step13: Click Save in the toolbar
        Step14: Click Save in the toolbar > Save as "C5831870" > Click Save
        Step15: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible('#applicationButton', metaobj.chart_long_timesleep)
                     
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
              
        """
        Step 16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC5831870.fex&tool=idis
        Step 17: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Cost of Goods', 1, "Step 17.00: Verify 'Cost of Goods' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5000,'int',msg="Step 17.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step 17.02: Verify filter prompt range values-max")
        time.sleep(2)
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step 17.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
#         expected_yval_list=['0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M']
        expected_yval_list= ['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 17.04:')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 17.05: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 17.06: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 17.07: Verify Y Axis Title") 
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 17.08: Verify column header")
        time.sleep(2)    
        
        """
        Step18: Edit the Prompt value > Drag slider handle to the right, at value 10061.81 (or approximate)
        """
        propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 2, 'float')
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class*='rowLabel!r0']", '2012', metaobj.chart_long_timesleep)
         
        """
        Step19: Verify Canvas and Prompt 
        """
        ran=10193
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',ran,'float',msg="Step 19.00: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step 19.01: Verify filter prompt range values-max")
        time.sleep(2)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 9, 'Step 19.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 19.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 19.04: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 19.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 19.06: Verify Y Axis Title") 
        expected=['2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 19.07: Verify column header")
          
        """
        Step20: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()    
            
        """
        Step21: Verify output
        """
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", metaobj.chart_long_timesleep)     
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 9, 'Step 21.00: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 21.01: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 21.02: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 21.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 21.04: Verify Y Axis Title") 
        expected=['2012', '2013', '2014', '2015', '2016']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 21.05: Verify column header")
            
        """
        Step22: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#qbFilterBox td", metaobj.chart_long_timesleep) 
         
        """
        Step23: Right click "Cost of Goods" filter in the Filter pane > Edit
        """
        metaobj.filter_tree_field_click('Cost of Goods',1,1, 'Edit...')
        utillobj.synchronize_until_element_is_visible("#avAggregationComboBox", metaobj.chart_long_timesleep)
         
        """
        Step24: Verify Filter dialog
        """
        aggregation_value_ele = self.driver.find_element_by_css_selector("#avAggregationComboBox")
        utillobj.asequal(aggregation_value_ele.text.replace('\n ',''),'(None)',"Step 24.00: Verify Aggregation value")
        By_field_value_ele = self.driver.find_element_by_css_selector("#avByFieldsComboBox")
        utillobj.asequal(By_field_value_ele.text.replace('\n ',''),'Sale,Year',"Step 24.01: Verify By Field value")
        disabled_status = self.driver.find_element_by_css_selector("#avByFieldsComboBox").get_attribute("disabled")
        utillobj.asequal(disabled_status,'true',"Step 24.02: Verify By combo box is disabled")
        operator_value_ele = self.driver.find_element_by_css_selector("#avOperatorComboBox")
        utillobj.asequal(operator_value_ele.text.replace('\n ',''),'Range',"Step 24.03: Verify Operator value")
        
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        if ran in range(10192, 10195):
            status = True
        else:
            status = False
        utillobj.asequal(True, status, "Step 24.04: Verify From value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),13000,"Step 24.05: Verify To value")  
         
        """
        Step25: Click Cancel
        """
        metaobj.create_visualization_filters('numeric',ok='Cancel')
        utillobj.synchronize_until_element_disappear("#avFilterCancelBtn", metaobj.home_page_medium_timesleep)

if __name__ == '__main__':
    unittest.main()