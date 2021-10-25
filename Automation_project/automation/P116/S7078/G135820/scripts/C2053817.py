'''
Created on Aug 29, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053817
TestCase Name = Verify Pivot option shows Across columns
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2053817_TestClass(BaseTestCase):

    def test_C2053817(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        
        """
        Step 02: Click dropdown menu for State column and mouse over Pivot(Cross Tab) > any column (Category)
        """
        time.sleep(3)
        values=['Across', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)->Category', values, 'Step 02: Verify Across columns are displayed', all_items='yes')
        

if __name__ == '__main__':
    unittest.main()