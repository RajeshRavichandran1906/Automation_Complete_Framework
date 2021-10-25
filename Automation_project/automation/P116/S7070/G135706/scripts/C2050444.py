'''
Created on Aug 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050444
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2050444_TestClass(BaseTestCase):

    def test_C2050444(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the 105369.fex.
        """
        utillobj.active_run_fex_api_login("105369.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 105369.fex and Verify the Report Heading')
        column_list=['DEALER_COST','COUNTRY','CAR','MODEL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 125381.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '105369.xlsx','Step 01.3: Expect to see the  Active Report')
        """
        Step 02: Select Dealer_Cost drop down --> sort descending
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Descending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050444_Ds01.xlsx','Step 02: Expect to see the report sorted in descending Dealer_Cost order')
        
        """
        Step 03: Select Dealer_Cost drop down --> sort ascending
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050444_Ds02.xlsx','Step 03: Expect to see the report sorted in descending Dealer_Cost order')
        """
        Step 04: Select Country drop down --> sort Ascending
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050444_Ds03.xlsx','Step 04: Expect to see the report sorted in ascending Country order')
        
if __name__ == '__main__':
    unittest.main()    
        
        
        
        
        
        
        
        
        
        
        
