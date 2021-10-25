'''
Created on Aug 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053815
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class C2053815_TestClass(BaseTestCase):

    def test_C2053815(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        toolsobj = active_tools.Active_Tools(self.driver)
        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001A.fex", "S7075", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001A.fex')
        column_list=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001A.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Click State > Grid Tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool','Step 02: Verify that Grid Tool is displayed.')
        
        """
        Step 03: Change Unit Sales and Dollar Sales aggregation from none to SUM
        """
        
        toolsobj.grid_tool_select_aggregate_function('gridtoolt1', 'Unit Sales', 1, 'Sum')
        toolsobj.grid_tool_select_aggregate_function('gridtoolt1', 'Dollar Sales', 1, 'Sum')
        
        """
        Step 04: Drag columns 'Category' and 'Product ID' from Column Order to Sort Order column
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Category', 1, 0)
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Product ID', 1, 1)
        
        sort_css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Select Sort Order']" 
        sort_btns=self.driver.find_elements_by_css_selector(sort_css)
        utillobj.take_screenshot(sort_btns[0], 'GT_Sort_Ascending', image_type='actual')
        utillobj.take_screenshot(sort_btns[1], 'GT_Sort_Ascending', image_type='actual')
        
        """
        Step 05: Check Group sort columns checkbox
        """
        toolsobj.grid_tool_select_group_checkbox('gridtoolt1')
        columns=['Column Order', 'Category', 'Product ID', 'Product', 'State', 'Sum', 'Unit Sales', 'Sum', 'Dollar Sales']
        toolsobj.grid_tool_verify_columns('gridtoolt1', 1, columns,'Step 05: Verify that under Column Order, Category and Product ID are grouped together')
        
        try:
            val2 = self.driver.find_element(By.XPATH,"//div[@onclick='ibiEditTools.Gt_toggleSortGroup(1,0)']/div/img").is_displayed()
            utillobj.asequal(True,val2,'Step 05: Verify Group sort columns checkbox is checked')
        except NoSuchElementException:
            print('Step 05: Verify Group sort columns checkbox is checked - Failed')
        
        
        """
        Step 06: Click Ok.
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        
        miscelanousobj.verify_calculated_value(2, 5, 'Total Sum 3688991', True, "Step 06: Verify unit Sales calculated value")
        miscelanousobj.verify_calculated_value(2, 6, 'Total Sum 46156290', True, "Step 06: Verify Dollar Sales calculated value")
        
        utillobj.verify_data_set('ITableData0','I0r','C2053815_Ds01.xlsx','Step 06: Verify that report sort records are based on Category & Product column')
        time.sleep(5)
        """
        Step 07: Click State > Grid Tool
        """
        ele = driver.find_element_by_css_selector("#TCOL_0_C_3")
        ele.click()
        time.sleep(5)
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        time.sleep(1)
        miscelanousobj.verify_popup_appears('wall1', 'Grid Tool','Step 07: Verify that Grid Tool is displayed.')
        
        """
        Step 08: Check Subtotal checkbox for Product ID column
        """
        self.driver.find_element(By.CSS_SELECTOR,'[onclick="ibiEditTools.Gt_changeSubCalc(1,0,1)"]').click()
        
        try:
            val3=self.driver.find_element(By.XPATH,"//div[@onclick='ibiEditTools.Gt_changeSubCalc(1,0,1)']/div/img").is_displayed()
            utillobj.asequal(True,val3,'Step 08: Verify that Product ID checkbox is checked')
        except NoSuchElementException:
            print('Step 08: Verify that Product ID checkbox is checked - Failed')
        
        """
        Step 09: Click OK.
        """
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        utillobj.verify_data_set('ITableData0','I0r','C2053815_Ds02.xlsx','Step 09: Verify that Total SUM for each Product ID is displayed for Unit Sales and Dollar Sales columns')
        
        
if __name__ == '__main__':
    unittest.main()  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        