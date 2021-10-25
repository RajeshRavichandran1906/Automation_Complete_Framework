'''
Created on Aug 30, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053833
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment, active_tools
from common.lib import utillity


class C2053833_TestClass(BaseTestCase):

    def test_C2053833(self):
        """
            TESTCASE VARIABLES
        """
        """
        Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary 107of107')
        
        """
        Step 02: Click State > Pivot Tool
        Verify this tab are displayed on tool: 
        - Columns 
        - Group By 
        - Across 
        - Measure
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Pivot Tool')  
        toolobj.pivot_tool_verify_columns('pivottoolt1', 1,['Columns','Category','Product','Product ID','State','Unit Sales','Dollar Sales'], 'Step 02.1:Verify Pivot Tool Columns')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By','Drag Column Here'], 'Step 02.2:Verify Pivot Tool Group By')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','Drag Column Here'], 'Step 02.3:Verify Pivot Tool Across')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Drag Column Here'], 'Step 02.4:Verify Pivot Tool Measure')
        
        """
        Step 03: Drag Category and State column under Group By, Product column under Across and Product ID column under Measure.
        """  
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Category', 1, 'Group By', 0)  
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Group By', 1)  
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product', 1, 'Across', 0) 
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product ID', 1, 'Measure', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By','Category','State'], 'Step 03.2:Verify Pivot Tool Group By')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','Product'], 'Step 03.3:Verify Pivot Tool Across')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Count:', 'Product ID'], 'Step 03.4:Verify Pivot Tool Measure')
        
        """
        Step 04: Click OK.
        Verify 'Product ID By Product, Category, State' pivot table is displayed. 
        Verify toolbar shows: 
        - Dropdown 
        - Freeze icon 
        - Aggregation icon 
        Verify selected columns/data are displayed
        """
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        pivobj.veryfy_pivot_table_title('piv2', 'ProductIDbyProduct,Category,State', 'Step 04.1: Verify pivot Title')
        utillobj.verify_pivot_data_set('piv2', 'C2053833_Ds01.xlsx','Step 04.2: Verify Pivot dataset')
        pivobj.verify_pivot_menu('wall2', 'Step 04.3: Verify pivot toolbar menus')  
        
        """
        Step 05: Now click down arrow for Product column (which is displayed horizontally)
        Verify options for Product will be displayed vertically instead of horizontally
        """
        pivobj.click_groupby_across_button('piv2', 1, 3, 1)
        utillobj.verify_pivot_data_set('piv2', 'C2053833_Ds02.xlsx','Step 05.1: Verify options for Product will be displayed vertically instead of horizontally')
        
        """
        Step 06: Now click upward arrow for State column (which is displayed vertically)
        Verify State will be displayed horizontally and not vertically.
        """
        pivobj.click_groupby_across_button('piv2', 1, 3, 1)
        utillobj.verify_pivot_data_set('piv2', 'C2053833_Ds03.xlsx','Step 06.1: Verify State will be displayed horizontally and not vertically')
        
        """
        Step 07: Now click left arrow for Category column
        Verify that Category column will be shifted to the left and Product column will be displayed first.
        """
        pivobj.click_groupby_across_button('piv2', 2, 2, 2)
        utillobj.verify_pivot_data_set('piv2', 'C2053833_Ds04.xlsx','Step 07.1: Verify that Category column will be shifted to the left and Product column will be displayed first.')
        
        """
        Step 08: Click right arrow for Category column
        Verify that Category column will be shifted to the right and Product column will be displayed second.
        """
        pivobj.click_groupby_across_button('piv2', 2, 1, 3)
        utillobj.verify_pivot_data_set('piv2', 'C2053833_Ds05.xlsx','Step 08.1: Verify that Category column will be shifted to the right and Product column will be displayed second.')
        
               

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
