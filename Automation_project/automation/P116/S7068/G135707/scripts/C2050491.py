'''
Created on Jul 22, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050491
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050491_TestClass(BaseTestCase):

    def test_C2050491(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050491'
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
            Step 02: Select Unit Sales > Calculate > Max
            Verify Total Max is applied for Unit Sales column and same is displayed under the column heading Verify the value: Total Max 141,403
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Calculate","Max")
        miscelanousobj.verify_calculated_value(2, 5, "Total Max 141403", True, 'Step 02: Verify Total Max is applied for Unit Sales column and same is displayed under the column headin')
        """
            Step 03: Select Unit Sales > Filter > Less Than or equal to
            Verify Filter Selection pop up appears
        """
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Less than or equal to")
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Verify Filter Selection pop up appears',['Unit Sales','Less than or equal to'])
        """
            Step 04: Click Value dropdown menu and select "59763" Click Filter option
            Verify that Unit Sales column heading shows : Filtered Max 59,763(42.26%) Total Max 141,403 Pagination shows: SUB/TOT See attached screenshot.
        """
        filterselectionobj.create_filter(1, 'Less than or equal to','large',value1= '59763')
        filterselectionobj.filter_button_click('Filter')
        
        miscelanousobj.verify_calculated_value(2, 5, 'Filtered Max 59763(42.26%)\nTotal Max 141403', True, "Step 04:  Verify that Unit Sales column heading shows : Filtered Max 59,763(42.26%) Total Max 141,403")

        miscelanousobj.verify_page_summary(0, 'SUB/TOT94of107records,Page1of2', 'Step 04: Verify Pagination shows: SUB/TOT')

        utillobj.verify_data_set('ITableData0','I0r', 'C2050491_Ds01.xlsx',"Step 04: Verify table")

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    