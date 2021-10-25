'''
Created on Sep 19, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064080
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

class C2064080_TestClass(BaseTestCase):

    def test_C2064080(self):
        
        """Test Case Variables"""
        combo_box = '[id="combobox_dPROMPT_1"]'
        risers = '#MAINTABLE_wbody0_f [class="risers"] [class*="riser!s0!g"]'
        
        """
            Step 01: Execute the attached repro - ACT-203.fex.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("act-203.fex", "S7215", 'mrid', 'mrpass')
        
        
        combo = self.driver.find_element(By.CSS_SELECTOR,combo_box)
        try: 
            val = combo.is_displayed()
            utillobj.asequal(True, val, 'Step 01.1: Expect to see A Combo Box')
        except NoSuchElementException:
            self.fail('Step 01.1: Expect to see A Combo Box - Failed')
            
        option = self.driver.find_element(By.CSS_SELECTOR,"[selected]").text
        utillobj.asequal(option,'Jun, 1988',"Step 01.2: Expect to see A Combo Box at the top set to Jun, 1988")
        risers_count = len(self.driver.find_elements(By.CSS_SELECTOR, risers))
        utillobj.asequal(risers_count,2,"Step 01.3: Expect to see a Bar Chart with two bars")
        
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', ['COPIES, ACTION/VERHOVEN P.: 3'], 'Step 01.4: Verify tooltip ')
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g1!mbar!', ['COPIES, FOREIGN/SCOLA E.: 1'], 'Step 01.5: Verify tooltip ')
            
        """
        Step 02: From the Combo Box, select the next to last value of Jun, 1990, near the bottom.
        """
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        if browser=='Edge':
            select = self.driver.find_element(By.CSS_SELECTOR,'select#combobox_dsPROMPT_1')    
            select.send_keys("Jun, 1990")
        else:
            select = Select(self.driver.find_element(By.TAG_NAME,'select'))    
            select.select_by_visible_text('Jun, 1990')
        
        time.sleep(5)
        risers_count1 = len(self.driver.find_elements(By.CSS_SELECTOR, risers))
        utillobj.asequal(risers_count1,1,"Step 02.1: Expect to see a single bar ")
        time.sleep(3)
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', ['COPIES, MYSTERY/BECKER H.: 4'], 'Step 02.2: Verify tooltip ')            
            
        """
        Step 03: From the Combo Box, select the first value of Jun, 1939 at the top.
        """

        if browser=='Edge':
            select = self.driver.find_element(By.CSS_SELECTOR,'select#combobox_dsPROMPT_1')    
            select.send_keys("Jun, 1939")
        else:
            select = Select(self.driver.find_element(By.TAG_NAME,'select'))    
            select.select_by_visible_text('Jun, 1939')
        
        time.sleep(4)
        risers_count1 = len(self.driver.find_elements(By.CSS_SELECTOR, risers))
        utillobj.asequal(risers_count1,1,"Step 03.1: Expect to see a single bar ")
        time.sleep(5)
        miscelanousobj.verify_active_chart_tooltip('MAINTABLE_wbody0', 'riser!s0!g0!mbar!', ['COPIES, CLASSIC/FLEMING V.: 3'], 'Step 03.2: Verify tooltip ')            
            
            
if __name__ == "__main__":
    unittest.main()
            
            
            
            
            
            
            