'''
Created on Aug 2, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2054137
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2054137_TestClass(BaseTestCase):

    def test_C2054137(self):
        
        """
            Step 01: Execute the C2054136.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("C2054136.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01: Execute the C2054136.fex")
        """
            Step 02: Verify that large report is generated where column does not fit on the window.
            User need to use scroll bar to view report horizontally.
        """
        miscelanousobj.verify_horizontal_page_scroll("IWindowBody0","yes", "Step 02: User need to use scroll bar to view report horizontally. ")
        """
            Step 03: Click dropdown for Bodytype > Freeze column
        """
        miscelanousobj.select_menu_items("ITableData0", "3", "Freeze Column")
        time.sleep(2)
        miscelanousobj.verify_horizontal_page_scroll("IWindowBody0","no", "Step 03: Verify horizontal scroll is not available ")
        miscelanousobj.verify_freeze_column('yes','IScrollWindowBody0',"Step 03: verify freeze column scroll bar")
        
        """
            Step 04: Click dropdown for Bodytype > Unfreeze All
        """
        time.sleep(10)
        driver.find_element_by_css_selector('#TCOL_0_C_3 > b > span').click()
        miscelanousobj.select_menu_items("IFixWindowBody0", "3", "Unfreeze All")
        """Verify that report is in original state. User can find 'Unfreeze All' option under any the columns"""
        miscelanousobj.verify_freeze_column('no','IScrollWindowBody0',"Step 04: verify freeze column scroll bar is not available & report is in original state")
        
if __name__ == '__main__':
    unittest.main()