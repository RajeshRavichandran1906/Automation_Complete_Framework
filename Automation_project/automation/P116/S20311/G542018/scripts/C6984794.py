'''
Created on December 21, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984794
Testcase Name : Verify a chart shows correct filtered output once filter via lasso applied - Line Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from common.wftools import chart
from common.wftools import visualization
from common.lib import base

class C6984794_TestClass(BaseTestCase):

    def test_C6984794(self):
        """
            TESTCASE Functions Object
        """
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
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
        
        """
        Test case variables
        """
        
        biscotti_after_filter = ['Capuccino', 'Espresso', 'Latte', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        biscotti_tooltip_list = ['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart']
        latte_after_filter = ['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Remove Filter']
        x_axis_labels= ['Capuccino', 'Espresso']
        y_axis_labels = ['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        y_axis_title = ['Unit Sales']
        latte_tooltip_list = ['Category:Coffee', 'Product:Latte', 'Unit Sales:878063', 'Filter Chart', 'Exclude from Chart']
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
        
        """
        Step 5: See corresponding data is displayed in the Live Preview pane.
        Verify that bar chart is displayed on canvas with selected data.
        """
        active_chart_obj.wait_for_number_of_element(riser_css, 2, base_obj.chart_short_timesleep)
        active_chart_obj.verify_x_axis_label_in_preview(x_axis_labels, msg='Step 5.1: Verify X axis label in preview')
        active_chart_obj.verify_y_axis_label_in_preview(y_axis_labels, msg='Step 5.2: Verify Y axis labels in preview')
        active_chart_obj.verify_number_of_risers_in_preview('rect', 1, 2, msg="Step 5.3: Verify Riser verification in preview")
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', msg='Step 5.4')
        active_chart_obj.verify_y_axis_title_in_preview(y_axis_title, msg='Step 5.5')
        
        """
        Step 6: Run the report
        Verify Active Chart 'Unit Sales BY Category, Product' is displayed on canvas with selected data.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.1: x-label verification in run window")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.2: y-label verification in run window")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 6.3: Riser verification in run window")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 6.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 6.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.6')
        
        """
        Step 7: Hover over on Latte bar. Verify context menu displays:
        Category: Coffee
        Product: Latte
        Unit Sales:878,063
        Filter Chart
        Exclude from Chart
        """
        chart_obj.verify_tooltip_values("MAINTABLE_wbody0", "riser!s0!g6!mbar!r0!c0!", latte_tooltip_list, msg='Step 7.1: Verify Latte bar tooltip list')
        
        """
        Step 8: Click Filter Chart option.
        Verify based on "Latte' product selection, that bar is displayed as filtered value and filter icon is displayed in the active tool bar.
        """
        chart_obj.select_tooltip_in_run_window("riser!s0!g6!mbar!r0!c0!", 'Filter Chart', "#MAINTABLE_wbody0")
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 2, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(['Latte'], parent_css='#MAINTABLE_wbody0', msg="Step 8.1: Verify only latte is present")
        util_obj.verify_object_visible(filter_css, True, 'Step 8.2: Verify Filter Button Visible')
        
        """
        Step 9: Click on Latte bar. Verify context menu displays:
        Category: Coffee
        Product: Latte
        Unit Sales: 878,063
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 2, base_obj.chart_medium_timesleep)
        chart_obj.verify_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", latte_after_filter, msg='Step 9.1: Verify Latte bar tooltip list')
        
        """
        Step 10: Click Remove Filter option.
        Verify original chart appears in the output. 
        Make sure filter icon is not present.
        """
        active_chart_obj.click_chart_menu_bar_items(filter_remove_css, 4)
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 10.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 10.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 10.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 10.6')
        
        """
        Step 11: Hover over on Biscotti bar. Verify context menu displays:
        Category: Food
        Product: Biscotti
        Unit Sales:421,377
        Filter Chart
        Exclude from Chart
        """
        chart_obj.verify_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c1!", biscotti_tooltip_list, msg='Step 11.1: Verify Biscotti bar tooltip list')
        
        """
        Step 12: Click Exclude from Chart option.
        Verify FOOD category is excluded from the chart and filter icon appears on the Active tool bar.
        """
        chart_obj.select_tooltip_in_run_window("riser!s0!g0!mbar!r0!c1!", 'Exclude from Chart', "#MAINTABLE_wbody0")
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 12, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(biscotti_after_filter, parent_css='#MAINTABLE_wbody0', msg="Step 12.1: Verify all labels except biscotti is present")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 9, parent_css="#MAINTABLE_wbody0", msg="Step 12.2: Verify the number of risers")
        
        """
        Step 13: Click remove filter icon from the active tool bar.
        Verify original chart appears with FOOD category and 'Remove filter' is not present.
        """
        active_chart_obj.click_chart_menu_bar_items(filter_remove_css, 4)
        active_chart_obj.wait_for_number_of_element(x_axis_labels_css, 13, base_obj.chart_medium_timesleep)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 13.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 13.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 13.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 13.6')
        util_obj.verify_object_visible(filter_css, False, 'Step 13.7: Verify Filter Button not visible')
        
        """
        Step 14: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()