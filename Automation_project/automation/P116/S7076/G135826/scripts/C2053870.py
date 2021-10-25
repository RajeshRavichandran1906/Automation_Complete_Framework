'''
Created on Aug 23, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053870
TestCase Name = Verify Rollup table is generated
'''
import unittest
from common.lib import utillity
from common.pages import active_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart

class C2053870_TestClass(BaseTestCase):

    def test_C2053870(self):
        
        """
            CLASS OBJECTS
        """
        active = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053870'
        
        """
            Step 01: Execute the 90298.fex
        """
        utillobj.active_run_fex_api_login('90289.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','448of448records,Page1of8', 'Step 01: Verify Page summary 448of448')
        column=['EMP_ID', 'FIRST_NAME', 'LAST_NAME', 'PAY_DATE', 'CURR_SAL', 'SALARY', 'DED_AMT']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 90289")
        utillobj.verify_data_set('ITableData0','I0r','90289.xlsx',"Step 01.3: Verify 90289 dataset")        
        
        """
        Step 02: Select Rollup option from CURR_SAL BY LAST_NAME
        """
        active_misobj.select_menu_items('ITableData0', 4, 'Rollup','LAST_NAME')
        active_misobj.verify_page_summary('1','11of11records,Page1of1', 'Step 02.1: Verify Page summary 11of11')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify all the matching records for rollup LASTNAME")
        
        """
        Step 03: In Rollup window from Toolbar deselect Add (Y)CURR_SAL
        """
#         rollobj.create_new_item(0, 'Add (Y)->CURR_SAL')
        active.create_new_item('wall1', 'Add (Y)->CURR_SAL')
        column=['LAST_NAME']
        active_misobj.verify_column_heading('ITableData1', column, "Step 03.1: Verify Column heading of rollup deselect")
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds02.xlsx',"Step 03.2: Verify all the matching records for rollup deselct CURR_SAL")

if __name__ == '__main__':
    unittest.main()