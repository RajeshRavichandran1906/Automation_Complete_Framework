'''
Created on Sep 28, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2072863
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from selenium.webdriver import ActionChains
from common.lib import utillity
import unittest,time
from common.lib.global_variables import Global_variables

class C2072863_TestClass(BaseTestCase):

    def test_C2072863(self):
        
        driver = self.driver 
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        browser=Global_variables.browser_name
        
        """
        Step 01: Execute the attached repro - ACT-628.fex.
        """
        utillobj.active_run_fex_api_login("ACT-628.fex", "S7215", 'mrid', 'mrpass')
        driver.set_window_size('900', '700')
        time.sleep(5)
        miscelanousobj.verify_freeze_column('yes', 'IScrollWindowBody0', 'Step 01.01: Expect to see only one scroll bar')
        
        """
        Step 02: Using the first scroll bar, slide the report all the way to the right.
        """
        column1 = ['COUNTRY','CAR','MODEL']
        miscelanousobj.verify_column_heading('IFixWindowBody0', column1, 'Step 02.01: Expect to see columns Country, Car & Model frozen, they should not move')
        column2 = ['DEALER_COST', 'RETAIL_COST', 'SALES', 'BODYTYPE', 'SEATS', 'RPM', 'MPG', 'ACCEL', 'BHP', 'FUEL_CAP', 'WARRANTY', 'STANDARD', 'STANDARD']
        miscelanousobj.verify_column_heading('IScrollWindowBody0',column2,'Step 02.02: Expect to see all columns to the right of Model move, so that the two fields of Standard are now visible')
        
        
        """
        Step 03: Click the maximize window control in the upper right of the screen.
        """
        
        driver.set_window_size('1000', '800')
        time.sleep(10)
        miscelanousobj.verify_freeze_column('yes', 'IScrollWindowBody0', 'Step 03.01: Expect to see only one scroll bar')
        
        """
        Step 04: Drag the scroll bar all the way to the left.
        """
        utillobj.synchronize_with_visble_text('#TCOL_0_C_14 > b > span', 'STANDARD', 50)
        move_scroll = self.driver.find_element_by_css_selector('#TCOL_0_C_14 > b > span')
        utillobj.synchronize_with_number_of_element('#popid0_14  img', 1, 2)
        pop_up=self.driver.find_element_by_css_selector('#popid0_14  img')
                
        if browser=='firefox' :
            driver.execute_script("return arguments[0].scrollIntoView();", pop_up)
            time.sleep(2)
            pop_up.click()
        else :
            action = ActionChains(driver)
            action.move_to_element(move_scroll).click(pop_up).perform()
        
        time.sleep(5)
        val1=self.driver.find_element_by_css_selector('[id="set0_14_0_3i_t"]').text
        utillobj.asequal(val1,'Filter','Step 04.01: Drag the scroll bar all the way to the left')
        val=self.driver.find_element_by_css_selector('#TCOL_0_C_14 > b > span').text
        time.sleep(5)
        utillobj.asequal(val,'STANDARD','Step 04.02: Expect to see only the first part of the first Standard field')
        time.sleep(5)
        column3 = ['COUNTRY','CAR','MODEL']
        miscelanousobj.verify_column_heading('IFixWindowBody0', column3, 'Step 04.03: Expect to see columns Country, Car & Model frozen, they should not move')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()