'''
Created on July25, 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050505

Test Description: Verify that the Avg option of Calculate shows adjusted Average for that particular column. The Average will reflect any Filters applied and show the original Average along with a percentage for the Filtered results.
Original test AR-RP-166.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050505_TestClass(BaseTestCase):

    def test_C2050505(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050505'
        
        """Step 01: Use the specified Pre-Condition Focexec to test the AVG option of CALCULATE along with Filter(s) specified.
            AVG is available only for numeric field types. """
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Report should contain columns representing mixed format output data.'
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', step01)
        
        
        """Execute AR-RP-141CA to produce the mixed field output report.
        
        For each field, including INTEGER, D10.2 and P9.2M, click the down arrow in the heading, then select CALCULATE. Then select AVG from the drop down options, then select FILTER.
        Use the values below to Filter the Total value.
        
        Select Order Number INTEGER, then AVG, then FILTER, then LESS THAN, then select value of 50. Click Filter.
        
        Select D10.2 Unit Price, then AVG, then FILTER, then LESS THAN, then select value of 140.00. Click Filter.
        Remove the Order Number INTEGER field by clicking the 'X'
        
        Select P9.2M Unit Price, then AVG, then FILTER, then BETWEEN, then select from value $25.00 and to value $100.00. Click Filter."""
        
        #Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0',0,'Calculate',option,'Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.')
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate", "Avg")
        time.sleep(4)
        #Select Order Number INTEGER, then SUM, then FILTER, then LESS THAN, then select value of 50.
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect total Avg 500 .") 
        
        #Select Order Number INTEGER, then SUM, then FILTER, then LESS THAN, then select value of 50.
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter", "Less than")
        
        filterselectionobj.create_filter(1, 'Less than','large', value1='50')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Filtered Avg 25(5%)
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Avg 25(5%)\nTotal Avg 500", True, "Step 02: Filtered Avg 25(5%)Total Avg 500")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        ''' Performing filter and calculate> sum action for column D10.2 Unit Price'''
        #Select D10.2 Unit Price, then Avg
        miscelanousobj.select_menu_items("ITableData0", 5, "Calculate", "Avg")
        time.sleep(4)
        #Expect to see Total Avg 59.50,
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", True, "Step 02: Expect to see Total Avg 59.50") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect total Avg 500 ."+"After adding second avg verification")
        
        #Select D10.2 Unit Price, then AVG, then FILTER, then LESS THAN, then select value of 140.00. Click Filter. 
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Less than")
        
        filterselectionobj.create_filter(1, 'Less than', value1='140.00')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Filtered Avg 53.72(90.29%)
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Avg 53.72(90.29%)\nTotal Avg 59.50", True, "Step 02: Filtered Avg 53.72(90.29%)")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select P9.2M Unit Price, then SUM, then FILTER, then NOT EQUAL, then select value $100.00
        
        ''' Performing filter and calculate> Avg action for column P9.2M Unit Price'''
        #Select P9.2M Unit Price, then Avg
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Avg")
        time.sleep(4)
        
        #Expect to see Total Avg $560.00, andFiltered Avg $67.42(12.04%)

        miscelanousobj.verify_calculated_value(4, 7, "Total Avg $560.00", True, "Step 02: Expect to see Total Avg $560.00") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", True, "Step 02: Expect to see Total Avg 59.50"+"After adding third avg verification") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", True, "Step 02: Expect total Avg 500 ."+"After adding third avg verification")
        
        #Select P9.2M Unit Price, then AVG, then FILTER, then BETWEEN, then select from value $25.00 and to value $100.00. Click Filter
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Between")
        
        filterselectionobj.create_filter(1, 'Between', 'large', value1='$25.00', value2='$100.00')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Total Avg $560.00, andFiltered Avg $67.42(12.04%)
        miscelanousobj.verify_calculated_value(4, 7, "Filtered Avg $67.42(12.04%)\nTotal Avg $560.00", True, "Step 02: Expect to see Filtered Avg Avg $67.42(12.04%)")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        """Step 03: End the Filter panel in preparation for the next field in the GROUP.Make sure the report is positioned at Page 1."""
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Clear All")
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 7, "Total Avg $560.00", False, "Step 02: Expect to see Total Avg $560.00"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Avg 59.50", False, "Step 02: Expect to see Total Avg 59.50"+"Not Present Verification") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Avg 500", False, "Step 02: Expect total Avg 500 ."+"Not Present Verification")
        
        #Expect full report to be displayed again.1000 rows
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', "Step 03: Expect full report to be displayed again.1000 rows")
        
        
        

        
        
if __name__ == '__main__':
    unittest.main()