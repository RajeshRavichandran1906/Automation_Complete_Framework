'''
Created on Oct 31, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7077
Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053856
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time

class C2053866_TestClass(BaseTestCase):

    def test_C2053866(self):
        
        driver = self.driver #Driver reference object created'
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Copy the act-468-revised.fex for WV= ON and 21383540.fex for WV=OFF to your WF content folder
        """
        
        utillobj.active_run_fex_api_login("act-468-revised.fex", "S7077", 'mrid', 'mrpass')
        
        time.sleep(200)
        
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', "Step 01.1: Verify Page Summary")
        
        column_list=['Product Category', 'Product Subcategory', 'Quantity Sold', 'MSRP', 'TESTCOMP', 'Sale Unit(s)', 'Revenue Per Sq. Ft.', 'Store Open Number of Days Store Open']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-468-revised.xlsx','Step 01.3: Verify data set')
        
#         utillobj.create_data_set('ITableData0', 'I0r', 'act-468-revised.xlsx')
        
        """
        Step 02:Export to Excel. Make sure While exporting an active report to XML (Excel) format, the % compute field is getting exported properly.  
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','Excel','All records')
        
        time.sleep(7)
        
        utillobj.save_window('C2053866_actual_1')
        
       
        utillobj.create_excel('C2053866_actual_1.xlsx','C2053866_actual_1.xlsx')
        
        time.sleep(5)
        
        utillobj.verify_excel_sheet('C2053866_Base_1.xlsx', 'C2053866_actual_1.xlsx', 'Sheet1', 'Step 02: Expect to see the same currency symbols in the same location on each column as in the Active Report')
        utillobj.infoassist_api_logout()
        
        """Step 03: Verification for 21383540 WV OFF """
        
        utillobj.active_run_fex_api_login("21383540.fex", "S7077", 'mrid', 'mrpass')
    
        time.sleep(200)
        
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', "Step 03.1: Verify Page Summary")
        
        column_list=['Product Category', 'Product Subcategory', 'Quantity Sold', 'MSRP', 'TESTCOMP', 'Sale Unit(s)', 'Revenue Per Sq. Ft.', 'Store Open Number of Days Store Open']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 03.2: Verify all columns listed on the report')
        
        
        utillobj.verify_data_set('ITableData0', 'I0r', '21383540.xlsx','Step 01.3: Verify data set')
        
#         utillobj.create_data_set('ITableData0', 'I0r', '21383540.xlsx')     
        
        
        """
        Step 04: :Export to Excel. Make sure While exporting an active report to XML (Excel) format, the % compute field is getting exported properly.
       
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Export','XML (Excel)','All records')
        time.sleep(7)
        utillobj.save_window('C2053866_actual_2')
        time.sleep(5)
        utillobj.create_excel('C2053866_actual_2.xls','C2053866_actual_2.xlsx')
        time.sleep(5)
        utillobj.verify_excel_sheet('C2053866_Base_2.xlsx', 'C2053866_actual_2.xlsx', 'AHTML', 'Step 04: Expect to see the Excel spreadsheet')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()