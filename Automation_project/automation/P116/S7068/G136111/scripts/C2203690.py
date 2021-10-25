'''
Created on Sep 23, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203690 
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest
import time
from selenium.webdriver import ActionChains



class C2203690_TestClass(BaseTestCase):

    def test_C2203690(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2203690'
        """
            Step 01: Execute the attached fex, 149857.fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login("149857.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18')
        column=['COUNTRY','CAR','DEALER_COST','RETAIL_COST','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 149857.fex")
        utillobj.verify_data_set('ITableData0','I0r','149857.xlsx',"Step 01.3: Verify 149857.fex dataset")      
        
        """
        Step 02: Click on Car column and select Filter.
        Select Values equals to "Jaguar" and click on Filter. 
        """
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        filterselectionobj.create_filter(1, 'Equals', value1='JAGUAR')
        filterselectionobj.filter_button_click('Filter')
        miscelanousobj.move_active_popup("1", "600", "200")
        miscelanousobj.verify_page_summary('0','2of18records,Page1of1', 'Step 02.1: Verify Page summary 2of18')
        utillobj.verify_data_set('ITableData0','I0r','C2203690_Ds01.xlsx',"Step 02.2: Verify dataset of filter equals JAGUAR")      
        
        """
        Step 03: Now after filtering click on Car column and click on "Restore Original".
        """
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 1, 'Restore Original')
        
        """
        Step 04: Verify filter window is closed and report is reverted back to original.
        """
        utillobj.verify_data_set('ITableData0','I0r','149857.xlsx',"Step 04.1: Verify dataset after Restore original")      
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        