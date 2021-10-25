'''
Created on Sep 19, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064085
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
import unittest

class C2064085_TestClass(BaseTestCase):

    def test_C2064085(self):
        
        """
            Step 01: Execute the attached repro - act-292-original.fex.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("act-292-original.fex", "S7215", 'mrid', 'mrpass')
        label = '[class="xaxisOrdinal-labels!g0!mgroupLabel!"]'
        label_value = self.driver.find_element(By.CSS_SELECTOR, label).text
        utillobj.asequal(label_value,'no country','Step 01: Expect to see the following Bar Chart combined and labeled as no country')
        
        """
        Step 02: Hover over the bar for 'no country'.
        """
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar!',['CNT COUNTRY, no country: 5'], 'Step 02: Expect to see the value of 5, which represents the counts for France and England added together ')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()