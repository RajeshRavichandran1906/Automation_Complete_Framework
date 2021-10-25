'''
Created on May 12, 2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2234934
TestCase Name = Verify that a default Bar Chart can be changed to a Line Chart via the Series option.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_resultarea
from common.lib import utillity

class C2234934_TestClass(BaseTestCase):

    def test_C2234934(self):
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        Test_Case_ID="C2234934"
        
        """ Step 1: Right click on folder created in IA. 
                    Select New > Chart. 
                    Select Reporting server as GGSALES.
                    On the Format tab, in the Output Types group, click Active report.
                    Click on Product and Unit Sales
        """
        utillobj.infoassist_api_login('chart', 'ibisamp/ggsales', 'P116/S7074', 'mrid', 'mrpass')
        element_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        ribbonobj.change_output_format_type('active_report')
        element_css="#HomeTab #HomeFormatType [class='bi-button-label']"
        utillobj.synchronize_with_visble_text(element_css, 'ActiveReport', 20)
        
        metadataobj.datatree_field_click('Product', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 20)
        
        metadataobj.datatree_field_click('Unit Sales', 2, 1)
        element_css="#TableChart_1 g.chartPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'UnitSales', 20)
         
        """ Step 1:01: Expect to see the following default Preview pane.
        """
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 3.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 3.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 3.3: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 3.4: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 3.5: Verify Color')
           
        """ Step 2: Right click on any Bar on the Preview pane.
                    For the Series Type, select LINE.
                    Expect to see the Series Selection set to Line.
        """
        parent_css="#TableChart_1 .chartPanel g rect[class='riser!s0!g0!mbar!']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(parent_obj, leftClick=True)
        element_css="#FieldFilter [class*='label']"
        utillobj.synchronize_with_visble_text(element_css, 'Filter', 20)
        utillobj.click_type_using_pyautogui(parent_obj, rightClick=True)
        utillobj.select_or_verify_bipop_menu('Series Type')
        utillobj.select_or_verify_bipop_menu('Line')
        element_css=".chartPanel .groupPanel [class*='mline']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 2: Expect to see the Series Selection set to Line.', custom_css=".chartPanel .groupPanel path[class='riser!s0!g0!mline!']")
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mline!', 'bar_blue1', 'Step 2.1: Verify Color', attribute_type='stroke')
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 2.2: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 2.3: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 2.4: ')
          
        """ Step 3: Click the Run button.
                    Expect to see the Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0_f .rootPanel g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Unit Sales', 20)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_0', 11, 'Step 3: Expect to see the Series Selection set to Line.')
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 3.1: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0 ', 'riser!s0!g0!mline!', 'bar_blue', 'Step 3.2: Verify Color', attribute_type='stroke')
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 3.3: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 3.4: Verify Y-Axis Title")
        utillobj.switch_to_default_content()
         
        """ Step 4: Close the Line Chart window and return to the Preview pane.
                    On the preview line again right-click and reset the Series Type to None.
                    Expect to see the original Bar Preview.
        """
#         result_obj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        result_css="#resultArea [class*='window-caption'] div[class*='window-close-button']"
        result_obj1=driver.find_element_by_css_selector(result_css)
        utillobj.default_click(obj_locator=result_obj1)
        time.sleep(5) #Don't remove time sleep here. Otherwise below step throw element is not attached to the page document error 
        
        parent_css="#TableChart_1 .chartPanel .groupPanel [class*='mline']"
        parent_obj=driver.find_element_by_css_selector(parent_css)
        utillobj.click_type_using_pyautogui(parent_obj, leftClick=True)
        element_css="#FieldFilter [class*='label']"
        utillobj.synchronize_with_visble_text(element_css, 'Filter', 20)
        utillobj.click_type_using_pyautogui(parent_obj, rightClick=True, y_offset=2)
        utillobj.select_or_verify_bipop_menu('Series Type')
        utillobj.select_or_verify_bipop_menu('None')
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 4.1: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 4.2: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 4.3: ')
        result_obj.verify_number_of_riser('TableChart_1', 1, 2, 'Step 4.4: ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mbar!', 'bar_blue1', 'Step 4.5: Verify Color')
          
        """ Step 5: Click the Series Tab in the upper right of the command line.
                    Expect to see the Series options appear.
            Step 6: Click the Type button and click Line.
                    Expect to see the Series Selection set to Line.
        """
        ribbonobj.select_ribbon_item("Series", "Type", opt='Line')
        element_css=".chartPanel .groupPanel [class*='mline']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 6: Expect to see the Series Selection set to Line.', custom_css=".chartPanel .groupPanel path[class='riser!s0!g0!mline!']")
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mline!', 'bar_blue1', 'Step 6.1: Verify Color', attribute_type='stroke')
        result_obj.verify_xaxis_title("TableChart_1", 'Product', "Step 6.2: Verify X-Axis Title")
        result_obj.verify_yaxis_title("TableChart_1", 'Unit Sales', "Step 6.3: Verify Y-Axis Title")
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        result_obj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 6.4: ')
          
          
        """ Step 7: Click the Run button.
                    Expect to seed the Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_0', 11, 'Step 7: Expect to see the Series Selection set to Line.')
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        result_obj.verify_riser_chart_XY_labels('MAINTABLE_0', expected_xval_list, expected_yval_list, 'Step 7.1: ')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mline!', 'bar_blue', 'Step 7.2: Verify Color', attribute_type='stroke')
        result_obj.verify_xaxis_title("MAINTABLE_wbody0", 'Product', "Step 7.3: Verify X-Axis Title")
        result_obj.verify_yaxis_title("MAINTABLE_wbody0", 'Unit Sales', "Step 7.4: Verify Y-Axis Title")
        utillobj.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()