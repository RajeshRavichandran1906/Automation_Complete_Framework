'''
Created on Oct 5, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203729
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2203729_TestClass(BaseTestCase):

    def test_C2203729(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
            Step 02.Another example:
        """
        utillobj.active_run_fex_api_login("C2203729.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.1: Execute the C2203729.fex and Verify the Report Heading')
        column_list=['COUNTRY','CARX','CARZ']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the C2203729.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203729_Ds01.xlsx','Step 01.3: Expect to see the  Active Report')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()