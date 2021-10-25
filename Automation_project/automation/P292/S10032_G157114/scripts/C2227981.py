'''
Created on Aug 10, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227981
Test case Name =  AHTML: Datatype - ALPHANUMERIC field variations.
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.lib import utillity
import unittest, time
from common.wftools import active_report

class C2227981_TestClass(BaseTestCase):

    def test_C2227981(self):
        
        """
        TESTCASE VARIABLES
        """
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(45) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        fex_name="AR_RP_ALPHANUMERIC_Fields.fex"
        
        """
        Step 01: Sign in to WebFOCUS using the below link.
        http://machine:port/ibi_apps
        Sign on screen will display. Login as admin/admin.
        
        Step 02: Execute the attached Fex - AR-RP-ALPHANUMERIC-Fields using the below API URL:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9066&BIP_item=AR-RP-ALPHANUMERIC-Fields.fex
        Expect to see an 18 Page, 1000 line report with 13 columns.
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 13)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02.1:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 02.2: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds01.xlsx', desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds01.xlsx', "Step 02.3: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
        """
        Step 03: For each of the columns, left click on the first row and select Filter Cell.
        After Filter Cell for each column, left-click and select
        Clear Remove Cell Filter to return to the initial 1000 rows.
        
        Expect to see the following number of rows for each column:

        Order Number INTEGER - 1 row
        Alpha Order A6 - 1 row
        Alpha Order Date A8YYMD - 180 rows
        Alpha Order Date A8YYMtD - 180 rows
        Alpha Order Date A6MDY - 180 rows
        Alpha A12V - 1 row
        Alpha Long A80 - 1 row
        Alpha Edit - 84 rows
        Alpha Store Code - 90 rows
        Alpha Vendor Code - 84 rows
        Alpha Vendor Name - 84 rows
        Alpha Product Code - 84 rows
        Alpha Product Descr. - 84 rows
        """
        
        """Order Number INTEGER - 1 row"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 0, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.1a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.1: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds02.xlsx', "Step 03.1: Expect to see '1of1000records,Page1of1'")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 0, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.1b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds01.xlsx', "Step 03.1c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
          
        """Alpha Order A6 - 1 row"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.2a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.2: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds03.xlsx', "Step 03.2c: Expect to see 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.2b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.2c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Order Date A8YYMD - 180 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 03.3a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.3: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds04.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds04.xlsx', "Step 03.3c: Expect to see 180of1000records,Page1of4.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.3b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.3c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Order Date A8YYMtD - 180 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 03.4a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.4: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds05.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds05.xlsx', "Step 03.4c: Expect to see 180of1000records,Page1of4.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.4b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.4c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Order Date A6MDY - 180 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '180of1000records,Page1of4', "Step 03.5a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.5: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds06.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds06.xlsx', "Step 03.5c: Expect to see 180of1000records,Page1of4.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.5b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.5c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha A12V - 1 row"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.6a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.6: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds07.xlsx', "Step 03.6c: Expect to see 1of1000records,Page1of1")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.6b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.6c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Long A80 - 1 row"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.7a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.7: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds08.xlsx', "Step 03.7c: Expect to 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.7b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.7c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Edit - 84 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.8a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.8: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds09.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds09.xlsx', "Step 03.8c: Expect to see 84of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.8b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.8c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Store Code - 90 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', "Step 03.9a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.9: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds10.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds10.xlsx', "Step 03.9c: Expect to see 90of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.9b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.9c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Vendor Code - 84 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.10a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.10: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds11.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds11.xlsx', "Step 03.10c: Expect to see 84of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.10b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.10c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Vendor Name - 84 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.11a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.11: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds12.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds12.xlsx', "Step 03.11c: Expect to see 84of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.11b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.11c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Product Code - 84 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.12a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.12: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds13.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds13.xlsx', "Step 03.12c: Expect to see 84of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.12b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227981_Ds01.xlsx', "Step 03.12c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
          
        """Alpha Product Descr. - 84 rows"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.13a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.13: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds14.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds14.xlsx', "Step 03.13c: Expect to see 84of1000records,Page1of2.", desired_no_of_rows=5)
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.13b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.13: Verify column heading')
#         iarunobj.verify_table_data_set('#ITableData0','C2227981_Ds01.xlsx', "Step 03.13c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds01.xlsx',"Step 03.13c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
         
        """
        Step 04: Clear the previous Filter.
        For the Alpha Order A6 column drop down, select the Filter option.
        Select Equals, then select values 000001, 000010 & 000050.
        Click the Filter button.
        Expect to see a 3 row report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001',value2='000010',value3='000050')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '3of1000records,Page1of1', "Step 04.1: Expect to see a 3 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 04: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds15.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds15.xlsx', "Step 04: Expect to see 3of1000records,Page1of1.")
        time.sleep(2)
          
        """
        Step 05: Clear the previous Filter.
        For the Alpha Order Date A8YYMD column drop down, select the Filter option.
        Select Not equal, then select value 1996/01/01.
        Click the Filter button.
        Expect to see a 820 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05:  Expect to see the following Active Report. - page summary verification")
        utillobj.infoassist_api_logout()
        resultobj.wait_for_property("#SignonbtnLogin", 1)
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        parent_css="#MAINTABLE_wbody0 .arGrid [id^='TCOL']"
        resultobj.wait_for_property(parent_css, 13)
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Not equal")
        filterselectionobj.create_filter(1, 'Not equal',value1='1996/01/01')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '820of1000records,Page1of15', "Step 05.1: Expect to see a 820 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 05: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds16.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds16.xlsx', "Step 05: Expect to see 820of1000records,Page1of15.", desired_no_of_rows=5)
        time.sleep(2)
          
        """
        Step 06: Clear the previous Filter.
        For the Alpha Order Date A8YYMtD column drop down, select the Filter option.
        Select Greater Than, then select value 1996 APR 01.
        Click the Filter button.
        Expect to see a 280 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 06:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Greater than")
        filterselectionobj.create_filter(1, 'Greater than',value1='1996 APR 01')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '280of1000records,Page1of5', "Step 06.1: Expect to see a 280 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 06: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds17.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds17.xlsx', "Step 06: Expect to see 280of1000records,Page1of5.", desired_no_of_rows=5)
        time.sleep(2)
          
        """
        Step 07: Clear the previous Filter.
        For the Alpha Order Date A6MDY column drop down, select the Filter option.
        Select Greater than or equal to, then select value 03/01/96.
        Click the Filter button.
        Expect to see a 640 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 07:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to',value1='03/01/96')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '640of1000records,Page1of12', "Step 07.1: Expect to see a 640 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 07: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds18.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds18.xlsx', "Step 07: Expect to see 640of1000records,Page1of12.", desired_no_of_rows=5)
        time.sleep(2)
          
        """
        Step 08: Clear the previous Filter.
        For the Alpha A12V column drop down, select the Filter option.
        Select Less than, then select value 000051.
        Click the Filter button.
        Expect to see a 50 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 08:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        filterselectionobj.create_filter(1, 'Less than','large',value1='000051')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '50of1000records,Page1of1', "Step 08.1: Expect to see a 50 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 08: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds19.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds19.xlsx', "Step 08: Expect to see 50of1000records,Page1of1.", desired_no_of_rows=5)
        time.sleep(2)
         
        """
        Step 09: Clear the previous Filter.
        For the Alpha Long A80 column drop down, select the Filter option.
        Select Less than or equal to, then select value that begins with
        000025_Abcd.....
        Click the Filter button.
        Expect to see a 25 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 09:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to','large',value1='000025_AbcdefghijklmnopqrstuvwxyZ')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '25of1000records,Page1of1', "Step 09.1: Expect to see a 25 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 09: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds20.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds20.xlsx', "Step 09: Expect to see 25of1000records,Page1of1.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Step 10: Clear the previous Filter.
        For the Alpha Edit column drop down, select the Filter option.
        Select Between, then select B-141 for the first value and B-144 for the second value.
        Click the Filter button.
        Expect to see a 335 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Between")
        filterselectionobj.create_filter(1, 'Between',value1='B-141',value2='B-144')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 10.1: Expect to see a 335 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 10: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds21.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds21.xlsx', "Step 10: Expect to see 335of1000records,Page1of6.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Step 11: Clear the previous Filter.
        For the Alpha Store Code column drop down, select the Filter option.
        Select Not Between, then select R1040 for the first value and R1200 for the second value.
        Click the Filter button.
        Expect to see a 405 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Not Between")
        filterselectionobj.create_filter(1, 'Not Between',value1='R1040',value2='R1200')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '405of1000records,Page1of8', "Step 11.1: Expect to see a 335 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 11: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds22.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds22.xlsx', "Step 11: Expect to see 405of1000records,Page1of8.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Step 12: Clear the previous Filter.
        For the Alpha Vendor Code column drop down, select the Filter option.
        Select Contains, then enter the string - 05 into the value box.
        Click the Filter button.
        Expect to see a 201 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 12:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter", "Contains")
        filterselectionobj.create_filter(1, 'Contains',value1='05')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '201of1000records,Page1of4', "Step 12.1: Expect to see a 201 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 12: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds23.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds23.xlsx', "Step 12: Expect to see 201of1000records,Page1of4.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Step 13: Clear the previous Filter.
        For the Alpha Vendor Name column drop down, select the Filter option.
        Select Contains(match case), then enter the string - Bakeries into the value box.
        Click the Filter button.
        Expect to see a 183 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 13.a:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter", "Contains (match case)")
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='Bakeries')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '183of1000records,Page1of4', "Step 13.a.1: Expect to see a 183 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 13: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds24.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds24.xlsx', "Step 13: Expect to see 183of1000records,Page1of4.", desired_no_of_rows=5)
        time.sleep(2)
        
        
        """
        Clear the previous Filter.
        Again, for the Alpha Vendor Name column drop down, select the Filter option.
        Select Contains(match case), then enter the string - BAKERIES into the value box.
        Click the Filter button.
        Expect to see a 0 row report because the case must match exactly.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 13.b:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter", "Contains (match case)")
        filterselectionobj.create_filter(1, 'Contains (match case)',value1='BAKERIES')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '0of1000records,Page1of1', "Step 13.b.1: Expect to see a 0 row report because the case must match exactly.")
        time.sleep(2)
        
        """
        Step 14: Clear the previous Filter.
        For the Alpha Product Code column drop down, select the Filter option.
        Select Omits, then enter the string - F into the value box.
        Click the Filter button.
        Expect to see a 669 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 14:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "11", "Filter", "Omits")
        filterselectionobj.create_filter(1, 'Omits',value1='F')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '669of1000records,Page1of12', "Step 14.a: Expect to see a 669 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 14: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds25.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds25.xlsx', "Step 14: Expect to see 669of1000records,Page1of12.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Step 15: Clear the previous Filter.
        For the Alpha Product Descr. column drop down, select the Filter option.
        Select Omits(match case), then enter the string - Mug into the value box.
        Click the Filter button.
        Expect to see a 866 row report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.a:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Omits (match case)")
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='Mug')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '866of1000records,Page1of16', "Step 15.a.1: Expect to see a 866 row report.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 15: Verify column heading')
#         utillobj.create_data_set('ITableData0','I0r', 'C2227981_Ds26.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds26.xlsx', "Step 15: Expect to see 866of1000records,Page1of16.", desired_no_of_rows=5)
        time.sleep(2)
        
        """
        Again for the Alpha Product Descr. column drop down, select the Filter option.
        Select Omits(match case), then enter the string - MUG into the value box.
        Click the Filter button.
        Expect to seed the entire 1000 rows because upper case MUD did not remove any rows.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.b:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Omits (match case)")
        filterselectionobj.create_filter(1, 'Omits (match case)',value1='MUG')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15.b.1: Expect to seed the entire 1000 rows because upper case MUD did not remove any rows.")
        heading=['Order Number INTEGER', 'Alpha Order A6', 'Alpha Order Date A8YYMD', 'Alpha Order Date A8YYMtD', 'Alpha Order Date A6MDY', 'Alpha A12V', 'Alpha Long A80', 'Alpha Edit', 'Alpha Store Code', 'Alpha Vendor Code', 'Alpha Vendor Name', 'Alpha Product Code', 'Alpha Product Descr.']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 15: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227981_Ds01.xlsx',"Step 15.b.2: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
        time.sleep(2)
        filterselectionobj.close_filter_dialog()
        
if __name__ == '__main__':
    unittest.main()