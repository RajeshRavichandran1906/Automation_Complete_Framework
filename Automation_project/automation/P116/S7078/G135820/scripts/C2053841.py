'''
Created on Aug 30, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053841
'''
import unittest, time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment
from common.lib import utillity

class C2053841_TestClass(BaseTestCase):

    def test_C2053841(self):
        driver = self.driver 
#         driver.implicitly_wait(15) 
        expected_function_list=['Sum', 'Avg', 'Min', 'Max', 'Count', 'Distinct']
        actual_function_list=[]
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        """
        Step 01: Execute the attached repro - AR_RP_CALCULATE.fex
        Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list, select Pivot(Cross Tab), 
        move to Group by(SUM) and select ALPHA Store Code, move to Across and select Date YYMD for the Across.

        Expect to see the Pivot Table from C1729 1st step.
        """
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')      
        active_misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01: Verify Page summary 1000of1000 records.')
        active_misobj.select_menu_items('ITableData0', 6, 'Pivot (Cross Tab)','ALPHA Store Code','Date YYMD')
        utillobj.verify_pivot_data_set('piv1','C2053841_Ds01.xlsx',"Step 01: Verify data set to see the Pivot Table from C1729 1st step")
        """
        Step 02: Click the first icon in the options bar and select New.
        Expect to see a copy of the first Pivot Table open. Drag and move the new Pivot Table to one side so both are visible.
        """
        time.sleep(5)
        pivobj.create_new_item('wall1', 0, 'New')
        active_misobj.move_active_popup("2", "600", "200")
        active_misobj.verify_popup_appears('wall1', 'P9.2M Unit Price by Date YYMD, ALPHA Store Code', 'Step 02: Verify first pivot table opened.')
        active_misobj.verify_popup_appears('wall2', 'P9.2M Unit Price by Date YYMD, ALPHA Store Code', 'Step 02: Verify Second pivot table opened.')
        """
        Step 03: Select the third icon on the options bar and change Sum to Avg for the new Pivot Table.
        Expect to see the new Pivot Table reflect Averages. The first Pivot Table of Sums should still be accessible.
        """
        pivobj.select_aggregate_function('wall2', 0, 'Avg')
        utillobj.verify_pivot_data_set('piv2','C2053841_Ds02.xlsx',"Step 03: Verify data set to see the second Pivot Table data for Avg.")
        pivobj.click_pivot_menu_bar_items('wall1', 2)
        x=self.driver.find_elements_by_css_selector("#dt0_SUM_1_x__0 span[id ^='set']")
        for i in range(len(x)):
            lineObjbj = re.match(r'(\S.*)?.*', x[i].text)
            actual_function_list.append(lineObjbj.group(1))
        utillity.UtillityMethods.asequal(self, expected_function_list, actual_function_list, "Step 03: Verify all the function list, to make sure first Pivot Table of Sums is accessible.")
        """
        Step 04: Reverse the Group By and Across sorts by clicking the down arrow in the Date YYMD box and then clicking the up arrow in the ALPHA Store Code area.
        Expect to see the Group By sort exchange places with the Across sort. There should now be two versions of the Pivot table, with their X and Y axis reversed.
        """
        pivobj.click_groupby_across_button('piv1', 2, 1, 1)
        time.sleep(1)
        pivobj.click_groupby_across_button('piv1', 1, 1, 1)
        utillobj.verify_pivot_data_set('piv1','C2053841_Ds03.xlsx',"Step 04: Verify data set to see the first Pivot Table data for after reversing By and Across.")

if __name__ == '__main__':
    unittest.main()
