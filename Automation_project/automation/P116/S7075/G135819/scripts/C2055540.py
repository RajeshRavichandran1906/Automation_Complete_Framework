'''
Created on Aug 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055540
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2055540_TestClass(BaseTestCase):

    def test_C2055540(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        """
        1. Execute the 144185.fex
        """
        utillobj.active_run_fex_api_login("144185.fex", "S7075", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 144185.fex')
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'SEATS', 'DEALER_COST', 'RETAIL_COST', 'SALES', 'LENGTH', 'WIDTH', 'HEIGHT', 'WEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'RPM', 'MPG', 'ACCEL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','144185.xlsx','Step 01.3: Verify data set')
        
        """
        STep 02: From any field select Grid Tool from the Active Menu.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        """
        Step 03: Drag COUNTRY into Sort Order
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'COUNTRY', 1, 0, sx_offset = 0, sy_offset = -7, tx_offset = 0, ty_offset = -7, browser_height = 70)
        """
        Step 04: Check the box: Group sort columns
        """
        toolsobj.grid_tool_select_group_checkbox('gridtoolt1')
        """
        Step 05: Check the box: Subtotal (appears after step 3)
        """
        self.driver.find_element(By.CSS_SELECTOR,'[onclick="ibiEditTools.Gt_changeSubCalc(1,0,0)"]').click()
        """
        Step 06: Click OK and check you should get a new window with the HTML No Data error page
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0','I0r','C2055540_Ds01.xlsx','Step 06: Verify data set')
        
if __name__ == '__main__':
    unittest.main()      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
