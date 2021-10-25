'''
Created on Aug 30, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053830
TestCase Name = Verify user can change calculation type of Measure
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools,active_pivot_comment
from common.lib import utillity

class C2053830_TestClass(BaseTestCase):

    def test_C2053830(self):
       
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')

        """
        Step 02: Click State > Pivot Tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot Tool')
        
        column_1=['Columns', 'Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        toolsobj.pivot_tool_verify_columns('pivottoolt1', 1, column_1, 'Step 02.1: Verify Columns tab')
        
        column_2 =  ['Group By', 'Drag Column Here']
        toolsobj.pivot_tool_verify_columns('pivottoolt1', 2, column_2, 'Step 02.2: Verify Group By tab')
        
        column_3 = ['Across', 'Drag Column Here']
        toolsobj.pivot_tool_verify_columns('pivottoolt1', 3, column_3, 'Step 02.3: Verify Across tab')
        
        column_4 = ['Measure', 'Drag Column Here']
        toolsobj.pivot_tool_verify_columns('pivottoolt1', 4, column_4, 'Step 02.4: Verify Measure tab')
        
        """
        Step 03: Drag Product column under Group By, State column under Across and Product ID column under Measure.
        """
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product', 1, 'Group By', 0)
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Across', 0)
        toolsobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        
        """
        Step 04: Click OK.
        """
        toolsobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053830_Ds01.xlsx','Step 04.1: Verify pivot table is displayed')
        pivotobj.verify_pivot_menu('wall2', 'Step 04.2: Verify pivot toolbar')
        
        """
        Step 05: Click aggregation icon from Sum (default state) to Count
        """
        pivotobj.select_aggregate_function('wall2', 0, 'Count')
        utillobj.verify_pivot_data_set('piv2', 'C2053830_Ds02.xlsx','Step 05: Verify pivot table shows the calculation changes')
        
if __name__ == '__main__':
    unittest.main()           
                