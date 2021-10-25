'''
Created on Aug 3, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050527
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_pivot_comment,active_tools
from common.lib import utillity
import unittest

class C2050527_TestClass(BaseTestCase):

    def test_C2050527(self):
        """
            TESTCASE VARIABLES
        """
        
        """
            Step 01: Execute the AR-RP-193.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        pivotobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        activeToolsobj = active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-193.fex", "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0", 1, 60)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Execute the AR-RP-193.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        """
        Step 02: Create a new Pivot Table by selecting P9.2M Unit Price and from the drop down list, 
        select Pivot(Cross Tab), move to Group BY(SUM) and 
        select ALPHA Store Code, move to Across and select Date YYMD for the Across.
        """
        miscelanousobj.select_menu_items('ITableData0', "6", "Pivot (Cross Tab)","ALPHA Store Code","Date YYMD")
        utillobj.verify_pivot_data_set("piv1", "C2050527_Ds01.xlsx","Step 02: Expect to see a Pivot Table")
        pivotobj.close_comment_dialog()
        
        """
        Step 03: Select Order Number INTEGER, then select the Pivot Tool located below the Chart/Rollup Tool.
        """
        miscelanousobj.select_menu_items('ITableData0', "0", "Pivot Tool")
        """"
        Expect to see the Pivot Tool open, a list of available fields, labeled by Columns, followed by empty areas for Group By, Across and Measure.
        """
        columns = ['Columns', 'Order Number INTEGER', 'ALPHA Store Code', 'Date YYMD', 'Date MDYY', 'Date DMYY', 'D10.2 Unit Price', 'P9.2M Unit Price', 'DATETIME HYYMDSA']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 1, columns, "Step 03: Expect to see a list of available fields, labeled by Columns,")
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, ['Group By', 'Drag Column Here'], "Step 03: Expect to see empty areas for Group By")
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 3, ['Across', 'Drag Column Here'], "Step 03: Expect to see empty areas for Across")
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 4, ['Measure', 'Drag Column Here'], "Step 03: Expect to see empty areas for Measure")
        
        """
        Step 04: From the Columns list, left click the Order Number INTEGER field drag and drop it on the Measure area, on the Drag Column Here text.
        """
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Columns", "Order Number INTEGER", 1, "Measure", 0)
        measure = ['Measure', 'Sum:', 'Order Number INTEGER']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 4, measure, "Step 04: Expect to see the Order Number INTEGER field added to the Measure area")
       
        """
        Step 05: From the Columns list, click on the ALPHA Store Code field and drop it on the Group By area, on the Drag Column Here text.
        """
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Columns", "ALPHA Store Code", 1, "Group By", 0)
        groupby=['Group By','ALPHA Store Code']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, groupby,"Step 05: Expect to see the ALPHA Store Code field added to the Group By area")
        
        """
        Step 06: From the Columns list, click on the Date YYMD field and drop it on the Across area, on the Drag Column Here text.
        """
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Columns", "Date YYMD", 1, "Across", 0)
        across = ['Across','Date YYMD']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 3, across,'Step 06: Expect to see the Date YYMD field added to the Across area')
        miscelanousobj.move_active_popup(1, 900, 150)
        
        """
        Step 07: Click the OK tab to produce the Pivot Table.
        """
        activeToolsobj.pivot_tool_close("pivottoolt1", "Ok")
        
        """Expect to see the following Pivot Table with Alpha Store code down the page and Date YYMD across the page."""
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds02.xlsx", "Step 07: Expect to see pivot table")
        
        """
        Step 08: Click the first icon on the Pivot report to re-open the Pivot menu.
        In the Group By area, click the 'X' next to ALPHA Store Code. 
        Then drag the D10.2 Unit Price field to the Group By area and click OK.
        """
        pivotobj.create_new_item("wall2", 0, "Pivot Tool")
        miscelanousobj.move_active_popup("2", "900", "400")
        activeToolsobj.pivot_tool_delete_column_items("pivottoolt1", 2, 0)
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, ['Group By', 'Drag Column Here'], "Step 08: Verify ALPHA Store Code deleted")
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Columns", "D10.2 Unit Price", 1, "Group By", 0)
        groupby1=['Group By','D10.2 Unit Price']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, groupby1,"Step 08: Expect to see the D10.2 Unit Price field added to the Group By area")
        activeToolsobj.pivot_tool_close("pivottoolt1", "Ok")
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds03.xlsx", "Step 08: Expect to see pivot table with D10.2 Unit Price")
        """
        Step 09: Add another Group By sort by clicking on the first icon and dragging ALPHA Store Code to the Group By area and 
        positioning it under D10.2 Unit Price until the red positioning bar appears. Click OK to for the new Pivot Table.
        """
        pivotobj.create_new_item("wall2", 1, "Pivot Tool")
        utillobj.wait_for_page_loads(5, pause_time=5)
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Columns", "ALPHA Store Code", 1, "Group By", 1)
        groupby2=['Group By','D10.2 Unit Price','ALPHA Store Code']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, groupby2,"Step 09: Expect to see the Pivot tool contain the second Group By column")
        activeToolsobj.pivot_tool_close("pivottoolt1", "Ok")
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds04.xlsx", "Step 09: Expect to see ALPHA Store Code added as a Group By sort after D10.2 Unit Price Group By sort")

        """
        Step 10: Reverse the order of the Group By sorts by clicking on the first icon, 
        selecting Pivot Tool and dragging the D10.2 Unit Price field below the ALPHA Store Code, 
        again dropping it on the red bar below ALPHA Store Code.
        """
        pivotobj.create_new_item("wall2", 1, "Pivot Tool")
        utillobj.wait_for_page_loads(5, pause_time=5)
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Group By", "D10.2 Unit Price", 1, "Group By", 2)
        groupby3=['Group By','ALPHA Store Code','D10.2 Unit Price']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 2, groupby3,"Step 10: Expect to see the Pivot tool with reverse the order of the Group By")
        activeToolsobj.pivot_tool_close("pivottoolt1", "Ok")
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds05.xlsx", "Step 10: Expect to see the table Group By sort field order changed to ALPHA Store Code followed by D10.2 Unit Price")
        
        """
        Step 11: Move then D10.2 Unit Price Group By sort to an Across sort by clicking on the first icon, selecting Pivot Tool 
        and dragging the D10.2 Unit Price field over to the Across area and positioning it below the Date YYMD field.
        """
        pivotobj.create_new_item("wall2", 1, "Pivot Tool")
        utillobj.wait_for_page_loads(5, pause_time=5)
        activeToolsobj.pivot_tool_drag_drop_items("pivottoolt1", "Group By", "D10.2 Unit Price", 1, "Across", 1)
        across1=['Across','Date YYMD','D10.2 Unit Price']
        activeToolsobj.pivot_tool_verify_columns("pivottoolt1", 3, across1, "Step 11: Expect to see the D10.2 Unit Price field repositioned as an Across sort field")
        activeToolsobj.pivot_tool_close("pivottoolt1", "Ok")
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds06.xlsx", "Step 11: Expect to see the table")
        
        """
        Step 12: Reverse the Across sorts by clicking the down arrow in the Date YYMD area. 
        Then click the up arrow in the Date YYMD field to move it under the D10.2 Unit Price Across sort.
        """
        pivotobj.click_groupby_across_button('piv2', 1, 2, 3)
        utillobj.verify_pivot_data_set("piv2", "C2050527_Ds07.xlsx", "Step 12: Expect to see the two Across sort fields reverse their order")
        
if __name__ == '__main__':
    unittest.main()