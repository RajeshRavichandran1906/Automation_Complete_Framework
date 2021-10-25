'''
Created on Jul 25, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050497
TestCase Name = Verify that Filters may be applied to Calculated values on an Active Report.
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


class C2050497_TestClass(BaseTestCase):

    def test_C2050497(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050497'
        """
            Step 01: Execute AR-RP-141CA to produce the multi-format output report.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01: Verify Page summary 1000of1000records')
        
        """
        Step 02: Select field for D10.2 Unit Price. Select CALCULATE, then SUM. 
        """
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', 5, 'Calculate','Sum')
        """Verify that the Total Sum is 59,503.00"""
        active_misobj.verify_calculated_value(4, 6, "Total Sum 59,503.00",True, "Step 02.1: Verify Total Sum 59,503.00 displayed on pagination bar")
        
        """Now select the Order Number INTEGER field and select FILTER, then EQUALS, then values 1 and 2. """
        active_misobj.select_menu_items('ITableData0', 0, 'Filter','Equals')
        active_filter.create_filter(1, 'Equals', 'large', value1='2',value2='1')
        
        """In the Filter menu, change the Operator to OR, then click Add Condition, then select field ALPHA Store Code.
        Select from the value box value R1020. Click on Filter."""
        active_filter.filter_button_click('Operator: AND')
        active_filter.filter_button_click('Add Condition')
        active_filter.add_condition_field('ALPHA Store Code')
        active_filter.create_filter(2, 'Equals',value1='R1020')      
        active_filter.filter_button_click('Filter')
        
        """Expect 92 rows, showing data for Order Numbers 1 & 2 OR ALPHA Store Code R1020.
        Filtered Sum 5,342.00(8.98%) added to Total Sum 59,503.00, under the D10.2 Unit Price column."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','92of1000records,Page1of2', 'Step 02.2: Verify First Page summary 92of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050497_Ds01_page1.xlsx', 'Step 02.3: Verify Data set first Page 92of1000records')
        """Filtered Sum 5,342.00(8.98%) added to Total Sum value of 59,503.00, under the D10.2 Unit Price column."""
        active_misobj.verify_calculated_value(4, 6, "Filtered Sum 5,342.00(8.98%)\nTotal Sum 59,503.00",True, "Step 02.4: Verify Filtered Sum 5,342.00(8.98%)/nTotal Sum 59,503.00 displayed on pagination bar")
        
        """ Next Page"""
        active_misobj.move_active_popup(1, 600, 200)
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar span[title='Next Page']")))
        active_misobj.navigate_page('next_page')
        """Expect to advance to Page 2 of the report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))
        time.sleep(6)
        active_misobj.verify_page_summary('0','Page2of2', 'Step 02.5: Verify Second Page summary 92of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050497_Ds01_page2.xlsx', 'Step 02.6: Verify Data set second Page 92of1000records')
        
                     
        """Now remove the field ALPHA Product Code by clicking the 'X' box to the left of the fieldname. Click FILTER."""
        active_filter.delete_filter(2)
        active_filter.filter_button_click('Filter')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))
        active_filter.verify_filter_selection_dialog(True,'Step 02.7: Verify Order Number INTEGER Equals 1 and 2 condition is on the top','Order Number INTEGER')
        active_filter.verify_filter_selection_dialog(False,'Step 02.8: Verify ALPHA Store Code Equals R1020 is removed from the Filter selection pop up.',['ALPHA Store Code', 'Equals','R1020'])
#         
        """Expect 2 rows for the remaining Order Number INTEGER.
        Filtered Sum 116.00(0.19%) added to Total Sum value of 59,503.00, under the D10.2 Unit Price column."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','2of1000records,Page1of1', 'Step 02.9: Verify Page summary 2of1000records')
        utillobj.verify_data_set('ITableData0','I0r','C2050497_Ds02.xlsx', 'Step 02.10: Verify Data set 2of1000records')
        active_misobj.verify_calculated_value(4, 6, "Filtered Sum 116.00(0.19%)\nTotal Sum 59,503.00",True, "Step 02.11: Verify Filtered Sum 116.00(0.19%)/nTotal Sum 59,503.00 displayed on pagination bar")
                
        """Lastly, click 'X' next to the remove the condition for the last field, ALPHA_ORDER."""
        active_filter.delete_filter(1)
        active_filter.filter_button_click('Filter')
        active_filter.verify_filter_selection_dialog(False,'Step 02.12: Verify Order Number INTEGER is removed from the Filter selection pop up.',['Order Number INTEGER', 'Equals'])
        
        """Expect to see the original 1000 row report."""
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 02.13: Verify Page summary 1000of1000records')
               
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


        
        
        
        
        
        
        
        
        
