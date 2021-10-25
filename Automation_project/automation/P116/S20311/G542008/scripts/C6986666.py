'''
Created on Dec 24, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986666
Testcase Name : Verify Straight Line chart with Markers via Advance chart tool bar.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from common.wftools import chart
from common.lib import base

class C6986666_TestClass(BaseTestCase):

    def test_C6986666(self):
        """
        Testcase objects
        """
        util_obj = utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        
        """
        Testcase CSS
        """
        chart_menu_css = "MAINTABLE_wmenu0"
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        colheader_css="#"+preview_parent_css+" g.chartPanel text[class^='colHeader-label']"
        legend_dc_css="#"+preview_parent_css+" [class='legend-labels!s1!']"
        x_axis_css = "text[class^='xaxis']"
        circle_marker_css = "circle[class*='marker!s0!g1']"
        advanced_chart_menu_css = "#wall1"
        run_window_parent_css = "#MAINTABLE_wbody0"
        
        """
        Testcase variables
        """
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        expected_run_yval_list_stacked=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        legend_list = ['Unit Sales','Dollar Sales']
        column_label_list = ['Category','Coffee','Food','Gifts']
        run_exp_chart_title='Unit Sales, Dollar Sales by Category, Product'

        """
        Step 1: Log in to WebFOCUS
        http://machine:port/{alias}
        Step 2: Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS2031%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
        Step 3: Select Active Report as Output file format
        """
        chart_obj.change_output_format_type('active_report')
          
        """
        Step 4: Add fields as follows:
        Category under Columns.
        Product under Horizontal axis.
        Unit Sales, Dollar Sales under Vertical axis.
        """
        active_chart_obj.drag_field_from_data_tree_to_query_pane('Category', 1, 'Columns', 1)
        active_chart_obj.wait_for_number_of_element(colheader_css, 1, base_obj.chart_short_timesleep)
        active_chart_obj.double_click_on_datetree_item('Product', 1)
        active_chart_obj.wait_for_number_of_element(x_axis_css, 2, base_obj.chart_short_timesleep)
        active_chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        active_chart_obj.wait_for_number_of_element(preview_yaxis_title_css, 1, base_obj.chart_short_timesleep)
        active_chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        active_chart_obj.wait_for_number_of_element(legend_dc_css, 1, base_obj.chart_short_timesleep)
        
        """
        Step 5: Right click Horizontal Axis and check 'Suppress Empty Group'
        Expect to see the following Preview pane with Suppress Empty Group checked.
        """
        active_chart_obj.verify_query_field_checked_context_menu('Horizontal Axis', 1, ['Suppress Empty Group'], 'Step 5.1: Verify Suppress empty group is checked')

        """
        Step 6: Click the Run button.
        Expect to see the following bucketized bar chart.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s1!']", 'Dollar Sales', base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css=run_window_parent_css, msg="Step 6.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css=run_window_parent_css, msg="Step 6.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, parent_css=run_window_parent_css, msg="Step 6.3: Riser verification")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.5')
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 6.6:", parent_css="#MAINTABLE_wbody0_ft")
        
        """
        Step 7: Select Advance Chart icon from the tool bar.
        Scroll down to the Line Charts.
        Expect to see the following Advanced Chart menu.
        Step 8:Select Curved + Markers and click OK.
        Expect to see the bar chart converted into a Curved Line Chart with Markers.
        """
        active_chart_obj.click_chart_menu_bar_items(chart_menu_css, 1)
        active_chart_obj.wait_for_number_of_element(advanced_chart_menu_css, 1, base_obj.chart_medium_timesleep)
        util_obj.verify_object_visible(advanced_chart_menu_css, True , 'Step 7.1: Verify the Advanced menu is visible')
        active_chart_obj.verify_items_in_advanced_chart_menu(['Line','Curved','Straight','Curved +Markers','Straight +Markers','Step'], 'asin', 'Step 7.2: Verify the chart items')
        active_chart_obj.select_advance_chart('wall1', 'strightplusmarkers', 0)
        active_chart_obj.wait_for_number_of_element(circle_marker_css, 3, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css=run_window_parent_css, msg="Step 8.1: x-label verification for the curved marker")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list_stacked, parent_css=run_window_parent_css, msg="Step 8.2: y-label verification for curved marker")
        chart_obj.verify_number_of_markers(run_window_parent_css, 1, 20, 'Step 8.3: Verify Number of markers in the run window')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class^='marker!s0!']", "bar_blue", parent_css=run_window_parent_css, attribute='stroke', msg='Step 8.4: Blue marker verification')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class^='marker!s1!']", "pale_green", parent_css=run_window_parent_css, attribute='stroke', msg='Step 8.5: Pale green marker verification')
        active_chart_obj.verify_x_axis_title_in_run_window(['Product'], parent_css=run_window_parent_css, msg="Step 8.6: y-label verification curved marker")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 8.7:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_legends_in_run_window(legend_list, parent_css=run_window_parent_css, msg='Step 8.8:')
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css=run_window_parent_css, msg='Step 8.9:')
        
        """
        Step 9: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()