'''
Created on Aug 29, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053823
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
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_tools
from common.lib import utillity


class C2053823_TestClass(BaseTestCase):

    def test_C2053823(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053823'
        """
        Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary 107of107')
        
        """
        Step 02: Click dropdown menu for Unit Sales column and mouse over Pivot(Cross Tab)
        Verify Group By (Columns) are displayed as: - Category - Product ID - Product - State - Unit Sales - Dollar Sales
        """
        option=['Group By(SUM)', 'Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_menu_items('ITableData0', 4, 'Pivot (Cross Tab)',option,"Step 02: Expect to see Group By (Columns) ")
        time.sleep(5)                
        """
        Step 03: Click dropdown menu for Unit Sales column and mouse over Pivot(Cross Tab) > any column (Category) > Product ID
        """
        ele = driver.find_element_by_css_selector("#TCOL_0_C_4")
        ele.click()
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', 4, 'Pivot (Cross Tab)','Category','Product ID')         
        """Verify Pivot table 'State By Product ID, Category' is generated based on the columns selection."""    
        utillobj.verify_pivot_data_set('piv1', 'C2053823_Ds01.xlsx','Step 03: Verify Pivot dataset')  
        
        """
        Step 04: Change the aggregation measure from SUM to AVG
        Verify that Pivot table is now is shows Sum as aggregation for Unit Sales on the pivot table. See attached screenshot.
        """
        time.sleep(3)
        pivobj.select_aggregate_function('wall1', 0, 'Avg',verify=True)                
        pivobj.veryfy_pivot_table_title('piv1', 'UnitSalesbyProductID,Category', 'Step 04.1: Verify pivot table title')
        utillobj.verify_pivot_data_set('piv1', 'C2053823_Ds02.xlsx','Step 04.2: Verify Pivot dataset')


if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
