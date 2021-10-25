
'''
Created on July 13, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055531
'''
__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity

class C2050460_TestClass(BaseTestCase):

    def test_C2050460(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(45) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050460'
        
        """Step 01: Execute the AR-RP-001.fex"""
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Verify output'
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        
        """Step 02: Select State > Filter""" 
        
        step02 = 'Step 02 : Verify user can move to next page by using the next page arrow (single arrow)'
        
        #Verify Filter menu shows all the filter options mentioned in the Test Description.
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',3,'Filter',option,step02)
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
        
        """Step 03: Select Filter > Not Equals"""
        
        #Verify Filter selection pop up is opened.
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Select Filter > Not Equals',['State', 'Not equal'])
        """Step 04 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All"""
        _step04 = 'Step 04 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All'
        
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], _step04)
        
        """Step 05 : Click dropdown next to <Value> (for State column)"""
        
        #Verify all the values under selected column are listed
        menu_list = ['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        filterselectionobj.verify_filter_values_menu_list(1, menu_list, 'Step 05 : Click dropdown next to <Value> (for State column)')
        
        """Step 06  :Select "CA ", "MA", "NY" values in this test (Use ctrl to apply multi selection for AFLEX/APDF) """
        
        filterselectionobj.create_filter(1, 'Not equal', value1='CA', value2='MA', value3='NY')
        
        filterselectionobj.filter_button_click('Filter')
        time.sleep(10)
        
        """ Step 07:Click Filter Verify all the records (77/107) except "CA", "MA", "NY" are displayed under a report.
                            Verify all selected options are checked under dropdown menu.  """
                            
        _step07 = 'Step 07: Verify all the records (77/107) except "CA", "MA", "NY" are displayed under a report.'
        miscelanousobj.verify_page_summary('0','77of107records,Page1of2', _step07 +"page summary verification")
        
        utillobj.verify_data_set('ITableData0','I0r','C2050460_Ds01.xlsx',_step07)
        
        #utillobj.create_data_set('ITableData0','I0r','C2050460_Ds01.xlsx')
        
       
        
  

if __name__ == '__main__':
    unittest.main()

