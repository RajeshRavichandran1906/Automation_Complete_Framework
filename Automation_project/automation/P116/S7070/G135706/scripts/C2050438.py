'''
Created on Aug 11, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050438
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050438_TestClass(BaseTestCase):

    def test_C2050438(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        1. Execute the AHTML_report.fex
        """
        utillobj.active_run_fex_api_login("97175.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the 97175.fex and Verify the Report Heading')
        column_list=['COUNTRY','CAR','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 97175.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '97175.xlsx','Step 01.3: Expect to see the  Active Report')
        
        """
        Step 02: From SALES dropdown, select Sort SALES ascending.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050438_Ds01.xlsx','Step 02: Expect to see the  Active Report')
        
        """
        Step 03: Apply Pivot on Sales > BY COUNTRY > ACROSS CAR.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Pivot (Cross Tab)','COUNTRY','CAR')
        
        """
        Step 04: Verify the values from the report and pivot are same and do not change.
        """
        
        utillobj.verify_pivot_data_set('piv1', 'C2050438_Ds02.xlsx', 'Step 04: Verify the values from the report and pivot are same and do not change.')
        
        
if __name__ == '__main__':
    unittest.main()    
    