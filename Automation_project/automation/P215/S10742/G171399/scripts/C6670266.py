'''
Created on Aug 30, 2018

@author: BM13368
Testcase Name : Verifyto Run and Edit 'Line - Product Revenue By Month - Sized by Discount'
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275855&group_by=cases:section_id&group_id=170569&group_order=asc
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6670266_TestClass(BaseTestCase):

    def test_C6670266(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 60
        long_wait= 300
        username= 'mrid'
        password= 'mrpass'
        fex_name='Line_Product_Revnue_By_Month_Sized_by_Discount'
        new_fex_name='Line Product Revenue By Month Sized by Discount1'
        reopen_fex_after_save='Line_Product_Revenue_By_Month_Sized_by_Discount1'
        folder_name='Retail_Samples/Charts'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Sale,Month', 'Marker', 'Color BY', 'Product,Category', 'Size', 'SUM.Discount', 'Tooltip', 'Multi-graph', 'Animate'] 
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M', '2.8M']
        preview_chart_x_axis_label=['1']
        preview_chart_y_axis_label=['0', '40', '80', '120', '160', '200', '240', '280']
        expected_chart_title='Revenue By Month for Product Categories - Sized By Discount'
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        filter_field='Sale,Year Equal to 2015'
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_1'
        total_riser_css_with_tagname=" path[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        parent_css_with_tag_name="#"+chart_parent_run_css+" path"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        expected_tooltip=['Sale Month:6', 'Revenue:$1,604,354.64', 'Discount:$80,546.48', 'Product Category:Media Player']
        tooltip_marker_css='marker!s3!g5!mmarker!'
        chart_color_css="[class='marker!s0!g0!mmarker!']"
        riser_preview_css="[class*='risers']"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Line_Product_Revnue_By_Month_Sized_by_Discount.fex 
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=total_riser_css, no_of_element=7)
         
        """
            Step 03 : Verify the following Line Chart
        """
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 03:01:Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 03:02:Verify y-axis label in runtime")
        chart_obj.verify_chart_title(expected_chart_title, 'run', "Step 03:03:Verify chart title at runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 03:04:Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 03:05:Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 03:06:Verify number of risers at runtime")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 91, "Step 03:07:Verify number of chart segments")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mline!', 'bar_blue', "Step 03:08:Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 03:09: Verify legends")
         
        """
            Step 04 : Hover over anywhere on Line Chart
            Verify the tooltip
        """
        chart_obj.verify_tooltip_in_run_window(tooltip_marker_css, expected_tooltip, "Step 04:01:Verify tooltip valus", use_marker_enable=True)
         
        """
            Step 05 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 7, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 91, "Step 05: Verify number of chart segments")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 7, medium_wait)
        
        """
            Step 06 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
         
        chart_obj.api_logout()
        
        """
            Step 07 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Line_Product_Revnue_By_Month_Sized_by_Discount.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 1, long_wait)
        
        """
            Step 08 : Verify the following Query Pane,Filter Pane and Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 08:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 08:02: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 08:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 08:04: Verify yaxis label")
#         chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 08:05: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 08:05: Verify number of chart segments in preview", custom_css=riser_preview_css)
#         chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 08:07: Verify chart color in preview')
        chart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 08:06:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 08:07:Verify yaxis title in preview")
        chart_obj.verify_chart_title(expected_chart_title, 'preview',"Step 08:08:Verify preview chart title")
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 08:09: Verify filter pane field is available in filterbox")
        
        """
            Step 09 : Click Run
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 7, medium_wait)
        
        """ Verify the output """
        
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, msg="Step 09:01:Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, msg="Step 09:02:Verify y-axis label in runtime")
        chart_obj.verify_chart_title(expected_chart_title, 'run', "Step 09:03:Verify chart title at runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 09:04:Verify x_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 09:05:Verify y_axis title at runtime")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 09:06:Verify number of risers at runtime")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 91, "Step 09:07:Verify number of chart segments")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mline!', 'bar_blue', "Step 09:08:Verify chart color")
        chart_obj.verify_legends_in_run_window(expected_legends, msg="Step 09:09: Verify legends")

        """
            Step 10 : Click IA > Save> Select "SmokeTest" folder > Enter title as "Line Product Revenue By Month Sized by Discount1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
            Step 11 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 12 :Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Line_Product_Revnue_By_Month_Sized_by_Discount1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_after_save, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 1, long_wait)
        
        """
            Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 12:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 12:02: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 12:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 12:04: Verify yaxis label")
#         chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 12:05: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 12:05: Verify number of chart segments in preview", custom_css=riser_preview_css)
#         chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 12:07: Verify chart color in preview')
        chart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 12:06:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, parent_css="#"+chart_parent_preview_css, msg="Step 12:07:Verify yaxis title in preview")
        chart_obj.verify_chart_title(expected_chart_title, 'preview',"Step 12:08:Verify preview chart title")
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 12:09: Verify filter pane field is available in filterbox")
        
        """
            Step 12 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()