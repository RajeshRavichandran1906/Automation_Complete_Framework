'''
Created on Aug 24, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053871
TestCase Name = Verify Rollup table is generated
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup
from common.lib import utillity

class C2053871_TestClass(BaseTestCase):

    def test_C2053871(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053871'
        """
            Step 01: Execute the attached 121427.fex
        """
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        utillobj.active_run_fex_api_login('121427.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18')
        column=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 121427")
        utillobj.verify_data_set('ITableData0','I0r','121427.xlsx',"Step 01.3: Verify 121427 dataset")        
        
        """
        Step 02: From the SALES column, click on drop down menu and select ROLLUP -> BODYTYPE (Group By(X)(SUM))
        """
        active_misobj.select_menu_items('ITableData0', 7, 'Rollup','BODYTYPE')
        active_misobj.verify_page_summary('1','5of5records,Page1of1', 'Step 02.1: Verify Page summary 5of5')
        column=['BODYTYPE','SALES']
        active_misobj.verify_column_heading('ITableData1', column, "Step 02.2: Verify Column heading after rollup")        
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds01.xlsx',"Step 02.2: Verify all the matching records for rollup BODYTYPE")
        
        """
        Step 03: In the Rollup window, click on aggregation icon (SUM) and select AVG option
        """
        rollobj.select_aggregate_function('wall1', 0, 'Avg', verify=True)
        """Verify the changes on aggregation function SUM to AVG/MIN/MAX/COUNT/DISTINCT should not throw IE error."""
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds02.xlsx',"Step 03.1: Verify all the matching records for rollup BODYTYPE Avg")
        rollobj.select_aggregate_function('wall1', 1, 'Min', verify=True)
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds03.xlsx',"Step 03.2: Verify all the matching records for rollup BODYTYPE Min")
        rollobj.select_aggregate_function('wall1', 1, 'Max', verify=True)
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds04.xlsx',"Step 03.3: Verify all the matching records for rollup BODYTYPE Max")
        rollobj.select_aggregate_function('wall1', 1, 'Count', verify=True)
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds05.xlsx',"Step 03.4: Verify all the matching records for rollup BODYTYPE Count")
        rollobj.select_aggregate_function('wall1', 1, 'Distinct', verify=True)
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds06.xlsx',"Step 03.5: Verify all the matching records for rollup BODYTYPE Distinct")

if __name__ == '__main__':
    unittest.main()