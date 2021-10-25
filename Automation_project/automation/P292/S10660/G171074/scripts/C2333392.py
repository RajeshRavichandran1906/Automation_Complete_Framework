'''
Created on Sep 16, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2333392
TestCase Name = Date Filter with Attributes date field YYMD - Sale,Date
'''
import unittest,time
from common.lib import utillity, core_utility
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties
from common.lib.basetestcase import BaseTestCase

class C2333392_TestClass(BaseTestCase):

    def test_C2333392(self):
        
        """
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2333392'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']", metaobj.chart_long_timesleep)         
                  
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit"
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g>g>text[class^='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, metaobj.chart_long_timesleep)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g>g>text[class^='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, metaobj.chart_long_timesleep)
            
        """
        Step03: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > "Sale,Day" > "Attributes" > Double click "Sale,Date" to add it to the canvas
        """
        metaobj.datatree_field_click('Sale,Date', 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g>g>text[class^='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 6, metaobj.chart_long_timesleep)
                    
        """
        Step04: Drag and drop "Sale,Date" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Date', 1)
        utillobj.synchronize_until_element_is_visible("#dateTimePickerFrom #dateInputCmb1 input", metaobj.chart_long_timesleep)
         
        """
        Step 05: Verify Filter dialog    Screenshot in testrail mismatch when edit    
        """
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Jan',"Step 05.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'01',"Step 05.02: Verify range from value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2011,"Step 05.03: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step 05.04: Verify range to value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step 05.05: Verify range to value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step 05.06: Verify range to value")
        time.sleep(2)
        
            
        """
        Step08: Change Starting Date to 01/01/2015
        Step07: Click OK                 
        """
        l1=['Jan','01','2015']
        metaobj.create_visualization_filters('numeric',['Starting Date',l1])
           
        """
        Step 08: Verify Canvas
        """
        utillobj.synchronize_with_number_of_element('#ar_Prompt_1 span[id$="s_min"]', 1, metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Sale,Date',1,"Step 08.00")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2015/01/01','str',msg="Step 08.01: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step 08.02: Verify filter prompt range values- max")
         
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_until_element_is_visible(parent_css, metaobj.chart_long_timesleep)         
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step 08.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03', '2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.05: Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08.06: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 08.07: Verify Y-Axis Title")
                       
        """
        Step09: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window()
                
        """
        Step10: Verify output
        """
        utillobj.synchronize_until_element_is_visible("#sliderPROMPT_1 span[id$='s_min']", metaobj.chart_long_timesleep)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2015/01/01','str',msg="Step 10.00: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03/19','str',msg="Step 10.01: Verify filter prompt range values- max") 
        time.sleep(2)
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step 10.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03', '2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 10.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.04: Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.05: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.06: Verify Y-Axis Title")
                       
        """
        Step11: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible("#topToolBar #saveButton img", metaobj.chart_medium_timesleep)      
                                       
        """
        Step12: Click Save in the toolbar
        Step13: Save as "C2158163" > Click Save
        Step14: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metaobj.chart_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
             
        """
        Step15: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        Step16: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", metaobj.chart_long_timesleep)
        metaobj.verify_filter_pane_field('Sale,Date',1,"Step 16.00: Verify Sale Date appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2015/01/01','str',msg="Step 16.01: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step 16.02: Verify filter prompt range values- max")
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step 16.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03','2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.05: Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16.06: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 16.07: Verify Y-Axis Title")
           
        """
        Step17: Drag left slider handle (in the Filter Prompt) to the right > change starting value to 12/25/15
        Step18: Verify Canvas
        """
        time.sleep(5)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str')    
        parent_css = "#MAINTABLE_wbody1  svg g.risers >g>rect[class^='riser']"   
        utillobj.synchronize_with_number_of_element(parent_css, 556, resultobj.home_page_long_timesleep)
          
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','2016/03/29','str',msg="Step 18.00: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','2017/03/19','str',msg="Step 18.01: Verify filter prompt range values- max")
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 278, 'Step 18.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2016/03/29', '2016/03/30', '2016/03/31', '2016/12/29', '2016/12/30', '2016/12/31']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 18.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 18.04 Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 18.05: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 18.06: Verify Y-Axis Title")
            
        """
        Step19: Right click "Sale,Date" filter in the Filter pane
        Step20: Verify dialog and Cancel 
        """
        time.sleep(2)
        metaobj.filter_tree_field_click('Sale,Date', 1, 1, 'Edit...')
        utillobj.synchronize_until_element_is_visible("#dateTimePickerFrom #dateInputCmb1 input", metaobj.chart_long_timesleep)
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step 20.00: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'29',"Step 20.01: Verify range from value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2016,"Step 20.02: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step 20.03: Verify range to value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step 20.04: Verify range to value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step 20.05: Verify range to value")
   
        metaobj.create_visualization_filters('numeric',ok='cancel')
        utillobj.synchronize_until_element_disappear("#avFilterCancelBtn", metaobj.chart_long_timesleep)
        
        """
        Step21: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_utilobj.switch_to_new_window() 
        utillobj.synchronize_until_element_is_visible("[class*='riser!s']", metaobj.chart_long_timesleep)   
               
        """
        Step22: Verify output
        """
       
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','2016/03/29','str',msg="Step 22.00: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','2017/03/19','str',msg="Step 22.01: Verify filter prompt range values- max")
                 
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 278, 'Step 22.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2016/03/29', '2016/04/29', '2016/12/29', '2016/12/30', '2016/12/31']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 22.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.04: Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 22.05: Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 22.06: Verify Y-Axis Title")

        time.sleep(3)
                         
        """
        Step23: Close output window
        """
        core_utilobj.switch_to_previous_window()
        utillobj.synchronize_until_element_is_visible('#applicationButton', metaobj.chart_long_timesleep)

if __name__ == '__main__':
    unittest.main()