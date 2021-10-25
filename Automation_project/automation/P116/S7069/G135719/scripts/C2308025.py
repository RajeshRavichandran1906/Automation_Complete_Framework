'''
Created on JUN 19, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2308025
TestCase Name = AHTML:Cache:VAL:Applying Calculate option shows"Undefined"report (ACT-614)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_run
from common.lib import utillity


class C2308025_TestClass(BaseTestCase):

    def test_C2308025(self):
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        """
            Step 01:Execute the attached AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7069','mrid','mrpass')
        parent_css="#MAINTABLE_wbody0 span[title='Move to Top'] img"
        resobj.wait_for_property(parent_css, 1) 
        miscelaneous_obj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2308025_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2308025_Ds01.xlsx',"Step 01.2: AR-AHTML-001.fex data verification")
        """
            Step 02:Click the down arrow for Dollar Sales >Calculate->Sum
        """
        miscelaneous_obj.select_menu_items('ITableData0', 5, 'Calculate','Sum')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2308025_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2308025_Ds02.xlsx',"Step 02: verify total sum values")
        """
            Step 03:Now from any field dropdown click restore original.
        """
        miscelaneous_obj.select_menu_items('ITableData0', 5, 'Restore Original')
        time.sleep(2)
        """
            Step 04:Verify restore original revert back to the original report
        """
        miscelaneous_obj.verify_page_summary('0','107of107records,Page1of2', 'Step 04.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2308025_Ds03.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2308025_Ds03.xlsx',"Step 04.2: AR-AHTML-001.fex data verification")
        
if __name__ == '__main__':
    unittest.main()
