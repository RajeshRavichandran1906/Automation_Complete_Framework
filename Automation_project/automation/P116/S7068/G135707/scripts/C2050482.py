'''
Created on Jul 21, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050482
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050482_TestClass(BaseTestCase):

    def test_C2050482(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050482'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Step 01: Execute the AR-RP-001.fex")
        columns1=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
            Step 02: Select Unit Sales > Calculate > Avg
            Verify Total Avg is applied for Unit Sales column and same is displayed under the column heading
        """
        miscelanousobj.select_menu_items('ITableData0', '4', 'Calculate', 'Avg')
        miscelanousobj.verify_calculated_value('2', '5', "Total Avg 34476", True, 'Step 02: Verify Total Avg is applied for Unit Sales column and same is displayed under the column heading')
        
        """
        Step 03: Select Unit Sales > Calaculate > Clear
        Verify calculation (Avg) is removed from the column and report is displayed in original form
        """
        miscelanousobj.select_menu_items('ITableData0', '4', 'Calculate', 'Clear')
        miscelanousobj.verify_calculated_value('2', '5', "Total Avg 34476", False, 'Step 03; Verify calculation (Avg) is removed from the column')
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        