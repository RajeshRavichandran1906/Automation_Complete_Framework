'''
Created on July 18, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2204891
TestCase Name = Verify that assigned frame color should be reflected in chart frame
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon, active_miscelaneous, visualization_resultarea, visualization_metadata, ia_styling, ia_resultarea
from common.lib import utillity


class C2204891_TestClass(BaseTestCase):

    def test_C2204891(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2204891'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        styling_obj = ia_styling.IA_Style(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
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
        
        """ Step 2: Add Category and Unit Sales
        """
        metadataobj.datatree_field_click('Category', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class$='title']"
        result_obj.wait_for_property(parent_css, 1, string_value='Category', with_regular_exprestion=True)
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        parent_css="#TableChart_1 g.chartPanel text[class='yaxis-title']"
        result_obj.wait_for_property(parent_css, 1, string_value='UnitSales', with_regular_exprestion=True)
        
        """ Step 3: Now right click on Chart frame, and choose Frame color (RGB: 255, 128, 192) and run the chart
                    Verify that assigned frame color should be reflected in chart frame
        """
        elem=driver.find_element_by_css_selector("#TableChart_1 [class*='riser!s0!g0!mbar']")
        utillobj.click_on_screen(elem, 'start', 1, x_offset=-100, y_offset=-50)
        parent_css="[id^='BiPopup'][style*='inherit'] table tr:nth-child(2) td:nth-child(2)"
        result_obj.wait_for_property(parent_css, 1, string_value='FrameColor...', with_regular_exprestion=True)
        utillobj.select_or_verify_bipop_menu('Frame Color...')
        time.sleep(2)
        styling_obj.set_color("tea_rose")
        parent_css="#TableChart_1 [class='chartFrame']"
        result_obj.wait_for_property(parent_css, 1)
        
        """ Step 4: Verify the Live Preview and Click Run
        """
        result_obj.verify_xaxis_title("TableChart_1", 'Category', "Step 4.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 4.2: Verify Y-Axis Title")
        expected_xval_list=['Coffee']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4.3: Verify XY Label')
        utillobj.verify_chart_color('TableChart_1', 'chartFrame', 'tea_rose', 'Step 4.5: Verify frame Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 4.6: Verify bar Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 4.7: Verify Number of riser', custom_css=".chartPanel rect[class^='riser']")
        
        """ Step 5: Verify Frame color are reflected during run time `
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Category', "Step 5.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 5.2: Verify Y-Axis Title")
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 5.3: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 3, 'Step 5.4: Verify Number of riser')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar', 'bar_blue1', 'Step 5.5: Verify Color')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'chartFrame', 'tea_rose', 'Step 5.6: Verify frame Color')
        expected_tooltip_list=['Category:  Coffee', 'Unit Sales:  1376266', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar', expected_tooltip_list, 'Step 5.7: verify the default tooltip values')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'Unit Sales by Category', 'Step 5.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 5.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 5.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 5.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(7)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)  

if __name__ == '__main__':
    unittest.main()