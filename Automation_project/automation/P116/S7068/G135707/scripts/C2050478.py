'''
Created on Jul 18, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050478
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050478_TestClass(BaseTestCase):

    def test_C2050478(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050478'
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
            Step 02: Select State > Filter > Equals
            Verify Filter selection pop up is opened Verify user has following options: 
            1. Operatior: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All
        """
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        
        option=['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        filterselectionobj.verify_filter_buttons(option, "Step 03: Verify Filter selection pop up")
        """
        Step 03: Select "MA" value in this test. Click 'Add condition' dropdown menu
        Verify all the columns are displayed: - 
        Category - Product ID - Product - State - Unit Sales - Dollar Sales See attached screenshot.
        """
        filterselectionobj.create_filter(1, "Equals", "small",value1="MA")
        
        condition_dropdown=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        filterselectionobj.verify_add_condition_menu(condition_dropdown, 'Step 03: Verify all the columns are displayed')
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        