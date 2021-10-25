'''
Created on Aug 11, 2017

@author: AAkhan/Updated by :Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157319
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227984
Description : AHTML: Datatype - INTEGER data field variations.

'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea, ia_run
from common.lib import utillity
import unittest, time
from common.wftools import active_report


class C2227984_TestClass(BaseTestCase):

    def test_C2227984(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227984'
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        fex_name="AR_RP_INTEGER_Fields.fex"
        
        
        """ Step 1: Sign in to WebFOCUS using the below link.
                    http://machine:port/ibi_apps
                    Sign on screen will display.
                    Login as admin/admin.
        """
        """ Step 2: Execute the attached Fex - AR-RP-INTEGER-Fields using 
                    the below API URL: http://machine:port/ibi_apps/run.bip?
                    BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9066&BIP_item=AR-RP-INTEGER-Fields.fex
                    Expect to see an 18 Page, 1000 line report with 12 columns.
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#ITableData0 tr:nth-child(3) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:  Expect to see the following Active Report. - page summary verification")
        exp=['Datetype-INTEGER']
        utillobj.verify_run_time_title('ITableData0', exp, "Step 1.2:", custom_css="[id^='THEAD']")
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 1.3:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 01.4: Verify table data set.",desired_no_of_rows=20)
           
        """ Step 3: For each column, left-click the cell for row 1 and select Filter cell.
                    After Filter Cell for each column, left-click and select
                    Clear Remove Cell Filter to return to the initial 1000 rows.
                    Expect to see the following row counts:
                    I6 Order Number - 1
                    I09 Unit Price - 84
                    I09L Unit Price - 84
                    I9C Unit Price * 100 - 84
                    I9M Unit Price - 2
                    I09 Unit Price -neg - 1
                    I09 Unit Price neg- 1 
                    I09B Unit Price - 84
                    I09R Unit Price - 2
                    I9% Unit Price - 84
                    I8YYMD Order Date - 180
                    I6DMY Order Date - 180
                    I8MtDYY Order Date - 180
        """
        miscelanousobj.select_field_menu_items("ITableData0", 0, 0, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 3: Expect 1 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds02.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds02.xlsx', "Step 3.1: Verify table data set for I6 Order Number .")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 0, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.2: Verify table data set.",desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.2a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds03.xlsx', "Step 3.3: Verify table data set for I09 Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.4: Verify table data set.", desired_no_of_rows=5)
                   
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.3a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds04.xlsx', "Step 3.4: Verify table data set for I09L Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.5: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.5a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds05.xlsx', "Step 3.6: Verify table data set for I9C Unit Price * 100.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.7: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 3.7a: Expect 2 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds06.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds06.xlsx', "Step 3.8: Verify table data set for I9M Unit Price.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.9: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 3.9a: Expect 1 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds07.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds07.xlsx', "Step 3.10: Verify table data set for I09 Unit Price -neg.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.11: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 3.11a: Expect 1 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds08.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds08.xlsx', "Step 3.11b: Verify table data set for I09 Unit Price neg.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.12: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.12a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds09.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds09.xlsx', "Step 3.13: Verify table data set for I09B Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.14: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 3.14a: Expect 2 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds10.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds10.xlsx', "Step 3.15: Verify table data set for I09R Unit Price.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.16: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.16a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds11.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds11.xlsx', "Step 3.17: Verify table data set for I9% Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.18: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.18a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds12.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds12.xlsx', "Step 3.19: Verify table data set for I8YYMD Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.20: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.19a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds13.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds13.xlsx', "Step 3.20: Verify table data set for I6DMY Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.21: Verify table data set.", desired_no_of_rows=5)
           
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.21a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds14.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds14.xlsx', "Step 3.22: Verify table data set for I8MtDYY Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.23: Verify table data set.", desired_no_of_rows=5)
                  
        """Step 4: Clear the previous Filter panel.
                    For the I6 Order Number column drop down, select the Filter option.
                    Select Equals, then select values 5, 10, 15 & 20.
                    Click the Filter button.
                    Expect to see a 4 row report.
        """
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter","Equals")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Equals','large',value1='5', value2='10', value3='15', value4='20')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 04: Expect 4 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 4.1:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds15.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds15.xlsx', "Step 4.2: Verify table data set for values 5, 10, 15 & 20.")
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 5: Clear the previous Filter panel.
                    For the I09 Unit Price column drop down, select the Filter option.
                    Select Not Equal, then select value 58.
                    Click the Filter button.
                    Expect to see a 916 row report.
        """
          
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 5: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not equal', value1='58')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 5.1: Expect 916 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 5.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds16.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds16.xlsx', "Step 5.3: Verify table data set for values 58.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
         
        """ Step 6: Clear the previous Filter panel.
                    For the I09L Unit Price column drop down, select the Filter option.
                    Select Greater than, then select value 00000125.
                    Click the Filter button.
                    Expect to see a 67 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 6: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Greater than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Greater than', value1='000000125')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 6.1: Expect 67 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 6.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds17.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds17.xlsx', "Step 6.3: Verify table data set for values 00000125.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 7: Clear the previous Filter panel.
                    For the I9C Unit Price * 100 column drop down, select the Filter option.
                    Select Greater than or equal to, then select value 7,600.
                    Click the Filter button.
                    Expect to see a 451 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 7: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Greater than or equal to")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Greater than or equal to', value1='7,600')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '451of1000records,Page1of8', "Step 7.1: Expect 451 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 7.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds18.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds18.xlsx', "Step 7.3: Verify table data set for values 7,600.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
         
        """ Step 8: Clear the previous Filter panel.
                    For the I9M Unit Price column drop down, select the Filter option.
                    Select Less Than, then select value $100.
                    Click the Filter button.
                    Expect to see a 43 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 8: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Less than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Less than','large', value1='$100')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '43of1000records,Page1of1', "Step 8.1: Expect 43 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 8.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds19.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds19.xlsx', "Step 8.3: Verify table data set for values $100.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 9: Clear the previous Filter panel.
                    For the I09 Unit Price -neg column drop down, select the Filter option.
                    Select Less than or equal to, then select value -1
                    Click the Filter button.
                    Expect to see a 59 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 9: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than or equal to")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Less than or equal to', 'large', value1='-1')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '59of1000records,Page1of2', "Step 9.1: Expect 59 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 9.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds20.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds20.xlsx', "Step 9.3: Verify table data set for values -1.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        result_obj.wait_for_property("#SignonbtnLogin", 1)
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        result_obj.wait_for_property(parent_css, 13) 
          
        """ Step 10:Clear the previous Filter panel.
            For the I09 Unit Price neg- column drop down, select the Filter option.
            Select Between, then select 9- for the first value and 9 for the second value.
            Click the Filter button.
            Expect to see a 19 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 10: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Between', 'large', value1='9-', value2='9')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '19of1000records,Page1of1', "Step 10.1: Expect 19 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 10.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds21.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds21.xlsx', "Step 10.3: Verify table data set for values between value 9- and 9.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 11: Clear the previous Filter panel.
            For the I09B Unit Price column drop down, select the Filter option.
            Select Not Between, then select (96) for the first value and (28) for the second value.
            Click the Filter button.
            Expect to see a 316 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 11: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Not Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not Between', value1='(96)', value2='(28)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '316of1000records,Page1of6', "Step 11.1: Expect 316 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 11.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds22.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds22.xlsx', "Step 11.3: Verify table data set for values Not Between value (96) and  (28).", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 12: Clear the previous Filter panel.
                    For the I09R Unit Price column drop down, select the Filter option.
                    Select Between or equal to, then select 1139 CR for the first value and 1073 CR for the second value.
                    Click the Filter button.
                    Expect to see a 14 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 12: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Between', 'large', value1='1139 CR', value2='1073 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '14of1000records,Page1of1', "Step 12.1: Expect 14 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 12.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds23.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds23.xlsx', "Step 12.3: Verify table data set for 12.55%.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 13: Clear the previous Filter panel.
                    For the I9% Unit Price column drop down, select the Filter option.
                    Select Not Between or equal to, then select 28% for the first value and 125% for the second value.
                    Click the Filter button.
                    Expect to see a 384 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 13: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter", "Not Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not Between', value1='28%', value2='125%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '384of1000records,Page1of7', "Step 13.1: Expect 384 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 13.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds24.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds24.xlsx', "Step 13.3: Verify table data set for values 28% & 125%.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 14: Clear the previous Filter panel.
                    For the I8YYMD Order Date column drop down, select the Filter option.
                    Select Contains, then enter the string - 02/01 into the value box.
                    Click the Filter button.
                    Expect to see a 180 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 14: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter", "Contains")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Contains', value1='02/01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 14.1: Expect 180 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 14.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds25.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds25.xlsx', "Step 14.3: Verify table data set for values 02/01.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
          
        """ Step 15: Clear the previous Filter panel.
                    For the I6DMY Order Date column drop down, select the Filter option.
                    Select Omits, then enter the string - 01/03/ into the value box.
                    Click the Filter button.
                    Expect to see a 820 row report.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.1:  Expect to see the following Active Report. - page summary verification")
        exp=['Datetype-INTEGER']
        utillobj.verify_run_time_title('ITableData0', exp, "Step 15.2:", custom_css="[id^='THEAD']")
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 15.3:")
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 15.4: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "11", "Filter", "Omits")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Omits', value1='01/03/')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 15.5: Expect 820 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 15.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds26.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds26.xlsx', "Step 15.3: Verify table data set for values 01/03/.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
          
        """ Step 16: Clear the previous Filter panel.
                    For the I8MtDYY Order Date column drop down, select the Filter option.
                    Select Contains(match case), then enter the string - JUN 01 into the value box.
                    Click the Filter button.
                    Expect to see a 100 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 16: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Contains (match case)")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Contains (match case)', value1='JUN 01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '100of1000records,Page1of2', "Step 16.1: Expect 100 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 16.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds27.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds27.xlsx', "Step 16.3: Verify table data set for values JUN 01.", desired_no_of_rows=10)
        time.sleep(2)
          
        """ Step 17: Again for the I8MtDYY Order Date column drop down, select the Filter option.
                    Select Contains(match case), then enter the string - Jun 01 into the value box.
                    Click the Filter button.
                    Expect to see a 0 row report because Jun 01 does not match the case of the data.
        """
        filterselectionobj.create_filter(1, 'Contains (match case)', value1='Jun 01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 17.1: Expect 0 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds28.xlsx')
        ia_runobj.verify_table_data_set('table#ITableData0',Test_Case_ID+'_Ds28.xlsx', "Step 17.2: Verify table data set for Jun 01.")
        time.sleep(2)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        """ Step 18: Clear the previous Filter panel.
                    For the I8MtDYY Order Date column drop down, select the Filter option.
                    Select Omits(match case), then enter the string - JUN 01 into the value box.
                    Click the Filter button.
                    Expect to see a 900 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 18: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Omits (match case)")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Omits (match case)', value1='JUN 01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '900of1000records,Page1of16', "Step 18.1: Expect 900 row.")
        time.sleep(2)
        exp1=['I6OrderNumber', 'I09UnitPrice', 'I09LUnitPrice', 'I9CUnitPrice*100', 'I9MUnitPrice', 'I09UnitPrice-neg', 'I09UnitPriceneg-', 'I09BUnitPrice', 'I09RUnitPrice', 'I9%UnitPrice', 'I8YYMDOrderDate', 'I6DMYOrderDate', 'I8MtDYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 18.2:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds29.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds29.xlsx', "Step 18.3: Verify table data set for values JUN 01.", desired_no_of_rows=10)
        time.sleep(2)
        
        """ Step 19: Again for the I8MtDYY Order Date column drop down, select the Filter option.
                    Select Omits(match case), then enter the string - Jun 01 into the value box.
                    Click the Filter button.
                    Expect to see the full 1000 row report because Jun 01 did not Omit data due to not matching the case of the data.
        """
        filterselectionobj.create_filter(1, 'Omits (match case)', value1='Jun 01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 19.1: Expect 1000 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds30.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds30.xlsx', "Step 19.2: Verify table data set for values Jun 01.", desired_no_of_rows=10)
        time.sleep(2)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()