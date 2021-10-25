'''
Created on Aug 31, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053836
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,active_pivot_comment, active_tools
from common.lib import utillity


class C2053836_TestClass(BaseTestCase):

    def test_C2053836(self):
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
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
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
        Step 03: Drag Product column under Group By, State column under Across and Product ID column under Measure.
        """    
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product', 1, 'Group By', 0)  
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'State', 1, 'Across', 0) 
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Product ID', 1, 'Measure', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By','Product'], 'Step 03.1:Verify Pivot Tool Group By')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','State'], 'Step 03.2:Verify Pivot Tool Across')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Count:', 'Product ID'], 'Step 03.3:Verify Pivot Tool Measure')
        
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
        pivobj.veryfy_pivot_table_title('piv2', 'ProductIDbyState,Product', 'Step 04.1: Verify pivot Title ProductIDbyState,Product.')
        utillobj.verify_pivot_data_set('piv2', 'C2053835_Ds01.xlsx','Step 04.2: Verify Pivot dataset')
        pivobj.verify_pivot_menu('wall2', 'Step 04.3: Verify pivot toolbar menus')  
        
        """
        Step 05: Click Freeze icon on the Pivot table
        Verify that freeze icon is locked.
        """
#         unlock = "//div[@id='LINKIMG2_-1']//img[contains(@src,'i3AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG2_-1']//img[contains(@src,'GNertexgnyiHAzoQJGG3')]"
        pivobj.click_pivot_menu_bar_items('wall2', 1)
        utillobj.asequal(len(self.driver.find_elements_by_xpath(lock)),1,"Step 05: Verify freeze icon is locked")
        active_misobj.move_active_popup(2,800,150)
        
        """
        Step 06: Now apply filter to the original report as follows: Category > Filter > Food
        Click Filter button.
        """
        active_misobj.select_menu_items('ITableData0', 0, 'Filter', 'Equals')
        active_misobj.move_active_popup(1,800,400)
        active_filter.create_filter(1, 'Equals', value1='Food')
        active_filter.filter_button_click('Filter')
        active_filter.verify_filter_selection_dialog(True,'Step 06.1: Verify filter row.',['Category','Equals','Food'])
        """Verify that report shows filtered records for Food. 
        Verify that Pivot table does not reflect any changes of the filter."""
        utillobj.verify_data_set('ITableData0','I0r','C2053835_Ds02.xlsx',"Step 06.2: Verify Filtered dataset Category Equals Food")
        utillobj.verify_pivot_data_set('piv2', 'C2053835_Ds01.xlsx','Step 06.3: Verify Pivot table does not reflect any changes of the filter')
        
        """
        Step 07: Now go back to Pivot table and Unfreeze Freeze icon
        Verify that freeze icon is unlocked. Verify that Pivot table also reflect the changes on pivot table.
        """
        unlock = "//div[@id='LINKIMG2_-1']//img[contains(@src,'i3AAAAAElFTkSuQmCC')]"
        lock = "//div[@id='LINKIMG2_-1']//img[contains(@src,'GNertexgnyiHAzoQJGG3')]"
        pivobj.click_pivot_menu_bar_items('wall2', 1)
        utillobj.asequal(len(self.driver.find_elements_by_xpath(unlock)),1,"Step 07.1: Verify freeze icon is unlocked")
        utillobj.verify_pivot_data_set('piv2', 'C2053836_Ds01.xlsx','Step 07.2: Verify Pivot table also reflect the changes on table')
               

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
