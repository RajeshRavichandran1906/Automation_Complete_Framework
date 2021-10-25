'''
Created on Aug 10, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050437
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050437_TestClass(BaseTestCase):

    def test_C2050437(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        1. Execute the AHTML_report.fex
        """
        utillobj.active_run_fex_api_login("99966.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 99966.fex and Verify the Report Heading')
        column_list=['CAR','COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 99966.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '99966.xlsx','Step 01: Expect to see the  Active Report')

        """
        Step 02: Once the ACTIVE Report appears on screen, select the CAR column sorting arrow, and re-sort the report by Descending order.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Descending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050437_Ds01.xlsx', 'Step 02: Expect to see the Active Report sorted in Descending CAR order')

        """
        STep 03: Select the COUNTRY column sorting arrow, and re-sort the report by Ascending order.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050437_Ds02.xlsx', 'Step 02: Expect to see the Active Report sorted in Ascending COUNTRY order')

        """
        Step 04: Select the DEALER_COST column sorting arrow, and re-sort the report by Descending order.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Sort Descending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050437_Ds03.xlsx', 'Step 02: Expect to see the Active Report sorted in Descending DEALER_COST order')


if __name__ == '__main__':
    unittest.main()














