'''
Created on Aug 29, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053822
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment, active_tools
from common.lib import utillity


class C2053822_TestClass(BaseTestCase):

    def test_C2053822(self):
        """
            TESTCASE VARIABLES
        """
        
        """
        Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary 107of107')
        
        """
        Step 02: Click dropdown menu for State column and mouse over Pivot(Cross Tab)
        Verify Group By (Columns) are displayed as: - Category - Product ID - Product - State - Unit Sales - Dollar Sales
        """
        option=['Group By(COU)', 'Category', 'Product', 'Product ID', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_menu_items('ITableData0', 3, 'Pivot (Cross Tab)',option,"Step 02: Expect to see Group By (Columns) ")
        
        temp=driver.find_element_by_css_selector("#TCOL_0_C_3")
        temp.click()
        time.sleep(2)
                         
        """
        Step 03: Click dropdown menu for State column and mouse over Pivot(Cross Tab) > any column (Category) > Product ID
        """
        active_misobj.select_menu_items('ITableData0', 3, 'Pivot (Cross Tab)','Category','Product ID')         
        """Verify Pivot table 'State By Product ID, Category' is generated based on the columns selection."""         
        utillobj.verify_pivot_data_set('piv1', 'C2053819_Ds01.xlsx','Step 03: Verify Pivot dataset')  
        
        """
        Step 04: Click New icon (dropdown) > Pivot Tool
        """
        pivobj.create_new_item('wall1', 0, 'Pivot Tool')
        
        """
        Verify that Pivot Tool opens up with these sections (as these combination is selected for the table): - Columns (shows all the columns of a report) 
        - Group By (Category) 
        - Across (Product ID) 
        - Measure (Count: State)    
        """
        toolobj.pivot_tool_verify_columns('pivottoolt2', 1,['Columns','Category','Product','Product ID','State','Unit Sales','Dollar Sales'], 'Step 04.1:Verify Pivot Tool Columns')
        toolobj.pivot_tool_verify_columns('pivottoolt2', 2,['Group By','Category'], 'Step 04.2:Verify Pivot Tool Group By has Category')
        toolobj.pivot_tool_verify_columns('pivottoolt2', 3,['Across','Product ID'], 'Step 04.3:Verify Pivot Tool Across has Product ID')
        toolobj.pivot_tool_verify_columns('pivottoolt2', 4,['Measure', 'Count:', 'State'], 'Step 04.4:Verify Pivot Tool Measure has Count: State')
        """Drage and drop Product column under Group By section and click Ok."""
        toolobj.pivot_tool_drag_drop_items('pivottoolt2', 'Columns', 'Product', 1, 'Group By', 1)
        toolobj.pivot_tool_verify_columns('pivottoolt2', 2,['Group By','Category','Product'], 'Step 04.5:Verify Pivot Tool Group By has Product')
        self.driver.find_element_by_css_selector("#pivottool2 .arToolButton").click()
                
        pivobj.veryfy_pivot_table_title('piv1', 'StatebyProductID,Category,Product', 'Step 04.6: Verify pivot table title')
        #utillobj.create_pivot_data_set('piv1', 'C2053822_Ds01.xlsx')
        utillobj.verify_pivot_data_set('piv1', 'C2053822_Ds01.xlsx','Step 04.7: Verify Pivot dataset')

    
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
