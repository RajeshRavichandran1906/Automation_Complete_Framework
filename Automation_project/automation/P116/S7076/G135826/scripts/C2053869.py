'''
Created on Aug 23, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053869
TestCase Name = Verify Rollup table is generated
'''
import unittest
from common.lib import utillity
from common.pages import active_miscelaneous
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart

class C2053869_TestClass(BaseTestCase):

    def test_C2053869(self):
        
        """
            CLASS OBJECTS
        """
        active = Active_Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
#         rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053869'
        
        """
            Step 01: Execute the 89965.fex
        """
        utillobj.active_run_fex_api_login('89965.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01: Verify Page summary 18of18')
        column=['CAR','COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 89965")
        utillobj.verify_data_set('ITableData0','I0r','89965.xlsx',"Step 01.3: Verify 89965 dataset")        
        
        """
        Step 02: Select Rollup option from RETAIL_COST BY COUNTRY
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Rollup','COUNTRY')
        active_misobj.verify_page_summary('1','5of5records,Page1of1', 'Step 02.1: Verify Page summary 5of5')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify all the matching records for rollup COUNTRY")
        
        """
        Step 03: Add sales column in Y axis
        """
#         rollobj.create_new_item(0, 'Add (Y)->SALES')
        active.create_new_item('wall1', 'Add (Y)->SALES')
        column=['COUNTRY','RETAIL_COST','SALES']
        active_misobj.verify_column_heading('ITableData1', column, "Step 03.1: Verify Column heading of 89965")
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds02.xlsx',"Step 03.2: Verify all the matching records for rollup COUNTRY, ADD(Y)-> SALES")
        
if __name__ == '__main__':
    unittest.main()