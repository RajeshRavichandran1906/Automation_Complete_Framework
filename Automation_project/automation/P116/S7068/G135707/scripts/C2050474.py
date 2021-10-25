'''
Created on Jul 22, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050474
TestCase Name = Verify 'x' button deletes a particular condition
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


class C2050474_TestClass(BaseTestCase):

    def test_C2050474(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050474'
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
        Step 02: Select State > Filter > equals
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Filter','Equals')               
        """Verify Filter selection pop up is opened."""           
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))     
        active_filter.verify_filter_selection_dialog(True,'Step 03: Verify Filter selection pop up is opened.',['State','Equals'])
        
        """
        Step 03: Verify user has following options:
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All 
        """
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 04: Verify All buttons Present.')     
        
        """
        Step 04: Click dropdown next to <Value> (for State column) and Select "IL " value in this test.
        Verify dropdown shows all the columns present under a report.
        """
        menu_list=['CA','CT','FL','GA','IL','MA','MO','NY','TN','TX','WA']
        active_filter.verify_filter_values_menu_list(1, menu_list, 'Step 04:  Verify dropdown shows all the columns present under a report')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ft1_0 img")))        
        active_filter.create_filter(1, 'Equals', value1='IL')
        
        """
        Step 05: Click dropdown menu for 'Add Condition'. Select 'Category' column to add
        """
        active_filter.add_condition_field('Category')
        """Verify filter condition for Category is added on the top"""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 tr:nth-child(2)")))
        active_filter.verify_filter_selection_dialog(True,'Step 05: Verify filter condition for Category is added on the top',['State', 'Equals','IL'],['Category', 'Equals'])
        
        """
        Step 06: Select 'Equals' for Category column. Click value dropdown and select 'Food' from the list
        """
        active_filter.create_filter(2, 'Equals',value1='Food') 
                              
        """ 
        Step 07: Click Filter button 
        """
        active_filter.filter_button_click('Filter')
        """ Verify result satisfies both the conditions. All records have State = IL and Category = Food"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','3of107records,Page1of1', 'Step 07: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050474_Ds01.xlsx',"Step 07:Verify result satisfies both the conditions. All records have State = IL and Category = Food")
        
        """
        Step 08: Now click 'X' next to Category column
        """
        time.sleep(3)
        active_filter.delete_filter(2)
        """Verify Category column and filter option is removed from the Filter selection pop up."""
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 08: Verify State Equals IL condition is on the top',['State', 'Equals','IL'])
        active_filter.verify_filter_selection_dialog(False,'Step 08: Verify Category column and filter option is removed from the Filter selection pop up.',['State', 'Equals'],['Category', 'Equals'])
        
        """
        Step 09: Click Filter button
        """
        active_filter.filter_button_click('Filter')
        """ Verify new result set is displayed based on modification made on column/filter selection."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','9of107records,Page1of1', 'Step 09: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2050474_Ds02.xlsx',"Step 09:Verify new result set is displayed based on modification made on column/filter selection")
        
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
