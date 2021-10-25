'''
Created on Sep 2, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053846
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, \
    active_pivot_comment, active_tools,visualization_resultarea,active_chart_rollup

class C2053846_TestClass(BaseTestCase):

    def test_C2053846(self):
        
        """
            TESTCASE OBJECTS
        """
        toolobj  = active_tools.Active_Tools(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        rollobj  = active_chart_rollup.Active_Chart_Rollup(self.driver)
        misobj   = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivobj   = active_pivot_comment.Active_Pivot_Comment(self.driver)
        resobj   = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step 01: Execute the attached repro - Pivot.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary 107of107')
        
        """
        Step 02: Click State > Pivot Tool
        Verify this tab are displayed on tool: 
        - Columns 
        - Group By 
        - Across 
        - Measure
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 3, 'Pivot Tool')  
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
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Count:','Product ID'], 'Step 03.3:Verify Pivot Tool Measure')
        
        """
        Step 04: Click OK.
        Verify 'Product ID By State, Product' pivot table is displayed.
        Verify selected columns/data are displayed.
        """
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        pivobj.veryfy_pivot_table_title('piv2', 'ProductIDbyState,Product', 'Step 04.1: Verify pivot table title')   
        utillobj.verify_pivot_data_set('piv2', 'C2053846_Ds01.xlsx', "Step 04.2: Verify pivot dataset")
        
        """
        Step 05: Again Execute the AR-RP-001.fex
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')  
        misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 05.1: Verify Page summary 107of107')
        
        """
        Step 06: Click State > Rollup > Group By Product.
        Verify that 'State By Product' pop up window opened with the columns selected for the table.
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 3, 'Rollup','Product') 
        column=['Product', 'State']
        misobj.verify_column_heading('ITableData1', column, "Step 06.1: Verify dataset column heading")
        time.sleep(5)
        utillobj.verify_data_set('ITableData1','I1r','C2053846_Ds02.xlsx',"Step 06.2: Verify dataset of Rollup product")
        
        """
        Step 07: Again Execute the AR-RP-001.fex
        """
        utillobj.infoassist_api_logout()
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7078','mrid','mrpass')  
        misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 07.1: Verify Page summary 107of107')
        
        """
        Step 08: Click Unit Sales > Chart > Column > By Product
        Expect to see a Bar Chart generated from the Active Report.
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 4, 'Chart','Column','Product')
        time.sleep(5)
        #Tooltip & Color
        misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mbar", ['Unit Sales: 421K', 'X: Biscotti'],"Step 08.1: Verify bar chart tooltip and its color")
        utillobj.verify_chart_color('wall1',"riser!s0!g0!mbar",'cerulean_blue',"Step 08.2: Verify Color")
        time.sleep(5)
        #Riser XY Label
        xval=['Biscotti', 'Capuccino', 'Coffee Gr...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        yval=['0','200K','400K','600K','800K','1000K']
        resobj.verify_riser_chart_XY_labels('wall1', xval, yval, 'Step 08.3: Verify Bar XY labels')
        #Title
        misobj.verify_popup_title('wall1', 'Unit Sales by Product', 'Step 08.4: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 08.5: Verify the chart Menu")
        
if __name__ == '__main__':
    unittest.main()