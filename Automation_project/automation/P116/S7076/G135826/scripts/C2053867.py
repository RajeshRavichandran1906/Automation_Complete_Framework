'''
Created on Aug 23, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053867
TestCase Name = Verify Rollup table is generated
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2053867_TestClass(BaseTestCase):

    def test_C2053867(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053867'
        """
            Step 01: Execute the AR-RP-001.fex
        """
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """
        Step 02: Click State > Rollup > Group By Product.
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Rollup','Product')        
         
        """Verify that 'State By Product' pop up window opened with the columns selected for the table.l"""
        active_misobj.verify_page_summary('1','10of10records,Page1of1', 'Step 02.1: Verify Page summary 10of10')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify all the matching records for rollup")

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
