'''
Created on Aug 8, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050542
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050542_TestClass(BaseTestCase):

    def test_C2050542(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050542'
        """
            Step 01: Execute repro 10903522.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("10903522.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute 10903522.fex")
        
        utillobj.verify_data_set('ITableData0', 'I0r', '10903522.xlsx',"Step 01: Verify table")
        columns1=['COUNTRY','CAR','MODEL','SALES']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')
        
        """
        Step 02: click on down arrow next to COUNTRY / select Filter / use default of EQ / click on down arrow to select a value.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        
        values = ['NA','FRANCE','ITALY','JAPAN','W GERMANY']
        filterselectionobj.verify_filter_values_menu_list(1, values, 'Step 02:  Verify that it says NA and not [MISSING]')
        
if __name__ == '__main__':
    unittest.main() 
    