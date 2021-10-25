'''
Created on Jan 4, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667256&group_by=cases:section_id&group_order=asc&group_id=512309
Testcase Name : Verify Vertical Waterfall Chart in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.chart import Chart

class C6667256_TestClass(BaseTestCase):

    def test_C6667256(self):
        
        """ TESTCASE VARIABLES """
        
        
        """ CLASS OBJECTS """
        active_chart_obj=Active_Chart(self.driver)
        chart_obj=Chart(self.driver)
        
        """ CSS """
        PREVIEW_PARENT_CSS1="TableChart_1"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        """
        Step 1:Launch IA Chart with GGSales.Mas
        """
        chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales', mrid='mrid', mrpass='mrpass')
 
        """
        Step 2:From Home tab Select Active Report format.
        """
        chart_obj.change_output_format_type('active_report')
 
        """
        Step 3:Double click on fields Category, Unit Sales & Dollar Sales.
        """

        chart_obj.double_click_on_datetree_item('Category', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='xaxisOrdinal-title']", visble_element_text="Category", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='yaxis-title']", visble_element_text="Unit Sales", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS1+" [class='legend-labels!s1!']", visble_element_text="Dollar Sales", time_out=20)
        
        preview_expected_xaxis_label_list=['Coffee']
        preview_expected_yaxis_label_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        preview_parent_css_with_tagname1="#"+PREVIEW_PARENT_CSS1+" rect"
        expected_legend_list=['Unit Sales','Dollar Sales']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 3:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 3:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 2, msg="Step 3:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "dark_cyan", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 3:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 2, "Step 3:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_preview(expected_legend_list,parent_css="#"+PREVIEW_PARENT_CSS1, msg='Step 3:06:Verify legends') 
 
        """
        Step 4:Click Run.
        Expect to see the following Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        run_exp_xaxis_label_list=['Coffee', 'Food', 'Gifts']
        run_exp_yaxis_label_list=['0', '4M', '8M', '12M', '16M','20M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Category']
        
        RUN_CHART_CSS="MAINTABLE_wbody0_f"
        RUN_PARENT_CSS_WITH_TAGNAME="#" + RUN_CHART_CSS + " rect"
        ACTIVE_MENUBAR_CSS="#MAINTABLE_wmenu0"
        run_exp_chart_title="Unit Sales, Dollar Sales BY Category"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 4:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 4:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 6, msg="Step 4:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 4:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 4:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'dark_cyan', parent_css="#"+RUN_CHART_CSS, msg="Step 4:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 6, "Step 4:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 4:08:")
        
        chart_obj.switch_to_default_content()

        """
        Step 5:Select Format tab > Click Other > Select 'Vertical Waterfall Chart' > Click OK
        Verify the Clustered bar chart converted into the Preview pane for Vertical Waterfall Chart.
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('bar', 'vertical_waterfall_charts', 3)
        preview_expected_yaxis_label_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 5:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 5:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 2, msg="Step 5:03:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "dark_cyan", parent_css="#"+PREVIEW_PARENT_CSS1, msg="Step 5:04:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS1, 2, "Step 5:05:Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_legends_in_preview(expected_legend_list,parent_css="#"+PREVIEW_PARENT_CSS1, msg='Step 5:06:Verify legends')
        
        """
        Step 6:Click Save and Run.
        Verify the following Vertical Waterfall Chart displayed as expected
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        run_exp_xaxis_label_list=['Coffee', 'Food', 'Gifts']
        run_exp_yaxis_label_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_xaxis_title_list=['Category']
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 6:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 6:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 4, msg="Step 6:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 6:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 6:05:", parent_css="#MAINTABLE_wbody0_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'dark_cyan', parent_css="#"+RUN_CHART_CSS, msg="Step 6:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 4, "Step 6:07: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 6:08:")
        chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+RUN_CHART_CSS, msg="Step 6:09:Verify legend in runtime chart")


        """
        Step 7:Exit IA
        """
        
        
if __name__ == "__main__":
    unittest.main()     
        
        