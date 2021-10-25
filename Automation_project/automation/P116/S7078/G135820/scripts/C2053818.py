'''
Created on Aug 29, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053818
TestCase Name = Verify Pivot table is generated
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2053818_TestClass(BaseTestCase):

    def test_C2053818(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)

        """
        1. Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7078", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.1: Execute the AR-RP-001.fex')
        column_list=['Category','Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        
        """
        Step 02: Click dropdown menu for State column and mouse over Pivot(Cross Tab)
        """
        values=['Group By(COU)', 'Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)', values, 'Step 02: Verify Group By (Columns) list are displayed', all_items='yes')
        
        temp=driver.find_element_by_css_selector("#TCOL_0_C_3")
        temp.click()
        time.sleep(2)
        
        """
        Step 03: Click dropdown menu for State column and mouse over Pivot(Cross Tab) > any column (Category) > Product ID
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot (Cross Tab)','Category','Product ID')
        miscelanousobj.verify_popup_appears('wall1', 'State by Product ID, Category', 'Step 02: Verify Pivot table State By Product ID, Category is generated based on the columns selection')
        utillobj.verify_pivot_data_set('piv1', 'C2053818_Ds01.xlsx','Step 03: Verify pivot data')
        
if __name__ == '__main__':
    unittest.main()