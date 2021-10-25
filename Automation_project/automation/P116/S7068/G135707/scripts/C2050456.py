'''
Created on Jul 14, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050456
TestCase Name = Verify report shows records for Equal (single select)
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


class C2050456_TestClass(BaseTestCase):

    def test_C2050456(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050456'
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
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary')
        active_misobj.verify_column_heading('ITableData0', ['Category','Product ID','Product','State','Unit Sales','Dollar Sales'], "Step 01.2: Verify Column heading of AR-RP-001.fex")
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001_page1.xlsx',"Step 01.3: Verify entire Data set in Page 1")
        
        """
        Step 02: Select State > Filter
        Step 03:  Select Filter > Equals
        """
        """ Verify Filter menu shows all the filter options mentioned in the Test Description - Equals"""
        option=['Equals','Not equal','Greater than','Greater than or equal to','Less than','Less than or equal to','Between','Not Between','Contains','Contains (match case)', 'Omits','Omits (match case)']
        active_misobj.verify_menu_items('ITableData0',3,'Filter',option, 'Step 2: Verify Filter menu shows all the filter options')
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')        
         
        """Step 03: Verify Filter selection pop up is opened Verify user has following options: 
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All"""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 3: Verify Filter selection pop up is opened.',['State', 'Equals'])
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 03: Verify All buttons Present.')     
         
        """ 
        Step 04: Click dropdown next to <Value> (for State column)        
        Verify all the values under selected column are listed"""
        menu_list=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        active_filter.verify_filter_values_menu_list(1, menu_list, 'Step 04: Click dropdown next to <Value> (for State column)')        
         
        """
        Step 05: Select "IL " value in this test and click Filter button
        """
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ft1_0 img")))
        active_filter.create_filter(1, 'Equals', value1='IL')
        active_filter.filter_button_click('Filter')        
        """ Verify all the matching records are displayed under a report. See attached screenshot."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','9of107records,Page1of1', 'Step 05: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050456_Ds01.xlsx',"Step 05: Verify all the matching records are displayed under a report")
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
