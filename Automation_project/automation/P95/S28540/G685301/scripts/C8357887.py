'''
Created on January 8, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8357887
TestCase Name = AHTML: Handle tooltip positioning during preview & runtime (ACT-623).
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base
from common.lib import utillity
from common.wftools import visualization

class C8357887_TestClass(BaseTestCase):

    def test_C8357887(self):
        
        """
        Test case Object's
        """
        visual_obj = visualization.Visualization(self.driver)
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
        chart_title = "DEALER_COST by CAR"
        alfa_romeo_tooltip = ['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        left_click_tooltip = ['1 point', 'Filter Chart', 'Exclude from Chart']
        group_x_labels = ['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        group_y_labels = ['0', '10', '20', '30', '40', '50']
        legend_series = ['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        right_click_menu_items = ['Filter Values...', 'Sort', 'Visibility', 'Change Title...', 'Series Type', 'Series Color...', 'More Style Options...', 
                                  'Data Labels', 'Color Mode', 'Add Trendline', 'Edit Format', 'Drill Down', 'More', 'Delete']
        
        """
        Test case CSS
        """
        alfa_romeo_css = "#MAINTABLE_wbody0_f rect[class='riser!s0!g0!mbar!']"
        preview_afla_romeo_css = "rect[class='riser!s0!g0!mbar!']"
        result_area_css = "#MAINTABLE_wbody0 rect[class^='eventCatcher']"
        
        """ 
        Step 1: Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2: Launch IA Chart using below API link
        http://machine:port/{alias}/iatool=Chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FP95_S7063%2FG135480%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/car',mrid='mriddev',mrpass='mrpassdev')
        
        """
        Step 3 : On the Format tab, in the Output Types group, click Active report.
        Expect to see the following empty canvas for the Car file.
        """
        chart_obj.change_output_format_type('active_report')
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
        Expect to see the following Active Report Preview pane Tooltip menu, including Filter Values, Sort, Visibility, etc.
        Verify that this Tooltip menu appears close to the Alfa Romeo Bar.
        """
        css="#pfjTableChart_1 rect[class='riser!s0!g0!mbar!']"
        obj_locator=util_obj.validate_and_get_webdriver_object(css, 'alfa-romeo-css')
        core_util_obj.left_click(obj_locator)
        util_obj.synchronize_with_visble_text('#FieldAggregation', 'Aggregation', base_obj.chart_long_timesleep)
        active_chart_obj.right_click_on_chart_bar_perview_and_verify_context_menu(preview_afla_romeo_css, right_click_menu_items, 'Step 5.1', parent_css = '#pfjTableChart_1')
            
        """
        Step 6: Click the Run button.
        Expect to see the following Active Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0_f text[class^='xaxis']", 11, base_obj.chart_short_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_label, msg='Step 6.1: Verify x axis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(y_label, msg='Step 6.2: Verify y axis labels')
        active_chart_obj.verify_chart_title(chart_title, msg='Step 6.3: Verify Chart title', parent_css = '#MAINTABLE_wbody0_ft')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g0!mbar!']", 'bar_blue', attribute='fill', msg='Step 6.4: Verify bar colour')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 6.5: Verify number of risers')
        
        """
        Step 7: Left-click the Alfa Romeo Bar.
        Expect to see the Tooltip menu appear, along with the Values for Car and Dealer_Cost.
        """
        source_element = util_obj.validate_and_get_webdriver_object(alfa_romeo_css, 'alfa-romeo-css')
        target_element = source_element
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-15, source_yoffset=-19, target_xoffset=19, target_yoffset=19)
        visual_obj.verify_lasso_tooltip(left_click_tooltip, msg='Step 7.1: Verify tooltip in alfa romeo')
        active_chart_obj.verify_x_axis_label_in_run_window(x_label, msg='Step 7.2: Verify car valeus appear')
        active_chart_obj.verify_y_axis_label_in_run_window(y_label, msg='Step 7.3: Verify dealer cost values appear')
        
        """
        Step 8: Click in the white area on the chart to reset.
        Hover over but do NOT click the Alfa Romeo Bar.
        Expect to see only the Filtering Tooltip menu.
        """
        result_area_element = util_obj.validate_and_get_webdriver_object(result_area_css, 'result area')
        core_util_obj.python_left_click(result_area_element)
        chart_obj.verify_active_chart_tooltip('MAINTABLE_wbody0_f', 'riser!s0!g0!mbar!', alfa_romeo_tooltip, msg='Step 8.1: Verify alfa romeo tooltip')
        
        """
        Step 9: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp 
        """
        
if __name__ == '__main__':
    unittest.main()