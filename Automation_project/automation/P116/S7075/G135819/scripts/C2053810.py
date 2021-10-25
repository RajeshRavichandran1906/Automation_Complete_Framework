'''
Created on Aug 25, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7075&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053810
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity
import time

class C2053810_TestClass(BaseTestCase):

    def test_C2053810(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolobj=active_tools.Active_Tools(driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-AHTML-001.fex and Verify the Report Heading')
        column_list=['Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-AHTML-001.fex and Verify the column heading')
        """
        2. Click State > Grid Tool
        Verify that Grid Tool is displayed.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool', 'Step 02.1: that Grid Tool is displayed.')
        """
        3. Click calculation icon next to Product column
        Verify that menu shows None, Count and Distinct options for Product (non-numeric) column
        4. Select Count option from the menu.
        Verify that on selecting Count option, column shows Count next to it under Grid tool.
        """
        time.sleep(2)
        toolobj.grid_tool_select_aggregate_function('gridtoolt1', 'Product', 1, 'Count', expected_aggregation_list=['None', 'Count', 'Distinct'])
        """
        5. Click OK.
        Verify that Product column shows total count = 107. 
        """
        toolobj.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(1)
        miscelanousobj.verify_calculated_value(2, 2, 'Total Cnt 107', True, 'Step 05.1: Verify that Product column shows total count = 107.')
        """
        6. Now click State > Grid tool again
        Grid tool winodw opens up.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool', 'Step 06.1: that Grid Tool is displayed.')
        """
        7. Click calculation icon next to Unit Sales column
        Verify that menu shows None, Sum, Avg, Min, Max, Cont and Distinct for Unit Sales (numeric) column.
        8. Select Sum option from the menu.
        Verify that on selecting Sum option, column shows Sum next to it under Grid tool.
        """
        time.sleep(2)
        toolobj.grid_tool_select_aggregate_function('gridtoolt1', 'Unit Sales', 1, 'Sum', expected_aggregation_list=['None', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct'])
        """
        9. Click OK.
        Verify that Unit Sales column shows Total Sum = 3,688,991.
        """
        toolobj.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(2)
        miscelanousobj.verify_calculated_value(2, 2, 'Total Cnt 107', True, 'Step 09.1: Verify that Product column shows total count = 107.')
        miscelanousobj.verify_calculated_value(2, 5, 'Total Sum 3688991', True, 'Step 09.2: Verify that Unit Sales column shows Total Sum = 3,688,991.')
        
if __name__ == '__main__':
    unittest.main()    