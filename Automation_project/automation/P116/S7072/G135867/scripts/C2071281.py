'''
Created on Aug 8, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2071281
Description : AHTML: LAYOUTRTL lost when using PRINT option (ACT-319).
'''
import unittest
import time
from selenium import webdriver
from common.lib import take_screenshot
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from common.locators.loginpage_locators import LoginPageLocators
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2071281_TestClass(BaseTestCase):

    def test_C2071281(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2071281'
        heading_value="//*[@text-anchor='middle' and @font-weight='bold' ]/../*[contains(text(),'Sample Heading')]"
        footing_value="//*[@y='-3']/../*[contains(text(),'Footing Text')]"
        """
            Step 01: Execute the attached repro - act-319.fex
        """
        
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('act-319.fex','S7072','mrid','mrpass')      
        time.sleep(8)
        
       

#         Expect to see the following Active Report.

#         Also expect to see the columns reversed, with the order
#         Dealer_Cost, Retail_Cost, Sales & Country. This is the opposite of the regular display.
#         Also expect to see the drop down controls on the left of each column.
        
        
        active_misobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01: Execute the act-319.fex - Top Head line verification")
        
        
        utillobj.verify_data_set('ITableData0','I0r','act-319.xlsx',"Step 01: Expect to see the following Active Report. ")
        
        #utillobj.create_data_set('ITableData0','I0r','act-319.xlsx')
        
        #Expect to see it in the upper right side of the pane.
        
        tab = driver.find_element_by_css_selector("table#ITableData0")
        
        y = driver.get_window_size()['width']
         
        a= tab.size['width']
        b=tab.location['x'] 
         
        x =a+b
        if x in range(y-50,y):
            print('Step 02: Expect to see table in the upper right side of the pane.')
             
        else:
            self.fail('Step 02:Expect to see table in the upper right side of the pane. Failed')
       
        """Step 03: Click the drop down for Dealer_Cost, select Print, then ALL Records."""
        
        active_misobj.select_menu_items("ITableData0", "2", "Print","All records")
        time.sleep(15)
        
        """Expect to see a Printer panel open.
        This will vary based on who runs thjs Fex.
        Verify ONLY that the menu appears."""
        
        
        """Step 04: From the list of Printers, select an addressable device to use for the hard copy report.Click Print."""
        
        """Expect to see a confirmation message from the Printer services menu.
        Again, verify ONLY that the print message was generated.
        Expect to see the Printed page match the report generated in Step 1."""
        utillobj.autoit_print("Step 04: Expect to see a confirmation message from the Printer services menu")
        time.sleep(9)

if __name__ == '__main__':
    unittest.main()  
                       
        
            
            
            
            
            
            
            
            
            
            
            
            