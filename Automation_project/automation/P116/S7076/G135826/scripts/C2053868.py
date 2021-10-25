'''
Created on Aug 24, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053868
TestCase Name = 765AHTML_Cache:Sorting,calculation in Rollup-get `No HTML `(Proj 89966)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity

class C2053868_TestClass(BaseTestCase):

    def test_C2053868(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053868'
        """
            Step 01: Execute the 89966.fex
        """
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('89966.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01: Verify Page summary 18of18')
        column=['CAR','COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 89966")
        utillobj.verify_data_set('ITableData0','I0r','89966.xlsx',"Step 01.3: Verify 89966 dataset")        
        
        """
        Step 02: Select sales drop down --> filter -> greater then -> 4800
        """
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Greater than')
        active_filter.create_filter(1, 'Greater than', value1='4800')
        active_filter.filter_button_click('Filter')
        active_misobj.move_active_popup("1", "600", "200")
        active_filter.verify_filter_selection_dialog(True,'Step 02.1: Verify filter row.',['SALES', 'Greater than', '4800'])
        active_misobj.verify_page_summary('0','12of18records,Page1of1', 'Step 02.2: Verify Page summary 12of18')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds01.xlsx',"Step 02.3: Verify SALES Greater than 4800 dataset")        
        
        """
        Step 03: Select Rollup option from Dealer_cost By COUNTRY
        """      
        active_misobj.select_menu_items('ITableData0', 2, 'Rollup','COUNTRY')
        element_css="#wall2 table[class='arGrid']"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=1, expire_time=30)
        active_misobj.verify_page_summary('1','4of4records,Page1of1', 'Step 03.1: Verify Page summary 4of4')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds02.xlsx',"Step 03.2: Verify all the matching records for rollup COUNTRY")
        
        """
        Step 04: In Rollup on Dealer_cost perform Visualize and Calculate->Sum
        """
        active_misobj.select_menu_items('ITableData1', 1,'Visualize')
        active_misobj.verify_visualization('ITableData1', 'I1r', 1, 'black', 'Step 04.1: Verify visualization added')
        active_misobj.select_menu_items('ITableData1', 1, 'Calculate','Sum')
        active_misobj.verify_calculated_value(3, 2, "Total Sum 82,589",True, "Step 04.2: Verify Total Sum 82,589", table_id='ITableData1')

if __name__ == '__main__':
    unittest.main()