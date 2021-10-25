'''
Created on December 21, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986660
Testcase Name : Verify a chart shows correct filtered output once filter via lasso applied - Bar Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from common.wftools import chart
from common.wftools import visualization
from common.lib import base

class C6986660_TestClass(BaseTestCase):

    def test_C6986660(self):
        """
            TESTCASE Functions Object
        """
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        
        """
        Test case css
        """
        riser_css = "rect[class*=riser]"
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        colheader_css="#"+preview_parent_css+" g.chartPanel text[class^='colHeader-label']"
        x_axis_css = "text[class^='xaxis']"
        filter_css = "#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']"
        filter_remove_css = "MAINTABLE_wmenu0"
        x_axis_labels_css = "#MAINTABLE_wbody0 text[class^='xaxis']"
        tooltip_css = "div[class*='tooltip']"
        
        """
        Test case variables
        """
        capuccino_list = ['Category:Coffee', 'Product:Capuccino', 'Unit Sales:189217', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        capuccino_espresso_tooltip = ['2 points', 'Filter Chart', 'Exclude from Chart']
        four_bar_drag = ['4 points', 'Filter Chart', 'Exclude from Chart']
        excluded_list = ['Capuccino', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        x_axis_labels= ['Capuccino', 'Espresso']
        y_axis_labels = ['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        y_axis_title = ['Unit Sales']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        column_label_list = ['Category','Coffee','Food','Gifts']
        run_exp_chart_title='Unit Sales BY Category, Product'

        """
        Step 1 : Log in to WebFOCUS
        http://machine:port/{alias}
        Step 2 : Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS20311%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
        Step 3: Change output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
         
        """
        Step 4: Select data from the left pane (Dimensions and Measures)
        Category - Columns
        Product - Horizontal Axis 
        Unit Sales - Vertical Axis
        """
        active_chart_obj.drag_field_from_data_tree_to_query_pane('Category', 1, 'Columns', 1)
        active_chart_obj.wait_for_number_of_element(colheader_css, 1, base_obj.chart_short_timesleep)
        active_chart_obj.double_click_on_datetree_item('Product', 1)
        active_chart_obj.wait_for_number_of_element(x_axis_css, 2, base_obj.chart_short_timesleep)
        active_chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        active_chart_obj.wait_for_number_of_element(preview_yaxis_title_css, 1, base_obj.chart_short_timesleep)
        active_chart_obj.wait_for_number_of_element(riser_css, 2, base_obj.chart_short_timesleep)
        active_chart_obj.verify_x_axis_label_in_preview(x_axis_labels, msg='Step 4.1: Verify X axis label in preview')
        active_chart_obj.verify_y_axis_label_in_preview(y_axis_labels, msg='Step 4.2: Verify Y axis labels in preview')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 2, msg="Step 4.3: Verify Riser verification in preview")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', msg='Step 4.4')
        active_chart_obj.verify_y_axis_title_in_preview(y_axis_title, msg='Step 4.5')
        
        """
        Step 5: Run the report
        Verify Active Chart 'Unit Sales BY Category, Product' is displayed on canvas with selected data.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 5.1: x-label verification in run window")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 5.2: y-label verification in run window")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 5.3: Riser verification in run window")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 5.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 5.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 5.6')
        
        """
        Step 6: Left click and drag a box around the Capuccino and Espresso bars.
        Verify context menu displays:
        2 Points
        Filter Chart
        Exclude from Chart
        Screenshot:
        """
        left_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g1!mbar!r0!c0!']", 'Capuccino')
        right_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']", 'Espresso')
        visual_obj.create_marker_lasso(left_element,right_element)
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, base_obj.chart_short_timesleep)
        visual_obj.verify_lasso_tooltip(capuccino_espresso_tooltip, "Step 6.1: Verify Tooltip values")
        
        """
        Step 7: Click Filter Chart option.
        Verify that only Capuccino and Espresso bars appear for the FOOD Category.
        Filter icon is also displayed in the active tool bar.
        """
        visual_obj.select_lasso_tooltip('Filter Chart')
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 3, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(x_axis_labels, parent_css='#MAINTABLE_wbody0', msg="Step 7.1: Verify only Capuccino and espresso labels in runwindow ")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 2, parent_css="#MAINTABLE_wbody0", msg="Step 7.2: Riser verification for 2 values in run window")
        util_obj.verify_object_visible(filter_css, True, 'Step 7.3: Verify Filter Button visible')
        
        """
        Step 8: Click on Capuccino bar.
        Category: Coffee
        Product: Capuccino
        Unit Sales: 189,217
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        chart_obj.verify_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", capuccino_list, msg='Step 8.1: Verify Cappucino bar tooltip list')
        
        """
        Step 9: Click Remove Filter option.
        Verify original chart appears in the output. 
        Make sure filter icon is not present.
        """
        active_chart_obj.click_chart_menu_bar_items(filter_remove_css, 4)
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 9.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 9.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 9.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 9.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 9.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 9.6')
        util_obj.verify_object_visible(filter_css, False, 'Step 9.7: Verify Filter Button not visible')
        
        """
        Step 10: Left click and drag a box around the Espresso, Latte, Biscotti and Croissant bars. 
        This will span two different Categories.
        Verify context menu displays:
        4 Points
        Filter Chart
        Exclude from Chart
        Screenshot:
        """
        left_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']", 'Espresso')
        right_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g4!mbar!r0!c1!']", 'Crossoint')
        visual_obj.create_marker_lasso(left_element,right_element, target_element_location='top_right')
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, base_obj.chart_short_timesleep)
        visual_obj.verify_lasso_tooltip(four_bar_drag, "Step 10.1: Verify Tooltip values")
        
        """
        Step 11: Click Exclude from Chart option.
        Verify that only Product Capuccino in Coffee and Scone in FOOD remain. All bars should appear for GIFTS.
        Also verify the filter icon appears on the Active tool bar.
        """
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 9, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(excluded_list, parent_css='#MAINTABLE_wbody0', msg="Step 11.1: x-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css="#MAINTABLE_wbody0", msg="Step 11.3: Riser verification")
        util_obj.verify_object_visible(filter_css, True, 'Step 11.3: Verify Filter Button visible')
        
        """
        Step 12: Click remove filter icon from the active tool bar.
        Verify original chart appears with FOOD category and 'Remove filter' is not present.
        """
        active_chart_obj.click_chart_menu_bar_items(filter_remove_css, 4)
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 12.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 12.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 12.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 12.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 12.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 12.6')
        util_obj.verify_object_visible(filter_css, False, 'Step 12.7: Verify Filter Button not visible')
        
        """
        Step 13: Dismiss the window and logout.
        """
if __name__ == '__main__':
    unittest.main()