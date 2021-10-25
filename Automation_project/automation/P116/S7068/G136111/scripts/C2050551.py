
'''
Created on Aug 16 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050551
Test CaseName = AHTML_CACHE:Filter Calculation-`Filtered Sum 0(0%)`displayed (Project 103440)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.pages import active_miscelaneous, active_filter_selection, visualization_resultarea
from common.lib import utillity


class C2050551_TestClass(BaseTestCase):

    def test_C2050551(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        
        """
        Step 01: Execute the attached 103440.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('103440.fex','S7068','mrid','mrpass')
        elem1=(By.CSS_SELECTOR, "table .arGridBar table table > tbody")
        resultobj._validate_page(elem1)
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18 records')
        
        """
        Step 02: Click on DEALER_COST drop down menu and select calculate -> SUM
        """ 
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', '1', 'Calculate', 'Sum')       
        time.sleep(10)
        active_misobj.verify_calculated_value(2, 2, "Total Sum 143,794", True,"Step 02: Verify Total Sum 143,794")
        
        """
        Step 03: Click on DEALER_COST dropdown menu and select FILTER option.
        Then select Greater than for the condition.
        Verify Filter menu shows all the filter conditions as mentioned in the below screenshot
        """
        option=['Equals', 'Not equal', 'Greater than', 'Greater than or equal to', 'Less than', 'Less than or equal to', 
     'Between', 'Not Between', 'Contains', 'Contains (match case)', 'Omits', 'Omits (match case)']
        time.sleep(3)
        active_misobj.verify_menu_items('ITableData0',1,'Filter',option,'Step 03: Verify Filter menu')
        active_misobj.select_menu_items('ITableData0', '1', 'Filter', 'Greater than')
        
        """
        Step 04: Click dropdown next to <Value> (for DEALER_COST column)
        """
        menu_list=['2,626','2,886','4,292','4,631','4,915','5,063','5,660','5,800','6,000','7,427','8,300','8,400','10,000','11,000','11,194','14,940','25,000']
        filterobj.verify_filter_values_menu_list(1, menu_list, 'Step 04: Verify all values present')
        
        """
        Step 05: Select "4631 " value in this test and click Filter button
        """
        filterobj.create_filter(1, 'Greater than', value1='4,631')
        filterobj.filter_button_click('Filter')
        """Verify the SUM and filtered values as below,
        Filtered Sum 129,359(89.96%)
        Total Sum 143,794"""
        active_misobj.verify_calculated_value(2, 2, "Filtered Sum 129,359(89.96%)\nTotal Sum 143,794", True,"Step 05.1: Verify Filtered Sum 129,359(89.96%) Total Sum 143,794")
        active_misobj.verify_page_summary(0, 'SUB/TOT14of18records,Page1of1', 'Step 05.2: Verify Pagination shows:SUB/TOT')
        utillobj.verify_data_set('ITableData0','I0r','C2050551_Ds01.xlsx',"Step 05.3: Verify entire Data set")
        
                        
if __name__ == '__main__':
    unittest.main()
    
