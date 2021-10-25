'''
Created on Jul 20, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050481
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050481_TestClass(BaseTestCase):

    def test_C2050481(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050481'
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
            Verify Filter menu shows all the filter options mentioned in the Test Description.
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        miscelanousobj.verify_menu_items('ITableData0',3,'Filter',option,'Step 02: Verify Filter menu shows all the filter options')
        """
            Step 03: Select Filter > Equals
            Verify Filter selection pop up is opened.
        """
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
        filterselectionobj.verify_filter_selection_dialog(True,"Step 03: Verify Filter selection pop up is opened.",['State', 'Equals'])
        """
        Step 04: Verify user has following options: 1. Operatior: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All
        """
        option=['Operator: AND', 'Add Condition', 'Filter', 'Highlight','Clear All']
        filterselectionobj.verify_filter_buttons(option, "Step 04: Verify user has options")
        
        """
        Step 05: Click dropdown next to <Value> (for State column)
        Verify all the values under selected column are listed
        """
        item=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        filterselectionobj.verify_filter_values_menu_list(1, item, 'Step 05: Verify all the values under selected column are listed')
        """
        Step 06: Select "IL " value in this test and click dropdown menu for 'Add Condition'
        Verify dropdown shows all the columns present under a report.
        """
        filterselectionobj.create_filter(1, 'Equals', value1='IL') 
        
        condition_dropdown=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        filterselectionobj.verify_add_condition_menu(condition_dropdown, 'Step 06: Verify dropdown shows all the columns present under a report.')
        
        """
        Step 07: Select 'Category' column to add.
        Verify filter condition for Category is added on the top
        """
        filterselectionobj.add_condition_field("Category")
        
        row1=['State', 'Equals','IL']
        row2=['Category','Equals']
        filterselectionobj.verify_filter_selection_dialog(True,"Step 03: Verify Filter selection pop up is opened.",row1,row2)
        
        """
        Step 08: Select 'Equals' for Category column and click value dropdown and select 'Food' from the list
        Verify Filter selection shows correct values and filter options for both the columns.
        """
        filterselectionobj.create_filter(2, 'Equals', value1='Food')
        
        filterselectionobj.verify_filter_condition_menu_list(1, 'Step 08: Verify Filter selection shows correct values')
        
        row1_1=['State', 'Equals','IL']
        row2_1=['Category','Equals','Food']
        filterselectionobj.verify_filter_selection_dialog(True,"Step 08: filter options for both the columns.",row1_1,row2_1)
        
        """
        Step 09: Click Filter button
        Verify result satisfies both the conditions. All records have State = IL and Category = Food.
        """
        filterselectionobj.filter_button_click('Filter')

        miscelanousobj.move_active_popup("1", "600", "200")
        
        miscelanousobj.verify_page_summary(0, '3of107records,Page1of1', 'Step 09: Verify report summary')
        
        utillobj.verify_data_set('ITableData0','I0r','C2050481_Ds01.xlsx','Step 09: Verify result satisfies both the conditions')
        """
        Step 10: Now click 'X' next to Category column
        Verify Category column and filter option is removed from the Filter selection pop up
        """
        filterselectionobj.delete_filter(2)
        
        filterselectionobj.verify_filter_selection_dialog(False, 'Step 10: Verify Category column and filter option is removed from the Filter selection pop up',row2_1)
        
        filterselectionobj.verify_filter_selection_dialog(True,"Step 10: Verify State column and filter option",row1_1)
        """
        Step 11: Click Filter button
        Verify new result set is displayed based on modification made on column/filter selection
        """
        filterselectionobj.filter_button_click('Filter')
        
        miscelanousobj.verify_page_summary(0, '9of107records,Page1of1', 'Step 11: Verify report summary')
        
        utillobj.verify_data_set('ITableData0','I0r','C2050481_Ds02.xlsx','Step 11: Verify new result set is displayed based on modification made on column/filter selection')
        
        
if __name__ == '__main__':
    unittest.main()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        