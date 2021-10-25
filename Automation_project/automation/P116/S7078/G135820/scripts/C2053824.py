'''
Created on Aug 29, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053824
TestCase Name = Verify columns are sorted horizontally/vertically/left/right
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_pivot_comment
from common.lib import utillity

class C2053824_TestClass(BaseTestCase):

    def test_C2053824(self):
        driver = self.driver
#         driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
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
        time.sleep(3)
        ele = driver.find_element_by_css_selector("#TCOL_0_C_3")
        ele.click()
        time.sleep(3)
        
        """
        Step 03: Click dropdown menu for State column and mouse over Pivot(Cross Tab) > any column (Category) > Product ID
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Pivot (Cross Tab)','Category','Product ID')
        miscelanousobj.verify_popup_appears('wall1', 'State by Product ID, Category', 'Step 03: Verify Pivot table State By Product ID, Category is generated based on the columns selection')
        utillobj.verify_pivot_data_set('piv1', 'C2053818_Ds01.xlsx','Step 03: Verify pivot data')
        
        """
        Step 04: Click New icon (dropdown) > Group By (X) > Product
        """
        pivotobj.create_new_item('wall1', 0, 'Group By (X)->Product')
        utillobj.verify_pivot_data_set('piv1', 'C2053824_Ds01.xlsx','Step 04: Verify that new Product column is added')
        
        """
        Step 05: Pivot table shows Category, Product columns vertically and Product ID horizontally. 
        Now click right arrow on first column (Category)
        """
        pivotobj.click_groupby_across_button('piv1', 2, 1, 3)
        utillobj.verify_pivot_data_set('piv1', 'C2053824_Ds02.xlsx','Step 05: Verify that Category column is shifted to the right side on the table')
        
        """
        Step 06: Pivot table shows Product , Category columns vertically and Product ID horizontally. 
        Now click left arrow on second column (Category)
        """
        pivotobj.click_groupby_across_button('piv1', 2, 2, 2)
        utillobj.verify_pivot_data_set('piv1', 'C2053824_Ds01.xlsx','Step 06: Verify that Category column is shifted to the left side on the table')
        
        """
        Step 07: Pivot table shows Product , Category columns vertically and Product ID horizontally. 
        Click upward bend arrow on Product column to shift the column horizontally.
        """
        pivotobj.click_groupby_across_button('piv1', 2, 2, 1)
        utillobj.verify_pivot_data_set('piv1', 'C2053824_Ds03.xlsx','Step 07: Verify that Product and Product ID are now displayed horizontally,Category is displayed vertically.')
        
        """
        Step 08: Pivot table shows Category column vertically and Product ID, Product columns horizontally. 
        Click downward bend arrow on Product ID column to shift the column vertically.
        """
        pivotobj.click_groupby_across_button('piv1', 1, 2, 1)
        utillobj.verify_pivot_data_set('piv1', 'C2053824_Ds04.xlsx','Step 08: Verify that Category and Product ID are now displayed Verically and Product horizontally')
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        