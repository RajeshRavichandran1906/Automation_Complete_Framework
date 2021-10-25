'''
Created on Jan 6, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667257&group_by=cases:section_id&group_order=asc&group_id=512309
Testcase Name : Verify Horizontal Waterfall Chart in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.chart import Chart

class C6667257_TestClass(BaseTestCase):

    def test_C6667257(self):
        
        """ TESTCASE VARIABLES """
        medium_wait=30
        
        
        """ CLASS OBJECTS """
        active_chart_obj=Active_Chart(self.driver)
        chart_obj=Chart(self.driver)
        
        """ CSS """
        PREVIEW_PARENT_CSS1="TableChart_1"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        """
        Step 1:Log in to WebFOCUS
        http://machine:port/{alias}
        Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S18157%2FG512309%2F
        """
        chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales', mrid='mrid', mrpass='mrpass')
        
        """
        Step 3:Change Output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
        Step 4: Double click on fields Product, Unit Sales & Dollar Sales.
        """
        
        chart_obj.double_click_on_datetree_item('Product', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='xaxisOrdinal-title']", visble_element_text="Product", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='yaxis-title']", visble_element_text="Unit Sales", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='legend-labels!s1!']", visble_element_text="Dollar Sales", time_out=20)
        
        preview_expected_xaxis_label_list=['Capuccino', 'Espresso']
        preview_expected_yaxis_label_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        preview_parent_css_with_tagname1="#"+PREVIEW_PARENT_CSS1+" rect"
        expected_legend_list=['Unit Sales','Dollar Sales']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 4, msg="Step 4:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "bar_blue", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 4, "Step 4:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_preview(expected_legend_list,parent_css="#"+PREVIEW_PARENT_CSS1, msg='Step 4:06:Verify legends')
        chart_obj.verify_x_axis_title_in_preview(['Product'], parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:07:")
        
        """
        Step 5:Click the Run button.
        Expect to see the following Vertical Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        run_exp_xaxis_label_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        run_exp_yaxis_label_list=['0', '2M','4M', '6M','8M', '10M', '12M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Product']
        
        RUN_CHART_CSS="MAINTABLE_wbody0_f"
        RUN_PARENT_CSS_WITH_TAGNAME="#" + RUN_CHART_CSS + " rect"
        ACTIVE_MENUBAR_CSS="#MAINTABLE_wmenu0"
        run_exp_chart_title="Unit Sales, Dollar Sales by Product"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 5:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 5:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 20, msg="Step 5:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 5:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 5:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_CHART_CSS, msg="Step 5:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 20, "Step 5:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 5:08:")
        
        """
        Step 6:Select Format tab > Click Other > Select 'Horizontal Waterfall Chart' > Click OK
        Expect to see the Clustered bar chart converted into the Preview pane for Horizontal Waterfall.
        """
        
        chart_obj.switch_to_default_content()
        
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('bar', 'horizontal_waterfall_charts', 22)
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS1+" [class^='riser']", 3, time_out=medium_wait)
        preview_expected_xaxis_label_list=['Capuccino', 'Espresso', 'Total']
        preview_expected_yaxis_label_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 3, msg="Step 6:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "dark_cyan", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 3, "Step 6:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_preview(expected_legend_list,parent_css="#"+PREVIEW_PARENT_CSS1, msg='Step 5:06:')
        chart_obj.verify_number_of_connector_lines("#"+PREVIEW_PARENT_CSS1, 1, 2, msg="Step 6:07:")
        chart_obj.verify_x_axis_title_in_preview(['Product'], parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:08:")

        """
        Step 7:Click and Run.
        Verify the following Horizontal Waterfall Chart displayed as expected.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        connector_line_css=" path[class*='connectorLine']"
        chart_obj.wait_for_number_of_element("#"+RUN_CHART_CSS+connector_line_css, 10, time_out=medium_wait)
        
        run_exp_xaxis_label_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos', 'Total']
        run_exp_yaxis_label_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Product']
        run_exp_chart_title='Unit Sales, Dollar Sales by Product'
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 7:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 7:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 11, msg="Step 7:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 7:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 7:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'dark_cyan', parent_css="#"+RUN_CHART_CSS, msg="Step 7:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 11, "Step 7:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 7:08:")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_CHART_CSS, msg="Step 7:09:")
        chart_obj.verify_number_of_connector_lines("#"+RUN_CHART_CSS, 1, 10, msg="Step 7:10:")

        """
        Step 8: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()