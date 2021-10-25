
'''
Created on July 21, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/20550472
'''
__author__ = "Gobizen"
__copyright__ = "IBI"



import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050472_TestClass(BaseTestCase):

    def test_C2050472(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050472'
        
        """Step 01: Execute the AR-RP-001.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Verify output'
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        
        """Step 02: Select State > Filter""" 
        
        step02 = 'Step 02 : Verify Filter menu shows all the filter options mentioned in the Test Description.'
        
        #Verify Filter menu shows all the filter options mentioned in the Test Description.    
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',3,'Filter',option,step02) 
        
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        
        """Step 03: Select Filter > Equals"""
        
        #Verify Filter selection pop up is opened.
        
        filterselectionobj.verify_filter_selection_dialog(True, 'Step 03: Select Filter > Equals', ['State', 'Equals'])
        
        """Step 04 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All"""
        _step04 = 'Step 04 :Verify user has following options: 1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All'
        
        
        filterselectionobj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], _step04)
        
        """Step 05 : Click dropdown next to <Value> (for State column)"""
        
        #Verify all the values under selected column are listed
         
        menu_list = ['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        filterselectionobj.verify_filter_values_menu_list(1, menu_list, 'Step 05 : Click dropdown next to <Value> (for State column)')
        
        """Step 06  : Select "MA" value in this test.  """
        
        filterselectionobj.create_filter(1, 'Equals', value1='MA')
        
        
        """ Step 07 :Click 'Operator: AND' once and click dropdown menu for 'Add Condition'"""
        
        filterselectionobj.filter_button_click('Operator: AND')
        #Verify on clicking 'Operator: AND' button shows 'Operator: OR' and Add conditon dropdown shows all the columns present under a report.
        
        filterselectionobj.verify_filter_buttons(['Operator: OR', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], _step04)
        
        
        """ Step 08 : Select 'Product' column to add."""
        
        filterselectionobj.add_condition_field('Product')

        #Verify filter condition for Product is added on the top
        #This verification combined in next steps by verifying all values in filter dialog box

        """Step 09: Select 'Equals' for Product column and click value dropdown and select 'Latte' from the list """
        filterselectionobj.create_filter(2, 'Equals', value1='Latte')
        
        #Verify Filter selection shows correct values and filter options for both the columns.
        _step09 = "Step 09: Verify Filter selection shows correct values and filter options for both the columns. "
        
        filterselectionobj.verify_filter_selection_dialog(True, _step09,['State', 'Equals', 'MA'], ['Product','Equals', 'Latte'])
        
        """Step 10 : Click Filter button"""
        
        filterselectionobj.filter_button_click('Filter')
        
        #VVerify result the conditions. All records have State = MA or Product = Latte See attached screenshot.
        time.sleep(5)
        _step10 = 'Step 10: Verify result the conditions. All records have State = MA or Product = Latte See attached screenshot.'
        miscelanousobj.verify_page_summary('0','20of107records,Page1of1', _step10)
        
        utillobj.verify_data_set('ITableData0','I0r','C2050472_Ds01.xlsx',_step10)
        #utillobj.create_data_set('ITableData0','I0r','C2050472_Ds01.xlsx')



if __name__ == '__main__':
    unittest.main()

