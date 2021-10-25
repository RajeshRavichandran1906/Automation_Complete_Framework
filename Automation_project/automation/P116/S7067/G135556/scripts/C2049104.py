'''
Created on Jul 13, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7067&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2049104
TestCase Name = Basic Report Navigation using the Pagination Control
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


class C2049104_TestClass(BaseTestCase):

    def test_C2049104(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2049104'
        """
            Step 01: Execute the attached Fex - Active_report
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('Active_report.fex','S7067','mrid','mrpass')     
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        """Expect to see a 3 page report containing 158 rows.
        Each Page is configured for 57 lines/page by default."""
        active_misobj.verify_page_summary('0','158of158records,Page1of3', 'Step 01: Verify Page summary')
        utillobj.verify_data_set('ITableData0','I0r','C2049104_Ds01.xlsx',"Step 01: Verify 57 lines in first Page using data set")
        time.sleep(30)
        
        """
        Step 02: In the Pagination area at the top of the report, click the first arrow to the right of the page numbers.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of3', 'Step 02: Verify Page summary updated to 2')
        """Verify that there are now two sets of arrows, those on the left,
        that go to previous page(s) and those on the right, that go forward in the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Last Page']")))
        time.sleep(6)
        active_misobj.verify_navigate_page('last_page',"Step 02: Verify Last Page double arrow displayed")
        time.sleep(6)
        active_misobj.verify_navigate_page('first_page',"Step 02: Verify First Page double arrow displayed")
                
        """
        Step 03: Click the first arrow on the right side to advance another single page.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to be positioned on Page 3 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(2)
        active_misobj.verify_page_summary('0','Page3of3', 'Step 03: Verify Page summary updated to 3')
        """Notice that there are no longer arrows on the right side of the Pagination bar. 
        Page 3 is the last page. Only the previous Page arrows are available."""
        try:
            img_status=self.driver.find_element_by_css_selector("table .arGridBar span[title='Last Page']").is_displayed()
        except NoSuchElementException:
            img_status='False'
            utillity.UtillityMethods.asequal(self,'False', img_status, "Step 03: Verify no arrows on the right side of the Pagination bar")
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Previous Page']")))
        active_misobj.verify_navigate_page('previous_page',"Step 03: Verify Previous Page double arrow displayed")
        active_misobj.verify_navigate_page('first_page',"Step 03: Verify first Page double arrow displayed")
        """
        Step 04: Click the double arrow on the left side page control.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='First Page']")))        
        """Hover over should say First Page."""
        action = ActionChains(self.driver) 
        Target = self.driver.find_element_by_css_selector("table .arGridBar span[title='First Page']")       
        action.move_to_element(Target)
        time.sleep(5)
        page1= self.driver.find_element_by_css_selector("table .arGridBar span[onclick*='Page(0)']").get_attribute('title')
        utillity.UtillityMethods.asequal(self,page1,'First Page',"Step 04: Hover over Tooltip doesn't display First Page")
        time.sleep(5)
        active_misobj.navigate_page('first_page')
        """Expect to be back on Page 1 of the report"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(3)
        active_misobj.verify_page_summary('0','Page1of3', 'Step 04: Verify Page summary back to 1')
        
        """
        Step 05: Click on the double arrow on the right side.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Last Page']")))
        time.sleep(4)
        active_misobj.navigate_page('last_page')
        """Expect to be at the bottom of the report, Page 3."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(3)
        active_misobj.verify_page_summary('0','Page3of3', 'Step 05: Verify Page summary updated to 3 ')
                
        """
        Step 06: Click the number 3, which is underlined, immediately following the text 'Page'
        Expect to see a small data entry box appear with the current page number of 3
        """
        time.sleep(3)
        active_misobj.verify_pagination_textbox('3', 'Step 06: Verify Textbox value')
        
        """
        Step 07:Change the value to 2.Hit the enter key.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Goto Page']")))
        active_misobj.navigate_page('goto_page',2)
        time.sleep(3)
        """Expect to see report positioned at the user entered Page number 2."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        active_misobj.verify_page_summary('0','Page2of3', 'Step 07: Verify Page summary updated to 2')
        
        """
        Step 08: Click the underlined Page 2 and change it to 99. Hit the enter key.
        """
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Goto Page']")))
        active_misobj.navigate_page('goto_page',99)
        time.sleep(3)
        """ Expect to stay on Page 2."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        active_misobj.verify_page_summary('0','Page2of3', 'Step 07: Verify Page summary updated to 2')

        
if __name__ == '__main__':
    unittest.main()
    
        
        
        
        
        
        
        
