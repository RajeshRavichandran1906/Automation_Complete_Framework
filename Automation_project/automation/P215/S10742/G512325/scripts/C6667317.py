'''
Created on Aug 03, 2018

@author: BM13368
TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667317
TestCase_Name : Verify to Run and Edit 'YTD Stats for Product Category'
'''
import unittest, time
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C6667317_TestClass(BaseTestCase):

    def test_C6667317(self):
        
        Test_Case_ID = "C6667317"
        report_obj=report.Report(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        fex_name="YTD_Stats_for_Product_Category"
        save_fex="YTD Stats for Product Category1"
        fex_name1="YTD_Stats_for_Product_Category1"
        folder_name="Retail_Samples/Reports/Auto_Link"
        edit_fex_after_save_folder="SmokeTest/~rsadv"
        run_cell_value = "$7,487,147.00"
        live_preview_cell_value = "$620.00"
        
        long_wait=report_obj.home_page_long_timesleep
        medium_wait=report_obj.home_page_medium_timesleep
        
        """
            Step 01 : Sign to Webfocus using rsadv (advanced user)
            http://machine:port/ibi_apps
            Step 02 : Run the Report using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link&BIP_item=YTD_Stats_for_Product_Category.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        css="table[summary='Summary'] table>tbody>tr>td[class='x3']"
        report_obj.wait_for_visible_text(css, "Monthly YTD Stats", long_wait)
         
        """
            Step 03: Verify the following output 
        """
        report_obj.create_report_dataset_using_start_end_rowcolumn(Test_Case_ID+"_Ds01.xlsx", start_rownum=4, end_colnum=2)
        report_obj.verify_report_dataset_using_start_end_rowcolumn(Test_Case_ID+"_Ds01.xlsx", "table[summary='Summary']", "Step 03:01:Verify report data", start_rownum=4, end_colnum=2)
          
        css1="table[summary='Summary'] table>tbody>tr>td[class='x3']"
        css2="table[summary='Summary'] td[class='x2']  table tbody tr td[class='x4']"
        report_obj.verify_table_cell_property(2, 2, table_css=css1, text_value='Monthly YTD Stats', msg="Step 03:02: Verify report title shown as Monthly YTD Stats")
        report_obj.verify_table_cell_property(3, 2, table_css=css2, text_value='For All', msg="Step 03:03: Verify report title shown as For All")
          
        """
           Verify values for Sale month from 1 to 12.
           Verify first row value output 
           Note: Sale month values increasing monthly based on Filter condition. 
        """
        css1="table[summary='Summary'] > tbody > tr td[class='x6']"
        report_obj.verify_table_cell_property(6, 2, table_css="table[summary='Summary'] > tbody > tr td[class='x6']", text_value='Sale,Month', msg="Step 03:04: Verify report column heading shows Sale, Month")
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(5) td:nth-child(2)", bg_color='saltpan', font_color='black', text_value=run_cell_value, msg="Step 03.05: Verify background color for first row value")
         
        """Verify total number of columns """
#         current_month=datetime.datetime.now()
#         current_month_in_string=current_month.strftime('%m')
#         current_month_in_number=int(current_month_in_string)
        columns_elem=self.driver.find_elements_by_css_selector("table[summary='Summary'] > tbody > tr td[class='x7']")
        total_no_of_columns=len(columns_elem)
        expected_month_in_number = 3
        utillobj.asequal(expected_month_in_number, total_no_of_columns, "Step 03:05: Verify total number of column shown baed on the current month in numbers")
         
        """
            Step 04 : Resize the browser window and verify it does not throws any error message
        """
        report_obj.set_browser_window_size()
        time.sleep(5)
         
        """Verify the report does not throws any error"""
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(5) td:nth-child(2)", bg_color='saltpan', font_color='black', text_value=run_cell_value, msg="Step04.1: Verify background color for Rank")
        report_obj.maximize_browser()
        time.sleep(3)                                      
         
        """
            Step 05 : Logout Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Reports/Auto_Link/YTD_Stats_for_Product_Category.fex&tool=Report
        """
        report_obj.api_logout()

        report_obj.edit_fex_using_api_url(fex_name = fex_name, folder_name = folder_name)
        css="#TableChart_1 div[class^='x']"
        report_obj.wait_for_number_of_element(css, 42, long_wait)
        
        """
            Verify the following Query panel,Filter Panel and Live Preview
            Verify first row value output
        """
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'SUM.Cost of Goods', 'MAX.Cost of Goods', 'MIN.Cost of Goods', 'AVE.Cost of Goods', 'MDN.Cost of Goods', 'Discount', 'MAX.Discount', 'MIN.Discount', 'AVE.Discount', 'MDN.Discount', 'Gross Profit', 'MAX.Gross Profit', 'MIN.Gross Profit', 'AVE.Gross Profit', 'MDN.Gross Profit', 'Revenue', 'MAX.Revenue', 'MIN.Revenue', 'AVE.Revenue', 'MDN.Revenue', 'By', 'Across', 'Sale,Month']
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step11.2.1: Verify the Query panel")
        filter_field_name1 = "Product,Category Equal to Optional Simple Parameter (Name: PRODUCT_CATEGORY)"
        filter_field_name2 = "Sale,Date From Beginning of Year to Today"
        
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 05:01: Verify the filter panel first field")
        report_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 05:02: Verify the filter panel first field")
        
#         report_obj.create_acrossreport_data_set_in_preview("TableChart_1", 2, 2, 19, 2, Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_across_report_data_set_in_preview("TableChart_1", 2, 2, 19, 2, Test_Case_ID+"_Ds02.xlsx", "Step 05:03: Verify the created across dataset")
        
        report_obj.verify_report_cell_property("TableChart_1", 4, bg_color='saltpan', bg_cell_no=5, text_value=live_preview_cell_value, msg="Step 05:04: Verify background color of the table cell")
        
        expected_report_title=['Monthly YTD Stats', 'For All PRODUCT_CATEGORY']
        report_obj.verify_report_header_footer_title_in_preview(expected_report_title, msg="Step 05:05: Verify report header title in preview")
                
        """
            Step 06 : Click Run inside IA tool
        """
        report_obj.run_report_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        report_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        report_obj.switch_to_frame()
        css="table[summary='Summary'] table>tbody>tr>td[class='x3']"
        report_obj.wait_for_visible_text(css, "Monthly YTD Stats", medium_wait)
        
        """
            Verify the Report run successfully
            Verify first row value output
            Verify the heading is center alignment
        """
        css1="table[summary='Summary'] table>tbody>tr>td[class='x3']"
        css2="table[summary='Summary'] td[class='x2']  table tbody tr td[class='x4']"
        report_obj.verify_table_cell_property(2, 2, table_css=css1, text_value='Monthly YTD Stats', msg="Step 06:01: Verify report title shown as Monthly YTD Stats")
        report_obj.verify_table_cell_property(3, 2, table_css=css2, text_value='For All', msg="Step 06:02: Verify report title shown as For All")
        
#         current_month=datetime.datetime.now()
#         current_month_in_string=current_month.strftime('%m')
#         current_month_in_number=int(current_month_in_string)
        columns_elem=self.driver.find_elements_by_css_selector("table[summary='Summary'] > tbody > tr td[class='x7']")
        total_no_of_columns=len(columns_elem)
        expected_month_in_number = 3
        utillobj.asequal(expected_month_in_number, total_no_of_columns, "Step 06:03: Verify second row columns are displayed based on the month name in numbers")
        
        report_obj.verify_table_cell_property(5, 2, table_css="table[summary='Summary'] > tbody > tr:nth-child(5) td:nth-child(2)", bg_color='saltpan', font_color='black', text_value=run_cell_value, msg="Step 06:04: Verify background color for first row value $27,007,104,00")
        report_obj.verify_report_dataset_using_start_end_rowcolumn(Test_Case_ID+"_Ds01.xlsx", "table[summary='Summary']", "Step 03:01:Verify report data", start_rownum=4, end_colnum=2)
        
        """
            Step 07 : Click IA > Save> Select "SmokeTest" folder > Enter title as "YTD Stats for Product Category1" > Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.save_as_from_application_menu_item(file_name = save_fex, target_table_path = 'SmokeTest->My Content')
        
        """
            Step 08 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
            Step 09 : Edit the Report using "rsadv" user
            http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/YTD_Stats_for_Product_Category1.fex
            &tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name = fex_name1, folder_name = edit_fex_after_save_folder)
        elem="#queryTreeColumn table>tbody>tr:nth-child(3)"
        report_obj.wait_for_visible_text(elem, "SUM.Cost of Goods", long_wait)
        
        """
            Verify it restored successfully without any error
        """
        query_field_list=['Report (wf_retail_lite)', 'Sum', 'SUM.Cost of Goods', 'MAX.Cost of Goods', 'MIN.Cost of Goods', 'AVE.Cost of Goods', 'MDN.Cost of Goods', 'Discount', 'MAX.Discount', 'MIN.Discount', 'AVE.Discount', 'MDN.Discount', 'Gross Profit', 'MAX.Gross Profit', 'MIN.Gross Profit', 'AVE.Gross Profit', 'MDN.Gross Profit', 'Revenue', 'MAX.Revenue', 'MIN.Revenue', 'AVE.Revenue', 'MDN.Revenue', 'By', 'Across', 'Sale,Month']
        report_obj.verify_all_fields_in_query_pane(query_field_list, "Step 09:01: Verify the Query panel")
        filter_field_name1 = "Product,Category Equal to Optional Simple Parameter (Name: PRODUCT_CATEGORY)"
        filter_field_name2 = "Sale,Date From Beginning of Year to Today"
        
        report_obj.verify_filter_pane_field(filter_field_name1, 1, "Step 09:01: Verify the filter panel first field")
        report_obj.verify_filter_pane_field(filter_field_name2, 2, "Step 09:02: Verify the filter panel first field")
        
#         report_obj.create_acrossreport_data_set_in_preview("TableChart_1", 2, 2, 19, 2, Test_Case_ID+"_Ds02.xlsx")
        report_obj.verify_across_report_data_set_in_preview("TableChart_1", 2, 2, 19, 2, Test_Case_ID+"_Ds02.xlsx", "Step 09:03: Verify the created across dataset")
        
        report_obj.verify_report_cell_property("TableChart_1", 4, bg_color='saltpan', bg_cell_no=5, text_value=live_preview_cell_value, msg="Step 09:04: Verify background color of the table cell and verify it's text value 360.00")
        
        expected_report_title=['Monthly YTD Stats', 'For All PRODUCT_CATEGORY']
        report_obj.verify_report_header_footer_title_in_preview(expected_report_title, msg="Step 09:05: Verify report header title in preview")
     
        """
            Step 10 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """



if __name__ == "__main__":
    unittest.main()