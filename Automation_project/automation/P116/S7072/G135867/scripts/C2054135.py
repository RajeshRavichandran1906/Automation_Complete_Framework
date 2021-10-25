'''
Created on Aug 02, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054135
TestCase Description = Verify Show <column> shows particular hidden column
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2054135_TestClass(BaseTestCase):

    def test_C2054135(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2054135'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 1. Execute the AR-AHTML-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
         
        """
        Step 02: Click drop down menu for Unit Sales column > Hide Column
        Verify that Unit Sales column is no more visible on the report.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Hide Column')        
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 02.1: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.2: Verify that Unit Sales column is no more visible on the report')
        
        """
        Step 03: Click drop down menu for State column > Hide Column
        Verify that State column is no more visible on the report.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Hide Column')        
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 03.1: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 03.2: Verify that State column is no more visible on the report')
        """
        Step 04: Click drop down menu for Dollar Sales column > Show Columns > State.
        Verify that only State column is visible on the report.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Show Columns','State')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 04.1: Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04.2: Verify that only State column is visible on the report.')
        
if __name__ == '__main__':
    unittest.main()
