'''
Created on Jul 27, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050512
TestCase Name = Verify that % of Total option of Calculate shows the % of Total for that particular column.
'''
import unittest,time
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import NoSuchElementException
# from common.lib import take_screenshot
# from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
# from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2050512_TestClass(BaseTestCase):

    def test_C2050512(self):
#         """
#             TESTCASE VARIABLES
#         """
#         Test_Case_ID = 'C2050512'
        """
            Step 01: Execute AR-RP-141CA to produce the mixed field output report.
        """
#         driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
#         active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')      
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01: Verify Page summary 1000of1000records')
        
        """
        Step 02: For each field, including Order Number INTEGER, D10.2 Unit Price and P9.2M Unit Price, 
        click the down arrow in the heading, then select CALCULATE. Then select
        % of Total from the drop down options.
        """
        menu=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        active_misobj.verify_menu_items('ITableData0', 0, 'Calculate', menu,"Step 02.1: Select the Order Number INTEGER field and select CALCULATE and verify menu list")
        
        """select INTEGER, then % of Total
        Expect to see % of Total column to right of the Order Number Integer column."""
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','% of Total')
        
        """select D10.2, then % of Total
        Expect to see % of Total column to the right of the D10.2 Unit Price column."""
        active_misobj.select_menu_items('ITableData0', 5, 'Calculate','% of Total')
        
        """select P9.2M, then % of Total
        Expect to see % of Total column to the right of the P9.2M Unit Price column."""
        active_misobj.select_menu_items('ITableData0', 6, 'Calculate','% of Total')
        
        """Verify Column Heading"""
        list=['Order Number INTEGER','% of Total','ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price','% of Total','P9.2M Unit Price','% of Total','DATETIME HYYMDSA']
        active_misobj.verify_column_heading('ITableData0', list,'Step 02.2: Verify column heading')
        
        """Expect to see the following first page, showing the three % of Total columns added."""
        utillobj.verify_data_set('ITableData0','I0r','C2050512_Ds01.xlsx', "Step 02.3: Expect to see the following first page, showing the three % of Total columns added.")
        
        """
        Step 03: End the Filter panel in preparation for the next field in the GROUP.
        Make sure the report is positioned at Page 1.
        Expect full report to be displayed again.1000 rows
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 0, 'Calculate','Clear All')      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 03: Verify Page summary 1000of1000records')
    

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
