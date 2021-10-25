'''
Created on Oct 16, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6984773&group_by=cases:section_id&group_id=542008&group_order=asc
Testcase Name : Verify Horizontal & Vertical Percent Line in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import active_chart, chart

class C6984773_TestClass(BaseTestCase):

    def test_C6984773(self):
        """
            TESTCASE Functions Object
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        preview_parent_css="TableChart_1"
        preview_yaxis_title_css="#"+preview_parent_css+" [class='yaxis-title']"
        colheader_css="#"+preview_parent_css+" g.chartPanel text[class^='colHeader-label']"
        legend_dc_css="#"+preview_parent_css+" [class='legend-labels!s1!']"
        expected_legend_list=['Unit Sales', 'Dollar Sales']
        
        short_time=25
        medium_time=35

        """
            Step 01 : Log in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Execute following URL to create Chart
            http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS2031%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        """
            Step 03 : Select Active Report as Output file format
        """
        chart_obj.change_output_format_type('active_report')
        
        """
            Step 04 : Click Format tab and click Other and Select Line chart
            Step 05 : From Select a chart pop up choose 'Horizontal Percent Line'. Click OK
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('line', 'horizontal_percent_line', 14)
        chart_obj.wait_for_number_of_element("#"+preview_parent_css+" [class*='riser!']", 6, medium_time)
       
        """
            Step 06 :  Add fields as follows:
            Region under Columns,
            Unit Sales and Dollar Sales under Horizontal Axis
            Product ID under Vertical Axis
        """
        field_name1='Region'
        field_name2='Unit Sales'
        field_name3='Dollar Sales'
        field_name4='Product ID'
        
        expected_column_header_label=['Region : Product ID', 'Midwest', 'Northeast', 'Southeast', 'West']
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name1, 1, 'Columns', 1)
        chart_obj.wait_for_visible_text(colheader_css, field_name1, short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name2, 1, 'Horizontal Axis', 1)
        chart_obj.wait_for_visible_text(preview_yaxis_title_css, field_name2, short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name3, 1, 'Horizontal Axis', 2)
        chart_obj.wait_for_visible_text(legend_dc_css, field_name3, short_time)
        
        chart_obj.drag_field_from_data_tree_to_query_pane(field_name4, 1, 'Vertical Axis', 1)
        chart_obj.wait_for_visible_text(colheader_css, 'Region : Product ID', short_time)
        
        preview_expected_xaxis_label_list=['C141', 'C144']
        preview_expected_yaxis_label_list=['0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%']
        riser_css="[class='riser!s0!g0!mline!r0!c1!']"
        preview_parent_css_with_tagname1="#"+preview_parent_css+" path"
        
        chart_obj.verify_column_label(expected_column_header_label, "#"+preview_parent_css, msg='Step 06:01:')
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+preview_parent_css, msg="Step 06:02:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+preview_parent_css, msg="Step 06:03:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 8, msg="Step 06:04:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", parent_css="#"+preview_parent_css, attribute='stroke', msg="Step 06:05:")
        chart_obj.verify_legends_in_preview(expected_legend_list, parent_css="#"+preview_parent_css, msg="Step 06:06:")
        chart_obj.verify_number_of_chart_segment(preview_parent_css, 8, "Step 06:07:Verify chart segments", custom_css="path[class^='riser']")
        
        """
            Step 07 : Click Run.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        run_parent_css="MAINTABLE_wbody0"
        
        run_parent_css_with_tagname="#"+run_parent_css+" path"
        
        run_exp_xaxis_label_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        run_exp_yaxis_label_list=['0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%', '0%', '20%', '40%', '60%', '80%', '100%']
        
        expected_toolbar_menu_list=['More Options','Advanced Chart','Original Chart', 'Aggregation', 'Sum']
        run_expected_column_label=['Region', 'Midwest', 'Northeast', 'Southeast', 'West']
        run_exp_chart_title='Unit Sales, Dollar Sales BY Region, Product ID'
        active_menubar_css="#MAINTABLE_wmenu0"
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 07:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, msg="Step 07:02:")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname, 1, 10, msg="Step 07:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 07:04:", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 07:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_expected_column_label, "#"+run_parent_css, msg='Step 07:06:')
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+run_parent_css, msg="Step 07:07:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'bar_blue', parent_css="#"+run_parent_css, attribute='stroke', msg="Step 07:08:")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 10, "Step 07:09: Verify chart segments", custom_css="path[class^='riser']")
        
        """
            Step 08 : Back in the Others/Line Chart menu, select Vertical Percent Line.
            Region under columns.
            Unit Sales and Dollar Sales under Vertical Axis
            Product ID under Horizontal Axis.
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('line', 'vertical_percent_line', 3)
        chart_obj.wait_for_number_of_element("#"+preview_parent_css+" [class*='riser!']", 12, medium_time)
        
        preview_expected_xaxis_label_list=['C141', 'C141', 'C144', 'C141', 'C144', 'C141', 'C144']
        preview_expected_yaxis_label_list=['0%', '20%', '40%', '60%', '80%', '100%']
        
        chart_obj.verify_column_label(expected_column_header_label, "#"+preview_parent_css, msg='Step 08:01:')
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+preview_parent_css, msg="Step 08:02:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list,parent_css="#"+preview_parent_css, msg="Step 08:03:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 8, msg="Step 08:04:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "bar_blue", parent_css="#"+preview_parent_css, attribute='stroke', msg="Step 08:05:")
        chart_obj.verify_legends_in_preview(expected_legend_list, parent_css="#"+preview_parent_css, msg="Step 08:06:")
        chart_obj.verify_number_of_chart_segment(preview_parent_css, 8, "Step 08:07:Verify chart segments", custom_css="path[class^='riser']")
        
        """
            Step 09 : Click Run.
        """
        chart_obj.run_chart_from_toptoolbar()
        utillobj.switch_to_frame(pause=2)
        
        run_exp_xaxis_label_list=['C...', 'C...', 'F...', 'F...', 'F...', 'G...', 'G...', 'G...']
        run_exp_yaxis_label_list=['0%', '20%', '40%', '60%', '80%', '100%']
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+run_parent_css, msg="Step 09:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+run_parent_css, xyz_axis_label_length=1, msg="Step 09:02:")
        chart_obj.verify_number_of_risers(run_parent_css_with_tagname, 1, 8, msg="Step 09:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 09:04:", parent_css=active_menubar_css)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 09:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_column_label(run_expected_column_label, "#"+run_parent_css, msg='Step 09:06:')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'bar_blue', parent_css="#"+run_parent_css, attribute='stroke', msg="Step 09:07:")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+run_parent_css, msg="Step 09:08:")
        chart_obj.verify_number_of_chart_segment(run_parent_css, 8, "Step 09:09: Verify chart segments", custom_css="path[class^='riser']")
        
        """
            Step 10 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        


if __name__ == "__main__":
    unittest.main()