'''
Created on Jul 22, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050475
TestCase Name = Verify value selection box as per # of unique field values
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
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2050475_TestClass(BaseTestCase):

    def test_C2050475(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050475'
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
        Step 02: Select Dollar Sales > Filter
        Verify Filter menu shows all the filter options mentioned in the Test Description.
        """
        list=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        active_misobj.verify_menu_items('ITableData0', 5, 'Filter',list,"Step 02: Verify Filter menu shows all the filter options")
        active_misobj.select_menu_items('ITableData0', 5, 'Filter','Equals')               
        
        """
        Step 03: Select Filter > Equals
        Verify Filter selection pop up is opened.
        """           
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))     
        active_filter.verify_filter_selection_dialog(True,'Step 03: Verify Filter selection pop up is opened.',['Dollar Sales','Equals'])
        
        """
        Step 04: Verify user has following options:
        1. Operator: AND 2. Add Condition (dropdown) 3. Filter 4. Highlight 5. Clear All 
        """
        active_filter.verify_filter_buttons(['Operator: AND','Add Condition','Filter','Highlight','Clear All'], 'Step 04: Verify All buttons Present.')     
        
        """
        Step 05: Click dropdown next to <Value> (for Dollar Sales column)
        Verify all the values under selected column are listed.
        Step 06: Click dropdown menu to select value in this test
        Verify that if there are more than 20 and less than 1,000 unique values, the value selection dialogbox appears.
        """
        self.driver.find_element_by_css_selector("#ftp1_1_0 img").click()
        time.sleep(3)
#         utillobj.create_popup_data_set('wall2','FiltSel2','C2050475_Ds01.xlsx')
        utillobj.verify_popup_data_set('wall2','FiltSel2','C2050475_Ds01.xlsx',"Step 06: Verify that if there are more than 20 and less than 1,000 unique values, the value selection dialogbox appears")
                
        
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
