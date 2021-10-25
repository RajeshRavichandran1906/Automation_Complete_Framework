'''
Created on Aug,5 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108674
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


class C2108674_TestClass(BaseTestCase):

    def test_C2108674(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108674'
        """
            Step 01: Execute the attached repro - act-703a.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('act-703a.fex','S7072','mrid','mrpass')      
        time.sleep(8)
        row1 = {'width': 62, 'height': 22}
        active_misobj.verify_cell_property_size('ITableData0', 0, 0,row1,"Step 02: Expect to see the following Active Report. This is the default, no gaps set.")
         
        """Step 02 : Execute the attached repro - act-703b.fex"""
        
        
        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login('act-703b.fex','S7072','mrid','mrpass') 
        time.sleep(4)
        row1 = {'width': 62, 'height': 22}
        active_misobj.verify_cell_property_size('ITableData0', 0, 0,row1,"Step 02: Expect to see the following Active Report. This is the default, no gaps set.")
         
        """Step 03: Execute the attached repro - act-703c.fex"""
        
#         Expect to see the following Active Report.
#         This is the version with minimal values for all four gap settings.
#         TOPGAP=.025
#         BOTTOMGAP=.025
#         LEFTGAP=.050
#         RIFGTGAP=.050
        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login('act-703c.fex','S7072','mrid','mrpass')   
        time.sleep(4)
        row1 = {'height': 24, 'width': 71}
        active_misobj.verify_cell_property_size('ITableData0', 0, 0,row1,"Step 03: Expect to see the following Active Report.  This is the version with minimal values for all four gap settings..")
         
        
        
        """Step 04: Execute the attached repro - act-703d.fex"""
        
#         Expect to see the following Active Report.
#         This is the version with median values for all four gap settings.
#         TOPGAP=.050
#         BOTTOMGAP=.050
#         LEFTGAP=.100
#         RIFGTGAP=.100


        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login('act-703d.fex','S7072','mrid','mrpass')   
        time.sleep(4)
        row1 = {'height': 28, 'width': 80}
        active_misobj.verify_cell_property_size('ITableData0', 0, 0,row1,"Step 04: Expect to see the following Active Report.  ")
         
        
       
        """Step 05: Execute the attached repro - act-703e.fex"""
#         Expect to see the following Active Report.
#         This is the version with large values for all four gap settings.
#         TOPGAP=.150
#         BOTTOMGAP=.150
#         LEFTGAP=.200
#         RIFGTGAP=.200

        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login('act-703e.fex','S7072','mrid','mrpass')   
        time.sleep(4)
        row1 = {'height': 42, 'width': 104}
        active_misobj.verify_cell_property_size('ITableData0', 0, 0,row1,"Step 05: Expect to see the following Active Report.")
         
        
        
       
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
