'''
Created on July25, 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050504

Test Description: Verify that Avg option shows average for that particular column.Original test AR-RP-165.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050504_TestClass(BaseTestCase):

    def test_C2050504(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050504'
        
        """Step 01: Use the specified Pre-Condition Focexec to test the AVG option of CALCULATE.AVG is available only for numeric field types. """
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Report should contain columns representing mixed format output data.'
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', step01)
        
        
        """Execute AR-RP-141CA to produce the mixed field output report.
        For each field, including INTEGER, D10.2 and P9.2M, click the down arrow in the heading, then select CALCULATE. 
        Then select AVG from the drop down options.
        select INTEGER, then AVG
        select D10.2, then AVG
        select P9.2M, then AVG
        
        """
        
        #Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0',0,'Calculate',option,'Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.')
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate", "Avg")
        time.sleep(4)
        #Expect to see Total Avg 500
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect to see Total Avg 500.") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        ''' Performing select D10.2, then AVG'''
        #select D10.2, then AVG
        miscelanousobj.select_menu_items("ITableData0", 5, "Calculate", "Avg")
        time.sleep(4)
        #Expect to see Total Avg 59.50
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", True, "Step 02: Expect to see Total Avg 59.50") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect to see Total Avg 500."+"After Adding second Avg") 
       
        
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select P9.2M Unit Price, then Avg, 
        
        ''' Performing filter and calculate> Avg action for column P9.2M Unit Price'''
        #Select P9.2M Unit Price, then Avg
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Avg")
        time.sleep(4)
        
        #Expect to see Total Avg $560.00

        miscelanousobj.verify_calculated_value(4, 7, "Total Avg $560.00", True, "Step 02: Expect to see Total Avg $560.00") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", True, "Step 02: Expect to see Total Avg 59.50"+"After Adding third avg") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect to see Total Avg 500."+"After Adding third Avg") 
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        """Step 03: End the Filter panel in preparation for the next field in the GROUP.Make sure the report is positioned at Page 1."""
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Clear All")
        
        #Expect full report to be displayed again.1000 rows
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', "Step 03: Expect full report to be displayed again.1000 rows")
        
        miscelanousobj.verify_calculated_value(4, 7, "Total Avg $560.00", False, "Step 03: Expect to see Total Avg $560.00"+"Not Present verification")
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", False, "Step 03: Expect to see Total Avg 59.50"+"Not Present verification")
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", False, "Step 03: Expect to see Total Avg 500."+"Not Present verification") 
        
        
if __name__ == '__main__':
    unittest.main()