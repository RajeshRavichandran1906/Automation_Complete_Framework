'''
Created on January 1, 2019

@author: AA14564

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/7063&group_by=cases:section_id&group_id=135480&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2074192
TestCase Name = AHTML: Verify that colors applied to Chart bars display correctly for Color Mode of Series vs. Group (ACT-625).
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C2074192_TestClass(BaseTestCase):

    def test_C2074192(self):
        
        """
        TESTCASE Object's
        """
        active_chart_obj = Active_Chart(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        PREVIEW_PARENT_CSS = "#pfjTableChart_1"
        RUN_PARENT_CSS = "#MAINTABLE_wbody0_fmg g.chartPanel"
        preview_dealer_cost_riser_css = " rect[class*='riser!s0!g{0}!mbar']"
        preview_retail_cost_riser_css = " rect[class*='riser!s1!g{0}!mbar']"
        run_dealer_cost_riser_css = RUN_PARENT_CSS + " rect[class*='riser!s0!g{0}!mbar']"
        run_retail_cost_riser_css = RUN_PARENT_CSS + " rect[class*='riser!s1!g{0}!mbar']"
        
        """
        Step 1: Sign in to WebFOCUS as a developer user
                http://machine:port/{alias}
        """
        """
        Step 2: Launch IA Chart using below API link
                http://machine:port/{alias}/iatool=Chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FP95_S7063%2FG135480%2FF
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/car', mrid='mriddev', mrpass='mrpassdev')
        
        """
        Step 3: On the Format tab, in the Output Types group, click Active report.
                Expect to see the following empty canvas for the Car file.
        """
        active_chart_obj.change_output_format_type('active_report')
        util_obj.synchronize_with_visble_text("#HomeFormatType", 'Active Report', 45)
        active_chart_obj.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 3')
        active_chart_obj.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 3.1')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 3.2')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('0'), 'bar_blue', parent_css=PREVIEW_PARENT_CSS, msg='Step 2.6')
        
        """
        Step 4: Select Country & Car for the Horizontal axis and
                Dealer_Cost and Retail_Cost for the Vertical axis.
                Expect to see the following Preview pane, containing the default colors for the Dealer_Cost and Retail_Cost bars.
        """
        active_chart_obj.right_click_on_datetree_item('COUNTRY', 1, 'Add To Query->Horizontal Axis')
        active_chart_obj.right_click_on_datetree_item('CAR', 1, 'Add To Query->Horizontal Axis')
        active_chart_obj.right_click_on_datetree_item('DEALER_COST', 1, 'Add To Query->Vertical Axis')
        active_chart_obj.right_click_on_datetree_item('RETAIL_COST', 1, 'Add To Query->Vertical Axis')
        util_obj.synchronize_with_visble_text("#pfjTableChart_1 .chartPanel text[class*='xaxisOrdinal-labels!g0!mgroupLabel']", 'ENGLAND:JAGUAR', 45)
        expected_x_axis = ['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        expected_y_axis = ['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        active_chart_obj.verify_x_axis_label_in_preview(expected_x_axis, msg='Step 4')
        active_chart_obj.verify_y_axis_label_in_preview(expected_y_axis, msg='Step 4.1')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 20, msg='Step 4.2')
        active_chart_obj.verify_x_axis_title_in_preview(['COUNTRY : CAR'], msg='Step 4.3')
        active_chart_obj.verify_legends_in_preview(['DEALER_COST', 'RETAIL_COST'], msg='Step 4.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('0'), 'bar_blue', parent_css=PREVIEW_PARENT_CSS, msg='Step 4.5')
        
        """
        Step 5: In the Preview pane, right-click on the fi255rst Bar for Dealer_Cost.
                Select the Series Color Menu, select Yellow and click OK.
                Expect to see the default color change to Yellow for all of the Dealer_Cost bars.
        """
        active_chart_obj.right_click_on_chart_bar_perview_and_select_context_menu(preview_dealer_cost_riser_css.format('0'), 'Series Color...', parent_css=PREVIEW_PARENT_CSS)
        util_obj.synchronize_until_element_is_visible("[id*='IAColorPicker'] div[class*='window-active'] .color-picker-box[style*='background-color']", 45)
        util_obj.set_color_in_color_picker_dialog("[id*='IAColorPicker']", 'yellow', close_dialog_button='ok')
        time.sleep(3)
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('0'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.1')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('1'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.2')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('2'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.3')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('3'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('4'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('5'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.6')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('6'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.7')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('7'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.8')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('8'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.9')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_dealer_cost_riser_css.format('9'), 'yellow', parent_css=PREVIEW_PARENT_CSS, msg='Step 5.10')
        
        """
        Step 6: In the Preview pane, right-click on the first Bar for Retail_Cost.
                Select the Series Color Menu, select Red and click OK.
                Expect to see the default color change to Red for all of the Retail_Cost bars.
        """
        active_chart_obj.right_click_on_chart_bar_perview_and_select_context_menu(preview_retail_cost_riser_css.format('0'), 'Series Color...', parent_css='#pfjTableChart_1')
        util_obj.synchronize_until_element_is_visible("[id*='IAColorPicker'] div[class*='window-active'] .color-picker-box[style*='background-color']", 45)
        util_obj.set_color_in_color_picker_dialog("[id*='IAColorPicker']", 'red')
        ok_button_obj = util_obj.validate_and_get_webdriver_object("[id*='IAColorPicker'] div[class*='window-active'] #BiColorPickerOkBtn", 'Ok button')
        core_util_obj.left_click(ok_button_obj)
        time.sleep(3)
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('0'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.1')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('1'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.2')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('2'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.3')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('3'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('4'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('5'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.6')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('6'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.7')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('7'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.8')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('8'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.9')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(preview_retail_cost_riser_css.format('9'), 'red', parent_css='#pfjTableChart_1', msg='Step 6.10')
        
        """
        Step 7: Again in the Preview pane, right-click the first bar for Retail_Cost, select Color Mode, then select BY SERIES
                Click the RUN button.
                Expect to see all Dealer_Cost bars as Yellow and all Retail_Cost bars as Red.
        """
        active_chart_obj.right_click_on_chart_bar_perview_and_select_context_menu(preview_retail_cost_riser_css.format('0'), 'Color Mode->By Series', parent_css='#pfjTableChart_1')
        time.sleep(2)
        active_chart_obj.run_chart_from_toptoolbar()
        active_chart_obj.switch_to_frame()
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY : CAR'], msg='Step 7')
        active_chart_obj.verify_chart_title('DEALER_COST, RETAIL_COST BY COUNTRY, CAR', msg='Step 7.1', parent_css='#MAINTABLE_wbody0_fmg')
        expected_x_axis=['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        expected_y_axis=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_axis, msg='Step 7.2')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_axis, msg='Step 7.3')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, msg='Step 7.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('0'), 'yellow', msg='Step 7.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('1'), 'yellow', msg='Step 7.6')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('2'), 'yellow', msg='Step 7.7')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('3'), 'yellow', msg='Step 7.8')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('4'), 'yellow', msg='Step 7.9')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('5'), 'yellow', msg='Step 7.9')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('6'), 'yellow', msg='Step 7.10')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('7'), 'yellow', msg='Step 7.11')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('8'), 'yellow', msg='Step 7.12')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('9'), 'yellow', msg='Step 7.13')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('0'), 'red', msg='Step 7.14')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('1'), 'red', msg='Step 7.15')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('2'), 'red', msg='Step 7.16')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('3'), 'red', msg='Step 7.17')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('4'), 'red', msg='Step 7.18')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('5'), 'red', msg='Step 7.19')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('6'), 'red', msg='Step 7.20')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('7'), 'red', msg='Step 7.21')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('8'), 'red', msg='Step 7.22')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('9'), 'red', msg='Step 7.23')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 7.24', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_legends_in_run_window(['DEALER_COST', 'RETAIL_COST'], msg='Step 7.25')
        
        """
        Step 8: Again in the Preview pane, right-click the first bar for Retail_Cost, select Color Mode, then select BY GROUP.
                Click the RUN button.
                Expect to see the first set of bars in Yellow and the second set in Red due to the Series Color changes.
                Also expect to see the colors of the remaining bar to resume the colors specified in ENWarm.sty.
        """
        active_chart_obj.switch_to_default_content()
        preview_obj = util_obj.validate_and_get_webdriver_object("#queryViewPane #showCurrentIAQueryEdtrBtn .bi-button-label", 'Preview pane tab')
        core_util_obj.left_click(preview_obj)
        time.sleep(2)
        active_chart_obj.right_click_on_chart_bar_perview_and_select_context_menu(preview_retail_cost_riser_css.format('0'), 'Color Mode->By Group', parent_css='#pfjTableChart_1')
        time.sleep(2)
        active_chart_obj.run_chart_from_toptoolbar()
        active_chart_obj.switch_to_frame()
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY : CAR'], msg='Step 8')
        active_chart_obj.verify_chart_title('DEALER_COST, RETAIL_COST BY COUNTRY, CAR', msg='Step 8.1', parent_css='#MAINTABLE_wbody0_fmg')
        expected_x_axis=['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        expected_y_axis=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        active_chart_obj.verify_x_axis_label_in_run_window(expected_x_axis, msg='Step 8.2')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_y_axis, msg='Step 8.3')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, msg='Step 8.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('0'), 'yellow', msg='Step 8.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('1'), 'red', msg='Step 8.6')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('2'), 'dark_green', msg='Step 8.7')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('3'), 'pale_yellow_2', msg='Step 8.8')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('4'), 'brick_red', msg='Step 8.9')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('5'), 'orange', msg='Step 8.10')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('6'), 'canary', msg='Step 8.11')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('7'), 'mona_lisa', msg='Step 8.12')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('8'), 'moss_green', msg='Step 8.13')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_dealer_cost_riser_css.format('9'), 'pale_yellow1', msg='Step 8.14')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('0'), 'yellow', msg='Step 8.15')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('1'), 'red', msg='Step 8.16')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('2'), 'dark_green', msg='Step 8.17')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('3'), 'pale_yellow_2', msg='Step 8.18')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('4'), 'brick_red', msg='Step 8.19')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('5'), 'orange', msg='Step 8.20')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('6'), 'canary', msg='Step 8.21')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('7'), 'mona_lisa', msg='Step 8.22')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('8'), 'moss_green', msg='Step 8.23')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(run_retail_cost_riser_css.format('9'), 'pale_yellow1', msg='Step 8.24')
        active_chart_obj.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 8.25', parent_css='#MAINTABLE_wmenu0')
        active_chart_obj.verify_legends_in_run_window(['DEALER_COST', 'RETAIL_COST'], msg='Step 8.26')
        active_chart_obj.switch_to_default_content()
        
        """
        Step 9: Logout using the below link:
                http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()