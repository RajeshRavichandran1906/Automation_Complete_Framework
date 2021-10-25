'''
Created on Sep 6, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275862&group_by=cases:section_id&group_order=asc&group_id=170569
TestCase Name : Verify to Run and Edit 'Stacked Bar - Units Sold by Stores vs Web (Animation)'
'''
import unittest
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C2275862_TestClass(BaseTestCase):

    def test_C2275862(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
    
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 90
        long_wait= 300
        username= 'mrid'
        password= 'mrpass'
        fex_name='Units_Sold_by_Stores_vs_Web_Over_time'
        new_fex_name='Stacked Bar - Units Sold by Stores vs Web1'
        reopen_fex_after_save='Stacked_Bar_-_Units_Sold_by_Stores_vs_Web1'
        folder_name='Retail_Samples/Charts'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Store Type', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis', 'Sale,Month', 'Marker', 'Color BY', 'Product,Category', 'Size', 'Tooltip', 'Multi-graph', 'Animate', 'Sale,Year']
        
        chart_yaxis_title=['Quantity Sold']
        chart_xaxis_title=['Sale Month']
        y_axis_label=['0', '4K', '8K', '12K', '16K', '20K']
        x_axis_label=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        preview_chart_y_axis_label=['0', '40', '80', '120', '160', '200']
        preview_chart_x_axis_label=['1']
        expected_column_header_label=['Store Type', 'Store Front']
        expected_label_list=['2013', '2014', '2015', '2016', '2017', '2018']
        filter_field='Sale,Year Greater than or equal to 2012'
        col_label_in_preview=['Store Type', 'Web']
        expected_preview_slider_labels=['2014']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        chart_parent_preview_css= 'TableChart_1'
        total_riser_css_with_tagname=" rect[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        chart_color_css="[class='riser!s0!g0!mbar!r0!c0!']" 
        sale_month_seventh_riser_css="riser!s4!g6!mbar!r0!c0!"
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        yaxis_label_css="[class^='yaxis-labels']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Units_Sold_by_Stores_vs_Web_Over_time.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password,run_chart_css=total_riser_css, no_of_element=84)
        
        """
            Step 03 : Verify the following Bar Chart with Animation slider 
        """
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 03:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 03:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 03:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 03:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 03:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 03:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 03:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 03:08:")
        chart_obj.verify_column_label_in_run_window(expected_column_header_label, msg="Step 03:09:")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list, "Step 03:10:Verify slider labels")
        
        """
            Step 04 : Hover over chart riser for the Sale month '7', Verify the tooltip
        """
        expected_tooltip_list=['Store Type:Store Front', 'Sale Year:2013', 'Sale Month:7', 'Quantity Sold:3,675', 'Product Category:Stereo Systems']
        msg="Step 04: Verify Sale Month 7 th tooltip values"
        parent_css="#"+chart_parent_run_css
        chart_obj.verify_tooltip_in_run_window(sale_month_seventh_riser_css, expected_tooltip_list, msg=msg, parent_css=parent_css)
        
        """
            Step 05 : Drag the slider from 2013 to 2014
        """
        slider_value_to_select='2014'
        chart_obj.move_chart_slider_in_run_window(slider_value_to_select)
        y_axis_value_2014=['0', '4K', '8K', '12K', '16K', '20K']
        x_axis_value_2014=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        exp_column_header_label=['Store Type', 'Store Front', 'Web']
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 05:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 05:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_value_2014, msg="Step 05:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_value_2014, xyz_axis_label_length=1, msg="Step 05:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", msg="Step 05:05: Verify stacked bar chart color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 168, "Step 05:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 6, msg="Step 05:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 05:08:")
        chart_obj.verify_column_label_in_run_window(exp_column_header_label, msg="Step 05:09:")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list, "Step 05:10:Verify slider labels")
        
        """
            Step 06 : Hover over any chart riser, Verify the tooltip
        """
        riser_css="riser!s4!g10!mbar!r0!c0!"
        msg="Step 04: Verify Sale Month 7 th tooltip values"
        parent_css="#"+chart_parent_run_css
        expected_tooltip_list=['Store Type:Store Front', 'Sale Year:2014', 'Sale Month:11', 'Quantity Sold:5,807', 'Product Category:Stereo Systems']
        chart_obj.verify_tooltip_in_run_window(riser_css, expected_tooltip_list, msg=msg, parent_css=parent_css)
        
        """
            Step 07 : Click the "play" button (on the slider)
        """
        
        chart_obj.click_chart_animate_button()
        
        """
            Step 08 : Verify the slider moves from 2014 to 2018 (Animate is working)
            y_axis_label_2015=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
            y_axis_label_2016=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K', '40K']
            y_axis_label_2017=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
            
        """
#         chart_obj.verify_number_of_y_axis_labels(6, "Step 07:01:Verify number of y_axis labels")
#         chart_obj.verify_number_of_y_axis_labels(8, "Step 07:02:Verify number of y_axis labels")
#         chart_obj.verify_number_of_y_axis_labels(9, "Step 07:03:Verify number of y_axis labels")
#         chart_obj.verify_number_of_y_axis_labels(8, "Step 07:04:Verify number of y_axis labels")
        
        chart_obj.wait_for_number_of_element(yaxis_label_css, 8, medium_wait)
        y_axis_label_2018=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        x_axis_value_2018=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 6, msg="Step 08:01: Verify number of risers in 2014 slider selection")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 08:02: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_label, msg="Step 08:03:")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list, "Step 08:04: Verify slider labels")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 168, "Step 08:05: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", msg="Step 08:06: Verify stacked bar chart color")
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 08:07: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 08:08: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label_2018, msg="Step 08:09: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_value_2018, xyz_axis_label_length=1, msg="Step 08:10: ")
        
        chart_obj.verfiy_animate_end_position()
        
        """
            Step 09 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 168, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 168, "Step 05: Verify number of chart segments")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 168, medium_wait)
        chart_obj.api_logout()
        
        """
            Step 10 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Units_Sold_by_Stores_vs_Web_Over_time.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 7, long_wait)
        
        """
            Step 11 : Verify the following Query Pane,Filter Pane and Chart in Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 11:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 11:02: Verify chart color in preview')
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 11:03: Verify filter pane field is available in filterbox")
        chart_obj.verify_column_label_in_preview(col_label_in_preview, msg="Step 11:04: ")
        chart_obj.verify_number_of_risers(preview_riser_css, 7, 1, msg="Step 11:05:")
        chart_obj.verify_legends_in_preview(expected_legend_list, msg="Step 11:06: ")
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, msg="Step 11:07: ")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, msg="Step 11:08: ")
        chart_obj.verify_slider_labels_in_preview(expected_preview_slider_labels, "Step 11:09: Verify slider labels")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, msg="Step 11:10: ")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, msg="Step 11:11: ")
        
        """
           Step 12 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(total_riser_css, 84, medium_wait)
        
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 12:01: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 12:02: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, msg="Step 12:03: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_label, msg="Step 12:04: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", attribute='fill', msg="Step 12:05: Verify line color")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 84, "Step 12:06: Verify number of chart segments in run window")
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 3, msg="Step 12:07: Verify number of risers")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 12:08:")
        chart_obj.verify_column_label_in_run_window(expected_column_header_label, msg="Step 12:09:")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list, "Step 12:10:Verify slider labels")
        
        """
            Step 13 : Click the "play" button (on the slider)
        """
        chart_obj.click_chart_animate_button()
        chart_obj.wait_for_number_of_element(yaxis_label_css, 8, medium_wait)
        y_axis_label_2018=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        x_axis_value_2018=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        chart_obj.verify_number_of_risers("#"+chart_parent_run_css+" rect", 28, 6, msg="Step 13:01: Verify number of risers in 2014 slider selection")
        chart_obj.verify_legends_in_run_window(expected_legend_list, msg="Step 13:02: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_label, msg="Step 13:03:")
        chart_obj.verify_slider_labels_in_run_window(expected_label_list, "Step 13:04: Verify slider labels")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 168, "Step 13:05: Verify number of chart segments in run window")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(chart_color_css, "bar_blue", msg="Step 13:06: Verify stacked bar chart color")
        chart_obj.verify_y_axis_title_in_run_window(chart_yaxis_title, msg="Step 13:07: Verify y-axis title")
        chart_obj.verify_x_axis_title_in_run_window(chart_xaxis_title, msg="Step 13:08: Verify x-axis label")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label_2018, msg="Step 13:09: Verify x-axis label")
        chart_obj.verify_x_axis_label_in_run_window(x_axis_value_2018, xyz_axis_label_length=1, msg="Step 13:10: ")
        
        """
            Step 14 : Click IA > Save> Select "SmokeTest" folder > Enter title as "Stacked Bar - Units Sold by Stores vs Web1" > Click Save
            Verify the Chart is saving under Mycontent folder
        """
        chart_obj.switch_to_default_content()
        chart_obj.wait_for_number_of_element(application_css, 1, medium_wait)
        chart_obj.save_as_from_application_menu_item(new_fex_name)
        
        """
            Step 15 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
            Step 16 : Edit the saved chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Stacked_Bar_-_Units_Sold_by_Stores_vs_Web1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_after_save, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 7, long_wait)
        
        """ Verify it restored successfully without any error"""
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 16:01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 16:02: Verify chart color in preview')
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 16:03: Verify filter pane field is available in filterbox")
        chart_obj.verify_column_label_in_preview(col_label_in_preview, msg="Step 16:04: ")
        chart_obj.verify_number_of_risers(preview_riser_css, 7, 1, msg="Step 16:05:")
        chart_obj.verify_legends_in_preview(expected_legend_list, msg="Step 16:06: ")
        chart_obj.verify_x_axis_title_in_preview(chart_xaxis_title, msg="Step 16:07: ")
        chart_obj.verify_y_axis_title_in_preview(chart_yaxis_title, msg="Step 16:08: ")
        chart_obj.verify_slider_labels_in_preview(expected_preview_slider_labels, "Step 16:09: Verify slider labels")
        chart_obj.verify_x_axis_label_in_preview(preview_chart_x_axis_label, msg="Step 16:10: ")
        chart_obj.verify_y_axis_label_in_preview(preview_chart_y_axis_label, msg="Step 16:11: ")
        
        """
            Step 17 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()