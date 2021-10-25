'''
Created on Jul 22, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050470
TestCase Name = Verify report shows records that does not contain EXACT Case text match
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


class C2050470_TestClass(BaseTestCase):

    def test_C2050470(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050470'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(25) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """
        Step 02: Select State > Filter > Omits (match case)
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Omits (match case)')        
        """Verify Filter selection pop up is opened."""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 02: Verify Filter selection pop up is opened.',['State', 'Omits (match case)'])
        
        """Step 03: Verify user has following options:
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All """
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 04: Verify All buttons Present.')     
        
        """ 
        Step 04: Enter 'G' in the text field.
        """      
        active_filter.create_filter(1, 'Omits (match case)', value1='G')    
                
        """ Step 05: Click Filter"""
        time.sleep(5)   
        active_filter.filter_button_click('Filter')
        """ Verify all the records returned do not contain filtered value. Verify that Filter result is case sensitive."""
        time.sleep(5)    
        active_misobj.verify_page_summary('0','97of107records,Page1of2', 'Step 05: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050470_Ds01.xlsx',"Step 05: Verify first page records returned do not contain filtered value G and result is case sensitive using data set comparision")
        """ Move Filter Selection box"""
        active_misobj.move_active_popup("1", "600", "200")
        
        time.sleep(5)
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report and verify records."""
        
        time.sleep(6)
        active_misobj.verify_page_summary('0','97of107records,Page2of2', 'Step 05: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050470_Ds02.xlsx',"Step 05: Verify second page records returned do not contain filtered value G and result is case sensitive using data set comparision")
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
