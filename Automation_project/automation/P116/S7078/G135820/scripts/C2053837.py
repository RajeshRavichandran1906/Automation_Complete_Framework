'''
Created on Aug 31, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053837
'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_tools
from common.lib import utillity


class C2053837_TestClass(BaseTestCase):

    def test_C2053837(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053837'
        """
        Step 01: Execute the AR_RP_CALCULATE.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
#         utillobj.create_data_set('ITableData0','I0r','AR_RP_CALCULATE_Page1a.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','AR_RP_CALCULATE_Page1a.xlsx',"Step 01.2: Verify AR_RP_CALCULATE Page1 datset")
        misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)', 'ALPHA Store Code','Date YYMD')
        
        """
        Expect to see a Grid(Matrix) Report with Order Number INTEGER summed By ALPHA Store Code, ACROSS Date YYMD.
        There should be 12 rows down and six columns across. Row and Column Totals are standard and the grand total should be 500,500.
        Any cells that contain dots indicate that there is no data for that row and column combination. Link is below.
        """
                
        pivobj.veryfy_pivot_table_title('piv1', 'OrderNumberINTEGERbyDateYYMD,ALPHAStoreCode', 'Step 01.3: Verify pivot Title')
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds01.xlsx','Step 01.4: Verify Pivot dataset')
        pivobj.verify_pivot_menu('wall1', 'Step 01.5: Verify pivot toolbar menus')          
        
        """
        Step 02: Select the third option from the tool bar and change the value from SUM to AVG.
        The same grid will appear but the numbers should change from totals to Averages.
        """
        pivobj.select_aggregate_function('wall1', 0, 'Avg',True)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds02.xlsx','Step 02.1: Verify Pivot dataset for the Avg')
         
        """
        Step 03: Select the third option from the tool bar and change the value from AVG to MIN.
        The same grid will appear but the numbers should change from Averages to Minimums.
        """
        pivobj.select_aggregate_function('wall1', 1, 'Min',True)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds03.xlsx','Step 03.1: Verify Pivot dataset for the Min')
        
        """
        Step 04: Select the third option from the tool bar and change the value from MIN to MAX.
        The same grid will appear but the numbers should change from Minimums to Maximums.
        """
        pivobj.select_aggregate_function('wall1', 1, 'Max',True)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds04.xlsx','Step 04.1: Verify Pivot dataset for the Max')
        
        """
        Step 05: Select the third option from the tool bar and change the value from MAX to COUNT.
        The same grid will appear but the numbers should change from Maximums to Counts.
        """
        pivobj.select_aggregate_function('wall1', 1, 'Count',True)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds05.xlsx','Step 05.1: Verify Pivot dataset for the Count')
        
        """
        Step 06: Select the third option from the tool bar and change the value from COUNT to DISTINCT. 
        Click the SUM option for the next step.
        The same grid will appear but the numbers should change from Counts to Distinct Counts. 
        Results should be same as Count. The Pivot Table should be back to the SUM mde for the next test.
        """
        pivobj.select_aggregate_function('wall1', 1, 'Distinct',True)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds06.xlsx','Step 06.1: Verify Pivot dataset for the Distinct')
        pivobj.select_aggregate_function('wall1', 1, 'Sum',True)
        
        """
        Step 07: Reverse the axis by clicking the downward arrow in the Date YYMD options box.
        Then click the upward arrow in the ALPHA Store Code box.
        Expect to see the same values but now with 6 rows for the By field Date YYMD and 12 columns for the Across field ALPHA Store Code.
        """
        pivobj.click_groupby_across_button('piv1', 1, 2, 1)
        pivobj.click_groupby_across_button('piv1', 1, 2, 1)
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds07.xlsx','Step 07.1: Verify Pivot dataset, 6 rows for the By field Date YYMD and 12 columns for the Across field ALPHA Store Code')
        
        """
        Step 08: Add another By sort row by clicking on the first option in the tool bar, selecting Group By(X) and selecting D10.2 Unit Price.
        Expect to see a second By column appear to the right of ALPHA Store Code. 
        The summed values for each Store Code are now broken out to the D10.2 Unit Price level.
        """
        pivobj.create_new_item('wall1', 1, 'Group By (X)->D10.2 Unit Price')
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds08.xlsx','Step 08.1: Verify Pivot dataset Store Code are now broken out to the D10.2 Unit Price level')
        
        """
        Step 09: Reverse the ALPHA Store Code and D10.2 Unit Price sort columns by clicking the right pointing arrow 
        in the ALPHA Store Code box or the left pointing arrow in the D10.2 Unit Price box.
        Expect to see the first two columns reverse their postions, with D10.2 Unit Price the major sort 
        and ALPHA Store Code the minor sort.
        """
        pivobj.click_groupby_across_button('piv1', 2, 1, 3)
        #utillobj.create_pivot_data_set('piv1', 'C2053837_Ds09.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2053837_Ds09.xlsx','Step 09.1: Verify Pivot dataset after interchanging columns')
        


if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
