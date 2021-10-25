'''
Created on Jul 28, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050522
Description : Generate Pivot Table using the manual method. This uses selections from the drop down options menu.
Original test AR-RP-183.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages import active_pivot_comment  
from common.lib import utillity
import unittest
import time
import re

class C2050522_TestClass(BaseTestCase):

    def test_C2050522(self):
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2050522'
        
        """
            Step 01:Execute AR-RP-193 for the report to drive Pivot.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        pivotobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(10)
       
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-193.fex - Top Head line verification")
        
       
         
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-193_page1.xlsx',"Step 01: Verify Page 1 data loaded correctly ")
        
        #utillobj.create_data_set('ITableData0','I0r','AR-RP-193_page1.xlsx')
         
 
        """Step 02 : Select Order Number INTEGER,
        select PIVOT(Cross Tab), then for Group By(SUM), select ALPHA Store Code and lastly, for ACROSS,select Date YYMD. """
       
        miscelanousobj.select_menu_items("ITableData0", 0, "Pivot (Cross Tab)", "ALPHA Store Code", "Date YYMD" )
        
        time.sleep(5)
        
        """Expect to see a Grid(Matrix) Report with Order Number INTEGER summed By ALPHA Store Code, ACROSS Date YYMD. 
        There should be 12 rows down and six columns across. 
        Row and Column Totals are standard and the grand total should be 500,500.
        Any cells that contain dots(...) indicate that there is no data for that row and column combination. """
        
        #pivot table verification 
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds01.xlsx', 'Step 02: Pivot table verification')
        
        
        """Step 03 : Select the third option from the tool bar and change the value from SUM to AVG. """
        
        pivotobj.select_aggregate_function('wall1', 0, 'Avg')
        
        time.sleep(3)
        
        #The same grid will appear but the numbers should change from Totals to Averages.
        
        
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds02.xlsx', 'Step 03: The same grid will appear but the numbers should change from Totals to Averages. ')
        
        """Step 04 : Select the third option from the tool bar and change the value from AVG to MIN."""
        
        pivotobj.select_aggregate_function('wall1', 1, 'Min')
        
        time.sleep(3)
        #The same grid will appear but the numbers should change from Averages to Minimums.
         
         
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds03.xlsx','Step 06: The same grid will appear but the numbers should change from Averages to Minimums.' )
        
        """Step 05: Select the third option from the tool bar and change the value from MIN to MAX."""
        
        pivotobj.select_aggregate_function('wall1', 1, 'Max')
        
        time.sleep(3)
        #The same grid will appear but the numbers should change from Minimums to Maximums.
         
         
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds04.xlsx' , 'Step 05:The same grid will appear but the numbers should change from Minimums to Maximums.')
        
        
        """Step 06: Select the third option from the tool bar and change the value from MAX to COUNT."""
        
        pivotobj.select_aggregate_function('wall1', 1, 'Count')
        
        time.sleep(3)
        #The same grid will appear but the numbers should change from Maximums to Counts.
         
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds05.xlsx','Step 06: The same grid will appear but the numbers should change from Maximums to Counts.' )
        
        #utillobj.create_pivot_data_set('piv1', 'C2050522_Ds05.xlsx')
       
        """Step 07: Select the third option from the tool bar and change the value from COUNT to DISTINCT.
        Click the SUM option for the next step. """
        pivotobj.select_aggregate_function('wall1', 1, 'Distinct')
        
        time.sleep(3)
        
        
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds05.xlsx','Step 07: The same grid will appear but the numbers should change from Counts to Distinct Counts. Results should be same as Count' )
        #The same grid will appear but the numbers should change from Counts to Distinct Counts. Results should be same as Count.
        #The Pivot Table should be back to the SUM mode for the next test.
        
        #Click the SUM option for the next step
        
        pivotobj.select_aggregate_function('wall1', 1, 'Sum')
        
        time.sleep(3)
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds01.xlsx', 'Step 02: The Pivot Table should be back to the SUM mode for the next test.')
        
        
        """Step 08: Reverse the axis by clicking the downward arrow in the Date YYMD options box.
         Then click the upward arrow in the ALPHA Store Code box."""
        
        pivotobj.click_groupby_across_button('piv1', 1, 2, 1)
        time.sleep(3)
        pivotobj.click_groupby_across_button('piv1', 1, 2, 1)
        time.sleep(3)
    
        
        #arrow in the ALPHA Store Code box.
        #Expect to see the same values but now with 6 rows for the By field Date YYMD and 12 columns for the Across field ALPHA Store Code
        
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds06.xlsx', 'Step 08: Expect to see the same values but now with 6 rows for the By field Date YYMD and 12 columns for the Across field ALPHA Store Code ')
        
        """Step 09 : Add another By sort row by clicking on the first option in the tool bar, selecting Group By(X) and selecting D10.2 Unit Price."""
        
        pivotobj.create_new_item('wall1', 1, 'Group By (X)->D10.2 Unit Price')
        
        time.sleep(4)
                               
        #Expect to see a second By column appear to the right of ALPHA Store Code.
        #The summed values for each Store Code are now broken out to the D10.2 Unit Price level.
        
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds07.xlsx', 'Step 09: The summed values for each Store Code are now broken out to the D10.2 Unit Price level. ')
        """Step 10: Reverse the ALPHA Store Code and D10.2
        Unit Price sort columns by clicking the right pointing arrow in the ALPHA Store Code box or the left pointing arrow in the D10.2 Unit Price box."""
        
        pivotobj.click_groupby_across_button('piv1', 2, 1, 3)
        time.sleep(3)
        
        #Expect to see the first two columns reverse their positions, with D10.2 Unit Price the major sort and ALPHA Store Code the minor sort.
        utillobj.verify_pivot_data_set('piv1', 'C2050522_Ds08.xlsx', 'Step 10:Expect to see the first two columns reverse their positions, with D10.2 Unit Price the major sort and ALPHA Store Code the minor sort.')
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        