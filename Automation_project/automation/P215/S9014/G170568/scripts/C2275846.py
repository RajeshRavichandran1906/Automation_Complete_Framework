'''
Created on Jul 24, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275846&group_by=cases:section_id&group_order=asc&group_id=170568
TestCase Name : Verify to Run and Edit 'Quantity Sold By Stores'
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_report

class C2275846_TestClass(BaseTestCase):

    def test_C2275846(self):
        
        Test_Case_ID = "C2275846"
        report_obj=report.Report(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        
        fex_name="Quantity_Sold_By_Stores"
        edit_fex_after_save="Quantity_Sold_By_Stores1"
        save_fex_name1="Quantity Sold By Stores1"
        folder_name="Retail_Samples/Reports"
        saved_fex_foldername="SmokeTest/~rsadv"
        
        """
            Step 01 :   
            Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports&BIP_item=Quantity_Sold_By_Stores.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', run_table_css='#ITableData0')
        css="#ITableData0 table tbody tr:nth-child(1) td[id='TCOL_0_C_1']"
        report_obj.wait_for_visible_text(css, "Store Name", time_out=50)
         
        """
            Verify the Report output with AHTML format and hyperlink displayed
            Verify first row value of Report output
            Scrolldown to see the full report and verify total no of records and page details
        """
        active_report_obj.verify_no_of_autolinks_in_activereport("#ITableData0", 1, 57, "Step 02:01: verify autolinks are available in the report")
        active_report_obj.verify_page_summary('0','86of86records,Page1of2', 'Step 02:02: Verify Page summary')
           
        """
            Step 03: Click New York , Verify the menus
        """
#         active_report_obj.create_data_set_using_table_rowid("ITableData0", "I0r", Test_Case_ID+"_Ds01.xlsx")
        active_report_obj.verify_data_set_using_table_rowid("ITableData0", "I0r", Test_Case_ID+"_Ds01.xlsx", "Step 03:01 Verify report data")
  
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 2, 'light_gray', "Step 03:02: Verify Visualization is present in the report")
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 3, 'light_gray', "Step 03:03: Verify Visualization is present in the report")
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 4, 'light_gray', "Step 03:04: Verify Visualization is present in the report") 
         
        """
            Step 04 :Hover over Auto link, verify the menus
            Step 05 :Click "Report - Store Product Metrics"
        """
        active_report_obj.select_activereport_field_menu_items('ITableData0', 8, 1, "New York->Auto Links")
#         expected_menu_list=['Gross_Profit_by_Sale_Year1', 'Gauge - Gross Profit by Sale Year', 'Report - Store Product Metrics']
        expected_menu_list=['Auto Links', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        active_report_obj.verify_activereport_field_menu_items("ITableData0", 8, 1, expected_menu_list, 'Step 04:01:  Verify the menus')
        active_report_obj.select_activereport_field_menu_items('ITableData0', 8, 1, "New York->Auto Links->Report - Store Product Metrics")
        
         
        """
            Step 06 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.switch_to_new_window()
        css="table[summary='Summary'] table>tbody>tr>td[class='x3']"
        report_obj.wait_for_visible_text(css, "Sales Metrics with Margins", time_out=50)
        
#         report_obj.create_report_dataset_using_start_end_rowcolumn(Test_Case_ID+"_Ds02.xlsx", start_rownum=1)
        report_obj.verify_report_dataset_using_start_end_rowcolumn(Test_Case_ID+"_Ds02.xlsx", "table[summary='Summary']", "Step 06:01:Verify report data", start_rownum=4, end_colnum=2)
         
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] td[class='x3']", text_value='Sales Metrics with Margins', msg="Step 06:02: Verify background color for report title Slaes Metrics with Margins")
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] td[class='x4']", text_value='Year to Year Comparison', msg="Step 06:03: Verify background color for report title Year to Year comparision")
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] td[class='x5']", text_value='New York', msg="Step 06:04: Verify background color for report title of New York")
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(6) td:nth-child(7)", bg_color='light_gray', font_color='black', text_value='42.05', msg="Step 06:05: Verify background color for Rank")
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(5) td:nth-child(2)", bg_color='chelsea_cucumber', font_color='white', text_value='Model', msg="Step 06:06: Verify background color for Rank")
        
        report_obj.set_browser_window_size()
        time.sleep(5)
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(5) td:nth-child(2)", bg_color='chelsea_cucumber', font_color='white', text_value='Model', msg="Step 06.05: Verify background color for Rank")
        self.driver.maximize_window()
        time.sleep(1)
         
        """
            Step 07 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
            Step 08 :Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Quantity_Sold_By_Stores.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        css="#TableChart_1 div[class^='x']"
        report_obj.wait_for_number_of_element(css, 12)
         
        """
            Step 09 : Verify the following Query panel,Filter Panel and Live Preview
            Verify first row value of Report output
            Verify Data bars displayed in Live Preview
        """
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Quantity,Sold', 'Revenue', 'Gross Profit', 'By', 'Gross Profit', 'Store Name', 'Across']
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel")
        
        filter_field_name1 = "Store Front Is true"
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 09:02: Verify the filter panel first field")
        
        expected_list=['', 'Store Name', 'Quantity', 'QuantitySold', '', 'Revenue', '', 'Gross Profit']
        report_obj.verify_report_column_titles_on_preview(4, 8, expected_list, msg='Step 09:03: Verify report preview titles')
        
#         report_obj.create_report_data_set_in_preview('TableChart_1', 2, 4, Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_report_data_set_in_preview('TableChart_1', 2, 4, Test_Case_ID+"_Ds03.xlsx", "Step 09:04: Verify report data in preview")
        
        report_obj.verify_visualize_bar_added_in_previewreport('light_gray', 3, "Step 09:05: Verify visualization bar is added in preview report")
        report_obj.verify_field_in_querypane('By','Gross Profit', 1, msg='Step 09:06: Verify querypane field which is added in grey colour with italic font', color_to_verify='Trolley_Grey', font_to_verify='italic')
                 
        """
            Step 10 : Click Format tab > Verify "Enable Auto Linking" is highlighted
        """
        report_obj.switch_ia_ribbon_tab('Format')
        time.sleep(5)
        elem=self.driver.find_element_by_css_selector("#FormatEnableAutoLink")
        report_obj.verify_checked_class_property_for_selected_object(elem, "Step 10:01:Verify whether Format tab Autodrill is enabled")
         
        """
            Step 11 : Click Run inside IA tool
        """
        report_obj.select_ia_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        report_obj.wait_for_number_of_element(parent_css, 1, timeout=40)
        report_obj.switch_to_frame()
        css="#ITableData0 table tbody tr:nth-child(1) td[id='TCOL_0_C_1']"
        report_obj.wait_for_visible_text(css, "Store Name", time_out=20)
         
        """
            Verify the Report run successfully
            Verify first row value of Report output
            Verify Data bars displayed
        """
         
        active_report_obj.verify_data_set_using_table_rowid("ITableData0", "I0r", Test_Case_ID+"_Ds01.xlsx", "Step 11:01 Verify report data")
        active_report_obj.verify_no_of_autolinks_in_activereport("#ITableData0", 1, 57, "Step 11:02: verify autolinks are available in the report")
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 2, 'light_gray', "Step 11:03: Verify Visualization is present in column 2 in the report")
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 3, 'light_gray', "Step 11:04: Verify Visualization is present in  column 3 the report")
        active_report_obj.verify_visualize_bar_added_in_activereport('#ITableData0', 4, 'light_gray', "Step 11:05: Verify Visualization is present  present in  column 4 in the report")
        
        active_report_obj.verify_page_summary('0','86of86records,Page1of2', 'Step 11:09: Verify Page summary')
        
        """
            Step 12 : Click IA > Save As> Select "SmokeTest"> MYContent folder > Enter title as "Quantity Sold By Stores1" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.save_as_from_application_menu_item(save_fex_name1)
         
        """
            Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
         
        """
            Step 14 : Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Quantity_Sold_By_Stores1.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(folder_name=saved_fex_foldername, fex_name=edit_fex_after_save, mrid='mrid', mrpass='mrpass')
        css="#TableChart_1 div[class^='x']"
        report_obj.wait_for_number_of_element(css, 12, time_out=60)
        
        """
            Verify it restored successfully without any error
        """
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'Quantity,Sold', 'Revenue', 'Gross Profit', 'By', 'Gross Profit', 'Store Name', 'Across']
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 14:01: Verify the Query panel")
        
        filter_field_name1 = "Store Front Is true"
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 14:02: Verify the filter panel first field")
        
        expected_list=['', 'Store Name', 'Quantity', 'QuantitySold', '', 'Revenue', '', 'Gross Profit']
        report_obj.verify_report_column_titles_on_preview(4, 8, expected_list, msg='Step 14:03: Verify report preview titles')
        
#         report_obj.create_report_data_set_in_preview('TableChart_1', 2, 4, Test_Case_ID+"_Ds03.xlsx")
        report_obj.verify_report_data_set_in_preview('TableChart_1', 2, 4, Test_Case_ID+"_Ds03.xlsx", "Step 14:04: Verify report data in preview")
        
        report_obj.verify_visualize_bar_added_in_previewreport('light_gray', 3, "Step 14:05: Verify visualization bar is added in preview report")
        report_obj.verify_field_in_querypane('By','Gross Profit', 1, msg='Step 14:06: Verify querypane field which is added in grey colour with italic font', color_to_verify='Trolley_Grey', font_to_verify='italic')
        
        """
            Step 15 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()