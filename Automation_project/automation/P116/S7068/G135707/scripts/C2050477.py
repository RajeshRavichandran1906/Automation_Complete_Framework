'''
Created on Jul 18, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050477
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050477_TestClass(BaseTestCase):

    def test_C2050477(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050477'
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
            Step 02: Select State > Filter 
            Verify Filter menu shows all the filter options mentioned in the Test Description
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',3,'Filter',option,'Step 02: Verify Filter menu shows all the filter options mentioned in the Test Description')
        """
            Step 03: Select Filter > Equals
            Verify Filter selection pop up is opened Verify user has following options: 1. Operatior: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All
        """
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        
        option=['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        filterselectionobj.verify_filter_buttons(option, "Step 03: Verify Filter selection pop up")
        
        """
            Step 04: Click dropdown next to <Value> (for State column)
            Verify all the values under selected column are listed
        """
        item=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        filterselectionobj.verify_filter_values_menu_list(1, item, 'Step 04: Verify all the values under selected column are listed')
        
        """
            Step 05: Select "MA" value in this test. Click 'Operator: AND' once and click dropdown menu for 'Add Condition'
            Verify on clicking 'Operator: AND' button shows 'Operator: OR' and Add conditon dropdown shows all the columns present under a report
        """ 
        
        filterselectionobj.create_filter(1, "Equals", "small",value1="MA")
        filterselectionobj.filter_button_click("Operator: AND")
        
        condition_dropdown=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        filterselectionobj.verify_add_condition_menu(condition_dropdown, 'Step 05: Add conditon dropdown shows all the columns present under a report')
        
        option1=['Operator: OR', 'Add Condition', 'Filter', 'Highlight', 'Clear All']
        filterselectionobj.verify_filter_buttons(option1, "Step 05: Verify on clicking 'Operator: AND' button shows 'Operator: OR")
        
        
        """
            Step 06: Select 'Product' column to add.
            Verify filter condition for Product is added on the top.
        """
        filterselectionobj.add_condition_field("Product")
        
        row1=['State','Equals','MA']
        row2=['Product','Equals']
        filterselectionobj.verify_filter_selection_dialog(True,'Step 06: Verify filter condition for Product is added on the top.',row1,row2)
        
        """
            Step 07: Select 'Equals' for Product column and click value dropdown and select 'Latte' from the list
            Verify Filter selection shows correct values and filter options for both the columns
        """
        filterselectionobj.create_filter(2, "Equals", "small",value1="Latte")
        
        item1=['Biscotti','Capuccino','Coffee Grinder','Coffee Pot','Croissant','Espresso','Latte','Mug','Scone','Thermos']
        filterselectionobj.verify_filter_values_menu_list(2,item1, 'Step 07: Verify Filter selection shows correct values')
        
        row2_1=['Product','Equals','Latte']
        filterselectionobj.verify_filter_selection_dialog(True,'Step 07: Verify Filter options for both the columns',row1,row2_1)
        
        """
            Step 08: Click Filter button
            Verify result satisfies either of the conditions. All records have State = MA and/or Product = Latte
        """
        
        filterselectionobj.filter_button_click("Filter")
        miscelanousobj.move_active_popup('1', '600', '200')
        utillobj.verify_data_set('ITableData0','I0r','C2050477_Ds01.xlsx',"Step 08: Verify All records have State = MA and/or Product = Latte")
        
        
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        