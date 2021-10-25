'''
Created on Sep 5, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275861&group_by=cases:section_id&group_order=asc&group_id=170569
TestCase Name : Verifyto Run and Edit 'Stacked Bar - Sales by Month and Product Category'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2275861_TestClass(BaseTestCase):

    def test_C2275861(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        visual_obj=visualization.Visualization(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 90
        long_wait= 300
        username= 'mrid'
        password= 'mrpass'
        fex_name='Sales_by_Month_and_Product_Category_stacked_bar'
        new_fex_name='Stacked Bar - Sales by Month and Product Category1'
        reopen_fex_after_save='Stacked_Bar_-_Sales_by_Month_and_Product_Category1'
        folder_name='Retail_Samples/Charts'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Sale,Month', 'Marker', 'Color BY', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate'] 
        chart_yaxis_title=['Revenue']
        chart_xaxis_title=['Sale Month']
        y_axis_label=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        x_axis_label=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_preview_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        preview_chart_y_axis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        preview_chart_x_axis_label=['1']
        drilldown_chart_y_axis_label=['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        drilldown_chart_x_axis_label=['5']
        drilldown_chart_expected_legend_list=['Product Subcategory', 'Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        frame_css="iframe[src]"
        chart_parent_preview_css= 'TableChart_1'
        total_riser_css_with_tagname=" rect[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        chart_color_css="[class='riser!s0!g0!mbar!']"
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        css1='riser!s4!g4!mbar!'
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Sales_by_Month_and_Product_Category_stacked_bar.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,run_chart_css=frame_css)
        chart_obj.switch_to_frame(frame_css=frame_css)
           
        """
            Step 03 : Verify the following Stacked Bar Chart
        """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 03:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 03:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 03:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 03:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 03:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 03:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 03:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 03:08:")
           
        """
            Step 04 : Hover over chart riser for the Sale month '5'
            Step 05 : Verify the tooltip and Auto Drill menu
        """
        expected_tooltip_list=['Sale Month:5', 'Revenue:$23,010,126.17', 'Product Category:Stereo Systems', 'Go up to Sale Quarter', 'Drill down to']
        chart_obj.verify_tooltip_in_run_window(css1, expected_tooltip_list, "Step 04: Verify tooltip")
          
        """
            Step 06 : Hover over "Drill down to Product Sub Category", Verify the menus
        """
        visual_obj.select_tooltip(css1, "Drill down to->Product Subcategory",parent_css=chart_parent_run_css,move_to_tooltip=True)
        chart_obj.wait_for_number_of_element("[class^='riser']", 6, long_wait)
           
        """
            Step 07: Verify the Chart drills down to "Product Sub Category"
        """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 07:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 07:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(drilldown_chart_y_axis_label, msg="Step 07:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(drilldown_chart_x_axis_label, msg="Step 07:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 07:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 5, "Step 07:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 5, 1, msg="Step 07:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(drilldown_chart_expected_legend_list, msg="Step 07:08:")
           
        """
            Step 08 : Hover over Chart riser Select "Drill down to Model"
        """
        visual_obj.select_tooltip('riser!s3!g0!mbar!', "Drill down to->Model",parent_css=chart_parent_run_css,element_location='middle')
        chart_obj.wait_for_number_of_element("[class^='riser']", 11, long_wait)
           
        """
            Step 09 : Verify the Chart drills down to Model
        """
        drilldown_chart_y_axis_label=['0', '2M', '4M', '6M', '8M', '10M']
        drilldown_chart_expected_legend_list=['Model', 'BOSE AM10IV', 'BOSE AM16II', 'Harman Kardon HKTS20BQ', 'Harman Kardon HKTS30BQ', 'Onkyo SKSHT540', 'Onkyo SKSHT750B', 'Onkyo SKSHT870', 'Polk Audio LSIFX', 'Polk Audio RM705', 'Yamaha NSSP1800']
       
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 09:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 09:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(drilldown_chart_y_axis_label, msg="Step 09:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(drilldown_chart_x_axis_label, msg="Step 09:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 09:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 10, "Step 09:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 10, 1, msg="Step 09:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(drilldown_chart_expected_legend_list, msg="Step 09:08:")
           
        """
            Step 10 : Hover over any Chart riser, Select "Restore Original"
        """
        visual_obj.select_tooltip('riser!s3!g0!mbar!', "Reset",parent_css=chart_parent_run_css,move_to_tooltip=True)
        chart_obj.wait_for_number_of_element("[class^='riser']", 85, long_wait)
           
           
        """
            Step 11 : Verify the Chart restored back to original
        """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 11:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 11:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 11:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 11:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 11:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 11:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 11:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 11:08:")
           
        """
            Step 12 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 84, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 05: Verify number of chart segments")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 84, medium_wait)
        chart_obj.api_logout()
        
        """
            Step 13 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Sales_by_Month_and_Product_Category_stacked_bar.fex&tool=Chart 
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 7, long_wait)
        
        """
            Step 14 : Verify the following Query panel and Stacked Bar Chart in Live Preview
        """
        preview_segment_css=".chartPanel .groupPanel rect[class^='riser']"
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 14:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 14:02: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 14:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 14:04: Verify yaxis label")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step 14:05: Verify number of chart segments in preview", custom_css=preview_segment_css)
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 14:06:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 14:07:Verify yaxis title in preview")
        chart_obj.verify_legends_in_preview(expected_preview_legend_list, msg="Step 14:08:")
        
        """
            Step 15 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame(frame_css=frame_css)
        chart_obj.wait_for_number_of_element(total_riser_css, 84, medium_wait)
        
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 15:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 15:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 15:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 15:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 15:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 15:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 15:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 15:08:")
        
        """
            Step 16 : Hover over chart riser for the Sale month '6'
            Step 17 : Select "Drill up to Sale Quarter"
        """
        riser_css='riser!s4!g1!mbar!'
        menu_path="Go up to Sale Quarter"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=chart_parent_run_css,move_to_tooltip=True)
        chart_obj.wait_for_number_of_element(total_riser_css, 28, medium_wait)
        
        """
            Step 18 : Verify the Chart drills up to Sale Quarter
        """
        sale_quarter_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        sale_quarter_x_axis_label=['1', '2', '3', '4']
        sale_quarter_chart_xaxis_title=['Sale Quarter']
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 18:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(sale_quarter_chart_xaxis_title, msg="Step 18:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(sale_quarter_y_axis_label, msg="Step 18:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(sale_quarter_x_axis_label, msg="Step 18:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", msg="Step 18:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 28, "Step 18:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 1, msg="Step 18:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 18:08:")
        
        """
            Step 19 : Hover over any chart riser, Select "Drill up to Sale Year"
        """
        menu_path="Go up to Sale Year"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=chart_parent_run_css,move_to_tooltip=True)
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        
        """
            Step 20 : Verify the Chart drills up to Sale Year
        """
        sale_year_y_axis_label=['0', '100M', '200M', '300M', '400M', '500M']
        sale_year_x_axis_label=['2013', '2014', '2015', '2016', '2017','2018']
        sale_year_chart_xaxis_title=['Sale Year']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 20:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(sale_year_chart_xaxis_title, msg="Step 20:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(sale_year_y_axis_label, msg="Step 20:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(sale_year_x_axis_label, msg="Step 20:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", msg="Step 20:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step 20:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 42, 1, msg="Step 20:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 20:08:")
        
        """
            Step 21 : Hover over any chart riser, Select "Restore Original"
        """
        menu_path="Reset"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=chart_parent_run_css,move_to_tooltip=True)
        chart_obj.wait_for_number_of_element(total_riser_css, 84, medium_wait)
        
        
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 21:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 21:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 21:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 21:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 21:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 21:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 21:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 21:08:")
        
        """
            Step 22 : IBFS:/WFC/Repository/SmokeTest > Enter title as "Stacked Bar - Sales by Month and Product Category1" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
            Step 23 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 24 :     
            Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/~rsadv/Stacked_Bar_-_Sales_by_Month_and_Product_Category1.fex&tool=Chart
        """
        
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_after_save, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 7, long_wait)
        
        """
           Verify it restoredd successfully
        """ 
        
        preview_segment_css=".chartPanel .groupPanel rect[class^='riser']"
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 24:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 24:02: Verify chart color in preview')
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 24:03: Verify xaxis label")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, parent_css="#"+chart_parent_preview_css, msg="Step 24:04: Verify yaxis label")
        chart_obj.verify_number_of_chart_segment(chart_parent_preview_css, 7, "Step 24:05: Verify number of chart segments in preview", custom_css=preview_segment_css)
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 24:06:Verify x-axis title in preview")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, parent_css="#"+chart_parent_preview_css, msg="Step 24:07:Verify yaxis title in preview")
        chart_obj.verify_legends_in_preview(expected_preview_legend_list, msg="Step 24:08:")     
        
        """
            Step 25 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()