'''
Created on Jul 25, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050495
TestCase Name = Verify numeric column show bar reflecting data values
'''
import unittest,time
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
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2050495_TestClass(BaseTestCase):

    def test_C2050495(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050495'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """
        Step 02: Click dropdown menu for Unit Sales column > Visualize option
        Verify on selecting this option bars that reflect the value of the data display in a column to the right of the data.
        """
        active_misobj.select_menu_items('ITableData0', 4, 'Visualize')
        active_misobj.verify_visualization('ITableData0', 'I0r', 4, 'green', 'Step 02: Verify visualization added')          
       

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
