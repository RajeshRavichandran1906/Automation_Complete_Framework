'''
Created on Jul 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055534
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2055534_TestClass(BaseTestCase):

    def test_C2055534(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2055534'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("AR_RP_001.fex", "S7067", 'mrid', 'mrpass')
        
        """
        Step 02: Click Next page arrow located on pagination bar.  
        Verify user can move to next page by using the next page arrow (single arrow)
        """
        miscelanousobj.navigate_page('next_page')
        
        miscelanousobj.verify_page_summary("0","107of107records,Page2of2", "Step 02: Verify user can move to next page by using the next page arrow (single arrow)")
        
        """
        Step 03: Click first page arrow located on pagination bar.  
        Verify user can move to first page by using the first page arrow (double arrow)
        """
        miscelanousobj.navigate_page("first_page")
        
        miscelanousobj.verify_page_summary("0","107of107records,Page1of2", "Step 03: Verify user can move to first page by using the first page arrow (double arrow)")
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
