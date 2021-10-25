'''
Created on Jul,18 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050466
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050466_TestClass(BaseTestCase):

    def test_C2050466(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050466'
        
        """Step 01: Execute the AR-RP-001.fex"""
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Verify output summary'
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        
        """Step 02: Select Dollar Sales > Filter > Between""" 
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Between")
        time.sleep(4)
        #Verify Filter selection pop up is opened.
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 02: Verify Filter selection pop up is opened.',['Dollar Sales', 'Between', '['])
        """Step 03 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All"""
        _step03 = 'Step 04 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All'
        
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], _step03)
        
        """Step 04 : Click dropdown next to <Value> (for Dollar sales column)"""
        
        #Verify all the values under selected column are listed
        
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Select Filter > Equals', ['Dollar Sales', 'Between', '['])
        
        """Step 05  : Select "606079" value in this test"""
        
        filterselectionobj.create_filter(1, 'Between','large', value1='349300', value2='587887')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)

        """ Step 06: Click Filter.  """
        _step06 = 'Step 06:Verify 29 matching records are displayed under a report.'
        
        miscelanousobj.verify_page_summary('0','29of107records,Page1of1', _step06+'page summary')
        
        utillobj.verify_data_set('ITableData0','I0r','C2050466_Ds01.xlsx',_step06)
        #utillobj.create_data_set('ITableData0','I0r','C2050466_Ds01.xlsx')
        
        
        
if __name__ == '__main__':
    unittest.main()