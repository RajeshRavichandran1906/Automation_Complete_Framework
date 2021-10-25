'''
Created on Sep 7, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2066748
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time


class C2066748_TestClass(BaseTestCase):

    def test_C2066748(self):
        
        """Test Case Variable"""
        
        convertible="#MAINTABLE_0 [class*='riser!s0!g0!mbar!']"
        roadster ="#MAINTABLE_0 [class*='riser!s0!g4!mbar!']"
        hardtop = "#MAINTABLE_1 [class*='riser!s0!g1!mbar!']"
        coupe = "#MAINTABLE_1 [class*='riser!s0!g3!mbar!']"
        tooltip = "[id='ibi$tt$0']"
        tooltip_1 = "[id='ibi$tt$1']" 
        
        """
            Step 01: Execute the ACT-318.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        
        utillobj.active_run_fex_api_login("ACT-318.fex", "S7074", 'mrid', 'mrpass')
        element = self.driver.find_element_by_css_selector("#orgdiv0")
    
        
        """
        Step 02: Hover over, then left-click the first bar on the vertical chart, for CONERTIBLE.
        """
        convertible_field=self.driver.find_element(By.CSS_SELECTOR,convertible)
        self.driver.find_element(By.CSS_SELECTOR,convertible).click()
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,tooltip)))
        tool_tip=self.driver.find_element(By.CSS_SELECTOR,tooltip)
        riser1 = tool_tip.location['x'] - convertible_field.location['x']
        if riser1 < 20:
            print('Step 02: Expect to see the hover over value, then the Context menu close to the host bar - Passed')
         
        else:
            self.fail('Step 02: Expect to see the hover over value, then the Context menu close to the host bar - Failed')
        
        """
        Step 03: Click in the body of the report, not on a bar to reset.
        Hover over, then left-click the last bar on the vertical chart, for ROADSTER.
        """
        roadster_bar = self.driver.find_element(By.CSS_SELECTOR,roadster)
        self.driver.find_element(By.CSS_SELECTOR,roadster).click()
        time.sleep(4)
        riser2 = tool_tip.location['x'] - roadster_bar.location['x']
        if riser2 < 20:
            print('Step 03: Expect to see the hover over value, then the Context menu close to the host bar - Passed')
         
        else:
            self.fail('Step 03: Expect to see the hover over value, then the Context menu close to the host bar - Failed')
        
        """
        Step 04: Hover over, then left-click the second bar on the vertical chart, for HARDTOP.
        """
        hardtop_bar = self.driver.find_element(By.CSS_SELECTOR,hardtop)
        self.driver.find_element(By.CSS_SELECTOR,hardtop).click()
        utillobj.synchronize_with_number_of_element(tooltip_1, 1, 10)
        tool_tip1=self.driver.find_element(By.CSS_SELECTOR,tooltip_1)
        time.sleep(4)
        riser3 = hardtop_bar.location['x'] - tool_tip1.location['x']
        if riser3 < 25:
            print('Step 04: Expect to see the hover over value, then the Context menu close to the host bar - Passed')
         
        else:
            self.fail('Step 04: Expect to see the hover over value, then the Context menu close to the host bar - Failed')
        
        """
        Step 05: Click in the body of the report, not on a bar to reset.
        Hover over, then left-click the fourth bar on the vertical chart, for COUPE.
        """
        
        coupe_bar = self.driver.find_element(By.CSS_SELECTOR,coupe)
        self.driver.find_element(By.CSS_SELECTOR,coupe).click()
        time.sleep(4)
        riser4 = coupe_bar.location['x'] - tool_tip1.location['x'] 
        if riser4 < 25:
            print('Step 05: Expect to see the hover over value, then the Context menu close to the host bar - Passed')
         
        else:
            self.fail('Step 05: Expect to see the hover over value, then the Context menu close to the host bar - Failed')
        
        
if __name__ == '__main__':
    unittest.main() 
             
        
        
        
        
        
        
        
        