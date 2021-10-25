'''
Created on Aug 16, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050447
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection
from common.lib import utillity
import time
class C2050447_TestClass(BaseTestCase):

    def test_C2050447(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        """
        1. Execute the attached repro - 89966.fex
        """
        utillobj.active_run_fex_api_login("89966.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the AR-RP-001.fex and Verify the Report Heading')
        column_list=['CAR','COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-RP-001.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','89966.xlsx','Step 01.3: Expect to see the  Active Report')
        """
        Step 02: Filter Sales GT 4800,click Filter button
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Filter','Greater than')
        time.sleep(5)
        filterobj.create_filter(1, 'Greater than', value1='4800')
        value = ['SALES','Greater than','4800']
        filterobj.verify_filter_selection_dialog(True, 'Step 02.1: Verify filter dialog',value)
        filterobj.filter_button_click('Filter')
        time.sleep(2)
        """
        Step 03: Select Rollup option Dealer_cost By COUNTRY
        """
        miscelanousobj.move_active_popup('1', '600', '200')
        time.sleep(2)
        utillobj.verify_data_set('ITableData0','I0r','C2050447_Ds01.xlsx','Step 02.2: Verify filter data set')
        miscelanousobj.select_menu_items('ITableData0', 2, 'Rollup','COUNTRY')
        """
        Step 04: In Rollup perform Sort, Visualize or Calculate
        """
        miscelanousobj.select_menu_items('ITableData1',1, 'Sort Ascending')
        time.sleep(3)
        utillobj.verify_data_set('ITableData1','I1r','C2050447_Ds02.xlsx','Step 04.1: Verify sort data set')
         
        miscelanousobj.select_menu_items('ITableData1',1, 'Visualize')
        miscelanousobj.verify_visualization('ITableData1', 'I1r', 1, 'black', 'Step 04.2: Verify visualization added')
       
        miscelanousobj.select_menu_items('ITableData1',1, 'Calculate','Count')
        miscelanousobj.verify_calculated_value(3, 2, 'Total Cnt 4', True, 'Step 04.4: Verify Calculated value', table_id='ITableData1')
       
        
if __name__ == '__main__':
    unittest.main()    
               
        
        
        
        
        
        
        
        
        
        
        
        
        