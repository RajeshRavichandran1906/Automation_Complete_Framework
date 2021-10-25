'''
Created on Sep 1, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053842
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_pivot_comment, active_tools

class C2053842_TestClass(BaseTestCase):

    def test_C2053842(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        toolobj  = active_tools.Active_Tools(self.driver)
        misobj   = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivobj   = active_pivot_comment.Active_Pivot_Comment(self.driver)
                
        """
        Step 01: Execute the AR_RP_CALCULATE.fex
        """
        utillobj.active_run_fex_api_login('AR_RP_CALCULATE.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
        
        """
        Step 02: Select Order Number INTEGER, then select the Pivot Tool located below the Chart/Rollup Tool.
        Expect to see the Pivot Tool open, a list of available fields, labeled by Columns, 
        followed by empty areas for Group By, Across and Measure.
        """
        self.driver.set_page_load_timeout(100)
        misobj.select_menu_items('ITableData0', 0, 'Pivot Tool')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By','Drag Column Here'], 'Step 02.2:Verify Pivot Tool Group By')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','Drag Column Here'], 'Step 02.3:Verify Pivot Tool Across')
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Drag Column Here'], 'Step 02.4:Verify Pivot Tool Measure')
        
        """
        Step 03: From the Columns list, left click the Order Number INTEGER field drag and drop it on the Measure area, on the Drag Column Here text.
        Expect to see the Order Number INTEGER field added to the Measure area.
        """
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Order Number INTEGER', 1, 'Measure', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 4,['Measure', 'Sum:','Order Number INTEGER'], 'Step 03.1:Verify Pivot Tool Measure')
        
        """
        Step04: From the Columns list, click on the ALPHA Store Code field and drop it on the Group By area, on the Drag Column Here text.
        Expect to see the ALPHA Store Code field added to the Group By area.
        """
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'ALPHA Store Code', 1, 'Group By', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By', 'ALPHA Store Code'], 'Step 04.1:Verify Pivot Tool Group By')
        
        """
        Step 05: From the Columns list, click on the Date YYMD field and drop it on the Across area, on the Drag Column Here text.
        Expect to see the Date YYMD field added to the Across area.
        """
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'Date YYMD', 1, 'Across', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across', 'Date YYMD'], 'Step 05.1:Verify Pivot Tool Across')
        
        """
        Step 06: Click the OK tab to produce the Pivot Table.
        Expect to see the same Pivot Table as generated in AR-RP-193
        """
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds01.xlsx', "Step 06.1: Verify Pivot datset")
        
        """
        Step 07: Change a Group By sort column by clicking on the first icon and selecting Pivot Tool again. 
        In the Group By area, click the 'X' next to ALPHA Store Code. 
        Then drag the D10.2 Unit Price field to the Group By area and press OK.
        Expect to see the Pivot Table with D10.2 Unit Price as the by sort and Date YYMD as the ACROSS sort. 
        ALPHA Store Code is no longer a sort axis.
        """
        misobj.move_active_popup("2", "900", "150")
        pivobj.create_new_item('wall2', 0, 'Pivot Tool')
        time.sleep(2)
        misobj.move_active_popup("1", "900", "400")
        toolobj.pivot_tool_delete_column_items('pivottoolt1', 2,0)
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'D10.2 Unit Price', 1, 'Group By', 0)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By', 'D10.2 Unit Price'], 'Step 07.1:Verify Pivot Tool Group By')
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds02.xlsx', "Step 07.2: Verify Pivot datset with D10.2 Unit Price as the by sort and Date YYMD as the ACROSS sort")
        
        """
        Step 08: Add another Group By sort by clicking on the first icon and dragging ALPHA Store Code to the 
        Group By area and positioning it under D10.2 Unit Price until the red positioning bar appears. 
        Click OK to for the new Pivot Table.
        Expect to see the Pivot tool contain the second Group By column. 
        Expect to see ALPHA Store Code added as a Group By sort after D10.2 Unit Price Group By sort.
        
        """
        time.sleep(5)
        pivobj.create_new_item('wall2', 1, 'Pivot Tool')
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'ALPHA Store Code', 1, 'Group By', 1)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By', 'D10.2 Unit Price','ALPHA Store Code'], 'Step 08.1:Verify Pivot Tool Group By')
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds03.xlsx','Step 08.2: Verify pivot dataset, ALPHA Store Code added as a Group By sort after D10.2 Unit Price Group By sort')
          
        """
        Step 09: Reverse the order of the Group By sorts by clicking on the first icon, selecting Pivot Tool 
        and dragging the D10.2 Unit Price field below the ALPHA Store Code, again dropping it on the red bar below ALPHA Stoe Code.
        Expect to see the Group By sort field order changed to ALPHA Store Code followed by D10.2 Unit Price.
        """
        time.sleep(5)
        pivobj.create_new_item('wall2', 1, 'Pivot Tool')
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Group By', 'D10.2 Unit Price', 1, 'Group By', 2)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 2,['Group By','ALPHA Store Code','D10.2 Unit Price'], 'Step 09.1:Verify Pivot Tool Group By columns interchanged')
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds04.xlsx','Step 09.2: Verify pivot dataset, ALPHA Store Code added as a Group By sort after D10.2 Unit Price Group By sort')
         
        """
        Step 10: Move then D10.2 Unit Price Group By sort to an Across sort by clicking on the first icon, selecting Pivot Tool
        and dragging the D10.2 Unit Price field over to the Across area and positioning it below the Date YYMD field.
        Expect to see the D10.2 Unit Price field repositioned as an Across sort field, below the Date YYMD Across sort field.
        """
        time.sleep(8)
        pivobj.create_new_item('wall2', 1, 'Pivot Tool')
        toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Group By', 'D10.2 Unit Price', 1, 'Across', 1)
        toolobj.pivot_tool_verify_columns('pivottoolt1', 3,['Across','Date YYMD','D10.2 Unit Price'], 'Step 10.1:Verify Pivot Tool Across')
        toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds05.xlsx','Step 010.2: Verify pivot dataset, D10.2 Unit Price field repositioned as an Across sort field')
         
        """
        Step 11: Reverse the Across sorts by clicking the down arrow in the Date YYMD area. 
        Then click the up arrow in the Date YYMD field to move it under the D10.2 Unit Price Across sort.
        Expect to see the two Across sort fields reverse their order.
        """
        time.sleep(5)
        pivobj.click_groupby_across_button('piv2', 1, 2, 1)
        pivobj.click_groupby_across_button('piv2', 2, 1, 1)
        utillobj.verify_pivot_data_set('piv2', 'C2053842_Ds06.xlsx','Step 011.1: Verify pivot dataset, two Across sort fields reverse their order')
        
if __name__ == '__main__':
    unittest.main()