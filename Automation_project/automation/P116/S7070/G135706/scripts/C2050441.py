'''
Created on Aug 12, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050441
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050441_TestClass(BaseTestCase):

    def test_C2050441(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the 125381.fex.
        """
        utillobj.active_run_fex_api_login("125381.fex", "S7070", 'mrid', 'mrpass')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table[id='IWindowBody0'] .arGridBar table")))
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the 125381.fex and Verify the Report Heading')
        column_list=['COUNTER','COL_1','COL_2']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the 125381.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', '125381.xlsx','Step 01.3: Expect to see the  Active Report')
        """
        Step 02: Select COL_1 drop down -> sort ascending
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050441_Ds01.xlsx','Step 02: Verify the report is now sorted in ascending order by COL_1')
        """
        Step 03: Select COL_2 drop down -> sort descending
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Sort Descending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050441_Ds02.xlsx','Step 03: Verify the report is now sorted in descending order by COL_2')
        """
        Step 04: Select COL_1 drop down -> sort ascending
        """ 
        miscelanousobj.select_menu_items('ITableData0', 1, 'Sort Ascending')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2050441_Ds01.xlsx','Step 04: Verify the report is now sorted in ascending order by COL_1')
        
if __name__ == '__main__':
    unittest.main()