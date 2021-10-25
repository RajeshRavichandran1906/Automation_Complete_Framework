'''
Created on Aug 02, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054132
TestCase Name = Verify selected column is hidden
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2054132_TestClass(BaseTestCase):

    def test_C2054132(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the AR-AHTML-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2054132_Ds_01.xlsx',"Step 01.c: Verify entire Data set in Page 1") 
        """
        Step 02: Click drop down menu for Unit Sales column > Hide Column
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Hide Column')        
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 02.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.b: Verify the Unit Sales column hidden')
        utillobj.verify_data_set('ITableData0','I0r','C2054132_Ds_02.xlsx',"Step 02.c: Verify Unit_Sales Data not displayed in Page 1")  
        """
        Step 03: Click the drop down for Category, select show columns and select Unit Sales.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Show Columns','Unit Sales')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 03.a: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.b: Verify the Unit Sales column displayed')
        utillobj.verify_data_set('ITableData0','I0r','C2054132_Ds_01.xlsx',"Step 03.c: Verify entire Data set in Page 1") 
                

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
