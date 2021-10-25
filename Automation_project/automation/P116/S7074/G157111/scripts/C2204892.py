'''
Created on July 19, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204892
TestCase Name = Verify that Chart should be presented in 3D view when 3D is on
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, active_miscelaneous, ia_resultarea, ia_ribbon
from common.lib import utillity


class C2204892_TestClass(BaseTestCase):

    def test_C2204892(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204892'
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ Step 1: Right click on folder created in IA and select New > Chart and select Reporting server as GGSALES.
                    On the Format tab, in the Output Types group, click
                    Active report/Active PDF.
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        parent_css="#TableChart_1 g.chartPanel g text"
        result_obj.wait_for_property(parent_css, 11)
        time.sleep(1)
        ribbonobj.change_output_format_type('active_report')
        time.sleep(9)
        
        """ Step 2: Add Category to Horizontal Axis and add Unit Sales and Dollar Sales to Vertical Axis.
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class$='title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Dollar Sales', 2, 1)
        parent_css="#TableChart_1 g.legend text[class*='s1']"
        result_obj.wait_for_property(parent_css, 1, string_value='DollarSales', with_regular_exprestion=True)
        '''verification check point'''
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 2.1: Verify X-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 2.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 2.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 2.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 2.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        
        """ Step 3: Select 'Format tab > Chart Types > Other', and choose 'Vertical Stacked Bars', and give OK
        """
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(5)
        ia_ribbonobj.select_other_chart_type('bar', 'vertical_stacked_bars', 2, ok_btn_click=True)
        time.sleep(9)
        elem1= driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar']")
        elem2=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s1!g0!mbar']")
        utillobj.verify_stack_chart(elem1, elem2, "Step 3: Verify Chart Converted to Vertical Stacked Bars")
        ''' Verification check point'''
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 3.1: Verify X-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 3.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 3.4: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 3.5: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 3.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
         
        
        """ Step 4: Now right click on Chart frame, and select 'Show 3D > On', Then Run the report
                    Verify that Chart should be presented in 3D view when 3D is on
        """
        elem=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar']")
        utillobj.click_on_screen(elem, 'start', 1, x_offset=-100, y_offset=-50)
        parent_css="[id^='BiPopup'][style*='inherit'] table tr:nth-child(2) td:nth-child(2)"
        result_obj.wait_for_property(parent_css, 1, string_value='FrameColor...', with_regular_exprestion=True)
        utillobj.select_or_verify_bipop_menu('Show 3D')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('On')
        parent_css="#TableChart_1 path[class^='riser!s']"
        result_obj.wait_for_property(parent_css, 4)
        
        """ Step 5: Check the Chart Frame gets changed in Live Preview 
        """
        ''' Verification check point'''
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 5.1: Verify X-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 5.2: Verify XY Label')
        expected_label_list=['Unit Sales', 'Dollar Sales']
        result_obj.verify_riser_legends('TableChart_1', expected_label_list, 'Step : 5.3 Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 5.4: Verify Color', custom_css="rect[class*='riser!s0!g0!mbar']")
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!mbar', 'bar_green', 'Step 5.5: Verify Color', custom_css="rect[class*='riser!s1!g0!mbar']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 5.6: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 5.7: Verify 3D chart apply', custom_css="path[class^='riser!s']")
        time.sleep(2)
        
        
        """ Step 6: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        
        """ Step 7: Verify the chart is displaying in 3D view
        """
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 7.1: Verify X-Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 7.3: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 18, 'Step 7.4: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 7.5: Verify Color', custom_css="rect[class*='riser!s0!g0!mbar']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s1!g0!mbar', 'pale_green', 'Step 7.6: Verify frame Color', custom_css="rect[class*='riser!s1!g0!mbar']")
        expected_tooltip_list=['Category:  Coffee', 'Unit Sales:  1376266', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar', expected_tooltip_list, 'Step 7.7: verify the default tooltip values',x_offset=-20)
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales, Dollar Sales by Category', 'Step 7.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 7.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 7.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 7.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step7', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)  

if __name__ == '__main__':
    unittest.main()