'''
Created on Aug 10, 2017

@author: AAkhan/Updated by :Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157319
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227983
Description : AHTML: Datatype - PACKED data field variations.

'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea, ia_run
from common.lib import utillity
import unittest, time
from common.wftools import active_report

class C2227983_TestClass(BaseTestCase):

    def test_C2227983(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227983'
        driver = self.driver #Driver reference object created
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        fex_name="AR_RP_PACKED_DATA_Fields.fex"
        
        """ Step 1: Sign in to WebFOCUS using the below link.
                    http://machine:port/ibi_apps
                    Sign on screen will display.
                    Login as admin/admin.
        """
        """ Step 2: Execute the attached Fex - AR-RP-PACKED-DATA-Fields using 
                    the below API URL: http://machine:port/ibi_apps/run.bip?
                    BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9066&BIP_item=AR-RP-PACKED-DATA-Fields.fex
                    Expect to see an 18 Page, 1000 line report with 14 columns.
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#ITableData0 tr:nth-child(3) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(1)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:  Expect to see the following Active Report. - page summary verification")
        exp=['Datatype-PACKED']
        utillobj.verify_run_time_title('ITableData0', exp, "Step 1:", custom_css="[id^='THEAD']")
        exp1=['OrderNumberINTEGER', 'PackedOrderP9', 'P9.2MUnitPrice', 'P9.2CUnitPrice', 'P9.2LUnitPrice', 'P15.2CUnitPrice*1000', 'P9.2UnitPriceneg.', 'P9.2BUnitPrice', 'P9.2RUnitPrice', 'P9.2%UnitPrice', 'P9.2MUnit+Order', 'P8YYMDOrderDate', 'P6MDYOrderDate', 'P8DMtYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 1.1:")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds01.xlsx', desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 01.2: Verify table data set.",desired_no_of_rows=20)
         
        """ Step 3: For each of the columns, starting with Packed Order P9, left click on the first row and select Filter Cell.
                    After Filter Cell for each column, left-click and select
                    Clear Remove Cell Filter to return to the initial 1000 rows.
                    Expect to see the following row counts:
                     
                    Packed Order P9 - 1
                    P9.2M Unit Price - 84
                    P9.2C Unit Price - 84
                    P9.2L Unit Price - 84
                    P15.2C Unit Price * 1000 - 84
                    P9.2 Unit Price neg - 84
                    P9.2B Unit Price - 84
                    P9.2R Unit Price - 84
                    P9.2% Unit Price - 84
                    P9.2M Unit Price - 2
                    P8YYMD Order Date - 180
                    P6MDY Order Date - 180
                    P8DMtYY Order Date - 180
        """
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 3a: Expect 1 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds02.xlsx', "Step 3: Verify table data set for Packed Order P9 - 1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.1: Verify table data set.")
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.1a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds03.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds03.xlsx', "Step 3.2: Verify table data set for P9.2M Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.3: Verify table data set.", desired_no_of_rows=5)
                 
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.3a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds04.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds04.xlsx', "Step 3.4: Verify table data set for P9.2C Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.5: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.5a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds05.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds05.xlsx', "Step 3.6: Verify table data set for P9.2L Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.7: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.7a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds06.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds06.xlsx', "Step 3.8: Verify table data set for P15.2C Unit Price * 1000.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.9: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.9a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds07.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds07.xlsx', "Step 3.10: Verify table data set for P9.2 Unit Price neg.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.11: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.11a: Expect 84 row.")
#         ia_runobj.create_table_data_set('table#ITableData0', Test_Case_ID+'_Ds08.xlsx', desired_no_of_rows=5)
        ia_runobj.verify_table_data_set('table#ITableData0', Test_Case_ID+'_Ds08.xlsx', "Step 3.11: Verify table data set for P9.2B Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.12: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.12a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds09.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds09.xlsx', "Step 3.13: Verify table data set for P9.2R Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.14: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 3.14a: Expect 84 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds10.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds10.xlsx', "Step 3.15: Verify table data set for P9.2% Unit Price.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.16: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 3.16a: Expect 2 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds11.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds11.xlsx', "Step 3.17: Verify table data set for P9.2M Unit Price.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.18: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.18a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds12.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds12.xlsx', "Step 3.19: Verify table data set for P8YYMD Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.20: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.19a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds13.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds13.xlsx', "Step 3.20: Verify table data set for P6MDY Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.21: Verify table data set.", desired_no_of_rows=5)
         
        miscelanousobj.select_field_menu_items("ITableData0", 0, 13, 'Filter Cell')
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 3.21a: Expect 180 row.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds14.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds14.xlsx', "Step 3.22: Verify table data set for P8DMtYY Order Date.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 13, 'Remove Cell Filter')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 3.23: Verify table data set.", desired_no_of_rows=5)
                
        """Step 4: Clear the previous Filter panel.
                    For the Packed Order P9 column drop down, select the Filter option.
                    Select Equals, then select values 24, 48 & 59.
                    Click the Filter button.
                    Expect to see the following 3 row report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Equals','large',value1='24', value2='48', value3='59')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '3of1000records,Page1of1', "Step 04: Expect 3 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds15.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds15.xlsx', "Step 4.1: Verify table data set for values 24, 48 & 59.")
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 5: Clear the previous filter panel.
                    For the P9.2M Unit Price column drop down, select the Filter option.
                    Select Not equal, then select values $58.55 & $81.55.
                    Click the Filter button.
                    Expect to see the following 698 row report.
        """
        
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 5: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Not equal")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not equal', value1='$58.55', value2='$81.55')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '698of1000records,Page1of13', "Step 5.1: Expect 698 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds16.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds16.xlsx', "Step 5.2: Verify table data set for values $58.55 & $81.55.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        """ Step 6: Clear the previous filter panel.
                    For the P9.2C Unit Price column drop down, select the Filter option.
                    Select Greater than, then select value 95.34.
                    Click the Filter button.
                    Expect to see the following 133 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 6: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Greater than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Greater than', value1='95.34')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 6.1: Expect 133 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds17.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds17.xlsx', "Step 6.2: Verify table data set for values 95.34.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 7: Clear the previous filter panel.
                    For the P9.2L Unit Price column drop down, select the Filter option.
                    Select Greater than or equal to, then select value 000081.05.
                    Click the Filter button.
                    Expect to see the following 418 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 7: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Greater than or equal to', value1='000081.05')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '418of1000records,Page1of8', "Step 7.1: Expect 418 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds18.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds18.xlsx', "Step 7.2: Verify table data set for values 000081.05.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 8: Clear the previous filter panel.
                    For the P15.2C Unit Price * 1000 column drop down, select the Filter option.
                    Select Less than, then select value 26,000.00
                    Click the Filter button.
                    Expect to see the following 183 row report.

        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 8: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Less than', value1='26,000.00')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 8.1: Expect 183 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds19.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds19.xlsx', "Step 8.2: Verify table data set for values 26,000.00.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 9: Clear the previous filter panel.
                    For the P9.2 Unit Price neg column drop down, select the Filter option.
                    Select Less than or equal to, then select value -95.55.
                    Click the Filter button.
                    Expect to see the following 200 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 9: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Less than or equal to")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Less than or equal to', value1='-95.55')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '200of1000records,Page1of4', "Step 9.1: Expect 200 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds20.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds20.xlsx', "Step 9.2: Verify table data set for values -95.55.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 10: Clear the previous filter panel.
                    For the P9.2B Unit Price column drop down, select the Filter option.
                    Select Between, then select value (26.25) for the first value and (17.25) for the second value.
                    Click the Filter button.
                    Expect to see the following 233 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 10: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Between', value1='(26.25)', value2='(17.25)')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '233of1000records,Page1of5', "Step 10.1: Expect 233 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds21.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds21.xlsx', "Step 10.2: Verify table data set for values between value (26.25) and (17.25).", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 11: Clear the previous filter panel.
                    For the P9.2R Unit Price column drop down, select the Filter option.
                    Select Not between, then select value 139.5 CR for the first value and 75.5 CR for the second value.
                    Click the Filter button.
                    Expect to see the following 549 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 11: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Not Between")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not Between', value1='139.5 CR', value2='75.5 CR')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '549of1000records,Page1of10', "Step 11.1: Expect 549 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds22.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds22.xlsx', "Step 11.2: Verify table data set for values Not Between value 139.5 CR and 75.5 CR.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 12: Clear the previous filter panel.
                    For the P9.2% Unit Price column drop down, select the Filter option.
                    Select Equals, then select value 12.55%.
                    Click the Filter button.
                    Expect to see the following 84 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 12: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter", "Equals")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Equals', value1='12.55%')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 12.1: Expect 84 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds23.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds23.xlsx', "Step 12.2: Verify table data set for 12.55%.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 13: Clear the previous filter panel.
                    For the P8YYMD Order Date column drop down, select the Filter option.
                    Select Not equal, then select values 1996/01/01 & 1996/06/01.
                    Click the Filter button.
                    Expect to see the following 720 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 13: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "11", "Filter", "Not equal")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Not equal', value1='1996/01/01', value2='1996/06/01')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '720of1000records,Page1of13', "Step 13.1: Expect 720 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds24.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds24.xlsx', "Step 13.2: Verify table data set for values 1996/01/01 & 1996/06/01.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 14: Clear the previous filter panel.
                    For the P6MDY Order Date column drop down, select the Filter option.
                    Select Greater than, then select value 04/01/96.
                    Click the Filter button.
                    Expect to see the following 280 row report.
        """
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 14: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Greater than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Greater than', value1='04/01/96')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 14.1: Expect 280 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds25.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds25.xlsx', "Step 14.2: Verify table data set for values 04/01/96.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
        """ Step 15:Clear the previous filter panel.
                    For the P8DMtYY Order Date column drop down, select the Filter option.
                    Select Less than, then select value 01 MAR 1996.
                    Click the Filter button.
                    Expect to see the following 360 row report.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.1:  Expect to see the following Active Report. - page summary verification")
        exp=['Datatype-PACKED']
        utillobj.verify_run_time_title('ITableData0', exp, "Step 15.2:", custom_css="[id^='THEAD']")
        exp1=['OrderNumberINTEGER', 'PackedOrderP9', 'P9.2MUnitPrice', 'P9.2CUnitPrice', 'P9.2LUnitPrice', 'P15.2CUnitPrice*1000', 'P9.2UnitPriceneg.', 'P9.2BUnitPrice', 'P9.2RUnitPrice', 'P9.2%UnitPrice', 'P9.2MUnit+Order', 'P8YYMDOrderDate', 'P6MDYOrderDate', 'P8DMtYYOrderDate']
        utillobj.verify_run_time_title('ITableData0', exp1, "Step 15.3:")
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 15.4: Verify table data set.", desired_no_of_rows=5)
        miscelanousobj.select_menu_items("ITableData0", "13", "Filter", "Less than")
        time.sleep(0.5)  
        filterselectionobj.create_filter(1, 'Less than', value1='01 MAR 1996')
        time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '360of1000records,Page1of7', "Step 15.5: Expect 360 row.")
        time.sleep(2)
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_Ds26.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+'_Ds26.xlsx', "Step 15.6: Verify table data set for values 01 MAR 1996.", desired_no_of_rows=10)
        time.sleep(3)
        filterselectionobj.filter_button_click('Clear All')
        time.sleep(1)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        

if __name__ == '__main__':
    unittest.main()