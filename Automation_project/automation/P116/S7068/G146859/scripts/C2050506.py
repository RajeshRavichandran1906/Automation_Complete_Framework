'''
Created on July25, 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050506

Test Description: Verify that Avg option shows average for that particular column.Original test AR-RP-165.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050506_TestClass(BaseTestCase):

    def test_C2050506(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(20) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050506'
        
        """Step 01: Use the specified Pre-Condition Focexec to test the MIN option of CALCULATE. """
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Report should contain columns representing mixed format output data.'
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', step01)
        
        
        """Step 02: Execute AR-RP-141CA to produce the mixed field output report.

        For each field, including Order Number INTEGER, DATE YYMD, D10.2 Unit Price, P9.2M Unit Price and DATETIME HYYMDSA. Click the down arrow in the heading, then select CALCULATE. Then select MIN from the drop down options.
        MIN is not available for alphanumeric fields.
        
        select INTEGER, then MIN
        select DATE, then MIN
        select D10.2, then MIN
        select P9.2M, then MIN
        select DATETIME, then MIN    
        """
        
        #Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0',0,'Calculate',option,'Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.')
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate", "Min")
        time.sleep(4)
        #Expect to see Total Min 1
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        ''' Performing select DATE YYMD, then Min'''
        #select DATE YYMD, then Min
        miscelanousobj.select_menu_items("ITableData0", 2, "Calculate", "Min")
        time.sleep(4)
        #Expect to see Total Min 1996/01/01
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see Total Min 1996/01/01") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1"+"After Adding second MIn") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        ''' Performing select D10.2, then Min'''
        #select D10.2, then Min
        miscelanousobj.select_menu_items("ITableData0", 5, "Calculate", "Min")
        time.sleep(4)
        #Expect to see Total Min 13.00
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1"+"After Adding third Avg")
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see Total Min 1996/01/01"+"After adding third min") 
         
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select P9.2M Unit Price, then Min, 
        
        ''' Performing filter and calculate> Min action for column P9.2M Unit Price'''
        #Select P9.2M Unit Price, then SUM
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Min")
        time.sleep(4)
        
        #Expect to see Total Min $24.00

        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", True, "Step 02: Expect to see Total Min $24.00") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see Total Min 1996/01/01"+"After Adding fourth min") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1."+"After Adding fourth Min") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00"+"After adding fourth min") 
        
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select select DATETIME, then MIN 
        
        ''' Performing filter and calculate> Min action for column DATETIME'''
        
        miscelanousobj.select_menu_items("ITableData0", 7, "Calculate", "Min")
        time.sleep(4)
        
        #Expect to see Total Min 2002/12/31 11:59:59PM

        miscelanousobj.verify_calculated_value(4, 8, "Total Min 2002/12/31 11:59:59PM", True, "Step 02: Expect to see Total Min 2002/12/31 11:59:59PM") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see Total Min 1996/01/01"+"After Adding fifth min") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1."+"After Adding fifth Min") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00"+"After adding fifth min") 
        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", True, "Step 02: Expect to see Total Min $24.00"+"After adding fifth min")
        
        time.sleep(3)#conditional sleep for verification to finish and close the window

        
        """Step 03: End the Filter panel in preparation for the next field in the GROUP.Make sure the report is positioned at Page 1."""
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Clear All")
        
        #Expect full report to be displayed again.1000 rows
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', "Step 03: Expect full report to be displayed again.1000 rows")
        
        miscelanousobj.verify_calculated_value(4, 7, "Total Min 2002/12/31 11:59:59PM", False, "Step 02: Expect to see Total Min 2002/12/31 11:59:59PM"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", False, "Step 02: Expect to see Total Min 1996/01/01"+"After clear all  min"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", False, "Step 02: Expect to see Total Min 1."+"Afterclear all Min"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", False, "Step 02: Expect to see Total Min 13.00"+"After clear all min"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", False, "Step 02: Expect to see Total Min $24.00"+"After clear all min"+"Not Present Verification")
        
         
        
        
if __name__ == '__main__':
    unittest.main()