'''
Created on Aug 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053813
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException

class C2053813_TestClass(BaseTestCase):

    def test_C2053813(self):
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7075", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        
        """
        Step 02: Click State > Grid Tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        try:
            val = utillobj.validate_and_get_webdriver_object('[class="arWindowBarTitle"]', 'window-title').is_displayed()
            utillobj.asequal(True,val,'Step 02: Verify that Grid Tool is displayed.')
        except NoSuchElementException:
            print('Step 02: Verify that Grid Tool is displayed - Failed')
            
        """
        Step 03: Drag 'Product' column and 'Unit Sales' column from Column Order to Sort Order area
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Product', 1, 0)
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Unit Sales', 1, 1)
        
        """
        Step 04: Change sort order of Product column from A to Z To Z to A by clicking sort arrow.
        """
        toolsobj.grid_tool_sort_item(1)
        
        """
        Step 05: Click Ok.
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0','I0r','C2053812_Ds01.xlsx','Step 04: Verify that other column data are displayed per Product column.')
        
        """
        Step 06: Now click State > Grid Tool again and change sort order for Unit Sales from Z to A.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        toolsobj.grid_tool_sort_item(2)

        """
        Step 07: Click Ok
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0','I0r','C2053813_Ds01.xlsx','Step 07: Verify that report Product column in Z to A order and on second level it sorts Unit Sales.')
            
if __name__ == '__main__':
    unittest.main()   
        
        
        
        
        
        
        
        