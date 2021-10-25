'''
Created on Aug 31, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275856&group_by=cases:section_id&group_order=asc&group_id=170569
Testcase Name : Verify to Run and Edit 'Pie Matrix - Quantity By Region'
'''
import unittest
from common.wftools import chart
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2275856_TestClass(BaseTestCase):

    def test_C2275856(self):
        
        driver = self.driver
        chart_obj = chart.Chart(driver)
        visual_obj=visualization.Visualization(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        medium_wait= 60
        long_wait= 300
        username= 'mrid'
        password= 'mrpass'
        fex_name='Pie_Matrix_Quantity_By_Region'
        new_fex_name='Pie Matrix - Quantity By Region1'
        reopen_fex_after_save='Pie_Matrix_-_Quantity_By_Region1'
        folder_name='Retail_Samples/Charts'
        fex_folder_after_save='SmokeTest/~rsadv'
        
        query_field_list=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Sale,Year', 'Columns', 'Product,Category', 'Metric', 'Measure', 'Quantity,Sold', 'Color', 'Store,Business,Region', 'Size', 'Revenue', 'Tooltip', 'Multi-graph', 'Animate'] 
        preview_chart_pie_label=['1']
        
        expected_pie_lebels=['46,735', '41,250', '19,820', '66,307', '100K', '8,371', '17,932', '63,836', '56,782', '34,626', '92,435', '139K', '11,542', '25,032']
        expected_row_header_title_list=['Sale Year','2015','2016']
        expected_column_header_title_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        filter_field='Sale,Year Equal to 2015 or 2016'
        expected_legends_list=['Store Business Region', 'EMEA', 'North America', 'South America', 'Revenue', '36.6M', '16.4M', '4.2M']
        expected_lengend_list_after_drilldown=['Store Business Sub Region', 'Asia', 'Europe']
        expected_row_header_title_list_after_drilldown=['Sale Year','2015']
        
        expected_column_header_title_list_after_drilldown=['Product Category', 'Stereo Systems']
        expected_pie_labels_list=['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold']
        drill_down_pie_ring_label=['57,364']
        drilldown_chart_pielabel=['Quantity Sold']
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css= 'jschart_HOLD_0'
        frame_css="iframe[src]"
        parent_css_with_tag_name="#"+chart_parent_run_css+" path"
#         riser_css="[class='riser!s0!g0!mwedge!r0!c4!']"
        riser_css= "[class='riser!s0!g0!mwedge!']"
        
        chart_parent_preview_css= 'TableChart_1'
        total_riser_css_with_tagname=" path[class^='riser!']"
        total_riser_css= "#"+chart_parent_run_css+total_riser_css_with_tagname
        iframe_css= '#resultArea [id^=ReportIframe-]'
        application_css= '#applicationButton'
        chart_color_css="[class='riser!s0!g0!mwedge!r0!c0!']"
        preview_riser_css="#"+chart_parent_preview_css+total_riser_css_with_tagname
        pie_label_css="[class^='totalLabel']"
        css1='riser!s0!g0!mwedge!r0!c4!'
        css2='riser!s0!g0!mwedge!r0!c0!'
        drilldown_chart_riser_css="[class='riser!s0!g0!mwedge!r0!c0!']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Chart using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FRetail_Samples/Charts&BIP_item=Pie_Matrix_Quantity_By_Region.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=frame_css)
        chart_obj.switch_to_frame(frame_css=frame_css)
         
        """
            Step 03 : Verify the following Pie Chart
        """
        chart_obj.verify_legends_in_run_window(expected_legends_list, msg="Step 03.01")
        chart_obj.verify_rows_label_in_run_window(expected_row_header_title_list, msg="Step 03.02")
        chart_obj.verify_column_label_in_run_window(expected_column_header_title_list, msg="Step 03.03")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step 03.04:")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, "Step 03.05: Verify number of risers at runtime in matrx chart")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'bar_blue', msg="Step 03.06:")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_labels_list, msg='Step 03.07: ')
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_lebels, label_css=pie_label_css, msg="Step 03.07:")
#         chart_obj.verify_legends_in_run_window(expected_legends_list, msg="Step 03:05: Verify expected legends at runtime")
         
        """
            Step 04 : Hover over on Pie chart "100K" > "Drill down to"
        """
        msg="Step 04.01: Verify ringpie chart tooltip values"
        expected_tooltip_list=['Sale Year:2015', 'Product Category:Stereo Systems', 'Store Business Region:EMEA', 'Quantity Sold:57,364  (57.21%)', 'Revenue:$14,986,027.58', 'Drill down to']
        chart_obj.verify_tooltip_in_run_window(css1, expected_tooltip_list, msg, element_location='middle_right', move_to_tooltip=True)
         
        """
            Step 05 : Click "Store Business Sub Region"
        """
        visual_obj.select_tooltip(css1, "Drill down to->Store Business Sub Region",parent_css=chart_parent_run_css,element_location="middle_right",move_to_tooltip=True)
        #chart_obj.wait_for_number_of_element("[class^='riser']", 2, long_wait)
        chart_obj.wait_for_visible_text(pie_label_css, "57,364", time_out = 180)
          
        """
            Step 06 : Verify it drills down to "Store Business Sub Region"
        """
        chart_obj.verify_pie_label_in_single_group_in_run_window(drill_down_pie_ring_label, label_css=pie_label_css, msg="Step 06.01:")
        chart_obj.verify_legends_in_run_window(expected_lengend_list_after_drilldown, msg="Step 06.02:")
        chart_obj.verify_rows_label_in_run_window(expected_row_header_title_list_after_drilldown, msg="Step 06.03: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_title_list_after_drilldown, msg="Step 06.04:")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 2, "Step 06.05:")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, "Step 06.06: Verify number of risers at runtime in chart")
        chart_obj.verify_pie_label_in_single_group_in_run_window(drilldown_chart_pielabel, msg="Step 06.07:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(drilldown_chart_riser_css, 'bar_blue', msg="Step 06.08:")
         
        """
            Step 07 : Hover over on "Asia" area > "Drill down to" > Click "Store Country"
        """
        visual_obj.select_tooltip(css2, "Drill down to->Store Country",parent_css=chart_parent_run_css,element_location="middle",move_to_tooltip=True)
        chart_obj.wait_for_visible_text(pie_label_css, '2,802', long_wait)
#         chart_obj.wait_for_number_of_element("[class^='riser']", 14, long_wait)
         
        """
            Step 08 : Verify the chart drills down to "Store Country"
        """
        drill_down_pie_ring_label=['2,802']
        expected_lengend_list_after_drilldown=['Store Country', 'Israel','Singapore']
        chart_obj.verify_pie_label_in_single_group_in_run_window(drill_down_pie_ring_label, label_css=pie_label_css, msg="Step 08.01:")
        chart_obj.verify_legends_in_run_window(expected_lengend_list_after_drilldown, msg="Step 08.02:")
        chart_obj.verify_rows_label_in_run_window(expected_row_header_title_list_after_drilldown, msg="Step 08.03: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_title_list_after_drilldown, msg="Step 08.04:")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 2, "Step 08.05:")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 2, "Step 08.06: Verify number of risers at runtime in chart")
        chart_obj.verify_pie_label_in_single_group_in_run_window(drilldown_chart_pielabel, msg="Step 08.07:")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(drilldown_chart_riser_css, 'bar_blue', msg="Step 08.08:")
         
        """
            Step 09 : Hover over anywhere on Pie chart, Click "Restore Original"
        """
        visual_obj.select_tooltip(css2, "Restore Original",parent_css=chart_parent_run_css,element_location="middle_right",move_to_tooltip=True)
        chart_obj.wait_for_visible_text("#jschart_HOLD_0", "Computers", time_out = 180)
         
        """
            Step 10 : Verify the Pie chart restored back to original
        """
        chart_obj.verify_legends_in_run_window(expected_legends_list, msg="Step 10.01:")
        chart_obj.verify_rows_label_in_run_window(expected_row_header_title_list, msg="Step 10.02: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_title_list, msg="Step 10.03:")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step 10.04:")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, "Step 10.05: Verify number of risers at runtime in matrx chart")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'bar_blue', msg="Step 10.06:")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_labels_list, msg='Step 10.07: ')
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_lebels, label_css=pie_label_css, msg="Step 10.08:")
         
         
        """
            Step 11 : Resize the browser window and verify it does not throws any error message
        """
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step 11.01: Verify number of chart segments")
        chart_obj.maximize_browser()
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        chart_obj.api_logout()
        
        """
            Step 12 : Edit the Chart using "rsadv" with the below API URL
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Pie_Matrix_Quantity_By_Region.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 1, long_wait)
        
        """
            Verify the following Query Pane,Filter Pane and Chart in Live Preview
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 12.01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 12.02: Verify chart color in preview')
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 12.03: Verify filter pane field is available in filterbox")
        chart_obj.verify_rows_label_in_preview(expected_row_header_title_list_after_drilldown, msg="Step 12.04")
        chart_obj.verify_column_label_in_preview(expected_column_header_title_list_after_drilldown, msg="Step 12.05")
        chart_obj.verify_pie_label_in_single_group_in_preview(drilldown_chart_pielabel, msg="Step 12.06:")
        chart_obj.verify_pie_label_in_single_group_in_preview(preview_chart_pie_label,label_css=pie_label_css, msg="Step 12.07:")
        chart_obj.verify_number_of_risers(preview_riser_css, 1, 1, msg="Step 12.08:")
        
        """
            Step 13 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.wait_for_number_of_element(iframe_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.switch_to_frame(frame_css=frame_css)
        chart_obj.wait_for_number_of_element(total_riser_css, 42, medium_wait)
        
        chart_obj.verify_legends_in_run_window(expected_legends_list, msg="Step 13.01:")
        chart_obj.verify_rows_label_in_run_window(expected_row_header_title_list, msg="Step 13.02: ")
        chart_obj.verify_column_label_in_run_window(expected_column_header_title_list, msg="Step 13.03:")
        chart_obj.verify_number_of_chart_segment(chart_parent_run_css, 42, "Step 13.04:")
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, "Step 13.05: Verify number of risers at runtime in matrx chart")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'bar_blue', msg="Step 13.06:")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_labels_list, msg='Step 13.07: ')
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_lebels, label_css=pie_label_css, msg="Step 13.08:")
        chart_obj.verify_legends_in_run_window(expected_legends_list, msg="Step 13.09: Verify expected legends at runtime")
        
        """
            Step 14 : Click IA > Save> Select "SmokeTest" folder > Enter title as "Pie Matrix - Quantity By Region1" > Click Save
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
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Pie_Matrix_-_Quantity_By_Region1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(fex_folder_after_save, fex_name=reopen_fex_after_save, mrid=username, mrpass=password)
        chart_obj.wait_for_number_of_element(preview_riser_css, 1, long_wait)
        
        """
            Verify it restored successfully without any error
        """
        chart_obj.verify_all_fields_in_query_pane(query_field_list, "Step 16.01: Verify the Query panel in preview")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(chart_color_css, "bar_blue", parent_css="#"+chart_parent_preview_css, msg='Step 16.02: Verify chart color in preview')
        chart_obj.verify_filter_pane_field(filter_field, 1, "Step 16.03: Verify filter pane field is available in filterbox")
        chart_obj.verify_rows_label_in_preview(expected_row_header_title_list_after_drilldown, msg="Step 16.04")
        chart_obj.verify_column_label_in_preview(expected_column_header_title_list_after_drilldown, msg="Step 16.05")
        chart_obj.verify_pie_label_in_single_group_in_preview(drilldown_chart_pielabel, msg="Step 16.06:")
        chart_obj.verify_pie_label_in_single_group_in_preview(preview_chart_pie_label,label_css=pie_label_css, msg="Step 16.07:")
        chart_obj.verify_number_of_risers(preview_riser_css, 1, 1, msg="Step 16.08:")
        
        """
            STep 17 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
   

if __name__ == "__main__":
    unittest.main()