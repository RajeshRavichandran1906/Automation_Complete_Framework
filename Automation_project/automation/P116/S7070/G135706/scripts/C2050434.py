'''
Created on Aug 8, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050434
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050434_TestClass(BaseTestCase):

    def test_C2050434(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute attached repro 122250.
    
        Expect to see a 12 row report with two Curr_Sal fields. Missing values are indicated by the underscore character '_'.
        Expect Missing data for the MIS Department for BANNING, IRVING, MCKNIGHT, ROMANS, RICHARD SMITH & STEVENS.
        Expect to see the exact opposite for the PRODUCTION Department, all that were not Missing from the MIS Department.
        """
        utillobj.active_run_fex_api_login("122250.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '12of12records,Page1of1', 'Step 01.1: Execute the 122250.fex and Verify the Report Heading')
        column_list=['LAST_NAME', 'FIRST_NAME', 'CURR_SAL', 'CURR_SAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 122250.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050434_Ds01.xlsx', 'Step 01.3: Verify entire table data with missing data indicated by underscore.')
        """
        2. Select the Active drop down arrow for the first CURR_SAL field and select the first option - Ascending Sort

        Expect to see the Missing valued rows sort to the top of the report.
        Expect to see the same Missing data character appear for the same names for the same Departments.
        Missing data values always sort to the top of a list.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050434_Ds02.xlsx', 'Step 02.1: Verify data under Dollar sales are sorted in descending order.')

        
if __name__ == '__main__':
    unittest.main()