'''
Created on July25, 2016
@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050503

Test Description: Verify that the Sum option of Calculate shows adjusted Total Sum for that particular column. The Total Sum will reflect any Filters applied and show the original Total along with a percentage for the Filtered results.
Original test AR-RP-164.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050503_TestClass(BaseTestCase):

    def test_C2050503(self):
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050503'
        
        """Step 01: For each field specified, select CALCULATE, then select the requested calculation type. """
        
        utillobj = utillity.UtillityMethods(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login('AR-RP-141CA.fex','S7068','mrid','mrpass')
        time.sleep(10)  
        
        step01 = 'Step 01 : Report should contain columns representing mixed format output data.'
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', step01)
        
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-141CA_page1.xlsx',step01)
        
        #utillobj.create_data_set('ITableData0','I0r','AR-RP-141CA_page1.xlsx')
        
        """Execute AR-RP-141CA to produce the mixed field output report.
        For each field, including Order Number INTEGER, D10.2 Unit Price and P9.2M Unit Price, click the down arrow in the heading, 
        then select CALCULATE. Then select SUM from the drop down options, then select FILTER.
        Use the values below to Filter the Total value.
        Select Order Number INTEGER, then SUM, then FILTER, then LESS THAN, then select value of 50.
        Exit the Filter for Order Number INTEGER.
        Select D10.2 Unit Price, then SUM, then FILTER, then EQUALS, then select value of 140.00.
        Exit the Filter for D10.2 Unit Price.
        Select P9.2M Unit Price, then SUM, then FILTER, then NOT EQUAL, then select value $100.00
        Exit the Filter for P9.2M Unit Price."""
        
        #Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        option=['Clear', 'Clear All', 'Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct', '% of Total']
        miscelanousobj.verify_menu_items('ITableData0',0,'Calculate',option,'Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.')
        
        miscelanousobj.select_menu_items("ITableData0", 0, "Calculate", "Sum")
        time.sleep(4)
        
        #Select Order Number INTEGER, then SUM, then FILTER, then LESS THAN, then select value of 50.
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", True, "Step 02: Expect total sum 500500.") 
        
        #Select Order Number INTEGER, then SUM, then FILTER, then LESS THAN, then select value of 50.
        
        miscelanousobj.select_menu_items("ITableData0", "0", "Filter", "Less than")
        
        filterselectionobj.create_filter(1, 'Less than','large', value1='50')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Filtered Sum 1,225(0.24%)
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Sum 1225(0.24%)\nTotal Sum 500500", True, "Step 02: Filtered Sum 1,225(0.24%)Total Sum 500,500")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        ''' Performing filter and calculate> sum action for column D10.2 Unit Price'''
        #Select D10.2 Unit Price, then SUM
        miscelanousobj.select_menu_items("ITableData0", 5, "Calculate", "Sum")
        time.sleep(4)
        #Expect to see Total Sum 59,503
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 59,503.00", True, "Step 02: Expect to see Total Sum 59,503") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", True, "Step 02: Expect total sum 500,500."+"After Adding second Sum") 
        #Select D10.2 Unit Price, then SUM, then FILTER, then EQUALS, then select value of 140.00.
        
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter", "Equals")
        
        filterselectionobj.create_filter(1, 'Equals', value1='140.00')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Filtered Sum 9,380.00(15.76%)
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Sum 9,380.00(15.76%)\nTotal Sum 59,503.00", True, "Step 02: Filtered Sum 9,380.00(15.76%)")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        #Select P9.2M Unit Price, then SUM, then FILTER, then NOT EQUAL, then select value $100.00
        
        ''' Performing filter and calculate> sum action for column P9.2M Unit Price'''
        #Select P9.2M Unit Price, then SUM
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Sum")
        time.sleep(4)
        
        #Expect to see Total Sum $560,003.00, then Filtered Sum $559,903.00(99.98%)

        miscelanousobj.verify_calculated_value(4, 7, "Total Sum $560,003.00", True, "Step 02: Expect to see Total Sum $560,003.00") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 59,503.00", True, "Step 02: Expect to see Total Sum 59,503"+"After Adding third Sum") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", True, "Step 02: Expect total sum 500,500."+"After Adding third Sum") 
        
        #Select P9.2M Unit Price, then SUM, then FILTER, then NOT EQUAL, then select value $100.00
        
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter", "Not equal")
        
        filterselectionobj.create_filter(1, 'Not equal', 'large', value1='$100.00')
        time.sleep(4)
        filterselectionobj.filter_button_click('Filter')
        time.sleep(4)
        
        #Expect to see Filtered Sum $559,903.00(99.98%)
        miscelanousobj.verify_calculated_value(4, 7, "Filtered Sum $559,903.00(99.98%)\nTotal Sum $560,003.00", True, "Step 02: Expect to see Filtered Sum $559,903.00(99.98%)")
        
        time.sleep(5)#conditional sleep for verification to finish and close the window
        filterselectionobj.close_filter_dialog()
        
        time.sleep(3)#conditional sleep for verification to finish and close the window
        
        
        """Step 03: End the Filter panel in preparation for the next field in the GROUP.Make sure the report is positioned at Page 1."""
        miscelanousobj.select_menu_items("ITableData0", 6, "Calculate", "Clear All")
        time.sleep(4)
        
        miscelanousobj.verify_calculated_value(4, 7, "Total Sum $560,003.00", False, "Step 02: Expect to see Total Sum $560,003.00"+"Not Present verification") 
        miscelanousobj.verify_calculated_value(4, 6, "Total Sum 59,503.00", False, "Step 02: Expect to see Total Sum 59,503"+"Not Present verification") 
        miscelanousobj.verify_calculated_value(4, 1, "Total Sum 500500", False, "Step 02: Expect total sum 500,500."+"Not Present verification") 
        
        
        #Expect full report to be displayed again.1000 rows
        
        miscelanousobj.verify_page_summary('0','1000of1000records,Page1of18', "Step 03: Expect full report to be displayed again.1000 rows")
        
        
        

        
        
if __name__ == '__main__':
    unittest.main()