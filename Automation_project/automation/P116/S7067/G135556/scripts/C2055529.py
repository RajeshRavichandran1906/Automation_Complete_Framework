'''
Created on Jul 14, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055529
TestCase Name = Verify move to bottom icon moves pagination to the bottom
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.lib import take_screenshot
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.locators.loginpage_locators import LoginPageLocators
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2055529_TestClass(BaseTestCase):

    def test_C2055529(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2055529'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_001.fex','S7067','mrid','mrpass')      
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        """Verify data set of AR_RP_001.fex"""   
        utillobj.verify_data_set('ITableData0','I0r','AR_RP_001_page1.xlsx',"Step 01: Verify data set of AR_RP_001.fex")
        time.sleep(20)
        
        """
        Step 02: Click 'Move to Bottom' button located on pagination bar
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'[title$="Bottom"] img')))
        self.driver.find_element(*ActiveMiscelaneousLocators.move_toBottom).click()
        """Verify user can move pagination options to the bottom of the page"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table[id='IWindowBody0'] .arGridBar span[title='Move to Top'] img")))
        active_misobj.verify_move_to_bottom('Bottom', 'Step 02: Verify Move to Top displayed')
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Last Page']")))
        active_misobj.navigate_page('last_page')
        try:
            WebDriverWait(self.driver, 90).until(lambda s: (s.find_element(By.CSS_SELECTOR, "table[id='IWindowBody0'] .arGridBar table #ipgnum0").get_attribute('innerHTML')) == '2')
            active_misobj.verify_page_summary('0','Page2of2', 'Step 02: Verify Page summary updated to 2 ')
        except:
            print("page_summary Page2of2 not found")
            

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
