'''
Created on Aug 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050441
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050442_TestClass(BaseTestCase):

    def test_C2050442(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the 154865.fex.
        """
        utillobj.active_run_fex_api_login("154865.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '15of15records,Page1of1', 'Step 01.1: Execute the 154865.fex and Verify the Report Heading')
        column_list=['SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 154865.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '154865.xlsx','Step 01.3:Verify report should get displayed without any scripting errors and contain a single column of Sales data, in Ascending order')
if __name__ == '__main__':
    unittest.main()