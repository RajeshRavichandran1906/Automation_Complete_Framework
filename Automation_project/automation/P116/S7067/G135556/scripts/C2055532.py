
'''
Created on July 13, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055532
'''


__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
import time
from selenium import webdriver
from common.lib import take_screenshot
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
from common.locators.loginpage_locators import LoginPageLocators


class C2055532_TestClass(BaseTestCase):

    def test_C2055532(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2055532'
  
        
        """Step 01: Execute the AR-RP-001.fex"""
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7067','mrid','mrpass')
         
        
        time.sleep(10)  
        
      
        step01 = 'Step 01 : Verify output'
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        
        """Step 02: Click last page arrow located on pagination bar..""" 
        miscelanousobj.navigate_page('last_page')  
        step02 = 'Step 02 : Verify user can move to last page by using the last page arrow (double arrow)'
        
        #Verify user can move to last page by using the last page arrow (double arrow)
        miscelanousobj.verify_page_summary('0','107of107records,Page2of2', step02)
  

if __name__ == '__main__':
    unittest.main()

