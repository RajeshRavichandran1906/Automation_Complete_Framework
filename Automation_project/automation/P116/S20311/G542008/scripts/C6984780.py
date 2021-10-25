'''
Created on Nov 19, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984780
Testcase Name : Verify Percent Area chart via Advance chart tool bar.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart, chart

class C6984780_TestClass(BaseTestCase):

    def test_C6984780(self):
        """
            TESTCASE Functions Object
        """
        
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        colheader_css="#"+preview_parent_css+" g.chartPanel text[class^='colHeader-label']"
        legend_dc_css="#"+preview_parent_css+" [class='legend-labels!s1!']"
        x_axis_css = "text[class^='xaxis']"
        expected_xval_list=['Capuccino', 'Espresso']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '2M', '4M', '6M', '8M', '10M','12M']
        expected_run_yval_list_percent=['0%', '20%', '40%', '60%', '80%', '100%']
        legend_list = ['Unit Sales','Dollar Sales']
        column_label_list = ['Category','Coffee','Food','Gifts']
        run_exp_chart_title='Unit Sales, Dollar Sales by Category, Product'
        chart_rollup_css = '#wall1 #wtitle1'
        chart_rollup_title = 'Chart/Rollup Tool'
        short_time=25
        medium_time=35

        """
            Step 1 : Log in to WebFOCUS
            http://machine:port/{alias}
            Step 2 : Execute following URL to create Chart
            http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS2031%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
            Step 3 : Select Active Report as Output file format
        """
        chart_obj.change_output_format_type('active_report')
          
        """
        Step 4 : Add fields as follows:
        Category under Columns.
        Product under Horizontal axis.
        Unit Sales, Dollar Sales under Vertical axis.
        Expect to see the following Preview pane.
        """
        active_chart_obj.drag_field_from_data_tree_to_query_pane('Category', 1, 'Columns', 1)
        active_chart_obj.wait_for_number_of_element(colheader_css, 1, short_time)
        active_chart_obj.double_click_on_datetree_item('Product', 1)
        active_chart_obj.wait_for_number_of_element(x_axis_css, 2, short_time)
        active_chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        active_chart_obj.wait_for_number_of_element(preview_yaxis_title_css, 1, short_time)
        active_chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        active_chart_obj.wait_for_number_of_element(legend_dc_css, 1, short_time)
        active_chart_obj.verify_x_axis_label_in_preview(expected_xval_list, parent_css='#TableChart_1', msg="Step 4.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_preview(expected_yval_list, parent_css='#TableChart_1', msg="Step 4.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 4, parent_css="#TableChart_1", msg="Step 4.3: Riser verification")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s0!g0!mbar!r0!c0!']", "bar_blue1", parent_css="#TableChart_1", attribute='fill', msg='Step 4.4, First bar Colour verification')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("[class='riser!s1!g0!mbar!r0!c0!']", "bar_green", parent_css="#TableChart_1", attribute='fill', msg='Step 4.5, Second bar Colour verification')
        
        """
        Step 5: Right click Horizontal Axis and check 'Suppress Empty Group'
        Expect to see the following Preview pane with Suppress Empty Group checked.
        """
        active_chart_obj.verify_query_field_checked_context_menu('Horizontal Axis', 1, ['Suppress Empty Group'], 'Step 05.01 : Verify Suppress Empty Group checked')
        
        """
        Step 6: Click the Run button.
        Expect to see the following bucketized bar chart.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_visible_text("#MAINTABLE_wbody0_f text[class='legend-labels!s1!']", 'Dollar Sales', medium_time)
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0 text[class^='xaxis']", 13, 25)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 20, parent_css="#MAINTABLE_wbody0", msg="Step 6.3: Riser verification")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.4')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s1!g1!mbar!r0!c0!']", 'pale_green', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.5')
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 6.6:", parent_css="#MAINTABLE_wbody0_ft")
        
        """
        Step 7: Select Advance Chart icon from the tool bar.
        Scroll down to the Area charts.
        Expect to see the following Advanced Chart menu.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        active_chart_obj.wait_for_number_of_element('#wall1', 1, short_time)
        observed_rollup_title=util_obj.validate_and_get_webdriver_object(chart_rollup_css, 'rollup title').text.strip()
        util_obj.asequal(chart_rollup_title,observed_rollup_title,'Step 7.1: Advanced chart menu is open')
        active_chart_obj.select_advance_chart('wall1', 'percentarea', 0)
        
        """
        Step 8: Select Stacked Area Chart and click OK.
        Expect to see the bar chart converted into a Stacked Area Chart.
        """
        active_chart_obj.wait_for_number_of_element("path[class*='g0!marea!r0']", 6, short_time)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 8.1: x-label verification for the area")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list_percent, parent_css='#MAINTABLE_wbody0', msg="Step 8.2: y-label verification for the area")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 6, parent_css="#MAINTABLE_wbody0", msg="Step 8.3: Riser verification in run window")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!marea!r0!c0!']", "bar_blue", parent_css="#MAINTABLE_wbody0", attribute='fill', msg='Step 8.4, First top area Colour verification')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s1!g0!marea!r0!c1!']", "pale_green", parent_css="#MAINTABLE_wbody0", attribute='fill', msg='Step 8.5, first bottom area Colour verification')
        active_chart_obj.verify_x_axis_title_in_run_window(['Product'], parent_css='#MAINTABLE_wbody0', msg="Step 8.6: y-label verification for the area")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 8.7:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_legends_in_run_window(legend_list, parent_css="#MAINTABLE_wbody0", msg='Step 8.8:')
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 8.9:')
        
        """
        Step 9: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        core_util_obj.switch_to_default_content()
        
if __name__ == '__main__':
    unittest.main()