
'''
Created on July 13, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055530
'''

__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
import time
from common.lib import take_screenshot
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
from selenium.webdriver import ActionChains
from common.locators.loginpage_locators import LoginPageLocators


class C2055530_TestClass(BaseTestCase):

    def test_C2055530(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2055530' 
        
        """Step 01: Execute the AR-RP-001.fex"""
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7067','mrid','mrpass')
         
        time.sleep(10)   
        
        """Step 02: Click 'Move to Bottom' button located on pagination bar"""
        
        movebottom = driver.find_element(*ActiveMiscelaneousLocators.move_toBottom)
        movebottom.click()
        time.sleep(2)
        
        try: 
        #Verify user can move pagination options to the bottom of the page.
            movetop = driver.find_element(*ActiveMiscelaneousLocators.move_toTop)
            s = movetop.is_displayed()
            if s is True:
                pass
            elif s is False:
                self.fail('Move top not present')
        except: 
            self.fail('Pagination bar not moved or locator changed no such elment exception observed')
          
        """Step 03 : Click 'Move to Top' button located on pagination bar"""
        time.sleep(5)
        movetop.click()
        
        browser = utillobj.parseinitfile('browser')
        if browser == 'Edge':
            time.sleep(5)
            btn_css="table[id='IWindowBody0'] .arGridBar span[title='Move to Bottom'] img"
            action=ActionChains(self.driver)
            action.move_to_element(driver.find_element_by_css_selector(btn_css)).perform()
            del action
        time.sleep(3)
        #Verify user can move pagination options to the top of the page.
        miscelanousobj.verify_move_to_bottom('Top', 'Step 03 : Click Move to Top button located on pagination bar')
        
        time.sleep(2)
         
       

if __name__ == '__main__':
    unittest.main()

