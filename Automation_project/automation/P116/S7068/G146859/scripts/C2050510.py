'''
Created on July25, 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050510

Test Description: Verify that Avg option shows average for that particular column.Original test AR-RP-165.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050510_TestClass(BaseTestCase):

    def test_C2050510(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050510'
        
        """Step 01: Use the specified Pre-Condition Focexec to test the MIN option of CALCULATE. """
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Report should contain columns representing mixed format output data.'
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', step01)
        
        
        """Execute AR-RP-141CA to produce the mixed field output report.

        For each field, including INTEGER, DATE, D10.2, P9.2M and DATETIME click the down arrow in the heading, then select CALCULATE. 
        Then select COUNT from the drop down options.
        
        select INTEGER, then COUNT
        select ALPHA, then COUNT
        select DATE, then COUNT
        select D10.2, then COUNT
        select P9.2M, then COUNT
        select DATETIME, then COUNT
        """
        
        #Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0',0,'Calculate',option,'Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.')
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate", "Count")
        time.sleep(4)
        #Expect to see Total Cnt 1,000
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        ''' Performing select ALPHA Store Code then Count'''
        #select DATE YYMD, then Count
        miscelanousobj.select_menu_items("ITableData0", 1, "Calculate", "Count")
        time.sleep(4)
        #Expect to see Total Cnt 1,000
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding second count") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        ''' Performing select DATE YYMD, then Count'''
        #select DATE YYMD, then Min
        miscelanousobj.select_menu_items("ITableData0", 2, "Calculate", "Count")
        time.sleep(4)
        #Expect to see Total Cnt 1,000
        miscelanousobj.verify_calculated_value(4, 3, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding third count") 
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding third count")
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        ''' Performing select D10.2, then Count'''
        #select D10.2, then Count
        miscelanousobj.select_menu_items("ITableData0", 5, "Calculate", "Count")
        time.sleep(4)
        #Expect to see Total Cnt 1,000
        miscelanousobj.verify_calculated_value(4, 6, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding fourth count")
        miscelanousobj.verify_calculated_value(4, 3, "Total Cnt 1,000", True, "Step 02: Expect to see Total Total Cnt 1,000"+"After adding fourth count") 
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding fourth count") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select P9.2M Unit Price, then Count, 
        
        ''' Performing filter and calculate> Count action for column P9.2M Unit Price'''
        #Select P9.2M Unit Price, then Count
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Count")
        time.sleep(4)
        
        #Expect to see Total Cnt 1,000
        miscelanousobj.verify_calculated_value(4, 7, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding fifth count") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding fifth count") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After adding fifth count") 
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding fifth count")
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select select DATETIME, then count 
        
        ''' Performing filter and calculate> count action for column DATETIME'''
        miscelanousobj.select_menu_items("ITableData0", 7, "Calculate", "Count")
        time.sleep(4)
        
        #Expect to see Total Cnt 1,000

        miscelanousobj.verify_calculated_value(4, 8, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding sixth count") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding sixth count") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After adding sixth count") 
        miscelanousobj.verify_calculated_value(4, 7, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After adding sixth count")
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", True, "Step 02: Expect to see Total Cnt 1,000"+"After Adding sixth count")
        
        time.sleep(3)#conditional sleep for verification to finish and close the window

        
        """Step 03: End the Filter panel in preparation for the next field in the GROUP.Make sure the report is positioned at Page 1."""
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Clear All")
        time.sleep(4)
        #Expect full report to be displayed again.1000 rows
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', "Step 03: Expect full report to be displayed again.1000 rows")
        
        miscelanousobj.verify_calculated_value(4, 7, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"After clear all"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"After clear all"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"After clear all"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 7, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"After clear all"+"Not Present Verification")
        miscelanousobj.verify_calculated_value(4, 2, "Total Cnt 1,000", False, "Step 02: Expect to see Total Cnt 1,000"+"After clear all"+"Not Present Verification")
         
        
        
if __name__ == '__main__':
    unittest.main()