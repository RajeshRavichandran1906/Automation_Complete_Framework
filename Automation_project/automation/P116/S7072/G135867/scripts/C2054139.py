'''
Created on Aug 5, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054139
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2054139_TestClass(BaseTestCase):

    def test_C2054139(self):
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        activeToolsobj = active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Execute the AR-RP-001.fex")
        columns1=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
        Step 02: Click State > Grid Tool
        """
        miscelanousobj.select_menu_items("ITableData0", 3, "Grid Tool")
        
        try:
            grid_tool=self.driver.find_element(By.CSS_SELECTOR ,'[id="gridtoolt1"]').is_displayed()
            utillity.UtillityMethods.asequal(self,True,grid_tool,"Step 02: Verify that Grid Tool is displayed.")
        except NoSuchElementException:
            print("Step 02: Verify that Grid Tool is displayed - Failed")
        
        """
        Step 03: Click Hide Column icon for column Unit Sales.
        """
        activeToolsobj.grid_tool_show_hide_column("gridtoolt1", "Unit Sales", 1, "Hide Column")
        activeToolsobj.verify_grid_tool_show_hide_column('gridtoolt1', 'Unit Sales',1,'Show Column', "Step 03: Verify that Unit Sales is marked as selected.")
        
        """
        Step 04: Click OK.
        """
        activeToolsobj.grid_tool_close('gridtoolt1', 'Ok')
        columns=['Category','Product','Product ID','State','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns, 'Step 04: Verify that Unit Sales will not appear on the report')
        utillobj.verify_data_set('ITableData0','I0r' ,'C2054138_Ds01.xlsx',"Step 04: Verify that Unit Sales will not appear on the report")

        """
        Step 05: Click State > Grid Tool
        """
        miscelanousobj.select_menu_items("ITableData0", 3, "Grid Tool")

        try:
            grid_tool=self.driver.find_element(By.CSS_SELECTOR ,'[id="gridtoolt1"]').is_displayed()
            utillity.UtillityMethods.asequal(self,True,grid_tool,"Step 05: Verify that Grid Tool is displayed.")
        except NoSuchElementException:
            print("Step 05: Verify that Grid Tool is displayed - Failed")
            
            
        """
        Step 06: Click Hide Column icon again for column Unit Sales.
        """
        activeToolsobj.grid_tool_show_hide_column("gridtoolt1", "Unit Sales", 1, "Show Column")
        activeToolsobj.verify_grid_tool_show_hide_column('gridtoolt1', 'Unit Sales',1,'Hide Column', "Step 06: Verify that Unit Sales is unchecked")    
        
        """
        Step 07: Click OK.
        """
        activeToolsobj.grid_tool_close('gridtoolt1', 'Ok')
        columns1=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 07: Verify that Unit Sales appears on the report')
        utillobj.verify_data_set('ITableData0','I0r' ,'AR-RP-001.xlsx',"Step 07: Verify that Unit Sales appears on the report")
            
if __name__ == '__main__':
    unittest.main()  
            
            
            
            
        