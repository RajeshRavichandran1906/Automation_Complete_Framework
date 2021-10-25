'''
Created on Aug 30, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053834
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment, active_tools
from common.lib import utillity


class C2053834_TestClass(BaseTestCase):

    def test_C2053834(self):
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
        time.sleep(3)
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Category', 1, 'Group By', 0)  
        time.sleep(3)
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Group By', 1)  
        time.sleep(3)
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product', 1, 'Across', 0) 
        time.sleep(3)
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product ID', 1, 'Measure', 0)
        time.sleep(3)
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
        Step 05: Click Dropdown menu > Pivot Tool
        """
        time.sleep(3)
        pivobj.create_new_item('wall2', 0, 'Pivot Tool')
        time.sleep(5)
        active_misobj.move_active_popup("2", "600", "200")
        
        """
        Step 06: Click on the (x) delete icon next to Product column and verify that Product field deleted correctly
        """
        toolobj.pivot_tool_delete_column_items('pivottoolt1', 3,0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','Drag Column Here'], 'Step 06.1:Verify Pivot Tool Across')
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053834_Ds01.xlsx','Step 06.2: Verify Pivot dataset after deleting Product')
        
               

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
