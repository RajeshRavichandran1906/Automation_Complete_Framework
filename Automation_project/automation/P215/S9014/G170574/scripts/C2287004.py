'''
Created on Aug 8, 2018

@author: BM13368
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2287004&group_by=cases:section_id&group_order=asc&group_id=170574
TestCase Name :Verify to Run and Edit Regional Profit by Category
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2287004_TestClass(BaseTestCase):

    def test_C2287004(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 40
        long_wait= 90
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Regional_Profit_by_Category'
        new_fex_name='Regional Profit by Category1'
        reopen_fex_name= 'Regional_Profit_by_Category1'
        folder_name='Retail_Samples/Portal/Small_Widgets'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        chart_yaxis_title=['Gross Profit']
        runtime_chart_y_axis_label=['0', '20M', '40M', '60M', '80M', '100M']
        runtime_chart_x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        tooltip_expected_value_list=['Product Category:Media Player', 'Gross Profit:$22,897,933.25', 'Store Region:EMEA']
        
        preview_chart_y_axis_label=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        preview_chart_x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Product,Category', 'Horizontal Axis', 'Gross Profit', 'Marker', 'Color BY', 'Store,Business,Region', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= '#TableChart_2'
        chart_color_preview_css="[class='riser!s0!g0!mbar!']"
        y_axis_title_css="#"+chart_parent_run_css+" [class='yaxis-title']"
        wait_for_visible_text="Gross Profit"
        iframe_css= '#resultArea [id^=ReportIframe-]'
        riser_preview_css = "[class*='riser!s']"
        barchart_labels= "[class*='labels!']"
        application_css= '#applicationButton'
        tooltip_riser_css="riser!s0!g3!mbar"
                
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02:Run the Chart using the below API URL
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets&BIP_item=Regional_Profit_by_Category.fex 
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=y_axis_title_css)
            
        """
        Verify the output:
        """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 02:01: Verify y-axis title")
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 02:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 02:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_preview_css, "bar_blue", attribute='fill', msg="Step 02:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 02:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 1, msg="Step 02:07: Verify number of risers")
        
        """
        Step 03 : Hover over Media Player, Verify the tooltip
        """
        chart_obj.verify_tooltip_in_run_window(tooltip_riser_css, tooltip_expected_value_list, "Step 03:01: Verify tooltip")
        
        """
        Step 04 :Resize the browser window and verify it does not throws any error message and then maximize the window
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(barchart_labels, 13, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 03:01: Verify number of pie segments after browser resize in run window")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(barchart_labels, 13, medium_wait)
        
        """
        Step 05:Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
         
        """
        Step 06: Edit the Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(barchart_labels, 13, long_wait)
        
        """
        Step 07: Verify the Chart launched in IA tool
        Verify the following Query panel and Chart Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 07:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css, msg="Step 07:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css, msg="Step 07:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css=chart_parent_preview_css,msg="Step 07:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment("TableChart_2", 7, "Step 07:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_number_of_risers(chart_parent_preview_css+" rect", 7, 1, msg="Step 07:06: Verify number of risers")
              
        """
        Step 08: Click Run 
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(y_axis_title_css, wait_for_visible_text, medium_wait)
        
        """ Verify the output: """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 08:01: Verify y-axis title")
        chart_obj.verify_x_axis_label_in_run_window(runtime_chart_x_axis_label, msg="Step 08:03: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(runtime_chart_y_axis_label, msg="Step 08:04: Verify x-axis label")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_preview_css, "bar_blue", attribute='fill', msg="Step 08:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 08:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 1, msg="Step 08:07: Verify number of risers")
        
        """
        Step 09: Click IA > Save as> Select "SmokeTest" > MyContent folder > Enter title as "Regional Profit by Category1" > Click Save"
        Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, long_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 11: Edit the saved chart using "rsadv" with the below API URL
        Edit the saved chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Regional_Profit_by_Category1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(barchart_labels, 13, long_wait)
        
        """
        Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 11:01: Verify the Query panel in preview")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css=chart_parent_preview_css, msg="Step 11:02: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css=chart_parent_preview_css, msg="Step 11:03: Verify yaxis label")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_preview_css, "bar_blue", parent_css=chart_parent_preview_css,msg="Step 11:04: Verify chart color")
        chart_obj.verify_number_of_chart_segment("TableChart_2", 7, "Step 11:05: Verify number of pie segments in preview", custom_css=riser_preview_css)
        chart_obj.verify_number_of_risers(chart_parent_preview_css+" rect", 7, 1, msg="Step 11:06: Verify number of risers in previeww")
        
        """
        Step 12 :Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()