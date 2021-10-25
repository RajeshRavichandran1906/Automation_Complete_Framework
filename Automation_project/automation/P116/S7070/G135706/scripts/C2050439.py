'''
Created on Aug 11, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050439
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2050439_TestClass(BaseTestCase):

    def test_C2050439(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        """
        1. Execute the 101227.fex
        """
        utillobj.active_run_fex_api_login("101227.fex", "S7070", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0", 1, 60)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the 101227.fex and Verify the Report Heading')
        column_list=['COUNTRY','DEALER_COST','RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 101227.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '101227.xlsx','Step 01.3: Expect to see the  Active Report')
        
        """
        STep 02: Click on any column drop-down and select 'Grid Tool' option
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Grid Tool')
        
        """
        Step 03: Drag and drop DEALER_COST and RETAIL_COST fields from column order to sort order section
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'DEALER_COST', 1, 0)
        time.sleep(5)
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'RETAIL_COST', 1, 1)
        time.sleep(5)
        
        """
        Step 04; In sort order section, make the sort order Z/A for both fields. click OK.
        """
        
        self.driver.find_element(By.CSS_SELECTOR ,'[onclick="ibiEditTools.Gt_changesort(1,0,0)"]').click()
        self.driver.find_element(By.CSS_SELECTOR ,'[onclick="ibiEditTools.Gt_changesort(1,0,1)"]').click()
        
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050439_Ds01.xlsx','Step 04: Verify table')
        
        """
        Step 05: Again click on any column drop-down and select 'Grid Tool' option.
        """
        time.sleep(4)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Grid Tool')
        
        try:
            grid_tool=self.driver.find_element(By.CSS_SELECTOR, '[id="wall1"]').is_displayed()
            utillity.UtillityMethods.asequal(self,True,grid_tool,'Step 05: Verify Grid Tool window should be re-opened without IE error')
        except NoSuchElementException:
            print("Step 05: Verify Grid Tool window should be re-opened without IE error - Failed")
        
        
if __name__ == '__main__':
    unittest.main()    
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        