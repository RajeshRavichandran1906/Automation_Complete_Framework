'''
Created on Aug 7, 2018

@author: BM13368
Testcase ID :http://172.19.2.180/testrail/index.php?/cases/view/2287007&group_by=cases:section_id&group_order=asc&group_id=170574
Testcase Name :Verify to Run and Edit 'Average Cost vs Revenue Scatter'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287007_TestClass(BaseTestCase):

    def test_C2287007(self):
        
        "Test Case Objects"
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "Test Case Variables"
        
        medium_wait= 30
        long_wait= 60
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Average_Cost_vs_Revenue_Scatter'
        new_fex_name='Average Cost vs Revenue Scatter'
        reopen_fex_name= 'Average_Cost_vs_Revenue_Scatter'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_xaxis_title=['Revenue']
        chart_yaxis_title=['AVE Cost of Goods']
        runtime_chart_y_axis_label=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        runtime_chart_x_axis_label=['0', '4M', '8M', '12M', '16M']
        
        preview_chart_y_axis_label=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        preview_chart_x_axis_label=['0','500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500', '4,000', '4,500']
        
        legend_list= ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Gross Profit', '1,218.4', '618.2', '17.9']
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'AVE.Cost of Goods', 'Horizontal Axis', 'Revenue', 'Marker', 'Size', 'AVE.Gross Profit', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip', 'Multi-graph', 'Animate'] 
        
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= '#TableChart_2'
        chart_color_preview_css="[class='riser!s1!g8!mmarker!']"
        x_axis_title_css="#"+chart_parent_run_css+" text[class^='xaxis'][class$='title']"
#         legends_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Gross Profit', '1,218.4', '618.2', '17.9']
        preview_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'AVE Gross Profit', '749.9', '385.4', '21']
        riser_preview_css = "[class*='riser!s']"
        scatter_labels= "[class*='labels!']"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
#                 
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Average_Cost_vs_Revenue_Scatter.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=x_axis_title_css)
              
        """
        Verify the output:
        """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 02:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 02:02: Verify pie Legend List in run window', legend_length=10)
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s1!g13!mmarker!']", "pale_green", attribute='fill', msg="Step 02:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 02:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_circles_in_run_window(0, 237, "Step 02:07: Verify number of circles", "#"+chart_parent_run_css)
            
        """
        Step 03 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(scatter_labels, 21, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 03:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(scatter_labels, 21, medium_wait)
                       
        """
        Step 04: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
          
        """
        Step 05: Edit the Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Average_Cost_vs_Revenue_Scatter.fex&tool=Chart
        """
        riser_css="[class*='riser']"
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(riser_css, 79, long_wait)
         
        """
        Step 06: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 06:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css,msg="Step 06:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css,msg="Step 06:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "pale_green", parent_css=chart_parent_preview_css,msg="Step 06:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment("TableChart_2", 79, "Step 06:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css=chart_parent_preview_css, msg="Step 06:06:Verify legends in preview", legend_length=10)
        chart_obj.verify_number_of_circles_in_preview(chart_parent_preview_css, 0, 80, "Step 06:07:Verify number of circles in preview window") 
              
        """
        Step 07: Click Run inside IA tool
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(riser_css, 157, long_wait)
        
        """ Verify the output: """
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg='Step 07:00: Verify x-axis title')
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 07:01: Verify y-axis title")
        chart_obj.verify_legends_in_run_window(legend_list, msg='Step 07:02: Verify pie Legend List in run window', legend_length=10)
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 07:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 07:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s1!g13!mmarker!']", "pale_green", attribute='fill', msg="Step 07:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 157, "Step 07:06: Verify number of chart segments in run window")
#         chart_obj.verify_legends_in_run_window(legends_list, msg="Step 07:07:Verify legends")
        chart_obj.verify_number_of_circles_in_run_window(0, 237, "Step 07:07: Verify number of circles", "#"+chart_parent_run_css)
        
        """
        Step 08: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Average Cost vs Revenue Scatter1" > Click Save
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 09: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 10: Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Average_Cost_vs_Revenue_Scatter1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(riser_css, 79, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 10:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css,msg="Step 10:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css,msg="Step 10:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "pale_green", parent_css=chart_parent_preview_css,msg="Step 10:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment("TableChart_2", 79, "Step 10:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_legends_in_preview(preview_legend_list, parent_css=chart_parent_preview_css, msg="Step 10:06:Verify legends in preview", legend_length=10)
        chart_obj.verify_number_of_circles_in_preview(chart_parent_preview_css, 0, 80, "Step 10:07:Verify number of circles in preview window") 
        
        """
        Step 11 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()