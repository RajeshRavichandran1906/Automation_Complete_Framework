'''
Created on Jul 27, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050511
TestCase Name = Verify that Distinct option of Calculate shows the Distinct Count for that particular column.
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


class C2050511_TestClass(BaseTestCase):

    def test_C2050511(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050511'
        """
            Step 01: Execute AR-RP-141CA to produce the mixed field output report.
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
        Step 02: For each field, including INTEGER, ALPHA, DATE, D10.2, P9.2M and DATETIME click the down arrow in the heading, then select CALCULATE
        Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        """
        """INTEGER"""
        menu=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        active_misobj.verify_menu_items('ITableData0', 0, 'Calculate', menu,"Step 02.1: Select the Order Number INTEGER field and select CALCULATE and verify menu list")
        """ALPHA"""
        menu=['Clear', 'Clear All', 'Count', 'Distinct']
        active_misobj.verify_menu_items('ITableData0', 1, 'Calculate', menu,"Step 02.2: Select the ALPHA Store Code field and select CALCULATE and verify menu list")
        """DATE"""
        menu=['Clear', 'Clear All', 'Min', 'Max', 'Count', 'Distinct']
        active_misobj.verify_menu_items('ITableData0', 2, 'Calculate', menu,"Step 02.3: Select the DATE YYMD field and select CALCULATE and verify menu list")
        """D10.2"""
        menu=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        active_misobj.verify_menu_items('ITableData0', 5, 'Calculate', menu,"Step 02.4: Select the D10.2 Unit Price field and select CALCULATE and verify menu list")
        """P9.2M"""
        menu=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        active_misobj.verify_menu_items('ITableData0', 6, 'Calculate', menu,"Step 02.5: Select the P9.2M Unit Price field and select CALCULATE and verify menu list")
        """DATETIME"""
        menu=['Clear', 'Clear All', 'Min', 'Max', 'Count', 'Distinct']
        active_misobj.verify_menu_items('ITableData0', 7, 'Calculate', menu,"Step 02.6: Select the DATETIME HYYMDSA field and select CALCULATE and verify menu list")
       
        """select Order Number INTEGER, then DISTINCT 
        Expect to see Total Cnt Dst 1,000
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 1, "Total Cnt Dist 1,000",True, "Step 02.7: Verify Total Cnt Dist 1,000 displayed on pagination bar")
        """select ALPHA Store Code, then DISTINCT
        Expect to see Total Cnt Dst 12"""
        active_misobj.select_menu_items('ITableData0', 1, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 2, "Total Cnt Dist 12",True, "Step 02.8: Verify Total Cnt Dist 12 displayed on pagination bar")
        """select DATE YYMD, then DISTINCT
        Expect to see Total Cnt Dist 6"""
        active_misobj.select_menu_items('ITableData0', 2, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 3, "Total Cnt Dist 6",True, "Step 02.9: Verify Total Cnt Dist 6 displayed on pagination bar")
        """select D10.2 Unit Price, then DISTINCT
        Expect to see Total Cnt Dst 10"""
        active_misobj.select_menu_items('ITableData0', 5, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 6, "Total Cnt Dist 10",True, "Step 02.10: Verify Total Cnt Dist 10 displayed on pagination bar")
        """select P9.2M Unit Price, then DISTINCT
        Expect to see Total Cnt Dst 677"""
        active_misobj.select_menu_items('ITableData0', 6, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 7, "Total Cnt Dist 677",True, "Step 02.11: Verify Total Cnt Dist 677 displayed on pagination bar")
        """select DATETIME, then DISTINCT
        Expect to see Total Cnt Dst 4"""
        active_misobj.select_menu_items('ITableData0', 7, 'Calculate','Distinct')
        active_misobj.verify_calculated_value(4, 8, "Total Cnt Dist 4",True, "Step 02.12: Verify Total Cnt Dist 4 displayed on pagination bar")
        
                
        """
        Step 03: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        Expect full report to be displayed again.1000 rows
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','Clear All')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03: Verify Page summary 1000of1000records')
    

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
