'''
Created on Aug 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055539
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2055539_TestClass(BaseTestCase):

    def test_C2055539(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        """
        1. Execute the 148558.fex
        """
        utillobj.active_run_fex_api_login("148558.fex", "S7075", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 148558.fex')
        column_list=['COUNTRY','DEALER_COST','RETAIL_COST','SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','148558.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: From SALES dropdown select GRID tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        """
        Step 03: Drag COUNTRY to Sort Order
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'COUNTRY', 1, 0, sx_offset = 0, sy_offset = -7, tx_offset = 0, ty_offset = -7, browser_height = 70)
        """
        Step 04: Select the check box "Group Sort Columns" and select the check box for Subtotal for COUNTRY
        """
        
        toolsobj.grid_tool_select_group_checkbox('gridtoolt1')
        self.driver.find_element(By.CSS_SELECTOR,'[onclick="ibiEditTools.Gt_changeSubCalc(1,0,0)"]').click()
        """
        Step 05: Select SUM for DEALER_COST from aggregation
        """
        toolsobj.grid_tool_select_aggregate_function('gridtoolt1', 'DEALER_COST', 1, 'Sum')
        
        """
        Step 06: Click OK and check that it displays report without FOC error
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        miscelanousobj.verify_calculated_value(2, 2, 'Total Sum 143,794', True, 'Step 06: Verify DEALER_COST calculated value')
        utillobj.verify_data_set('ITableData0','I0r','C2055539_Ds01.xlsx','Step 06: Verify data set')
        
if __name__ == '__main__':
    unittest.main()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        