'''
Created on Jul 26, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050500
TestCase Name = Verify that Calculations applied to columns can be removed by CLEAR option.
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


class C2050500_TestClass(BaseTestCase):

    def test_C2050500(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050500'
        """
            Step 01: Execute AR-RP-141CA to produce the mixed field output report.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')      
        time.sleep(6)      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01: Verify Page summary 1000of1000records')
        
        """
        Step 02: Select the Order Number INTEGER field and select CALCULATE.
        Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total. 
        """
        time.sleep(3)
        menu=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        active_misobj.verify_menu_items('ITableData0', 0, 'Calculate', menu,"Step 02: Select the Order Number INTEGER field and select CALCULATE and verify menu list")
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','Sum')
        
        """Expect to see Total Sum 500,500"""
        active_misobj.verify_calculated_value(4, 1, "Total Sum 500500",True, "Step 02: Verify Total Sum 500500 displayed on pagination bar")
        
        """Re-select Order Number INTEGER field Select CLEAR from the drop down list 
        Expect to see original report, without any of the Totaling labels for the Order Number INTEGER data."""
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','Clear')
        active_misobj.verify_calculated_value(4, 1, "Total Sum 500500",False, "Step 02: Verify Total Sum 500500 is not displayed on pagination bar")
                       
        """
        Step 03: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        Expect full report to be displayed again.1000 rows
        """
        time.sleep(3)      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03: Verify Page summary 1000of1000records')
    

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
