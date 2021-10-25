'''
Created on Aug 17, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050454
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050454_TestClass(BaseTestCase):

    def test_C2050454(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the attached repro - 144126.fex
        """
        utillobj.active_run_fex_api_login("144126.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 144126.fex and Verify the Report Heading')
        column_list=['RETAIL_COST','DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 144126.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','144126.xlsx','Step 01.3: Expect to see the  Active Report')
        
        """
        Step 02: From Dealer cost select->calculate and click %of Total
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Calculate','% of Total')
        utillobj.verify_data_set('ITableData0','I0r','C2050454_Ds01.xlsx','Step 02: Expect to see the %of Total column')
    
        """
        Step 03: Again Select Dealer cost and select calcuatle and click Clear/Clear All option
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Calculate','Clear All')
        utillobj.verify_data_set('ITableData0','I0r','144126.xlsx','Step 03: Verify calculated column not display')
        
        
if __name__ == '__main__':
    unittest.main()           
