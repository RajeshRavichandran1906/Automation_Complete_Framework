'''
Created on Jul 26, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050498
TestCase Name = Verify that as Filters are removed from multiple OR Filters, record counts decrease.
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


class C2050498_TestClass(BaseTestCase):

    def test_C2050498(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050498'
        """
            Step 01: Execute AR-RP-141AL to produce the alphanumeric output report.
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
        
        """
        Step 02: Select field ALPHA_ORDER, then EQUALS, then select the value 000005. 
        """
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', 'large',value1='000005')        
        
        """ Add another condition by selecting 'OR' and select ALPHA_Product Code, then select value B141."""
        active_filter.filter_button_click('Operator: AND')
        active_filter.filter_button_click('Add Condition')
        active_filter.add_condition_field('ALPHA Product Code')
        active_filter.create_filter(2, 'Equals',value1='B141')  
        
        """Lastly, add another condition, also using 'OR' and select field ALPHA Product Descr.
        then select value Coffee Pot. Click FILTER.  """
        active_filter.filter_button_click('Add Condition')
        active_filter.add_condition_field('ALPHA Product Descr.')
        active_filter.create_filter(3, 'Equals',value1='Coffee Pot')
        active_filter.filter_button_click('Filter')
        
        """Expect 152 rows initially, each Filter condition accounting for the total number of rows."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','152of1000records,Page1of3', 'Step 02.1: Verify First Page summary 152of1000records')
#         utillobj.create_data_set('ITableData0','I0r','C2050498_Ds01_page1.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds01_page1.xlsx', 'Step 02.2: Verify Data set first Page 152of1000records')
        
        """ Next Page"""
        active_misobj.move_active_popup(1, 600, 200)
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of3', 'Step 02.3: Verify Second Page summary 152of1000records')
#         utillobj.create_data_set('ITableData0','I0r','C2050498_Ds01_page2.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds01_page2.xlsx', 'Step 02.4: Verify Data set second Page 152of1000records')
        
        """ Next Page"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 3 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page3of3', 'Step 02.5: Verify Third Page summary 152of1000records')
#         utillobj.create_data_set('ITableData0','I0r','C2050498_Ds01_page3.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds01_page3.xlsx', 'Step 02.6: Verify Data set second Page 152of1000records')
                     
        """Now remove the field ALPHA Product Code by clicking the 'X' box to the left of the fieldname. Click FILTER."""
        active_filter.delete_filter(2)
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 02.7: Verify ALPHA ORDER and ALPHA Product Descr. condition is there',['ALPHA ORDER', 'Equals','000005'],['ALPHA Product Descr.','Equals','Coffee Pot'])
        active_filter.verify_filter_selection_dialog(False,'Step 02.8: Verify ALPHA Product Code is removed from the Filter selection pop up.',['ALPHA Product Code', 'Equals','R141'])
         
        """Expect to see 68 rows, after B141 is removed."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','68of1000records,Page1of2', 'Step 02.9: Verify First Page summary 68of1000records')
#         utillobj.create_data_set('ITableData0','I0r','C2050498_Ds02_page1.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds02_page1.xlsx', 'Step 02.10: Verify Data set first page 68of1000records')
        
        """ Next Page"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of2', 'Step 02.11: Verify Second Page summary 68of1000records')
#         utillobj.create_data_set('ITableData0','I0r','C2050498_Ds02_page2.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds02_page2.xlsx', 'Step 02.12: Verify Data set second Page 68of1000records')
        
                
        """Lastly, click 'X' next to the remove the condition for the last field, ALPHA_ORDER."""
        active_filter.delete_filter(1)
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 02.13: Verify ALPHA Product Descr. condition is there',['ALPHA Product Descr.','Equals','Coffee Pot'])
        active_filter.verify_filter_selection_dialog(False,'Step 02.14: Verify ALPHA ORDER is removed from the Filter selection pop up.',['ALPHA ORDER', 'Equals','000005'])
        
        """Expect to see 67 rows, after 000005 is removed."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','67of1000records,Page1of2', 'Step 02.15: Verify First Page summary 67of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds03_page1.xlsx', 'Step 02.16: Verify Data set first page 67of1000records')
#         active_misobj.verify_calculated_value(4, 6, "Filtered Sum 116.00(0.19%)/nTotal Sum 59,503.00",True, "Step 02: Verify Filtered Sum 116.00(0.19%)/nTotal Sum 59,503.00 displayed on pagination bar")
        
        """ Next Page"""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of2', 'Step 02.17: Verify Second Page summary 67of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050498_Ds03_page2.xlsx', 'Step 02.18: Verify Data set second Page 67of1000records')
        
        """Lastly, click 'X' for the remaining Filter and click Filter."""
        active_filter.delete_filter(1)
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(False,'Step 02.19: Verify ALPHA Product Descr. condition is there',['ALPHA Product Descr.','Equals','Coffee Pot'])
        
        """Expect to see the original 1000 row report."""
        active_misobj.navigate_page('previous_page')
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.20: Verify Page summary 1000of1000records')
               
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


        
        
        
        
        
        
        
        
        
