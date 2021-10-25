'''
Created on Aug 5, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064087
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2064087_TestClass(BaseTestCase):

    def test_C2064087(self):
        """
            TESTCASE VARIABLES
        """
        heading_value="//*[@text-anchor='middle' and @font-weight='bold' ]/../*[contains(text(),'Sample Heading')]"
        footing_value="//*[@y='-3']/../*[contains(text(),'Footing Text')]"
        """
            Step 01: Execute the attached repro - act-475.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("act-475.fex", "S7072", 'mrid', 'mrpass')
        
        bar=['DEALER_COST, ENGLAND: 37,853']
        miscelaneousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', bar,"Step 01a: Verify the bar riser")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!mbar!','cerulean_blue_1', "Step 01.a: Verify the color")
#         fill2 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='riser!s0!g0!mbar!']").value_of_css_property("fill")
#         browser=utillobj.parseinitfile('browser')
#         if browser=='IE':
#             utillobj.asequal('#2d66b6',fill2,"Step 01a.1: Verify the bar color")
#         else:
#             utillobj.asequal('rgb(45, 102, 182)',fill2,"Step 01a.1: Verify the bar color")
        try:
            heading = self.driver.find_element(By.XPATH,heading_value).is_displayed()
            utillity.UtillityMethods.asequal(self,True,heading,"Step 01b: Expect to see the Heading centered and in bold")
        except NoSuchElementException:
            print("Step 01b: Expect to see the Heading centered and in bold - Failed")
            
        try:
            footing = self.driver.find_elements(By.XPATH, footing_value)
            value = footing[0].is_displayed()
            utillity.UtillityMethods.asequal(self,True,value,"Step 01c: Expect to see the Footing in default location, left-justified at the bottom and normal intensity")
        except NoSuchElementException:
            print("Step 01c: Expect to see the Footing in default location, left-justified at the bottom and normal intensity")
 
if __name__ == '__main__':
    unittest.main()  
                    
            