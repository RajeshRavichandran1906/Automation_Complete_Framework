'''
Created on Jul 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055535
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium import webdriver


class C2055535_TestClass(BaseTestCase):

    def test_C2055535(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2055535'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("AR_RP_001.fex", "S7067", 'mrid', 'mrpass')

        """
        Step 02: Click underlined page number. By default current page number is underlined.  
        Verify that go to page text box opens up
        """
        
        miscelanousobj.verify_pagination_textbox("1","Step 02: Verify that go to page text box opens up")
        
        """
        Step 03: Enter the page number for eg. # 2 and hit enter  
        Verify that entered page number is displayed with the records.
        """
        miscelanousobj.navigate_page('goto_page', 2)
        
        miscelanousobj.verify_page_summary("0","107of107records,Page2of2", "Step 03: Verify that entered page number is displayed with the records.")
        
        """
        Step 04: Enter the invalid page number like # 4 in this case.  
        Verify that user remains on the current page as page number 4 does not exist in this report.
        """
        miscelanousobj.navigate_page('goto_page', 4)
        
        miscelanousobj.verify_page_summary("0","107of107records,Page2of2", "Step 04: Verify that user remains on the current page as page number 4 does not exist in this report.")
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
