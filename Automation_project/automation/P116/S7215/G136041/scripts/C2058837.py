'''
Created on Sep 28, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2058837
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest

class C2058837_TestClass(BaseTestCase):

    def test_C2058837(self):
        
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
        Step 01: Execute the attached repro ACT-485t.fex
        """

        utillobj.active_run_fex_api_login("ACT-485-18pt.fex", "S7215", 'mrid', 'mrpass')
        
        heading = '#THEAD_0_1_0_0 div'
        title = '[class="xaxisOrdinal-title"]'
        val = self.driver.find_element_by_css_selector(title).text
        utillobj.asequal(val,'CAR','Step 01.1: Expect to see the ACT-485-18pt.fex Active Report')
        heading_text = self.driver.find_element_by_css_selector(heading).value_of_css_property('font-size')
        utillobj.asequal(heading_text,'18px','Step 01.2: Verify Heading font size shows 18 point')
        utillobj.infoassist_api_logout()
        
        """
        Step 02: Execute the attached repro act485-24pt.fex
        """
        utillobj.active_run_fex_api_login("ACT-485-24pt.fex", "S7215", 'mrid', 'mrpass')
        
        val1 = self.driver.find_element_by_css_selector(title).text
        utillobj.asequal(val1,'CAR','Step 02.1: Expect to see the ACT-485-24pt.fex Active Report')
        heading_text_1 = self.driver.find_element_by_css_selector(heading).value_of_css_property('font-size')
        utillobj.asequal(heading_text_1,'24px','Step 02.2: Verify Heading font size shows 24 point')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()