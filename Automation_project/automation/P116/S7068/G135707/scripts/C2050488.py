
'''
Created on July 22, 2016
@author: gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/20550488
'''
__author__ = "Gobizen"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from common.lib import utillity


class C2050488_TestClass(BaseTestCase):

    def test_C2050488(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050488'
        
        """Step 01: Execute the AR-RP-001.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Verify output summary'
        
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2', step01)
        """Step 02: Select Unit Sales > Calculate > Min""" 
        
        miscelanousobj.select_menu_items('ITableData0', '4', 'Calculate', 'Min')
        step02 = 'Step 02 : Verify Total Min is applied for Unit Sales column and same is displayed under the column heading Verify the value: Total Min 12,386'
        
        miscelanousobj.verify_calculated_value('2', '5', "Total Min 12386", True, step02) 



if __name__ == '__main__':
    unittest.main()

