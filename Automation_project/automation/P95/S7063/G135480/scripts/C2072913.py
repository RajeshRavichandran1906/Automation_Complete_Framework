'''
Created on January 7, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2072913
TestCase Name = AHTML:Document:Applying style color to the chart is not reflected during run time (ACT-630).
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base
from common.lib import utillity
from common.wftools import report

class C2072913_TestClass(BaseTestCase):

    def test_C2072913(self):
        
        """
        Test case Object's
        """
        report_obj = report.Report(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        x_label = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        y_label = ['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_title = "DEALER_COST BY CAR"
        group_x_labels = ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        group_y_labels = ['0', '10', '20', '30', '40', '50']
        legend_series = ['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        right_click_menu_items = ['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Series Type', 'Series Color...', 'More Style Options...', 
                                  'Data Labels', 'Color Mode', 'Add Trendline', 'Edit Format', 'Drill Down', 'More', 'Delete']
        first_color_variable = 'First color'
        riser_mixed_color = 'url(#MAINTABLE_wbody0_f__lineargradient_0_0_100p_0_0_2552550_1_1_00255_1_0_2552550_1)'
        
        """
        Test case CSS
        """
        ok_button_css = "#seriesGradientOkBtn"
        color_picker_css = "div[id^='IAColorPicker']"
        first_color_css = "#gradientFirstColorLabel"
        fill_table_css = "#fillPane"
        first_color_select_css = "#gradientColor1 img"
        second_color_select_css = "#gradientColor2 img"
        gradient_fill_css = "#gradientFillRadioBtn input[type='radio']"
        alfa_romeo_css = "#MAINTABLE_wbody0_f rect[class='riser!s0!g0!mbar!']"
        preview_afla_romeo_css = "rect[class='riser!s0!g0!mbar!']"
        result_area_css = "#pfjTableChart_1 rect[class^='eventCatcher']"
        
        """ 
        Step 1: Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2: Launch IA to create document using below API link
        http://machine:port/{alias}/iatool=Document&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FP95_S7063%2FG135480%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='document', master='ibisamp/car', mrid='mriddev', mrpass='mrpassdev')
        chart_obj.wait_for_number_of_element("#canvasContainer", 1 , base_obj.chart_medium_timesleep)
        
        """
        Step 3 : On the Insert tab , Click chart.
        Expect to see the following Preview pane.
        """
        chart_obj.select_ia_ribbon_item('Insert', 'chart')
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='xaxis']", 5, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_preview(group_x_labels, msg='Step 3.1 verify the x axis labels')
        chart_obj.verify_y_axis_label_in_preview(group_y_labels, msg='Step 3.2 verify the y axis labels')
        chart_obj.verify_legends_in_preview(legend_series, msg='Step 3.3: Verify legends')
        
        """
        Step 4 : Select Car for the Horizontal axis and
        Dealer_Cost for the Vertical axis.
        Expect to see the following Preview pane.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane('CAR', 1, 'Horizontal Axis', 1)
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='xaxis']", 11, base_obj.chart_short_timesleep)
        chart_obj.drag_field_from_data_tree_to_query_pane('DEALER_COST', 1, 'Vertical Axis', 1)
        chart_obj.wait_for_number_of_element("#pfjTableChart_1 text[class^='yaxis']", 8, base_obj.chart_short_timesleep)
        chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 4.1 verify the x axis labels')
        chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 4.2 verify the y axis labels')
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 10, msg='Step 4.3: Verify Number of risers')
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', attribute='fill', msg='Step 4.4: Verify bar colour')
        
        """
        Step 5: In the Preview pane, right-click on the Bar for Alfa Romeo.
        """
        active_chart_obj.right_click_on_chart_bar_perview_and_verify_context_menu(preview_afla_romeo_css, right_click_menu_items, 'Step 5.1', parent_css = '#pfjTableChart_1')
        
        """
        Step 6: Click on More Style Options.
        Select Gradient Fill from the Radio Button selection menu.
        Expect to see the following Style Options selection screen.
        """
        result_area_element = util_obj.validate_and_get_webdriver_object(result_area_css, 'result area')
        core_util_obj.python_left_click(result_area_element)
        active_chart_obj.right_click_on_chart_bar_perview_and_select_context_menu(preview_afla_romeo_css, 'More Style Options...', parent_css = '#pfjTableChart_1')
        chart_obj.wait_for_number_of_element(fill_table_css, 1, base_obj.chart_short_timesleep)
        gradient_fill = util_obj.validate_and_get_webdriver_object(gradient_fill_css, 'gradient fill')
        core_util_obj.python_left_click(gradient_fill)
        
        """
        Step 7: Click on the box next to First Color and select Yellow. Click OK.
        Click on the box next to Second Color and select Blue. Click OK.
        Expect to see the following color gradients in the Style Option menu.
        """
        chart_obj.wait_for_visible_text(first_color_css, first_color_variable, base_obj.chart_short_timesleep)
        first_color_element = util_obj.validate_and_get_webdriver_object(first_color_select_css, 'first_css')
        core_util_obj.python_left_click(first_color_element)
        chart_obj.wait_for_number_of_element(color_picker_css, 1, base_obj.chart_short_timesleep)
        util_obj.set_color_in_color_picker_dialog("[id*='IAColorPicker']", 'yellow', close_dialog_button='ok')
        chart_obj.wait_for_number_of_element(second_color_select_css, 1, base_obj.chart_short_timesleep)
        second_color_element = util_obj.validate_and_get_webdriver_object(second_color_select_css, 'second_css')
        core_util_obj.python_left_click(second_color_element)
        chart_obj.wait_for_number_of_element(color_picker_css, 1, base_obj.chart_short_timesleep)
        util_obj.set_color_in_color_picker_dialog("[id*='IAColorPicker']", 'blue', close_dialog_button='ok')
        
        """
        Step 8: Click OK.
        Click the Run button.
        Expect to see the following Active Bar Chart, with the selected colors shown for each Bar.
        """
        chart_obj.wait_for_number_of_element(ok_button_css, 1, base_obj.chart_short_timesleep)
        ok_element = util_obj.validate_and_get_webdriver_object(ok_button_css, 'ok-element')
        core_util_obj.python_left_click(ok_element)
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 11, base_obj.chart_short_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_label, msg='Step 6.1: Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(y_label, msg='Step 6.2: Verify y axis labels')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 6.3: Verify Chart title', parent_css = '#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 6.4: Verify number of risers')
        riser_element = util_obj.validate_and_get_webdriver_object(alfa_romeo_css, "alfa_romeo")
        observed_riser_color = riser_element.get_attribute('fill')
        util_obj.asequal(riser_mixed_color, observed_riser_color, "Step 6.5: Verify Riser color")
        
        """
        Step 9: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()