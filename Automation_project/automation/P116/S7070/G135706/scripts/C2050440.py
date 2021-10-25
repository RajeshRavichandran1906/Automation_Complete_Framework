'''
Created on Aug 11, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050440
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050440_TestClass(BaseTestCase):

    def test_C2050440(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the AR-RP-001.fex.
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex and Verify the Report Heading')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-RP-001.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050440_Ds01.xlsx','Step 01.3: Expect to see the  Active Report')
        
        """
        Step 02: Select Dollar Sales and select 'Sort Ascending' from dropdown option.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Sort Ascending')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050440_Ds02.xlsx','Step 02: Verify Sorted table')

        """
        Step 03: Select Unit Sales and select 'Sort Descending' from dropdown option.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Sort Descending')
        
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050440_Ds03.xlsx','Step 03: Verify Sorted table')

        """
        Step 04: Select Unit Sales and select calculate->sum from dropdown option.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Calculate','Sum')
        miscelanousobj.verify_calculated_value(2, 5, 'Total Sum 3688991', True, 'Step 04: Verify calculated-Sum value')
        
        """
        Step 05: Select Dollar Sales and select calculate->max from dropdown option.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Calculate','Max')
        miscelanousobj.verify_calculated_value(2, 6, 'Total Max 1745509', True, 'Step 05: Verify calculated-max value')
        miscelanousobj.verify_calculated_value(2, 5, 'Total Sum 3688991', True, 'Step 05: Verify calculated-Sum value')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050440_Ds03.xlsx','Step 05: Verify multiple sort displays as expected')
        
        
if __name__ == '__main__':
    unittest.main()    
        
        
    
        