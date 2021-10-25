'''
Created on Jul 26, 2018

@author: BM13368
TestCase ID :http://172.19.2.180/testrail/index.php?/cases/view/2275847
TestCase Name :Verify to Run and Edit 'Sales Metrics YTD'
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import active_chart, active_report

 
class C2275847_TestClass(BaseTestCase):
 
    def test_C2275847(self):
         
        Test_Case_ID = "C2275847"
        report_obj=report.Report(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
         
        fex_name="Sales_Metrics_YTD"
        edit_fex_name="Sales_Metrics_YTD1"
        save_fex_name="Sales Metrics YTD1"
        folder_name="Retail_Samples/Reports"
        saved_fex_foldername="SmokeTest/~rsadv"
        
        wall1_window_text='Gross Profit by Product Category'
        wall2_window_text="Revenue by Product Category" 
        filter_wall_text='Filter Selection'
        
        report_row_value_runtime="$157,883.00" 
        sort_ascending_row_value='$188,390.38'
        after_filter_computers_row_value='1,442'
        preview_report_data_value=28
        row_two_val="$304,830.00"
        
        active_chart_title_runtime="Gross Profit by Product Category"
        expected_activebar_title=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        expected_xaxis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_label_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        expected_legend_list=['Gross Profit']
        
        expected_active_stacked_bar_title=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        expected_stacked_bar_xaxis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_stacked_bar_yaxis_label_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M']
        expected_stacked_bar_legend_list=['Revenue']
        
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Gross Profit', 'Revenue', 'Cost of Goods', 'Quantity,Sold', 'By', 'Product,Category', 'Product,Subcategory', 'Model', 'Across']
        filter_field_name1 = "Sale,Year Equal to 2016"
        preview_expected_title_list=['ProductCategory', 'ProductSubcategory', 'Model', 'Gross Profit', 'Revenue', 'Cost of Goods', 'QuantitySold']
        preview_expected_subtotal_row=['Subtotal: Media Player', '', '', '$42.98', '$662.98', '$620.00']
        preview_report_header_footer_title=['Sales Metrics YTD']
        
        long_time=240
        medium_time=60
        
        "-------------------------------------------------------------------CSS--------------------------------------------------------------------------"
        table_css="ITableData0"
        wall1_dialog_css="wall1"
        wall2_dialog_css="wall2"
        chart_rollup_tool_table_id="charttoolt1"
        preview_report_css="TableChart_1"
        
        report_runtime_row_value_css="#"+table_css+" tbody tr[id='I0r0.0'] td[id='I0r0.0C3']"
        sort_ascending_row_css="#"+table_css+" tbody tr[id='I0r1.0'] td[id='I0r0.0C4']"
        after_filter_computer_css="#"+table_css+" tbody tr[id='I0r0.0'] td[id='I0r0.0C6']"
        runtime_subtotal_css="#"+table_css+" tbody tr:nth-child({0}) td[id^='THEAD']:nth-child({1})"
        
        wall1_window_css= "#"+wall1_dialog_css+" .arWindowBarTitle"
        wall2_window_css="#"+wall2_dialog_css+" .arWindowBarTitle"
        
        preview_report_data_css="#"+preview_report_css+" div[class^='x']"
        frame_css="#resultArea [id^=ReportIframe-]"
        riser_css="[class='riser!s0!g4!mbar!']"
        table_row_val_css="#"+table_css+" > tbody > tr:nth-child({0}) td:nth-child({1})"
        application_css="#applicationButton"
        no_of_rows="#"+table_css+" > tbody > tr"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
            Step 01:Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports&BIP_item=Sales_Metrics_YTD.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', run_table_css=no_of_rows,no_of_element=28,wait_time=300)
   
        """
            Step 03: Verify the output with AHTML format
            Verify the background color for Subtotal : Accessories
        """
        active_report_obj.verify_page_summary('0','101of101records,Page1of5', 'Step 02:02: Verify Page summary')
#         report_obj.create_table_data_set("#ITableData0",Test_Case_ID+"_Ds01.xlsx")
        report_obj.verify_table_data_set("#"+table_css,Test_Case_ID+"_Ds01.xlsx","Step x: Verify report table")
              
        """
            Step 04 : Click 'Gross Profit' dropdown
            Step 05 : Hover over Chart > Column > Product Category
        """
        active_report_obj.select_menu_items(table_css, 3, 'Chart', 'Column', 'Product Category')
        report_obj.wait_for_visible_text(wall1_window_css, wall1_window_text, medium_time)
              
        """
            Step 06 :Verify the following Chart is displayed  
        """
        active_chart_obj.verify_chart_title(active_chart_title_runtime, msg='Step 06:01:Verify active chart title', parent_css="#"+wall1_dialog_css)
        active_chart_obj.verify_active_chart_toolbar(expected_activebar_title, msg='Step 06:02: Verify active chart toolbar items', parent_css="#"+wall1_dialog_css)
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 14, 1, parent_css="#"+wall1_dialog_css, msg='Step 06:03: Verify number of risers')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xaxis_label_list, parent_css="#"+wall1_dialog_css, msg='Step 06:04:Verify xaxis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_yaxis_label_list, parent_css="#"+wall1_dialog_css, msg="Step 06:05:Verify yaxis labels")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list, parent_css="#"+wall1_dialog_css, msg='Step 06:06:Verify legends')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'chelsea_cucumber1', parent_css="#"+wall1_dialog_css, msg="Step 06:07:Verify riser color")
              
        """
            Step 07 : Close the Chart window
        """
        active_chart_obj.close_active_chart_popup_dialog('1')
        time.sleep(4)
              
        """
            Step 08 : Click Revenue dropdown > Select "Sort Ascending"
        """
        active_report_obj.select_menu_items(table_css, 4, 'Sort Ascending')
        report_obj.wait_for_visible_text(sort_ascending_row_css, sort_ascending_row_value, medium_time)
              
        """
            Step 09 : Verify the following Report gets sorted in Ascending order
        """
#         report_obj.create_table_data_set("#ITableData0",Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_table_data_set("#"+table_css,Test_Case_ID+"_Ds02.xlsx","Step 08:01: Verify report table whether it shown the data in ascending order")
           
        """
            Step 10 : Click "Quantity Sold" dropdown > Select "Visualize"
        """
        active_report_obj.select_menu_items(table_css, 6, 'Visualize')
        time.sleep(10)
        active_report_obj.verify_visualize_bar_added_in_activereport("#ITableData0", 6, 'green', "Step 10:01:Verify visualize bar is shown in green color")
           
        """
            Step 11 :     
            Click "Cost of Goods" dropdown > Select "Chart/Rollup Tool"
        """
        active_report_obj.select_menu_items(table_css, 5, 'Chart/Rollup Tool')
        report_obj.wait_for_number_of_element("#"+chart_rollup_tool_table_id, 1, medium_time)
           
        """
            Step 12 : Drag and drop 'Product Category' to Group By and Drag an drop 'Revenue' to Measure
        """
        active_chart_obj.chart_rollup_tool_drag_drop_items(chart_rollup_tool_table_id, 'Columns', 'Product Category', 1, 'Group By', 0)
        time.sleep(2)
        active_chart_obj.chart_rollup_tool_drag_drop_items(chart_rollup_tool_table_id, 'Columns', 'Revenue', 1, 'Measure', 0)
           
        """
            Step 13 : Click Charts button (Next to Series) > Select Stacked Bar > Click OK
        """
        active_chart_obj.select_advance_chart(wall1_dialog_css, 'stackedbar')
        report_obj.wait_for_visible_text(wall2_window_css, wall2_window_text, medium_time)
           
        """
            Step 14 : Verify the following Chart output is displayed
        """
        active_chart_obj.verify_chart_title('Revenue by Product Category', msg='Step 14:01:Verifyactive chart title', parent_css="#"+wall2_dialog_css)
        active_chart_obj.verify_active_chart_toolbar(expected_active_stacked_bar_title, msg='Step 14:02: Verify active chart toolbar items', parent_css="#"+wall2_dialog_css)
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 14, 1, parent_css="#"+wall2_dialog_css, msg='Step 14:03: Verify number of risers')
        active_chart_obj.verify_x_axis_label_in_run_window(expected_stacked_bar_xaxis_label_list, parent_css="#"+wall2_dialog_css, msg='Step 14:04:Verify xaxis labels')
        active_chart_obj.verify_y_axis_label_in_run_window(expected_stacked_bar_yaxis_label_list, parent_css="#"+wall2_dialog_css, msg="Step 14:05:Verify yaxis labels")
        active_chart_obj.verify_legends_in_run_window(expected_stacked_bar_legend_list, parent_css="#"+wall2_dialog_css, msg='Step 14:06:Verify legends')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(riser_css, 'chelsea_cucumber1', parent_css="#"+wall2_dialog_css, msg="Step 14:07:Verify riser color")
           
        """
            Step 15 : Close the Chart window
        """
        active_chart_obj.close_active_chart_popup_dialog('2')
        time.sleep(5)
           
        """
            Step 16 :    
            Click "Product Category" dropdown > Select Filter > Equals
        """
        active_report_obj.select_menu_items(table_css, 0, 'Filter','Equals')
        report_obj.wait_for_visible_text(wall1_window_css, filter_wall_text, medium_time)
           
        """
            Step 17 : Click dropdown next to Equals > Select Computers
            Step 18 : Click Filter button (Move the filter window towards right to view output)
        """
        active_report_obj.create_filter(1, 'Equals', value1="Computers")
        active_report_obj.filter_button_click('Filter')
        report_obj.wait_for_visible_text(after_filter_computer_css, after_filter_computers_row_value, medium_time)
           
        """
            Verify the selected Computers report is displayed 
        """
        active_report_obj.verify_page_summary('0','7of101records,Page1of1', 'Step 18:01: Verify Page summary')
#         report_obj.create_table_data_set("#ITableData0",Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_table_data_set("#"+table_css,Test_Case_ID+"_Ds03.xlsx","Step 18:02: Verify the selected Computers report is displayed")
          
        active_report_obj.verify_visualize_bar_added_in_activereport("#"+table_css, 6, 'green',"Step 18:03: Verify visualize is added in the report")
           
        """
            Step 19 : Click close (x)
        """
        active_report_obj.close_filter_dialog()
        time.sleep(2)
           
        """
            Verify Filter Selection window is disappeared
        """
        utillobj.verify_object_visible("#"+wall1_dialog_css, False, "Step 19:01:Verify filter popup is disappeared")
               
        """
            Step 20 : Click Model dropdown > Select Restore Original
        """
        active_report_obj.select_menu_items(table_css,2,'Restore Original')
        report_obj.wait_for_visible_text(report_runtime_row_value_css, report_row_value_runtime, medium_time)
           
        """
            Step 21 :     
            Verify the Report is restored back to original
        """
        active_report_obj.verify_page_summary('0','101of101records,Page1of5', 'Step 02:02: Verify Page summary')
        report_obj.verify_table_data_set("#"+table_css,Test_Case_ID+"_Ds01.xlsx","Step x: Verify report table")
           
        """
            Step 22 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.set_browser_window_size()
        report_obj.verify_table_cell_property(2, 2, table_css=table_row_val_css.format(3,5), font_color='black', text_value=row_two_val, msg="Step 22:01: Verify background color for 304,830,00")
           
        """
            Step 23 :      
            Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        self.driver.maximize_window()
        
        """
            Step 24 : Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Sales_Metrics_YTD.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name=fex_name,folder_name=folder_name)
        report_obj.wait_for_number_of_element(preview_report_data_css, preview_report_data_value, long_time)
         
        """
            Verify report in IA tool
            Step 25 : Verify the following Query panel,Filter Panel and Report output in Live Preview
        """
        
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 25:01: Verify the Query panel")
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 25:02: Verify the filter panel first field")
        report_obj.verify_column_title_on_preview(7, 14, table_id=preview_report_css, expected_list=preview_expected_title_list, msg='Step 25:03: Verify report preview titles')
        
        table_elems=self.driver.find_elements_by_css_selector(preview_report_data_css)
        table_items=[i.text.strip() for i in table_elems]
        act_subtotal_row=table_items[21:-1]
        utillobj.asequal(preview_expected_subtotal_row,act_subtotal_row,"Step 25:04:Verify subtotal row values for Media Player field")
        
#         report_obj.create_report_data_set_in_preview('TableChart_1', 4, 7, Test_Case_ID+"_Ds04.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css, 4, 7, Test_Case_ID+"_Ds04.xlsx", "Step 25:05: Verify report data in preview")
        report_obj.verify_report_header_footer_title_in_preview(preview_report_header_footer_title, msg="Step 25:06:Verify report title in preview report")
          
        """
            Step 26 : Click Run
            Verify the Report run successfully
            Verify the background color for Subtotal : Accessories
        """
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.wait_for_number_of_element(frame_css, 1, medium_time)
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(report_runtime_row_value_css, report_row_value_runtime, medium_time)
        
        subtotal_value="Subtotal Accessories"
        report_obj.verify_table_cell_property(17, 1, runtime_subtotal_css.format(17,1), bg_color='saltpan', text_vlue=subtotal_value, msg="Step 26:01: Verify back ground color for Subtotal Accessories")
        
        """
            Step 27 : Click IA > Save As> Select "SmokeTest" > MYContent folder > Enter title as "Sales Metrics YTD1" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.wait_for_number_of_element(application_css, 1, medium_time)
        report_obj.save_as_from_application_menu_item(save_fex_name, target_table_path = 'SmokeTest->My Content')
        
        """
            Step 28 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
            Step 29 :     
            Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Sales_Metrics_YTD1.fex&tool=Report
        """
        
        report_obj.edit_fex_using_api_url(fex_name = edit_fex_name, folder_name = saved_fex_foldername)
        report_obj.wait_for_number_of_element(preview_report_data_css, preview_report_data_value, long_time)
        
        """
            Verify it restored successfully without any error
        """
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 29:01: Verify the Query panel")
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 29:02: Verify the filter panel first field")
        report_obj.verify_column_title_on_preview(7, 14, table_id=preview_report_css, expected_list=preview_expected_title_list, msg='Step 29:03: Verify report preview titles')
        
        table_elems=self.driver.find_elements_by_css_selector(preview_report_data_css)
        table_items=[i.text.strip() for i in table_elems]
        act_subtotal_row=table_items[21:-1]
        utillobj.asequal(preview_expected_subtotal_row,act_subtotal_row,"Step 29:04:Verify subtotal row values for Media Player field")
        
#         report_obj.create_report_data_set_in_preview('TableChart_1', 4, 7, Test_Case_ID+"_Ds04.xlsx")
        report_obj.verify_report_data_set_in_preview(preview_report_css, 4, 7, Test_Case_ID+"_Ds04.xlsx", "Step 29:05: Verify report data in preview")
        report_obj.verify_report_header_footer_title_in_preview(preview_report_header_footer_title, msg="Step 29:06:Verify report title in preview report")
        
        
        """
            Step 30 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()