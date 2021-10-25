'''
Created on Jul 31, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2275850&group_by=cases:section_id&group_id=170569&group_order=asc
TestCase_Name : Verify to Run and Edit 'YTD Daily Sales Trend
'''
import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C2275850_TestClass(BaseTestCase):

    def test_C2275850(self):
        
        chart_obj=chart.Chart(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        fex_name="YTD_Daily_Sales_Trend"
        save_fex="YTD Daily Sales Trend1"
        save_fex_to_edit="YTD_Daily_Sales_Trend1"
        folder_name="Retail_Samples/Charts/Autolink_Targets"
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts/Autolink_Targets&BIP_item=YTD_Daily_Sales_Trend.fex
        """
        xaxis_title_css="#jschart_HOLD_0 [class^='xaxis'][class$='title']"
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid="mrid", mrpass="mrpass", home_page="old", run_chart_css=xaxis_title_css, no_of_element=1)
        utillobj.synchronize_with_visble_text(xaxis_title_css, "Sale Month Name : Sale Day", 25)
         
        """
            Step 03 : Verify the following Chart
        """
        chart_xaxis_title=['Sale Month Name : Sale Day']
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 03:01: Verify x-axis title')
         
        chart_yaxis_title=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 03:02: Verify y-axis title")
         
        chart_xaxis_label_list=['JAN : 1', 'JAN : 2', 'JAN : 3', 'JAN : 4', 'JAN : 5', 'JAN : 6', 'JAN : 7', 'JAN : 8', 'JAN : 9', 'JAN : 10', 'JAN : 11', 'JAN : 12', 'JAN : 13', 'JAN : 14', 'JAN : 15', 'JAN : 16', 'JAN : 17', 'JAN : 18', 'JAN : 19', 'JAN : 20', 'JAN : 21', 'JAN : 22', 'JAN : 23', 'JAN : 24', 'JAN : 25', 'JAN : 26', 'JAN : 27', 'JAN : 28', 'JAN : 29', 'JAN : 30', 'JAN : 31', 'FEB : 1', 'FEB : 2', 'FEB : 3', 'FEB : 4', 'FEB : 5', 'FEB : 6', 'FEB : 7', 'FEB : 8', 'FEB : 9', 'FEB : 10', 'FEB : 11', 'FEB : 12', 'FEB : 13', 'FEB : 14', 'FEB : 15', 'FEB : 16', 'FEB : 17', 'FEB : 18', 'FEB : 19', 'FEB : 20', 'FEB : 21', 'FEB : 22', 'FEB : 23', 'FEB : 24', 'FEB : 25', 'FEB : 26', 'FEB : 27', 'FEB : 28', 'MAR : 1']
        chart_obj.verify_x_axis_label_in_run_window(chart_xaxis_label_list, msg="Step 03:03: Verify x-axis label")
 
        chart_yaxis_label_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        chart_obj.verify_y_axis_label_in_run_window(chart_yaxis_label_list, msg="Step 03:04 : Verify y-axis label")
         
        title_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg g .title")
        act_title=title_elem.text.replace('\n','')
        expected_title ="Current Month - Daily Sales TrendFor All"
        utillobj.asequal(expected_title,act_title, "Step 03:05: Verify chart title")
         
        title_alignment_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg g .title span")
        act_title_alignment=title_alignment_elem.value_of_css_property('text-align')
        utillobj.asequal('center',act_title_alignment, "Step 03:06: Verify chart title alignment")
         
        css="[class='riser!s0!g0!mline!']"
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(css, "bar_blue", attribute='stroke', msg="Step 03:07: Verify chart color")
         
        """
            Step 04 : Hover over anywhere on line chart, Verify the Tooltip
        """
        expected_tooltip_list=['Sale Month Name:FEB', 'Sale Day:4', 'Revenue:$1,141,129.50']
        chart_obj.verify_tooltip_in_run_window("marker!s0!g34!mmarker!", expected_tooltip_list, "Step 04:01: Verify tooltip values", use_marker_enable=True)
                 
        """
            Step 05 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        time.sleep(4)
        chart_xaxis_title=['Sale Month Name : Sale Day']
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 05:01: Verify x-axis title')
         
        self.driver.maximize_window()
        time.sleep(3)
         
        chart_obj.api_logout()
        
        """
            Step 06 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Autolink_Targets/YTD_Daily_Sales_Trend.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        css="#TableChart_1 [class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(css, "Sale Month Name : Sale Day", 60)
        
        """
            Verify the following Query Pane,Filter Pane and Live Preview
        """
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Sale,Month', 'Sale,Month Name', 'Sale,Day', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 06:01 : Verify the Query panel")
         
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis','Sale,Month',1, msg="Step 06:02 : Verify query tree field name and colur", color_to_verify="Trolley_Grey", font_to_verify="italic")
        filter_field_name1 = "Model Equal to Optional Simple Parameter (Name: MODEL)"
        chart_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 06:03: Verify the filter panel")
         
        filter_field_name2 = "Sale,Date From Beginning of Year to Today"
        chart_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 06:04: Verify the filter panel")
         
        """ Verify live preview chart"""
        title_elem=self.driver.find_element_by_css_selector("#TableChart_1 svg g div")
        act_title_elem=title_elem.text.replace('\n','')
        expected_title="Current Month - Daily Sales TrendFor All MODEL"
        utillobj.asequal(expected_title, act_title_elem, "Step 06:05: Verify chart title in preview")
         
        title_alignment_elem=self.driver.find_element_by_css_selector("#TableChart_1 svg g div span")
        act_title_alignment=title_alignment_elem.value_of_css_property('text-align')
        utillobj.asequal('center',act_title_alignment, "Step 06:06: Verify chart title alignment")
         
        expected_xaxis_label_list=['JAN : 1']
        chart_obj.verify_x_axis_label_in_preview(expected_xaxis_label_list,  msg="Step 06:07: Verify x-axis label in preview chart")
         
        expected_yaxis_label_list=['0', '100', '200', '300', '400', '500', '600']
        chart_obj.verify_y_axis_label_in_preview(expected_yaxis_label_list,  msg="Step 06:08: Verify y-axis label in preview chart")
         
        riser_css="[class='marker!s0!g0!mmarker!']"
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "yellow", msg="Step 06:09: Verify chart color")
         
        """
            Step 07 : Click Run
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 45)
        chart_obj.switch_to_frame()
        time.sleep(3)
         
        """
            Verify the Chart run successfully
        """
        chart_xaxis_title=['Sale Month Name : Sale Day']
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 07:01: Verify x-axis title')
         
        chart_yaxis_title=['Revenue']
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 07:02: Verify y-axis title")
         
        chart_xaxis_label_list=['JAN : 1', 'JAN : 2', 'JAN : 3', 'JAN : 4', 'JAN : 5', 'JAN : 6', 'JAN : 7', 'JAN : 8', 'JAN : 9', 'JAN : 10', 'JAN : 11', 'JAN : 12', 'JAN : 13', 'JAN : 14', 'JAN : 15', 'JAN : 16', 'JAN : 17', 'JAN : 18', 'JAN : 19', 'JAN : 20', 'JAN : 21', 'JAN : 22', 'JAN : 23', 'JAN : 24', 'JAN : 25', 'JAN : 26', 'JAN : 27', 'JAN : 28', 'JAN : 29', 'JAN : 30', 'JAN : 31', 'FEB : 1', 'FEB : 2', 'FEB : 3', 'FEB : 4', 'FEB : 5', 'FEB : 6', 'FEB : 7', 'FEB : 8', 'FEB : 9', 'FEB : 10', 'FEB : 11', 'FEB : 12', 'FEB : 13', 'FEB : 14', 'FEB : 15', 'FEB : 16', 'FEB : 17', 'FEB : 18', 'FEB : 19', 'FEB : 20', 'FEB : 21', 'FEB : 22', 'FEB : 23', 'FEB : 24', 'FEB : 25', 'FEB : 26', 'FEB : 27', 'FEB : 28', 'MAR : 1']
        chart_obj.verify_x_axis_label_in_run_window(chart_xaxis_label_list, msg="Step 07:03: Verify x-axis label")
 
        chart_yaxis_label_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        chart_obj.verify_y_axis_label_in_run_window(chart_yaxis_label_list, msg="Step 07:04 : Verify y-axis label")
         
        title_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg g .title")
        act_title=title_elem.text.replace('\n','')
        expected_title ="Current Month - Daily Sales TrendFor All"
        utillobj.asequal(expected_title,act_title, "Step 07:05: Verify chart title")
         
        title_alignment_elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 svg g .title span")
        act_title_alignment=title_alignment_elem.value_of_css_property('text-align')
        utillobj.asequal('center',act_title_alignment, "Step 07:06: Verify chart title alignment")
         
        css="[class='riser!s0!g0!mline!']"
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(css, "bar_blue", attribute='stroke', msg="Step 07:07: Verify chart color")
         
        """
            Step 08 : Click IA > Save> Select "SmokeTest" folder > Enter title as "YTD Daily Sales Trend1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.save_as_from_application_menu_item(save_fex)
        
        """
            Step 09 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
            Step 10 : Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/~rsadv/YTD_Daily_Sales_Trend1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(edit_fex_folder_after_save, fex_name=save_fex_to_edit, mrid="mrid", mrpass="mrpass")
        css="#TableChart_1 [class^='xaxis'][class$='title']"
        utillobj.synchronize_with_visble_text(css, "Sale Month Name : Sale Day", 60)
         
        """
            Verify the following Query Pane,Filter Pane and Live Preview
        """
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Sale,Month', 'Sale,Month Name', 'Sale,Day', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 10:01 : Verify the Query panel")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis','Sale,Month',1, msg="Step 10:02 : Verify query tree field name and colur", color_to_verify="Trolley_Grey", font_to_verify="italic")
        
        filter_field_name1 = "Model Equal to Optional Simple Parameter (Name: MODEL)"
        chart_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 10:03: Verify the filter panel")
         
        filter_field_name2 = "Sale,Date From Beginning of Year to Today"
        chart_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 10:04: Verify the filter panel")
         
        """ Verify live preview chart"""
        title_elem=self.driver.find_element_by_css_selector("#TableChart_1 svg g div")
        act_title_elem=title_elem.text.replace('\n','')
        expected_title="Current Month - Daily Sales TrendFor All MODEL"
        utillobj.asequal(expected_title, act_title_elem, "Step 10:05: Verify chart title in preview")
         
        title_alignment_elem=self.driver.find_element_by_css_selector("#TableChart_1 svg g div span")
        act_title_alignment=title_alignment_elem.value_of_css_property('text-align')
        utillobj.asequal('center',act_title_alignment, "Step 10:06: Verify chart title alignment")
         
        expected_xaxis_label_list=['JAN : 1']
        chart_obj.verify_x_axis_label_in_preview(expected_xaxis_label_list,  msg="Step 10:07: Verify x-axis label in preview chart")
         
        expected_yaxis_label_list=['0', '100', '200', '300', '400', '500', '600']
        chart_obj.verify_y_axis_label_in_preview(expected_yaxis_label_list,  msg="Step 10:08: Verify y-axis label in preview chart")
         
        riser_css="[class='marker!s0!g0!mmarker!']"
        chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_css, "yellow", msg="Step 10:09: Verify chart color")
        
        """
            Step 11 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()