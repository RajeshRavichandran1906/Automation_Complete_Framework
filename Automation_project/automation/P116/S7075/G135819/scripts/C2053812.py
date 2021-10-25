'''
Created on Aug 25, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053812
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_tools
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2053812_TestClass(BaseTestCase):

    def test_C2053812(self):
        driver = self.driver
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
            val=self.driver.find_element(By.CSS_SELECTOR,'[class="arWindowBarTitle"]').is_displayed()
            utillobj.asequal(True,val,'Step 02: Verify that Grid Tool is displayed.')
        except NoSuchElementException:
            print('Step 02: Verify that Grid Tool is displayed - Failed')
            
        """
        Step 03: Drag 'Product' column and 'Unit Sales' column from Column Order to Sort Order area
        """
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Product', 1, 0)
        toolsobj.grid_tool_drag_drop_items('gridtoolt1', 'Unit Sales', 1, 1)
        
        sort_css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) div[title='Select Sort Order']" 
        sort_btns=self.driver.find_elements_by_css_selector(sort_css)
        utillobj.take_screenshot(sort_btns[0], 'GT_Sort_Ascending', image_type='actual')
        utillobj.take_screenshot(sort_btns[1], 'GT_Sort_Ascending', image_type='actual')
        
        """
        STep 04: Change sort order of Product column from A to Z To Z to A by clicking sort arrow. Click Ok.
        """
        toolsobj.grid_tool_sort_item(1)
        toolsobj.grid_tool_close('gridtoolt1', 'Ok')
        
        utillobj.verify_data_set('ITableData0','I0r','GT_Sort_Descending.xlsx','Step 04: Verify that report shows sort order from Z to A. Verify that other column data are displayed per Product column.')
            
            
if __name__ == '__main__':
    unittest.main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            