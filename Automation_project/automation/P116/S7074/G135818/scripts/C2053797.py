'''
Created on Sep 7, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053797

'''
import unittest
import time,re
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup, visualization_resultarea,active_tools
from common.lib import utillity


class C2053797_TestClass(BaseTestCase):

    def test_C2053797(self):
        """
            TESTCASE VARIABLES
        """

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
        Step 02: For the Dollar Sales drop down, click > Chart/Rollup Tool
        Verify it opens up Advance Chart pop up.
        Verify pop up has following tabs: - Series - Charts
        """

        active_misobj.select_menu_items('ITableData0', 5, 'Chart/Rollup Tool')  
        col_css="#charttoolt1 .arToolColumnBorder tr"
        tabs=[el.strip() for el in driver.find_element_by_css_selector(col_css).text.split("\n") if bool(re.match('\S', el))]
        utillobj.asequal(['Series','Charts'],tabs,"Step 02: Verify Chart/Rollup Tool 2 tabs") 
        
        
        """
        Step 03: By Default, user is on Series tab
        Verify this tab shows: - Columns - Group By - Measure
        Drag Product column under Group By and Dollar Sales column under Measure.
        Verify Dollar Sales under Measure and Product under Group By.
        """
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 1,['Columns','Category','Product ID','Product','State', 'Unit Sales','Dollar Sales'],"Step 03.1a: Verify Chart/Rollup Columns")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By', 'Drag Column Here'],"Step 03.1b: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure', 'Drag Column Here'],"Step 03.1c: Verify Chart/Rollup Measure")
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product', 1, 'Group By', 0)
        time.sleep(5)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Dollar Sales', 1, 'Measure', 0)
        time.sleep(5)
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By','Product'],"Step 03.2: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure','Sum:','Dollar Sales'],"Step 03.3: Verify Chart/Rollup Measure")
        
        """
        Step 04: Click OK.
        Verify 'Dollar Sales By Product' chart is displayed.
        """
        toolobj.chart_rollup_tool_close('charttoolt1', 'Ok')  
        
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2053797_Actual_Step04', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall2',"riser!s0!g0!mbar",['Dollar Sales: 5.3M','X: Biscotti'],"Step 04.1a: Verify Chart tooltip")
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar','cerulean_blue',"Step 04.1a: Verify Chart piebevel Color ")
        time.sleep(5)
        #XY Labels
        x=['Biscotti']
        y=['0','2M','4M','6M','8M','10M','12M']
        resobj.verify_riser_chart_XY_labels('wall2',x,y,"Step 05.1c: Verify XY Labels")   
        #Title
        active_misobj.verify_popup_title('wall2', 'Dollar Sales by Product', 'Step 05.1c: Verify the dialog title')        
        #Legend
        resobj.verify_riser_legends('wall2', ['Dollar Sales'],"Step 05.1c: Verify Chart Legend")
        #Menu
        rollobj.verify_arChartMenu('wall2',"Step 04.1d: Verify the chart Menu")
        
        """
        Step 05: From the first icon, More Options, select Chart/Rollup Tool again.
        Drag State under Product in the Group By area.
        Click OK.
        """
        rollobj.create_new_item(0, 'Chart/Rollup Tool',False,'wall2')
        #active_misobj.move_active_popup("2", "600", "200")
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'State', 1, 'Group By', 1, sx_offset=0, sy_offset=-7, tx_offset=0, ty_offset=1)
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By','Product','State'],"Step 05.1a: Verify Chart/Rollup Group By")
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure','Sum:','Dollar Sales'],"Step 05.1b: Verify Chart/Rollup Measure")
        toolobj.chart_rollup_tool_close('charttoolt1', 'Ok')
        
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2053797_Actual_Step05', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall2',"riser!s0!g0!mbar",['Dollar Sales: 536K','X: Biscotti/CA'],"Step 05.1a: Verify Chart tooltip")
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar','cerulean_blue',"Step 05.1b: Verify Chart piebevel Color ")
        time.sleep(5)
        #XY Labels
        x=['Biscotti/CA']
        y=['0', '0.4M','0.8M','1.2M','1.6M','2M']
        resobj.verify_riser_chart_XY_labels('wall2',x,y,"Step 05.1c: Verify XY Labels")
        #Title
        title=driver.find_element_by_css_selector("#wbody2_ft div").text
        utillobj.asequal(title,"Dollar Sales by Product, State", 'Step 05.1d: Verify the dialog title')
        #Legend
        resobj.verify_riser_legends('wall2', ['Dollar Sales'],"Step 05.1e: Verify Chart Legend")
        
        """
        Step 06: Click X next to column name Product and click Ok
        Verify that Product column is no more available under Group By . Verify 'Product ID By State' chart is displayed.
        """
        rollobj.create_new_item(1, 'Chart/Rollup Tool',False,'wall2')
        toolobj.chart_rollup_tool_delete_column_items('charttoolt1',1,0)
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By', 'State'],"Step 06.1: Verify Chart/Rollup Group By after deleting Product")
        toolobj.chart_rollup_tool_close('charttoolt1', 'Ok')
        
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2053797_Actual_Step06', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall2',"riser!s0!g0!mbar",['Dollar Sales: 7.6M','X: CA'],"Step 06.2a: Verify Chart tooltip")
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar','cerulean_blue',"Step 06.2b: Verify Chart piebevel Color ")
        time.sleep(5)
        #XY Labels
        expected_xval_list=['CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M', '9M']
        resobj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, 'Step 06.3: Verify XY Labels')
        #Title
        title=driver.find_element_by_css_selector("#wbody2_ft div").text
        utillobj.asequal(title,"Dollar Sales by State", 'Step 06.4: Verify the dialog title')
        #Legend
        resobj.verify_riser_legends('wall2', ['Dollar Sales'],"Step 06.5: Verify Chart Legend")
                
if __name__ == '__main__':
    unittest.main()

