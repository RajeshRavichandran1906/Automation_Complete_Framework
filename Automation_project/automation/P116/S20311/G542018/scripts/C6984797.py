'''
Created on Nov 19, 2018

@author: Varun
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6984797
Testcase Name : Verify a chart shows correct filtered output once filter via lasso applied - Bar Chart
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility
from common.lib import utillity
from common.wftools import active_chart
from common.wftools import chart
from common.wftools import visualization

class C6984797_TestClass(BaseTestCase):

    def test_C6984797(self):
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
        riser_css_runwindow = "#MAINTABLE_wbody0  rect[class^='riser']"
        capuccino_tooltip_list = ['Category:Coffee', 'Product:Capuccino', 'Unit Sales:189217', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        lasso_verify_list = ['2 points', 'Filter Chart', 'Exclude from Chart']
        lasso_verify_list_4_bars = ['4 points', 'Filter Chart', 'Exclude from Chart']
        expected_xval_list=['Capuccino', 'Espresso']
        expected_run_xval_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        expected_run_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        x_label_after_excluding = ['Capuccino', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        y_label_after_excluding = ['0','50K','100K','150K','200K','250K','300K','350K','400K']
        column_label_list = ['Category','Coffee','Food','Gifts']
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
        Step 4: Select data from the left pane (Dimensions and Measures)
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
        Step 5: Run the report
        Verify Active Chart 'Unit Sales BY Category, Product' is displayed on canvas with selected data.
        """
        active_chart_obj.run_chart_from_toptoolbar()
        core_util_obj.switch_to_frame()
        active_chart_obj.wait_for_number_of_element("#MAINTABLE_wbody0 text[class^='xaxis']", 13, 25)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 5.1: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 5.2: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 5.3: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 5.4:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 5.5:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 5.6')
        
        """
        Step 6: Left click and drag a box around the Capuccino and Espresso bars.
        Verify context menu displays:
        2 Points
        Filter Chart
        Exclude from Chart Screenshot:
        """
        left_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g1!mbar!r0!c0!']", 'Capuccino')
        right_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']", 'Espresso')
        visual_obj.create_lasso(left_element,right_element)
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, short_time)
        visual_obj.verify_lasso_tooltip(lasso_verify_list, "Step 6.1: Verify Tooltip values")
        
        """
        Step 7: Click Filter Chart option.
        Verify that only Capuccino and Espresso bars appear for the FOOD Category.
        Filter icon is also displayed in the active tool bar.
        """
        visual_obj.select_lasso_tooltip('Filter Chart')
        active_chart_obj.wait_for_number_of_element(riser_css_runwindow, 2, short_time)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 7.1: x-label verification")
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 7.2: Verify Filter Button Visible')
        
        """
        Step 8: Click on Capuccino bar.
        Verify context menu displays:
        Category: Coffee
        Product: Capuccino
        Unit Sales: 189,217
        Filter Chart
        Exclude from Chart
        Remove Filter
        """
        chart_obj.verify_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", capuccino_tooltip_list, msg='Step 8.1: Verify Capuccino bar tooltip list')
        
        """
        Step 9: Click Remove Filter option.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        active_chart_obj.wait_for_number_of_element(riser_css_runwindow, 10, short_time)
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 9.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 9.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 9.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 9.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 9.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 9.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 9.7')
        
        """
        Step 10: Left click and drag a box around the Espresso, Latte, Biscotti and Croissant bars. 
        This will span two different Categories.
        Verify context menu displays:
        4 Points
        Filter Chart
        Exclude from Chart
        """
        left_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g5!mbar!r0!c0!']", 'Espresso')
        right_element = util_obj.validate_and_get_webdriver_object("rect[class='riser!s0!g4!mbar!r0!c1!']",'Croissant')
        visual_obj.create_lasso(left_element,right_element)
        active_chart_obj.wait_for_number_of_element(tooltip_css, 1, short_time)
        visual_obj.verify_lasso_tooltip(lasso_verify_list_4_bars, "Step 10.1: Verify lasso tooltip" )
        
        """
        Step 11: Click Exclude from Chart option.
        Verify that only Product Capuccino in Coffee and Scone in FOOD remain. All bars should appear for GIFTS.
        Also verify the filter icon appears on the Active tool bar.
        """
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        active_chart_obj.wait_for_number_of_element(riser_css_runwindow, 6, short_time)
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 11.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(x_label_after_excluding, parent_css='#MAINTABLE_wbody0', msg="Step 11.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(y_label_after_excluding, parent_css='#MAINTABLE_wbody0', msg="Step 11.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 6, parent_css="#MAINTABLE_wbody0", msg="Step 11.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 11.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 11.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c2!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 11.7')
        
        """
        Step 12: Click remove filter icon from the active tool bar.
        Verify original chart appears with FOOD category and 'Remove filter' is not present.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        active_chart_obj.wait_for_number_of_element(riser_css_runwindow, 10, short_time)
        util_obj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 12.1: Verify Filter Button not Visible')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_run_xval_list, parent_css='#MAINTABLE_wbody0', msg="Step 12.2: x-label verification")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_run_yval_list, parent_css='#MAINTABLE_wbody0', msg="Step 12.3: y-label verification")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, parent_css="#MAINTABLE_wbody0", msg="Step 12.4: Riser verification")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 12.5:", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_column_label_in_run_window(column_label_list, parent_css="#MAINTABLE_wbody0", msg='Step 12.6:')
        active_chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g1!mbar!r0!c0!']", 'bar_blue', parent_css='#MAINTABLE_wbodyMain0', msg='Step 12.7')
        
if __name__ == '__main__':
    unittest.main()      
