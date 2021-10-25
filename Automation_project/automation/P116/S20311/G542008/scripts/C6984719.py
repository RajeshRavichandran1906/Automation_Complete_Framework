'''
Created on Oct 15, 2018

@author: BM13368
Testcase ID :  http://172.19.2.180/testrail/index.php?/cases/view/6984719&group_by=cases:section_id&group_order=asc&group_id=542008
Testcase Name :  Verify BAR, PIE, LINE, AREA & SCATTER charts are displayed correctly
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_chart_rollup
from common.lib import utillity
from common.wftools import active_chart, chart

class C6984719_TestClass(BaseTestCase):

    def test_C6984719(self):
        """
            TESTCASE Functions Object
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        chart_rollup_obj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        preview_parent_css_with_tagname="#"+preview_parent_css+" rect"
        
        short_time=25
        medium_time=50
          
        """
            Step 01 : Log in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Execute following URL to create Chart
            http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS20311%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
            Step 03 : Change Output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
            Step 04 : Select data from the left pane (Dimensions and Measures)
            Category under Columns
            Product under Horizontal Axis, & 
            Unit Sales under Vertical Axis
        """
        field_name1='Category'
        field_name2='Product'
        field_name3='Unit Sales'
        preview_expected_column_header_label=['Category : Product', 'Coffee']
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name1, 1, 'Columns', 1)
        
        css1="#"+preview_parent_css+" text[class='colHeader-label!']"
        chart_obj.wait_for_visible_text(css1, field_name1,short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name2, 1, 'Horizontal Axis', 1)
        chart_obj.wait_for_visible_text(css1, 'Category : Product', short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name3, 1, 'Vertical Axis', 1)
        chart_obj.wait_for_visible_text(preview_yaxis_title_css, field_name3, short_time)
        
        """ See corresponding data is displayed in the Live Preview pane."""
        
        exp_yaxis_title_list=['Unit Sales','Unit Sales', 'Unit Sales']
        preview_expected_label_list=['Capuccino', 'Espresso']
        preview_expected_yaxis_label_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        riser_css="[class='riser!s0!g0!mbar!r0!c0!']"
        
        chart_obj.verify_y_axis_title_in_preview(exp_yaxis_title_list, msg="Step 04:01:")
        chart_obj.verify_column_label(preview_expected_column_header_label, "#"+preview_parent_css, msg='Step 04:02')
        chart_obj.verify_x_axis_label_in_preview(preview_expected_label_list, msg="Step 04:03")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, msg="Step 04:04:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname, 1, 2, msg="Step 04:05")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", parent_css="#"+preview_parent_css, msg="Step 04:06")
        
        """
            Step 05:Click the Run button.
        """ 
        chart_obj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=2)
        run_parent_css="MAINTABLE_wbody0"
        run_exp_yaxis_title="#"+run_parent_css+" .chartPanel text[class*='yaxis-title']"
        run_parent_css_with_tagname="#"+run_parent_css+" rect"
        
        chart_obj.wait_for_visible_text(run_exp_yaxis_title, field_name3)
        run_exp_yaxis_label_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        run_exp_xaxis_label_list=['Capuccino', 'Espresso', 'Latte', 'Biscotti', 'Croissant', 'Scone', 'Coffee Grinder', 'Coffee Pot', 'Mug', 'Thermos']
        run_exp_xaxis_title_list=['Product']
        run_exp_column_label=['Category', 'Coffee', 'Food', 'Gifts']
        
        expected_toolbar_menu_list=['More Options','Advanced Chart','Original Chart', 'Aggregation', 'Sum']
        run_exp_chart_title="Unit Sales BY Category, Product"
        active_menubar_css="#MAINTABLE_wmenu0"
        
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 05:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 05:04")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname, 1, 10, msg="Step 05:05")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 05:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 05:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 05:08')
        
        
        """ Step 06 : Using the Advanced Chart icon at the top of the Chart, scroll to the PIE chart options and select the first PIE chart.
                    Click OK.
        """
        run_parent_css1='MAINTABLE_0'
        color_riser_css="[class='riser!s0!g0!mwedge!r0!c1!']"
        chartrollup_tool_css="#wall1 [class='arWindowBarTitle'] span[id='wtitle1']"
        chart_rollup_obj.click_chart_menu_bar_items(run_parent_css1, 1)
        chart_obj.wait_for_visible_text(chartrollup_tool_css, 'Chart/Rollup Tool', short_time)
        chart_rollup_obj.select_advance_chart('wall1', 'piebevel')
        parent_css_pie="#MAINTABLE_wbody0_f path"+color_riser_css
        chart_obj.wait_for_number_of_element(parent_css_pie, 1, medium_time)
        
        exp_pie_label=['Unit Sales','Unit Sales','Unit Sales']
        expected_legend_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        
        """ Expect to see the Bar Chart converted to a Line chart."""
        
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 06:01')
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 06:02", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 06:03", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_pie_label_in_single_group_in_run_window(exp_pie_label, parent_css="#"+run_parent_css, label_css="text[class^='pieLabel!g']", msg='Step 06:04:')
        chart_obj.verify_legends_in_run_window(expected_legend_list, "#"+run_parent_css, 5, 'Step 06:05: Verify pie Legend List in preview')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(color_riser_css, "bar_blue", parent_css="#"+run_parent_css, msg="Step 06:06")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 30, "Step 06:07: Verify number of pie segments in preview", custom_css="[class*='riser!s']")
          
        """ Step 07 : Using the Advanced Chart icon at the top of the Chart, scroll to the Line Chart options and select the first Line chart.
            Click OK.
        """
        chartrollup_tool_css="#wall1 [class='arWindowBarTitle'] span[id='wtitle1']"
        chart_rollup_obj.click_chart_menu_bar_items(run_parent_css1, 1)
        chart_obj.wait_for_visible_text(chartrollup_tool_css, 'Chart/Rollup Tool', short_time)
        
        chart_rollup_obj.select_advance_chart('wall1', 'line')
        parent_css="#MAINTABLE_wbody0_f path[class*='riser!s0!g0!mline!r0!c1!']"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_time)
        run_parent_css_with_tagname_line="#"+run_parent_css+" path"
        
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 07:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 07:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 07:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 07:04")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname_line, 1, 3, msg="Step 07:05")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 07:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 07:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 07:08')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class*='riser!s0!g0!mline!r0!c1!']", "bar_blue", parent_css="#"+run_parent_css,attribute="stroke", msg="Step 06:06")
         
        
        """ Step 08: Using the Advanced Chart icon at the top of the Chart, scroll to the Area Chart options and select the first Area chart.
            Click OK.
        """
        
        chart_rollup_obj.click_chart_menu_bar_items(run_parent_css1, 1)
        chartrollup_tool_css="#wall1 [class='arWindowBarTitle'] span[id='wtitle1']"
        chart_obj.wait_for_visible_text(chartrollup_tool_css, 'Chart/Rollup Tool', short_time)
        chart_rollup_obj.select_advance_chart('wall1', 'area')
        
        parent_css="#MAINTABLE_wbody0_f path[class*='riser!s0!g0!marea!r0!c1!']"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_time)
       
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 08:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 08:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 08:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 08:04")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname_line, 1, 3, msg="Step 08:05")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 08:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 08:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 08:08')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class*='riser!s0!g0!marea!r0!c1!']", "bar_blue", parent_css="#"+run_parent_css, msg="Step 08:09")
        
        """ Step 9 : Using the Advanced Chart icon at the top of the Chart, scroll to the Scatter/Bubble options and select the Scatter Diagram.
            Click OK.
        """
        chart_rollup_obj.click_chart_menu_bar_items(run_parent_css1, 1)
        chart_obj.wait_for_visible_text(chartrollup_tool_css, 'Chart/Rollup Tool', short_time)
        chart_rollup_obj.select_advance_chart('wall1', 'scatter(xy_plot)')
        parent_css="#MAINTABLE_wbody0_f path[class='riser!s0!g1!mmarker!r0!c1!']"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_time)
        run_exp_yaxis_label_list=['0','250K','500K','750K']
        run_parent_css_with_tagname_scatter="#"+run_parent_css+" circle"
        run_exp_xaxis_label_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos', 'Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos', 'Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+run_parent_css, msg="Step 09:01")
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 09:02")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, xyz_axis_label_length=3, msg="Step 09:03")
        chart_obj.verify_x_axis_title_in_run_window(run_exp_xaxis_title_list, parent_css="#"+run_parent_css, msg="Step 09:04")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname_scatter, 1, 10, msg="Step 09:05")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 09:06", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 09:07", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_exp_column_label, "#"+run_parent_css, msg='Step 09:08')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class*='riser!s0!g1!mmarker!r0!c1!']", "bar_blue", parent_css="#"+run_parent_css, attribute='stroke', msg="Step 09:09")
        
        """
            Step 10 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()