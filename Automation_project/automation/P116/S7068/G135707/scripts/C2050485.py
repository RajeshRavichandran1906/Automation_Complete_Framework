'''
Created on Jul 21, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050485
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050485_TestClass(BaseTestCase):

    def test_C2050485(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050485'
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
            Step 02: Select Unit Sales > Calculate > Sum
            Verify Total Sum is applied for Unit Sales column and same is displayed under the column heading.
        """
        miscelanousobj.select_menu_items('ITableData0', '4', 'Calculate', 'Sum')
        miscelanousobj.verify_calculated_value('2', '5', "Total Sum 3688991", True,'Step 02: Verify Total Sum is applied for Unit Sales column and same is displayed under the column heading.')
        """
            Step 03: Select Unit Sales > Filter > Equals
            Verify Filter Selection pop up appears
        """
        miscelanousobj.select_menu_items('ITableData0', '4', 'Filter', 'Equals')
        filterselectionobj.verify_filter_selection_dialog('Step 03: Verify Filter Selection pop up appears',['Unit Sales', 'Equals'])
        """
            Step 04: Click Value dropdown menu and select "30157". Click Filter option
            Verify that Unit Sales column heading shows : Filtered Sum 30,157(0.82%) Total Sum 3,688,991 Pagination shows: SUB/TOT
        """
        filterselectionobj.create_filter(1, 'Equals','large', value1='30157')
        
        filterselectionobj.filter_button_click('Filter')
        
        miscelanousobj.move_active_popup('1', '600', '200')
        miscelanousobj.verify_calculated_value('2','5','Filtered Sum 30157(0.82%)\nTotal Sum 3688991',True,'Step 04: Verify that Unit Sales column heading shows : Filtered Sum 30,157(0.82%) Total Sum 3,688,991')
        
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, 'SUB/TOT1of107records,Page1of1', 'Step 04: Verify Pagination shows: SUB/TOT')
            
            
if __name__ == '__main__':
    unittest.main()       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            