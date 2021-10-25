'''
Created on Nov 20, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984798
Testcase Name : Verify a chart shows correct filtered output once filter via lasso applied - Line Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from common.wftools import chart
from common.wftools import visualization

class C6984798_TestClass(BaseTestCase):

    def test_C6984798(self):
        """
            TESTCASE Functions Object
        """
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        colheader_css="#"+preview_parent_css+" g.chartPanel text[class^='colHeader-label']"
        x_axis_css = "text[class^='xaxis']"
        tooltip_css = "div[class*='tooltip']"
        biscotti_tooltip_list = ['Category:Food', 'Product:Biscotti', 'Unit Sales:421377', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        lasso_verify_list = ['2 points', 'Filter Chart', 'Exclude from Chart']
        expected_xval_list=['Biscotti', 'Croissant']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        x_label_after_excluding = ['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Mug', 'Thermos']
        column_label_list = ['Category','Coffee','Food','Gifts']
        filtered_column_label_list = ['Category','Food']
        run_exp_chart_title='Unit Sales BY Category, Product'
        short_time=25

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
        Step 4: From the Format tab, select Line chart.
        """
        active_chart_obj.select_chart_type('Line')
        
        """
        Step 5: Select data from the left pane (Dimensions and Measures)
        Category - Columns
        Product - Horizontal Axis 
        Unit Sales - Vertical Axis
        """
        active_chart_obj.drag_field_from_data_tree_to_query_pane('Category', 1, 'Columns', 1)
        active_chart_obj.wait_for_number_of_element(colheader_css, 1, short_time)
        active_chart_obj.double_click_on_datetree_item('Product', 1)
        active_chart_obj.wait_for_number_of_element(x_axis_css, 2, short_time)
        active_chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        active_chart_obj.wait_for_number_of_element(preview_yaxis_title_css, 1, short_time)
        
        """
        Step 6: Run the Line Chart.
        Verify Active Chart 'Unit Sales BY Category, Product' is displayed on canvas with selected data.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0 text[class^='xaxis']", 13, 25)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 6.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 3, parent_css="#MAINTABLE_wbody0", msg="Step 6.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 6.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 6.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 6.6',attribute='stroke')
        
        """
        Step 7: Left click and drag a box around Biscotti and Croissant points in the FOOD Category.
        Verify context menu displays:
        2 Points
        Filter Chart
        Exclude from Chart Screenshot:
        """
        left_element = util_obj.validate_and_get_webdriver_object("circle[class='marker!s0!g0!mmarker!r0!c1!']", 'Biscotti')
        right_element = util_obj.validate_and_get_webdriver_object("circle[class='marker!s0!g4!mmarker!r0!c1!']", 'Croissant')
        visual_obj.create_marker_lasso(left_element,right_element,target_xoffset=20)
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, short_time)
        visual_obj.verify_lasso_tooltip(lasso_verify_list, "Step 7.1: Verify Tooltip values")
        
        """
        Step 8: Click Filter Chart option.
        Verify that the only points on the Line chart are for Biscotti and Croissant.
        The Lines for Coffee and Gifts do NOT appear.
        Filter icon is also displayed in the active tool bar.
        """
        visual_obj.select_lasso_tooltip('Filter Chart')
        active_chart_obj.wait_for_number_of_element("text[class^='xaxis']", 5, 25)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 8.1: x-label verification")
        active_chart_obj.verify_column_label_in_run_window(filtered_column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 8.2:')
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 8.3: Verify Filter Button Visible')
        
        """
        Step 9: Hover over the Biscotti point.
        Verify context menu displays:
        Category: Food
        Product: Biscotti
        Unit Sales: 421,377
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        chart_obj.verify_tooltip_in_run_window('marker!s0!g0!mmarker!r0!c0!', biscotti_tooltip_list, 'Step 9.1: Verify Capuccino bar tooltip list', parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        """
        Step 10: Click Remove Filter option.
        Verify original chart appears in the output.
        Make sure filter icon is not present.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        active_chart_obj.wait_for_number_of_element("text[class^='xaxis']", 15, 25)
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 10.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 10.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 3, parent_css="#MAINTABLE_wbody0", msg="Step 10.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 10.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 10.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 10.7',attribute='stroke')
        
        """
        Step 11: Left click and drag a box around the Coffee Grinder and Coffee Pot points in the GIFTS Category.
        Verify context menu displays:
        2 points
        Filter Chart
        Exclude from Chart
        """
        left_element = util_obj.validate_and_get_webdriver_object("circle[class='marker!s0!g2!mmarker!r0!c2!']", 'Coffee Grinder')
        right_element = util_obj.validate_and_get_webdriver_object("circle[class='marker!s0!g3!mmarker!r0!c2!']", 'Coffee Pot')
        visual_obj.create_marker_lasso(left_element,right_element,target_xoffset=20,target_yoffset=10)
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, short_time)
        visual_obj.verify_lasso_tooltip(lasso_verify_list, "Step 11.1: Verify Tooltip values")
        
        """
        Step 12: Click Exclude from Chart option.
        Verify that Coffee Grinder and Coffee Pot have been removed from the GIFTS Category and only Mug and Thermos remain.
        """
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        active_chart_obj.wait_for_number_of_element("text[class^='xaxis']", 13, 25)
        active_chart_obj.verify_x_axis_label_in_run_window(x_label_after_excluding, parent_css='#MAINTABLE_wbody0', msg="Step 12.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 12.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1, 3, parent_css="#MAINTABLE_wbody0", msg="Step 12.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 12.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 12.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 12.6',attribute='stroke')
        
        """
        Step 13: Click remove filter icon from the active tool bar.
        Verify original chart appears with GIFTS category and 'Remove filter' is not present.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        active_chart_obj.wait_for_number_of_element("text[class^='xaxis']", 15, 25)
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 13.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 13.3: y-label verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 13.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 13.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mline!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 13.6',attribute='stroke')
        
if __name__ == '__main__':
    unittest.main()      
