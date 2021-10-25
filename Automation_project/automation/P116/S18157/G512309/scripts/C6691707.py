'''
Created on Jan 7, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6691707
Testcase Name : Verify Error Bar in others tab under Format menu.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods


class C6691707_TestClass(BaseTestCase):

    def test_C6691707(self):
        
        """ TESTCASE VARIABLES """
        medium_wait=30
        
        
        """ CLASS OBJECTS """
        active_chart_obj=Active_Chart(self.driver)
        chart_obj=Chart(self.driver)
        utillobj=UtillityMethods(self.driver)
        
        """ CSS """
        PREVIEW_PARENT_CSS1="TableChart_1"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        QUERY_TREE_CSS = "#queryTreeColumn div table tbody tr:nth-child({0})"
        
        """
        Step 1:Log in to WebFOCUS
        http://machine:port/{alias}
        Step 2:Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS18157%2F
        """
        chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
              
        """
        Step 3:Change Output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
        
        """
        Step 4:Add following fileds
        Category to Horizontal Axis 
        Dollar Sales to Vertical Axis
        """
        chart_obj.double_click_on_datetree_item('Category', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='xaxisOrdinal-title']", visble_element_text="Category", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='yaxis-title']", visble_element_text="Dollar Sales", time_out=20)
        
        preview_expected_xaxis_label_list=['Coffee']
        preview_expected_yaxis_label_list=['0', '1M','2M','3M','4M','5M','6M','7M']
        preview_parent_css_with_tagname1="#"+PREVIEW_PARENT_CSS1+" rect"
        exp_xaxis_title=['Category']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 1, msg="Step 4:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "bar_blue", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 4:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 1, "Step 4:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_preview(exp_xaxis_title, parent_css="#"+PREVIEW_PARENT_CSS1, msg='Step 4:06:')
        
        """
        Step 5:Click Run Button
        Expect to see the following Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        run_exp_xaxis_label_list=['Coffee', 'Food', 'Gifts']
        run_exp_yaxis_label_list=['0', '4M', '8M','12M', '16M', '20M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Category']
        exp_yaxis_title_list=['Dollar Sales']
        
        RUN_CHART_CSS="MAINTABLE_wbody0_f"
        RUN_PARENT_CSS_WITH_TAGNAME="#" + RUN_CHART_CSS + " rect"
        ACTIVE_MENUBAR_CSS="#MAINTABLE_wmenu0"
        run_exp_chart_title="Dollar Sales by Category"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 5:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 5:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 3, msg="Step 5:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 5:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 5:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_CHART_CSS, msg="Step 5:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 3, "Step 5:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 5:08:")
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+RUN_CHART_CSS,msg="Step 5:09:")
        
        """
        Step 6:Select Format > Other and Select a chart pop up choose 'Error Bar' and Click ok
        """
        chart_obj.switch_to_default_content()
        
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('bar', 'error_bar', 5)
        time.sleep(2)
        
        """
        Step 7:Add following fileds
        Unit Sales to the Errorbar Low bucket.
        Add Dollar Sales to the Errorbar High bucket
        Expect to see the Clustered bar chart converted into the Preview pane for Error Bar.
        """
        chart_obj.drag_field_from_data_tree_to_query_pane('Unit Sales', 1, 'Errorbar Low', 1)
        chart_obj.wait_for_visible_text(QUERY_TREE_CSS.format('5'),'Unit Sales',time_out=10)
        
        chart_obj.drag_field_from_data_tree_to_query_pane('Dollar Sales', 1, 'Errorbar High', 1)
        chart_obj.wait_for_visible_text(QUERY_TREE_CSS.format('7'),'Dollar Sales',time_out=10)
        error_bar_css="#"+PREVIEW_PARENT_CSS1+" path[class^='errorBar!s0!g0!']"
        chart_obj.wait_for_number_of_element(error_bar_css, 1, time_out=10)
        
        utillobj.verify_object_visible(error_bar_css, True, "Step 7: Verify error line is displayed in preview chart")
        
        preview_expected_xaxis_label_list=['Coffee']
        preview_expected_yaxis_label_list=['0', '1M','2M','3M','4M','5M','6M','7M']
        exp_yaxis_title_list=['Category']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 1, msg="Step 6:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "bar_blue", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 6:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 1, "Step 6:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_yaxis_title_list,"#"+PREVIEW_PARENT_CSS1, msg="Step 6:08:")
        chart_obj.verify_data_labels(PREVIEW_PARENT_CSS1, ['6,097,561'], "Step 6:09: Verify data labels", custom_css="text[class^='dataLabels']")
        
        """
        Step 8:Click Run Button
        Expect to see the following Error Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        bar_css=" rect[class^='riser']"
        chart_obj.wait_for_number_of_element("#"+RUN_CHART_CSS+bar_css, 9, time_out=medium_wait)
        
        run_exp_xaxis_label_list=['Coffee', 'Food', 'Gifts']
        run_exp_yaxis_label_list=['0', '4M', '8M', '12M', '16M', '20M']
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Category']
        exp_yaxis_title_list=['Dollar Sales']
        run_exp_chart_title='Dollar Sales, Unit Sales, Dollar Sales by Category'
        expected_label=['17,231,455', '17,229,333', '11,695,502', '1,376,266', '1,384,845', '927,880', '17,231,455', '17,229,333', '11,695,502']
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 8:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 8:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 9, msg="Step 8:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 8:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 8:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_CHART_CSS, msg="Step 8:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 9, "Step 8:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 8:08:")
        chart_obj.verify_data_labels(RUN_CHART_CSS, expected_label, "Step 8:11: Verify data labels", custom_css="text[class^='dataLabels']")
        
        """
        Step 9:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()