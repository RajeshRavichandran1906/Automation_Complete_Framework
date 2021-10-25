'''
Created on Jul 18, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050457
TestCase Name = Verify report shows records for Equal (multi select)
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


class C2050457_TestClass(BaseTestCase):

    def test_C2050457(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050457'
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
        Step 02: Select State > Filter
        Step 03:  Select Filter > Equals
        """
        """ Verify Filter menu shows all the filter options mentioned in the Test Description - Equals"""
        option=['Equals','Not equal','Greater than','Greater than or equal to','Less than','Less than or equal to','Between','Not Between','Contains','Contains (match case)', 'Omits','Omits (match case)']
        active_misobj.verify_menu_items('ITableData0',3,'Filter',option, 'Step 2: Verify Filter menu shows all the filter options')
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')        

        """Step 03: Verify Filter selection pop up is opened."""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 3: Verify Filter selection pop up is opened.',['State', 'Equals'])        
        
        """Step 04: Verify user has following options:
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All """        
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 04: Verify All buttons Present.')     
        """ 
        Step 05: Select "CA ", "MA", "NY" values in this test (Use ctrl to apply muti selection)
        """
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ft1_0 img")))
        active_filter.create_filter(1, 'Equals', value1='CA',value2='NY', value3='MA')
        
        """ Step 06: Click Filter button"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))         
        active_filter.filter_button_click('Filter')
        """ Verify all selected options are checked under dropdown menu."""
        menu_list=['CA','MA','NY']
        active_filter.verify_value_selection(1, menu_list, 'Step 06: Verify all selected options are checked under dropdown menu')
        
        """ Verify 30/107 records (matching records) are displayed under a report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','30of107records', 'Step 06: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050457_Ds01.xlsx',"Step 06: Verify all the matching records are displayed under a report")
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
