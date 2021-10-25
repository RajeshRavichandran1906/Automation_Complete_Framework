'''
Created on Sep 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203638
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2203638_TestClass(BaseTestCase):

    def test_C2203638(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        Step 01: Execute the attached repro - 90213.fex:
        """
        utillobj.active_run_fex_api_login("90213.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 90213.fex and Verify the Report Heading')
        column_list=['MPG','WHEELBASE','BHP']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 90213.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '90213.xlsx', 'Step 01.3: Execute the 90213.fex and Verify the entire data')
        
        """
        Step 02: For the MPG column drop down, select Sort Ascending.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203638_Ds01.xlsx', 'Step 02.1: Expect to see the report sorted in ascending order of MPG & two duplicate values for 0')
        
        """
        Step 03: For the MPG column drop down, select Sort Descending.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Descending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2203638_Ds02.xlsx', 'Step 02.1: Expect to see the report sorted in descending order of MPG & two duplicate values for 24')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()