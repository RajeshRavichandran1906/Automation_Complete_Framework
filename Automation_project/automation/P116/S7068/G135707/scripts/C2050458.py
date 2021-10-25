'''
Created on Jul 19, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050458
TestCase Name = Verify report highlights records for Equal
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


class C2050458_TestClass(BaseTestCase):

    def test_C2050458(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050458'
        """
            Step 01: Execute the AR_RP_001.fex
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
        Step 03: Select Filter > Equals
        """
        """ Verify Filter menu shows all the filter options mentioned in the Test Description - Equals"""
        list1=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        active_misobj.verify_menu_items('ITableData0', 3, 'Filter',list1,"Step 2: Verify Filter menu shows all the filter options")
        time.sleep(3)
        ele = driver.find_element_by_css_selector("#TCOL_0_C_3")
        ele.click()
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')
        
        """Step 03: Verify Filter selection pop up is opened."""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog('Step 3: Verify Filter selection pop up is opened.',['State', 'Equals'])
        
        """Step 04: Verify user has following options:
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All """
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 04: Verify All buttons Present.')     
        """ 
        Step 05: Click dropdown next to <Value> (for State column)
        """
        """Verify all the values under selected column are listed."""
        menu_list=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        active_filter.verify_filter_values_menu_list(1, menu_list, 'Step 04: Click dropdown next to <Value> (for State column)')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ft1_0 img")))        
        active_filter.create_filter(1, 'Equals', value1='IL')    
                
        """ Step 06: Select "IL " value in this test and click Highlight button"""
        active_filter.filter_button_click('Highlight')
        """ Verify all the matching records (9 rows) are highlighted under a report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page1of2', 'Step 06: Verify Page summary is 1')
        active_misobj.verify_highlighted_rows('ITableData0', 5, "Step 06: Verify all matching records (5rows) are highlighted under a report in Page 1")
        utillobj.verify_data_set('ITableData0','rgb','C2050458_Ds01.xlsx',"Step 06: Verify all the matching records are displayed under a report")
        """ Move Filter Selection box"""
        active_misobj.move_active_popup("1", "600", "200")
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        time.sleep(4)
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of2', 'Step 06: Verify Page summary updated to 2')
        time.sleep(4)
        active_misobj.verify_highlighted_rows('ITableData0', 4, "Step 06: Verify all matching records (4rows) are highlighted under a report in Page 2")
        utillobj.verify_data_set('ITableData0','rgb','C2050458_Ds02.xlsx',"Step 06: Verify all the matching records are displayed under a report")
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
