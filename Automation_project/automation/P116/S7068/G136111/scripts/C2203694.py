'''
Created on Sep 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203694
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
import unittest

class C2203694_TestClass(BaseTestCase):

    def test_C2203694(self):
        
        """
        Step 01: Execute the attached fex.
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("89499.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.1: Execute 89499.fex verify Page Summary 18of18")
        columns1 = ['CAR','RETAIL_COST','DEALER_COST']
        active_misobj.verify_column_heading('ITableData0', columns1, 'Step 01.2: Verify column heading')
        utillobj.verify_data_set('ITableData0','I0r', "89499.xlsx","Step 01.3: Verify 89499.fex dataset")
        
        """
        Step 02: Select filter from Retail_Cost.
        """
        
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Greater than')
        
        """
        Step 03: Select Greater than "3139" from filter
        """
        active_filter.create_filter(1, 'Greater than', value1='3,139')
        active_filter.filter_button_click('Filter')
        utillobj.verify_data_set('ITableData0','I0r', "C2203694_Ds01.xlsx","Step 02: Verify filter dataset")
        
        
        """
        Step 04: Click on Retail_cost and rollup by Car
        """
        active_misobj.move_active_popup('1', '600', '200')
        active_misobj.select_menu_items('ITableData0', 1, 'Rollup','CAR')
        
        """
        Step 05: In Rollup windows select Car column and select calculation = count
        """
        active_misobj.select_menu_items('ITableData1', 0, 'Calculate','Count')
        active_misobj.verify_calculated_value(3, 1, 'Total Cnt 9', True, 'Step 05: Verify Calculated value', table_id='ITableData1')
        
        """
        Step 06: Apply sorting in Retail_cost by click on Sort descending option from dropdown
        """
        active_misobj.select_menu_items('ITableData1', 1, 'Sort Descending')
        
        """
        Step 07: Verify values are not changed and also the expected values.
        """
        active_misobj.verify_calculated_value(3, 1, 'Total Cnt 9', True, 'Step 07: Verify Calculated value', table_id='ITableData1')
        utillobj.verify_data_set('ITableData1','I1r', "C2203694_Ds02.xlsx","Step 07: Verify dataset")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()