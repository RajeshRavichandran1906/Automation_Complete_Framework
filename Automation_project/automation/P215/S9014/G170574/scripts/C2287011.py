'''
Created on Aug 10, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2287011&group_by=cases:section_id&group_id=170574&group_order=asc
TestCase Name : Verify to Run and Edit 'Revenue Region Bar'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287011_TestClass(BaseTestCase):

    def test_C2287011(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 40
        long_wait= 240
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Revenue_Region_Bar'
        new_fex_name='Revenue Region Bar1'
        reopen_fex_name= 'Revenue_Region_Bar1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_yaxis_title=['Revenue']
        chart_xaxis_title=['Store Business Region']
        runtime_chart_y_axis_label=['0%', '20%', '40%', '60%', '80%', '100%']
        runtime_chart_x_axis_label=['EMEA', 'North America', 'Oceania', 'South America']
        tooltip_expected_value_list=['Store Business Region:North America', 'Revenue:$139,282,702.54', 'Product Category:Media Player']
        
        preview_chart_y_axis_label=['0%', '20%', '40%', '60%', '80%', '100%']
        preview_chart_x_axis_label=['North America']
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Store,Business,Region', 'Horizontal Axis', 'Revenue', 'Marker', 'Color BY', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'] 
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_2'
        chart_color_preview_css="[class='riser!s0!g0!mbar!']"
        x_axis_title_css="#"+chart_parent_run_css+" text[class^='xaxis'][class$='title']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        riser_preview_css = "[class*='riser!s']"
        barchart_labels= "[class*='labels!']"
        application_css= '#applicationButton'
        tooltip_riser_css="riser!s3!g1!mbar!"
        no_of_risers="#"+chart_parent_run_css+" rect[class^='riser']"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Revenue_Region_Bar.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=no_of_risers, no_of_element=28)
            
        """
        Verify the output:
        """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 02:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 02:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_preview_css, "bar_blue", attribute='fill', msg="Step 02:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 02:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 1, msg="Step 02:07: Verify number of risers")
        """
        Hover over chart riser and Verify the output:
        """
        chart_obj.verify_tooltip_in_run_window(tooltip_riser_css, tooltip_expected_value_list, "Step 02:08: Verify tooltip")
        """
        Step 03 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(barchart_labels, 17, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 03:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(barchart_labels, 17, medium_wait)
       
        chart_obj.api_logout()
         
        """
        Step 04:Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Revenue_Region_Bar.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(barchart_labels, 14, long_wait)
        
        """
        Step 05: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 05:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 05:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 05:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 05:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step 05:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 05:06:Verify legends in preview") 
        chart_obj.verify_number_of_risers("#"+chart_parent_preview_css+" rect", 7, 1, msg="Step 05:07:Verify number of risers in preview chart")
              
        """
        Step 06: Click Run 
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(x_axis_title_css, "Store Business Region", medium_wait)
        
        """ Verify the output: """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 06:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 06:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 06:02: Verify pie Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 06:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 06:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_preview_css, "bar_blue", attribute='fill', msg="Step 06:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 06:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 1, msg="Step 02:07: Verify number of risers")
        
        """
        Step 07: Click IA > Save> Select "SmokeTest" folder > Enter title as "Revenue Region Bar1" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 09: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Revenue_Region_Bar1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(barchart_labels, 14, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 09:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 09:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css="#"+chart_parent_preview_css,msg="Step 09:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step 09:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(legend_list, parent_css="#"+chart_parent_preview_css, msg="Step 09:06:Verify legends in preview") 
        chart_obj.verify_number_of_risers("#"+chart_parent_preview_css+" rect", 7, 1, msg="Step 09:07:Verify number of risers in preview chart") 
        """
        Step 10 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()