'''
Created on Dec 16, 2017

@author: Praveen Ramkumar/Re-Automated by : Bhagavathi Date : 07-May-2018
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227782
TestCase Name : Chart:Verify basic chart production for Column, PIE, Line chart and Scatter diagram.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon, active_miscelaneous
from common.wftools import active_chart
from common.lib import utillity

class C2227782_TestClass(BaseTestCase):

    def test_C2227782(self):
        """
        TESTCASE VARIABLES
        """
        
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        actchart_obj=active_chart.Active_Chart(self.driver)
        act_misc_obj=active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        expected_default_x_axis_label_list=['Group 0', 'Group 1', 'Group 2', 'Group 3','Group 4']
        expected_default_y_axis_label_list=['0', '10', '20', '30', '40', '50']
        expected_y_axis_title_list=['Gross Profit']
        expected_x_axis_title_list=['Product Category']
        expected_x_axis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_label_list=['0', '20M', '40M', '60M', '80M', '100M']
        
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        
        expected_piechart_preview_title_list=['Gross Profit']
        expected_piechart_preview_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        """
        Step 01:Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 02:Navigate to folder: P292_S10032_G157266
        Execute the following URL:
        http://machine:port/{alias}/ia?tool=chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
        Change the Output type to Active Report.
        """
#         actchart_obj.invoke_chart_tool_using_api(master='baseapp/wf_retail_lite', mrid="autodevuser01")
        utillobj.infoassist_api_login_('Chart', 'baseapp/wf_retail_lite', 'mrid01', 'mrpass01')
        parent_css="#TableChart_1 text[class='legend-labels!s0!']"
        utillobj.synchronize_with_visble_text(parent_css, 'Series0', 290)
        actchart_obj.verify_x_axis_label_in_preview(expected_default_x_axis_label_list, msg="Step 01:01:")
        actchart_obj.verify_y_axis_label_in_preview(expected_default_y_axis_label_list, msg="Step 01:02:")
        ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 03:From the Measures group, select the Sales sub-group of fields, then select the Gross_Profit field.
        From the Dimensions group, select the Product sub-group, then select the Product,Category field.
        """
        actchart_obj.double_click_on_datetree_item('Gross Profit', 1)
        actchart_obj.wait_for_number_of_element("#TableChart_1 text[class^='yaxis'][class$='title']", 1, 35)
        actchart_obj.double_click_on_datetree_item('Product,Category', 1)
        actchart_obj.wait_for_number_of_element("#TableChart_1 text[class^='xaxis'][class$='title']", 1, 35)
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, msg="Step 03:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 03:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 03:03:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 03:04:")
        actchart_obj.verify_number_of_risers_in_preview('rect', 1, 7, msg='Step 03:05')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g3!mbar!", "bar_blue", "Step 03:06 verify bar chart color")
        
        """
        Step 04:Click the Run button
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 04:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:04:")
        actchart_obj.verify_number_of_risers_in_run_window('rect', 1, 7, parent_css="#MAINTABLE_wbody0",msg='Step 04:06:')
        actchart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 04:07:Verify chart title", parent_css="#MAINTABLE_wmenu0")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g3!mbar!", "bar_blue", "Step 04:08 verify bar chart color")
        
        """
        Step 05:Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the PIE icon.
        """
        actchart_obj.switch_to_default_content()
        actchart_obj.select_chart_type('pie')
        actchart_obj.wait_for_number_of_element("#TableChart_1 .chartPanel text", expected_number=1)
        actchart_obj.verify_x_axis_title_in_preview(expected_piechart_preview_title_list, x_or_y_axis_title_css="text[class^='pieLabel']", msg="Step 05:01:")
        actchart_obj.verify_legends_in_preview(expected_piechart_preview_legends, msg='Step 05:02')
#         pie_riser_css="riser!s4!g0!mwedge!"
#         actchart_obj.verify_chart_color_using_get_attribute_in_preview(pie_riser_css, 'brick_red', msg='Step 05:03:Verify chart')
        actchart_obj.verify_number_of_pie_segments('#TableChart_1', 1, 7, "Step 05:03:Verify number of pie segements")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mwedge!", "bar_blue", "Step 05:04 verify bar chart color")
        
        
        """
        Step 06: Click the Run button.
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        expected_x_axis_title_list1=['Gross Profit']
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list1,parent_css="#MAINTABLE_wbody0_f", x_or_y_axis_title_css="text[class^='pieLabel']", msg="Step 06:01: Verify x-axis title")
        actchart_obj.verify_number_of_pie_segments('#MAINTABLE_wbody0', 1, 7, "Step 06:02:Verify number of pie segements")
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        act_misc_obj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 06:03:Verify chart title")
        act_misc_obj.verify_chart_title("MAINTABLE_wbody0_ft", 'Gross Profit by Product Category', "Step 06:04:Verify chart title")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mwedge!", "bar_blue", "Step 06:05 verify bar chart color")
        
        """
        Step 07: Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the LINE icon.
        """
        actchart_obj.switch_to_default_content()
        #select formattab line chart
        actchart_obj.select_chart_type('line')
        utillobj.synchronize_with_number_of_element("#TableChart_1 path[class='riser!s0!g0!mline!']", 1, 20)
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, x_or_y_axis_title_css="[class='xaxisOrdinal-title']",msg="Step 07:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 07:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 07:03:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 07:04:")
        actchart_obj.verify_number_of_risers_in_preview('path', 1, 1, msg='Step 07:05:')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 07:06 verify Line chart color",attribute_type="stroke")
        
        """
        Step 08: Click the Run button.
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        xaxis_title=['Product Category']
        actchart_obj.verify_x_axis_title_in_run_window(xaxis_title, parent_css="#MAINTABLE_wbody0_f",x_or_y_axis_title_css="[class='xaxisOrdinal-title']", msg="Step 08:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 08:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 08:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 08:04:")
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        act_misc_obj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 08:05:Verify chart title")
        act_misc_obj.verify_chart_title("MAINTABLE_wbody0_ft", 'Gross Profit by Product Category', "Step 08:06:Verify chart title")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mline!", "bar_blue", "Step 08:07 verify bar chart color", attribute_type='stroke')
        
        """
        Step 09: Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the SCATTER icon.
        """
        actchart_obj.switch_to_default_content()
        actchart_obj.select_chart_type('scatter')
        actchart_obj.wait_for_number_of_element("#TableChart_1 circle[class^='riser']", expected_number=7)
        expected_x_axis_title_list=['Product Category']
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, x_or_y_axis_title_css="[class='xaxisOrdinal-title']", msg="Step 09:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 09:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 09:03:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 09:04:")
        actchart_obj.verify_number_of_risers_in_preview('circle', 1, 7, msg='Step 09:05:Verify number of circles inm preview')
        
        """
        Step 10: Click run button
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)

        expected_x_axis_title_list=['Product Category']
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 10:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 10:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 10:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css="#MAINTABLE_wbody0_f", msg="Step 10:04:")
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        act_misc_obj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 10:05:Verify chart title")
        act_misc_obj.verify_chart_title("MAINTABLE_wbody0_ft", 'Gross Profit by Product Category', "Step 10:06:Verify chart title")
        

if __name__ == '__main__':
    unittest.main()