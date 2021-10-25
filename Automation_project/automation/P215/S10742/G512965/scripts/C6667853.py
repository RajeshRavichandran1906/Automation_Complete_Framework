'''
Created on Aug 6, 2018

@author: BM13368
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/6667853&group_by=cases:section_id&group_id=512965&group_order=asc
TestCase_Name : Verify to Run and Edit Regional Sales Trend
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C6667853_TestClass(BaseTestCase):

    def test_C6667853(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 60
        long_wait= 240
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Regional_Sales_Trend'
        new_fex_name='Regional Sales Trend1'
        reopen_fex_name= 'Regional_Sales_Trend1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_yaxis_title=['Revenue']
        chart_xaxis_title=['Month']
        runtime_chart_y_axis_label=['0','10M','20M','30M','40M','50M','60M','70M']
        runtime_chart_x_axis_label=['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_tooltip_list=['Month:6', 'Revenue:$46,702,358.43', 'Business Region:North America']
        
        preview_chart_y_axis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        preview_chart_x_axis_label=['1']
        
        legend_list= ['EMEA', 'North America', 'Oceania', 'South America']
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Sale,Month', 'Marker', 'Color', 'Store,Business,Region', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_2'
        chart_color_preview_css="[class='marker!s0!g0!mmarker!']"
        x_axis_title_css="#"+chart_parent_run_css+" text[class^='xaxis'][class$='title']"
        
        riser_preview_css = "[class*='riser!s']"
        line_totallabel_css= "[class*='labels!']"
        
        application_css= '#applicationButton'
        chart_color_css="[class='riser!s0!g0!mline!']"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Regional_Sales_Trend.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=x_axis_title_css)
          
        """
        Verify the output:
        """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 02:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 02:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", attribute='stroke', msg="Step 02:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 52, "Step 02:06: Verify number of pie segments in run window")
           
        """
        Step 03: Hover over anywhere on Line chart, Verify the tooltip
        """
        chart_obj.verify_tooltip_in_run_window("marker!s1!g5!mmarker!", expected_tooltip_list, "Step 03:01: Verify tooltip values", use_marker_enable=True)
           
        """
        Step 04 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(line_totallabel_css, 24, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 52, "Step 04:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(line_totallabel_css, 24, medium_wait)
                   
        """
        Step 05: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
        Step 06: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Sales_Trend.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(line_totallabel_css, 8, long_wait)
        
        """
        Step 07: Verify the Chart launched in IA tool
        Verify the following Query panel and Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 07:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 07:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 07:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 07:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 07:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 07:06: Verify chart color in preview')
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 07:07:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 07:08:Verify yaxis title in preview")
        
        """
        Step 08: Click Run inside IA tool
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        chart_obj.wait_for_number_of_element(parent_css, 1, time_out=medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(x_axis_title_css, 'Month', time_out=medium_wait)
        
        """ Verify the output: """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 08:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 08:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 08:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 08:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 08:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", attribute='stroke', msg="Step 08:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 52, "Step 08:06: Verify number of pie segments in run window")
        
        """
        Step 09: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Regional Sales Trend1" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 11: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Regional_Sales_Trend1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(line_totallabel_css, 8, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 11:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 11:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 11:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "white", parent_css="#"+chart_parent_preview_css, msg="Step 11:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 1, "Step 11:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, attribute='stroke', msg='Step 11:06: Verify chart color in preview')
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 11:07:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 11:08:Verify yaxis title in preview")
        
        
        """
        Step 12 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()