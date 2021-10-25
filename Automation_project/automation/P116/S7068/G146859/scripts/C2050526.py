'''
Created on Jul 28, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050526
Test case Name = Verify Pivot Table can spawn another Pivot Table.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,active_pivot_comment
from common.lib import utillity
import unittest,time
from selenium.webdriver import ActionChains

class C2050526_TestClass(BaseTestCase):

    def test_C2050526(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050526'
        """
        Step 01: Execute AR-RP-193 for the report to drive Pivot.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_pivot = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute AR-RP-193.fex verify Page Summary 1000of1000")
        
        """
        Step 02: Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list, 
        select Pivot(Cross Tab), move to Group BY(SUM) and select ALPHA Store Code, move to Across and 
        select Date YYMD for the Across.        
        """  
        active_misobj.select_menu_items('ITableData0', 5, 'Pivot (Cross Tab)','ALPHA Store Code','Date YYMD')
        
        """Expect to see a Pivot Table with summed values of P9.2M Unit Price sorted by ALPHA Store Code Across Date YYMD."""
        utillobj.verify_pivot_data_set('piv1', "C2050526_Ds01.xlsx", "Step 02: Verify data set of Unit Price column(last)")
     
        """        
        Step 03: Click the first icon in the options bar and select New.
        """
        active_pivot.create_new_item('wall1', 0, 'New')     
        """Expect to see a copy of the first Pivot Table open.
        Drag and move the new Pivot Table to one side so both are visible."""
        active_misobj.move_active_popup("2", "600", "200")
        
        """
        Step 04: Select the third icon on the options bar and change Sum to Avg for the new Pivot Table.
        """
        active_pivot.select_aggregate_function('wall2', 0, 'Avg')
        """Expect to see the new Pivot Table reflect Averages. """
        utillobj.verify_pivot_data_set('piv2', "C2050526_Ds02.xlsx", "Step 04.1: Verify data set, new Pivot Table reflect Averages")
        """The first Pivot Table of Sums should still be accessible."""
        utillobj.verify_pivot_data_set('piv1', "C2050526_Ds01.xlsx", "Step 04.2: Verify data set of Sums should still be accessible.")
     
        """Reverse the Group By and Across sorts by clicking the down arrow in the Date YYMD box and 
        then clicking the up arrow in the ALPHA Store Code area."""
        active_pivot.click_groupby_across_button('piv2', 1, 2, 1)
        active_pivot.click_groupby_across_button('piv2', 1, 2, 1)
        """Expect to see the Group By sort exchange places with the Across sort.
        There should now be two versions of the Pivot table, with their X and Y axis reversed."""
        utillobj.verify_pivot_data_set('piv2', "C2050526_Ds03.xlsx", "Step 04.2: Verify data set with their X and Y axis reversed.")
        
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        