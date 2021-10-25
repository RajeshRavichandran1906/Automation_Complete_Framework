'''
Created on Jul 25, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050496
TestCase Name = Verify that when user can select rows using more than one condition with OR operator.
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


class C2050496_TestClass(BaseTestCase):

    def test_C2050496(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050496'
        """
            Step 01: Execute AR-RP-141AL to produce the Alphanumeric field output.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141AL.fex','S7068','mrid','mrpass')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01: Verify Page summary 1000of1000records')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141AL_page1.xlsx', 'Step 01: Verify AR-RP-141AL_Page1 Data set')
        
        """
        Step 02: For field ALPHA_ORDER, enter the FILTER, EQUALS, then 000001 from the drop down value box.
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', 'large', value1='000001')
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1of1000records,Page1of1', 'Step 02: Verify Page summary 1of1000records')
        """Add another selection criteria by changing the Operator to 'OR', then click Add Condition.
        Select field ALPHA Product Descr., then select 'French Roast', from its drop down value box."""
        active_filter.filter_button_click('Operator: AND')
        active_filter.filter_button_click('Add Condition')
        active_filter.add_condition_field('ALPHA Product Descr.')
#         WebDriverWait(self.driver, 50).until(
#             EC.visibility_of_element_located((By.XPATH,"//*[@id='WCS2']//tr//td[2]//img"))) 
#         self.driver.find_element_by_xpath("//*[@id='WCS2']//tr//td[2]//img").click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ft1_0 img")))
        active_filter.create_filter(2, 'Equals', value1='French Roast')
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','219of1000records,Page1of4', 'Step 02: Verify Page summary 219of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050496_Ds01.xlsx', 'Step 02: Verify Data set')
        
        """
        Step 03: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        """
        active_filter.close_filter_dialog()
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03: Verify Page summary 1000of1000records')
        
        
        
       

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
