'''
Created on Sep 7, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2062892
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest
from selenium.webdriver.common.by import By


class C2062892_TestClass(BaseTestCase):

    def test_C2062892(self):
        
        """
            Step 01: Execute the 121426.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("act-195.fex", "S7074", 'mrid', 'mrpass')
        element = self.driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(element, 'C2062892_pic01', image_type='actual_images')
        
        value = self.driver.find_element(By.CSS_SELECTOR,'#MAINTABLE_wbody0_ft div').text
        utillobj.asequal('RETAIL_COST, P6.2 Dcost by COUNTRY, CAR',value,'Step 01.2: Verify 121426.fex title')
        
        """
        Step 02: Hover over the last P6.2 Dcost Bar for W GERMANY/BMW.
        """
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0_f', 'riser!s1!g9!mbar', ['P6.2 Dcost, W GERMANY/BMW: 49,500.00'], 'Step 02: Expect to see the value 49,500.00 with no overflow characters')
        utillobj.verify_chart_color('MAINTABLE_wbody0_f', 'riser!s1!g9!mbar','gold_tips',"Step 02.2: Verify Chart piebevel Color ")
        
if __name__ == '__main__':
    unittest.main() 
        