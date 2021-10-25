'''
Created on Aug 11, 2017

@author: Magesh/updated by :Bhagavathi

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227982
Test case Name =  AHTML: Datatype - FLOATING POINT field variations.
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest, time
from common.wftools import active_report

class C2227982_TestClass(BaseTestCase):

    def test_C2227982(self):
        
        """
        TESTCASE VARIABLES
        """
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AR_RP_FLOATING_POINT_Fields.fex"
        
        """
        Step 01: Sign in to WebFOCUS using the below link.
        http://machine:port/ibi_apps
        Sign on screen will display. Login as admin/admin.
        
        Step 02: Execute the attached Fex - AR-RP-FLOATING-POINT-Fields using the below API URL:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9066&BIP_item=AR-RP-FLOATING-POINT-Fields.fex
        Expect to see an 18 Page, 1000 line report with 19 columns.
        """
        active_reportobj.run_active_report_using_api(fex_name, synchronize_visible_element_text='1')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02.1:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 02.2: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx', "Step 02.3: Expect to see an 18 Page, 1000 line report with 19 columns.")
        
        """
        Step 03: For each of the columns, left click on the first row and select Filter Cell.
        After Filter Cell for each column, left-click and select
        Clear Remove Cell Filter to return to the initial 1000 rows.
        
        Expect to see the following number of rows for each column:

        F8 Unit Price - 2
        F6.0 Unit Price - 2
        F9.2 Unit Price - 2
        F9.2LM Unit Price - 2
        F9.2E Unit Price - 84
        F9.2B Unit Price - 2
        F9.2R Unit Price - 1
        F7.2% - 84
        F7.2 Unit Price - 2
        
        D8 Unit Price - 84
        D11.0 Unit Price - 2
        D09.2 Unit Price - 1
        D10.2LM Unit Price - 1
        D15.2E Unit Price - 1
        D10.2B Unit Price - 2
        D10.2R Unit Price - 2
        D10.2% Unit Price - 2
        D10.2 Unit Price - 6
        """
        
        """F8 Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.1a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.1: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds02.xlsx', "Step 03.1: Expect to see '2of1000records,Page1of1'")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 1, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.1b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx', "Step 03.1c: Expect to see an 18 Page, 1000 line report with 13 columns.", desired_no_of_rows=20)
            
            
        """F6.0 Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.2a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.2: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds03.xlsx', "Step 03.2c: Expect to see 2of1000records,Page1of1")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 2, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.2b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.2c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F9.2 Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.3a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.3: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds04.xlsx', "Step 03.3c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 3, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.3b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.3c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F9.2LM Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.4a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.4: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds05.xlsx', "Step 03.4c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 4, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.4b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.4c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F9.2E Unit Price - 84"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.5a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.5: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds06.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds06.xlsx', "Step 03.5c: Expect to see 84of1000records,Page1of2.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 5, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.5b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.5c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F9.2B Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.6a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.6: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds07.xlsx', "Step 03.6c: Expect to see 2of1000records,Page1of1")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 6, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.6b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.6c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F9.2R Unit Price - 1"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.7a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.7: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds08.xlsx', "Step 03.7c: Expect to 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 7, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.7b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.7c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F7.2% - 84"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.8a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.8: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds09.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds09.xlsx', "Step 03.8c: Expect to see 84of1000records,Page1of2.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 8, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.8b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.8c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """F7.2 Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.9a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.9: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds10.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds10.xlsx', "Step 03.9c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 9, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.9b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.9c: Expect to see an 18 Page, 1000 line report with 13 columns.")
           
            
            
        """D8 Unit Price - 84"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 03.10a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.10: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds11.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds11.xlsx', "Step 03.10c: Expect to see 84of1000records,Page1of2.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 10, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.10b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.10c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """D11.0 Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.11a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.11: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds12.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds12.xlsx', "Step 03.11c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 11, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.11b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.11c: Expect to see an 18 Page, 1000 line report with 13 columns.")
           
        """D09.2 Unit Price - 1"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.12a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.12: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds13.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds13.xlsx', "Step 03.12c: Expect to see 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 12, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.12b:  Expect to see the following Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0','I0r','C2227982_Ds01.xlsx', "Step 03.12c: Expect to see an 18 Page, 1000 line report with 13 columns.")
            
        """D10.2LM Unit Price - 1"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 13, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.13a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.13: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds14.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds14.xlsx', "Step 03.13c: Expect to see 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 13, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.13b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.13: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.13c: Expect to see an 18 Page, 1000 line report with 13 columns.")
          
        """D10.2E Unit Price - 1"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 14, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 03.14a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.14: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds15.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds15.xlsx', "Step 03.14c: Expect to see 1of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 14, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.14b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.14: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.14c: Expect to see an 18 Page, 1000 line report with 13 columns.")
          
        """D10.2B Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 15, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.15a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.15: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds16.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds16.xlsx', "Step 03.15c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 15, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.15b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.15: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.15c: Expect to see an 18 Page, 1000 line report with 13 columns.")
          
        """D10.2R Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 16, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.16a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.16: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds17.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds17.xlsx', "Step 03.16c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 16, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.16b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.16: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.16c: Expect to see an 18 Page, 1000 line report with 13 columns.")
          
        """D10.2% Unit Price - 2"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 17, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 03.17a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.17: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds18.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds18.xlsx', "Step 03.17c: Expect to see 2of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 17, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.17b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.17: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.17c: Expect to see an 18 Page, 1000 line report with 13 columns.")
          
        """D10.2 Unit Price - 6"""
        miscelanousobj.select_field_menu_items("ITableData0", 0, 18, "Filter Cell")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '6of1000records,Page1of1', "Step 03.18a:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.18: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds19.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds19.xlsx', "Step 03.18c: Expect to see 6of1000records,Page1of1.")
        miscelanousobj.select_field_menu_items("ITableData0", 0, 18, "Remove Cell Filter")
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 03.18b:  Expect to see the following Active Report. - page summary verification")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 03.18: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds01.xlsx',"Step 03.18c: Expect to see an 18 Page, 1000 line report with 13 columns.")
         
        """
        Step 04: For the F8 Unit Price column drop down, select the Filter option.
        Select Equals, then select values 24, 48 & 59.
        Click the Filter button.
        Expect to see the following 4 row filtered report.
        """
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='24',value2='48',value3='59')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4of1000records,Page1of1', "Step 04.1: Expect to see a 3 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 04: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds20.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds20.xlsx', "Step 04: Expect to see 4of1000records,Page1of1.")
        time.sleep(2)
            
        """
        Step 05: Clear the previous filter panel.
        For the F6.0 Unit Price column drop down, select the Filter option.
        Select Not Equal, then select values 59 & 60.
        Click the Filter button.
        Expect to see the following 997 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 05:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter", "Not equal")
        filterselectionobj.create_filter(1, 'Not equal','large',value1='59.',value2='60.')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '997of1000records,Page1of18', "Step 05.1: Expect to see a 820 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 05: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds21.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds21.xlsx', "Step 05: Expect to see 997of1000records,Page1of18.")
        time.sleep(2)
         
        """
        Step 06: Clear the previous filter panel.
        For the F9.2 Unit Price column drop down, select the Filter option.
        Select Greater than, then select value 100.
        Click the Filter button.
        Expect to see the following 956 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 06:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter", "Greater than")
        filterselectionobj.create_filter(1, 'Greater than','large',value1='100.00')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '956of1000records,Page1of17', "Step 06.1: Expect to see a 956 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 06: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds22.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds22.xlsx', "Step 06: Expect to see 956of1000records,Page1of17.")
        time.sleep(2)
        
        """
        Step 07: Clear the previous filter panel.
        For the F9.2LM Unit Price column drop down, select the Filter option.
        Select Greater than or equal, then select value $000,144.50.
        Click the Filter button.
        Expect to see the following 919 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 07:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter", "Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to','large',value1='$000,144.50')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '919of1000records,Page1of17', "Step 07.1: Expect to see a 919 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 07: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds23.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds23.xlsx', "Step 07: Expect to see 919of1000records,Page1of17.")
        time.sleep(2)
        
        """
        Step 08: Clear the previous filter panel.
        For the F9.2E Unit Price column drop down, select the Filter option.
        Select Less than, then select value 0.76E+02.
        Click the Filter button.
        Expect to see the following 549 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 08:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        filterselectionobj.create_filter(1, 'Less than',value1='0.76E+02')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '549of1000records,Page1of10', "Step 08.1: Expect to see a 549 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 08: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds24.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds24.xlsx', "Step 08: Expect to see 549of1000records,Page1of10.")
        time.sleep(2)
        
        """
        Step 09: Clear the previous filter panel.
        For the F9.2B Unit Price column drop down, select the Filter option.
        Select Less than or equal to, then select value (1000.00).
        Click the Filter button.
        Expect to see the following 62 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 09:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to','large',value1='(1000.00)')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '62of1000records,Page1of2', "Step 09.1: Expect to see a 62 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 09: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds25.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds25.xlsx', "Step 09: Expect to see 62of1000records,Page1of2.")
        time.sleep(2)
        
        """
        Step 10: Clear the previous filter panel.
        For the F9.2R Unit Price column drop down, select the Filter option.
        Select Between, then select 595.00CR for the first value and 555.00CR for the second value.
        Click the Filter button.
        Expect to see the following 30 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 10:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter", "Between")
        filterselectionobj.create_filter(1, 'Between','large',value1='595.00 CR',value2='555.00 CR')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '30of1000records,Page1of1', "Step 10.1: Expect to see a 30 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 10: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds26.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds26.xlsx', "Step 10: Expect to see 30of1000records,Page1of1.")
        time.sleep(2)
        
        """
        Step 11: Clear the previous filter panel.
        For the F7.2% Unit Price column drop down, select the Filter option.
        Select Not Between, then select 17.00% for the first value and 125.00% for the second value.
        Click the Filter button.
        Expect to see the following 151 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 11:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter", "Not Between")
        filterselectionobj.create_filter(1, 'Not Between',value1='17.00%',value2='125.00%')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '151of1000records,Page1of3', "Step 11.1: Expect to see a 151 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 11: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds27.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds27.xlsx', "Step 11: Expect to see 151of1000records,Page1of3.")
        time.sleep(2)
        
        """
        Step 12: Clear the previous filter panel.
        For the F7.2 Unit Price column drop down, select the Filter option.
        Select Equals, then select value 75.50.
        Click the Filter button.
        Expect to see the following 2 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 12:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='75.50')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 12.1: Expect to see a 2 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 12: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds28.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds28.xlsx', "Step 12: Expect to see 2of1000records,Page1of1.")
        time.sleep(2)
        
        """
        Step 13: Clear the previous filter panel.
        For the D8 Unit Price column drop down, select the Filter option.
        Select Equals, then select values 13, 58 & 140.
        Click the Filter button.
        Expect to see the following 235 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 13:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals',value1='13',value2='58',value3='140')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '235of1000records,Page1of5', "Step 13.1: Expect to see a 235 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 12: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds29.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds29.xlsx', "Step 13: Expect to see 235of1000records,Page1of5.")
        time.sleep(2)
        
        """
        Step 14: Clear the previous filter panel.
        For the D11.0 Unit Price column drop down, select the Filter option.
        Select Not Equal, then select values 46, 50 & 55.
        Click the Filter button.
        Expect to see the following 993 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 14:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "11", "Filter", "Not equal")
        filterselectionobj.create_filter(1, 'Not equal','large',value1='46.',value2='50.',value3='55.')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '993of1000records,Page1of18', "Step 14.1: Expect to see a 993 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 14: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds30.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds30.xlsx', "Step 14: Expect to see 993of1000records,Page1of18.")
        time.sleep(2)
        
        
        """
        Step 15: Clear the previous filter panel.
        For the D09.2c Unit Price column drop down, select the Filter option.
        Select Greater than, then select value 14.99.
        Click the Filter button.
        Expect to see the following 969 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 15:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "12", "Filter", "Greater than")
        filterselectionobj.create_filter(1, 'Greater than','large',value1='14.99')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '969of1000records,Page1of17', "Step 15.1: Expect to see a 969 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 15: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds31.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds31.xlsx', "Step 15: Expect to see 969of1000records,Page1of17.")
        time.sleep(2)
        
        """
        Step 16: Clear the previous filter panel.
        For the D15.2LM Unit Price column drop down, select the Filter option.
        Select Greater than or equal to, then select value
        $000,000,014.99.
        Click the Filter button.
        Expect to see the following 970 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 16:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "13", "Filter", "Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to','large',value1='$000,000,000,014.99')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '970of1000records,Page1of18', "Step 16.1: Expect to see a 970 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 16: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds32.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds32.xlsx', "Step 16: Expect to see 970of1000records,Page1of18.")
        time.sleep(2)
        
        """
        Step 17: Clear the previous filter panel.
        For the D10.2E Unit Price column drop down, select the Filter option.
        Select Less than, then select the first occurrence of
        0.14D+02
        Click the Filter button.
        Expect to see the following 6 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 17:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "14", "Filter", "Less than")
        filterselectionobj.create_filter(1, 'Less than','large',value1='0.14D+02')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '6of1000records,Page1of1', "Step 17.1: Expect to see a 6 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 17: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds33.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds33.xlsx', "Step 17: Expect to see 6of1000records,Page1of1.")
        time.sleep(2)
        
        """
        Step 18: Clear the previous filter panel.
        For the D10.2B Unit Price column drop down, select the Filter option.
        Select Less than or equal to, then select value (635.00)
        Click the Filter button.
        Expect to see the following 18 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 18:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "15", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, 'Less than or equal to','large',value1='(635.00)')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '18of1000records,Page1of1', "Step 18.1: Expect to see a 18 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 18: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds34.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds34.xlsx', "Step 18: Expect to see 18of1000records,Page1of1.")
        time.sleep(2)
        
        """
        Step 19: Clear the previous filter panel.
        For the D10.2R Unit Price column drop down, select the Filter option.
        Select Between, then select 635.00 CR for the first value and 600.00 CR for the second value.
        Click the Filter button.
        Expect to see the following 25 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 19:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "16", "Filter", "Between")
        filterselectionobj.create_filter(1, 'Between','large',value1='635.00 CR',value2='600.00 CR')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '25of1000records,Page1of1', "Step 19.1: Expect to see a 25 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 19: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds35.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds35.xlsx', "Step 19: Expect to see 25of1000records,Page1of1.")
        time.sleep(2)
        
        """
        Step 20: Clear the previous filter panel.
        For the D10.2% Unit Price column drop down, select the Filter option.
        Select Not Between, then select 20.40% for the first value and 51.00% for the second value.
        Click the Filter button.
        Expect to see the following 897 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 20:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "17", "Filter", "Not Between")
        filterselectionobj.create_filter(1, 'Not Between','large',value1='20.40%',value2='51.00%')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '897of1000records,Page1of16', "Step 20.1: Expect to see a 897 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 20: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds36.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds36.xlsx', "Step 20: Expect to see 897of1000records,Page1of16.")
        time.sleep(2)
        
        """
        Step 21: Clear the previous filter panel.
        For the D10.2B Unit Price column drop down, select the Filter option.
        Select Equals, then select value 50.00.
        Click the Filter button.
        Expect to see the following 2 row filtered report.
        """
        filterselectionobj.close_filter_dialog()
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 21:  Expect to see the following Active Report. - page summary verification")
        miscelanousobj.select_menu_items("ITableData0", "18", "Filter", "Equals")
        filterselectionobj.create_filter(1, 'Equals','large',value1='50.00')
        time.sleep(2)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 21.1: Expect to see a 2 row report.")
        heading=['Order Number INTEGER', 'F8 Unit Price', 'F6.0 Unit Price', 'F9.2 Unit Price', 'F9.2LM Unit Price', 'F9.2E Unit Price', 'F9.2B Unit Price', 'F9.2R Unit Price', 'F7.2% Unit Price', 'F7.2 Unit Price', 'D8 Unit Price', 'D11.0 Unit Price', 'D09.2c Unit Price', 'D15.2LM Unit Price', 'D10.2E Unit Price', 'D10.2B Unit Price', 'D10.2R Unit Price', 'D10.2% Unit Price', 'D10.2 Unit Price']
        miscelanousobj.verify_column_heading('ITableData0', heading,'Step 21: Verify column heading')
        utillobj.create_data_set('ITableData0','I0r', 'C2227982_Ds37.xlsx')
        utillobj.verify_data_set('ITableData0','I0r', 'C2227982_Ds37.xlsx', "Step 21: Expect to see 2of1000records,Page1of1.")
        time.sleep(2)
        filterselectionobj.close_filter_dialog()
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()