'''
Created on Aug 13, 2018

@author: KS13172
TestCase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2287008
TestCase_Name : Verify to Run and Edit 'Product Profit Line By Month'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287008_TestClass(BaseTestCase):

    def test_C2287008(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 30
        long_wait= 60
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Product_Profit_Line_By_Month'
        new_fex_name='Product Profit Line By Month1'
        reopen_fex_name= 'Product_Profit_Line_By_Month1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_yaxis_title=['Gross Profit']
        chart_xaxis_title=['Sale Month']
        runtime_chart_y_axis_label=['0','2M','4M','6M','8M','10M']
        runtime_chart_x_axis_label=['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_tooltip_list=['Sale Month:6', 'Gross Profit:$6,538,869.12', 'Product Category:Stereo Systems']
        preview_chart_y_axis_label=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000']
        preview_chart_x_axis_label=['1']
        legend_list= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        query_field_list= ['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'Sale,Month', 'Marker', 'Color BY', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run= 'jschart_HOLD_0'
        chart_parent_preview_css= '#TableChart_1'
        chart_parent_preview= 'TableChart_1'
        chart_color_preview_css="[class='marker!s0!g0!mmarker!']"
        x_axis_title_css= "text[class^='xaxis'][class$='title']"
        
        riser_preview_css = "[class*='marker!s']"
        line_totallabel_css= "[class*='labels!']"
        
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        chart_color_css="[class='riser!s0!g0!mline!']"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Product_Profit_Line_By_Month.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=x_axis_title_css, home_page='old')
          
        """
        Verify the output:
        """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step02:01a: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step02:01b: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step02:02: Verify Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step02:04: Verify y-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue1", attribute='stroke', msg="Step02:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run, 91, "Step02:06: Verify number of segments in run window")
           
        """
        Step03: Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(line_totallabel_css, 25, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run, 91, "Step03:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(line_totallabel_css, 25, medium_wait)
                   
        """
        Step 04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
        Step 05: Edit the Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Product_Profit_Line_By_Month.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(line_totallabel_css, 15, long_wait)
        
        """
        Step 06: Verify the Chart launched in IA tool
        Verify the following Query panel and Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step06:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_preview_css, msg='Step06.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_preview_css, msg='Step06.1b')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css, msg="Step06:02a: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css, msg="Step06:02b: Verify yaxis label")
        chart_obj.verify_legends_in_preview(legend_list, chart_parent_preview_css, msg='Step06:03: Verify Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "yellow", chart_parent_preview_css, msg="Step06:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview, 7, "Step06:05: Verify number of segments in preview", custom_css=riser_preview_css)
        
        """
        Step07: Click Run inside IA tool
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, time_out=medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(line_totallabel_css, 25, medium_wait)
        
        """Click Run, Hover anywhere verify tooltip"""
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step07:01a: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step07:01b: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step07:02: Verify Legend List in run window')
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step07:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step07:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue1", attribute='stroke', msg="Step07:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run, 91, "Step07:06: Verify number of segments in run window")
        
        chart_obj.verify_tooltip_in_run_window("marker!s4!g5!mmarker!", expected_tooltip_list, "Step07:07: Verify tooltip values", use_marker_enable=True)
        
        """
        Step08: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Product Profit Line By Month1" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step10: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Product_Profit_Line_By_Month1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(line_totallabel_css, 15, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step10:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, chart_parent_preview_css, msg='Step10.1a')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, chart_parent_preview_css, msg='Step10.1b')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css, msg="Step10:02a: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css, msg="Step10:02b: Verify yaxis label")
        chart_obj.verify_legends_in_preview(legend_list, chart_parent_preview_css, msg='Step10:03: Verify Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "yellow", chart_parent_preview_css, msg="Step10:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview, 7, "Step10:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        
        """
        Step11: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()