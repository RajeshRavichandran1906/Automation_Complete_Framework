'''
Created on Sep 8, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053799

'''
import unittest
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_chart_rollup, visualization_resultarea,active_tools
from common.lib import utillity


class C2053799_TestClass(BaseTestCase):

    def test_C2053799(self):
        """
        Step 01: Execute the AR-RP-001A.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        toolobj= active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary 107of107')
        
        """
        Step 02: Click State > Chart/Rollup Tool
        Verify it opens up Advance Chart pop up.
        Verify pop up has following tabs: - Series - Charts
        """
        time.sleep(8)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart/Rollup Tool')  
        col_css="#charttoolt1 .arToolColumnBorder tr"
        tabs=[el.strip() for el in driver.find_element_by_css_selector(col_css).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(['Series','Charts'],tabs,"Step 02: Verify Chart/Rollup Tool 2 tabs") 
        
        """
        Step 03: By Default, user is on Series tab
        Verify this tab shows: - Columns - Group By - Measure
        """
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 1,['Columns','Category','Product ID','Product','State', 'Unit Sales','Dollar Sales'],"Step 03.1a: Verify Chart/Rollup Columns")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By', 'Drag Column Here'],"Step 03.1b: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure', 'Drag Column Here'],"Step 03.1c: Verify Chart/Rollup Measure")
             
        """
        Step 04: Drag Product column under Group By and Product ID column under Measure.
        Verify 'Product ID By Product' Donut type chart is displayed.
        """
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product', 1, 'Group By', 0)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product ID', 1, 'Measure', 0)
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By','Product'],"Step 04.1a: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure','Count:','Product ID'],"Step 04.1b: Verify Chart/Rollup Measure")
        
        """
        Step 05: Click Charts tab. Select Donut chart from the window and click Ok.
        """
        self.driver.find_element_by_css_selector("#charttoolt1 #ttpanel_1_1_0").click()
        time.sleep(5)
        rollobj.select_advance_chart('wall1', 'dountcylinder')
        time.sleep(8)
        import pyautogui
        pyautogui.hotkey('pageup')
        #screenshot
        time.sleep(2)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2053799_Actual_Step05', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall2',"riser!s2!g0!mwedge", ['Coffee Grinder','Product ID: 11','10.3% of 107'],"Step 05.1a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall2', 'riser!s2!g0!mwedge','oslo_gray',"Step 05.2b: Verify Chart piebevel Color ")
        
        time.sleep(5)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Product ID'],"Step 05.1b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall2',['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], "Step 05.1c: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall2', 'Product ID by Product', 'Step 05.1d: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall2',"Step 05.1e: Verify the chart Menu")
                
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
