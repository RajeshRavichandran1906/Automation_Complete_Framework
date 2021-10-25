'''
Created on Jan 24, 2017

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050554
Description : Verify selected column inside the filter window should be autofit and move along anywhere in the browser.
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui


class C2214174_TestClass(BaseTestCase):

    def test_C2214174(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2214174'
        """
            Step 01: Project 129369 AHTML:Filter Cell - Highlight Row - selects no or wrong row 
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("ACT-1028.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(8)
        
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', "Step 01: Execute the ahtmltab.fex - Top Head line verification Table 1")
    
        
        utillobj.verify_data_set('ITableData0','I0r','C2214174_Ds01.xlsx',"Step 01: Verify table loaded data correctly table1")
        
        #utillobj.create_data_set('ITableData0','I0r','C2214174_Ds01.xlsx')     

        
        """Step 02 : Enter the string - ITALY into the Text Box, no quotes. Hit Enter.'"""
        #Expect to see a 4 line report displaying only Italian cars.
        
        input_1 = driver.find_element_by_css_selector("#textinputPROMPT_1 > input[type='text']")
        utillobj.set_text_field_using_actionchains(input_1, "ITALY")
        time.sleep(2)
        input_1.send_keys(Keys.ENTER)
        time.sleep(6)
        utillobj.verify_data_set('ITableData0','I0r','C2214174_Ds02.xlsx',"Step 02: Verify table loaded data correctly table1")
        #utillobj.create_data_set('ITableData0','I0r','C2214174_Ds02.xlsx')
        
        """Step 03: Enter the string - [All] into the Text Box, no quotes and case sensitive. Hit Enter."""
        
        
        input_1 = driver.find_element_by_css_selector("#textinputPROMPT_1 > input[type='text']")
        utillobj.set_text_field_using_actionchains(input_1, "[All]")
        time.sleep(2)
        input_1.send_keys(Keys.ENTER)
        time.sleep(6)
        #utillobj.create_data_set('ITableData0','I0r','C2214174_Ds03.xlsx')   
        utillobj.verify_data_set('ITableData0','I0r','C2214174_Ds03.xlsx',"Step 03: Verify table loaded data correctly table1")
        
        
if __name__ == '__main__':
    unittest.main()                         