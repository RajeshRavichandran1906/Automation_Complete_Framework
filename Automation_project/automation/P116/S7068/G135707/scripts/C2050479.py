'''
Created on Jul 19, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050479
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050479_TestClass(BaseTestCase):

    def test_C2050479(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050479'
        """
            Step 01: Execute the attached repro - AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Execute the AR-RP-001.fex")
        columns1=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """"
            Step 02: Using the drop down for State, select Filter/Equals, then pick the value of 'MA'.
            Expect to see the following Filter pane.
        """
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        filterselectionobj.create_filter(1, "Equals", "small",value1="MA")
        
        row1=['State','Equals','MA']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02: Expect to see Filter pane',row1)
        """
            Step 03: In the Filter pane, click Add Condition. Using the drop down for Product, select Not Equal, then pick the value of 'Latte'.
            Expect to see the additional Filter in the Filter pane.
        """
        filterselectionobj.add_condition_field("Product")
        filterselectionobj.create_filter(2, "Not equal", "small",value1="Latte")
        
        row2=['Product','Not equal','Latte']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Expect to see the additional Filter in the Filter pane.',row1,row2)
        """
            Step 04: In the Filter pane, click Add Condition. Using the drop down for Unit Sales, select Less Than, then pick the value of 14614.
            Expect to see the third Filter condition in the Filter pane.
        """
        filterselectionobj.add_condition_field("Unit Sales")
        filterselectionobj.create_filter(3, "Less than","large",value1="14614")
        
        row3=['Unit Sales','Less than','14614']
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 04:  Expect to see the third Filter condition in the Filter pane.',row1,row2,row3)
        """
            Step 05: Click the Filter button.
            Expect to see the following 1 row report.
        """ 
        filterselectionobj.filter_button_click('Filter')
        utillobj.verify_data_set('ITableData0','I0r','C2050479_Ds01.xlsx','Step 05: Expect to see the following 1 row report.')
        """
            Step 06: Click 'Clear All' button in the Filter selection pop up
            Verify that all the columns and filter options are wiped out from the pop up and result set is set to original 
        """
        filterselectionobj.filter_button_click('Clear All')
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 06:  Verify filter options are wiped out from the pop up',[])
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001_page1.xlsx',"Step 06: Verify result set is set to original")
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
