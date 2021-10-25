'''
Created on JUN 19, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2308027
TestCase Name = AHTML:Cache:VAL:Applying Visualization shows "Undefined"report (ACT-613)
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_run
from common.lib import utillity

class C2308027_TestClass(BaseTestCase):

    def test_C2308027(self):
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
            Step 01:Execute the attached AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7073','mrid','mrpass')
        parent_css="table[id='ITableData0'] tr[id^='I0r']"
        utillobj.synchronize_with_number_of_element(parent_css, 57, expire_time=50)
        miscelaneous_obj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.01: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2308027_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2308027_Ds01.xlsx',"Step 01.02: AR-RP-001.fex data verification")
        """
            Step 02:Click down arrow for Dollar Sales, and click visualize option.
        """
        miscelaneous_obj.select_menu_items('ITableData0', 5, 'Visualize')
        time.sleep(10)
        
        """
            Step 03:Check the reports are visualized.
        """
        miscelaneous_obj.verify_visualization('ITableData0', 'I0r', 5, 'light_gray', 'Step 03.01: Verify visualization added')
        
        """
            Step 04:Click dropdown from any fields and select Restore original     
        """
        miscelaneous_obj.select_menu_items('ITableData0', 5, 'Restore Original')
        time.sleep(5)
        
        """
            Step 05:Verify restore original revert back to the original report.
        """
        miscelaneous_obj.verify_page_summary('0','107of107records,Page1of2', 'Step 05.01: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2308027_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2308027_Ds02.xlsx',"Step 05.02: AR-RP-001.fex data verification")

if __name__ == '__main__':
    unittest.main()
