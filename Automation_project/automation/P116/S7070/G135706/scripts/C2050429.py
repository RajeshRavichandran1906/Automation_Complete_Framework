'''
Created on Aug 8, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050429
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050429_TestClass(BaseTestCase):

    def test_C2050429(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-AHTML-001.fex and Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-AHTML-001.fex and Verify the column heading')
        """
        2. Select Dollar Sales column and select 'Sort Descending' filter
        Verify data under Dollar Sales column are sorted in descending order and 
        corresponding data displayed correctly. See attached screenshot.
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Sort Descending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050429_Ds01.xlsx', 'Step 02.1: Verify data under Dollar sales are sorted in descending order.')
        
        """
        3. Click 'Restore Original' from the filter menu.
        Verify that report is set back to original state.

        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Restore Original')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050428_DS02.xlsx', 'Step 03.1: Verify that report is set back to original state.')
        
if __name__ == '__main__':
    unittest.main()