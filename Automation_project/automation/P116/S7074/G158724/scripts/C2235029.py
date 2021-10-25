'''
Created on JUN 18, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235029
TestCase Name = Funnel/Pyramid displays are different for IA vs. Chart Tool.Proj 159218
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run,active_tools
from common.lib import utillity

class C2235029_TestClass(BaseTestCase):

    def test_C2235029(self):
        
        Test_Case_ID="C2235029"
        """
            TESTCASE VARIABLES
        """
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        rollupobj =active_chart_rollup.Active_Chart_Rollup(driver)
        ia_runobj=ia_run.IA_Run(driver)
        active_toolsobj = active_tools.Active_Tools(self.driver)
        """
            Step 01:Execute attached repro - 159199.fex.
        """
        utillobj.active_run_fex_api_login("159199.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Top'] img"
        resobj.wait_for_property(parent_css, 1)
        miscelaneous_obj.verify_page_summary('0','10of10records,Page1of1', 'Step 02.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2235029_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2235029_Ds01.xlsx',"Step 02.2: ahtml_chart.fex data verification")
        time.sleep(2)
     
        """
            Step 02:From any field drop down control, 
            select the Chart Rollup Tool.
             
        """
         
        miscelaneous_obj.select_menu_items("ITableData0", "0", "Chart/Rollup Tool")
        time.sleep(6)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product ID', 'Unit Sales', 'Dollar Sales'], 'Step 02.3: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Drag Column Here'], 'Step 02.4: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Drag Column Here'], 'Step 02.5: Expect to see the following Advanced Chart menu.')
        time.sleep(3)
        """
            Step 03:Drag Unit Sales to the Measure column. Drag Product ID to the Group By column.
        """
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        time.sleep(2)
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product ID', 1, 'Group By', 0)
        time.sleep(3)
        rollupobj.select_advance_chart('charttoolt1', 'pyramid')
        time.sleep(3)
        expected_label_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        resobj.verify_riser_legends('wall2', expected_label_list, 'Step 03.1: Verify pyramid lablesList')
        utillobj.verify_chart_color("wall2", "riser!s0!g0!mriser", "bar_blue", "Step 03.2: Verify first pyramid bar color")
        miscelaneous_obj.verify_chart_title('wbody2_ft', 'Unit Sales by Product ID', 'Step 03.3: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['More Options', 'Column','Pie','Line', 'Scatter', 'Rollup','Advanced Chart', 'Original Chart'],"Step 03.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Aggregation'],"Step 03.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Sum'],"Step 03.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('wall2', 20, "Step 03.7: Verify number of segment", custom_css=".chartPanel g path[class*='riser!s']")    
        expected_tooltip_list=['F103', 'X: Unit Sales', 'Y: 630K']
        miscelaneous_obj.verify_active_chart_tooltip("wall2", "riser!s5!g0!mriser!", expected_tooltip_list, "Step 03.8: Verify bar value")
        utillobj.verify_object_visible("#wmenu2 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.9: toggleFiltLink Visible')
        time.sleep(3)
        miscelaneous_obj.close_popup_dialog("2")
        """
            Step 04:From any field drop down control, 
            select the Chart Rollup Tool.
             
        """
         
        miscelaneous_obj.select_menu_items("ITableData0", "0", "Chart/Rollup Tool")
        time.sleep(6)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product ID', 'Unit Sales', 'Dollar Sales'], 'Step 02.3: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Drag Column Here'], 'Step 02.4: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Drag Column Here'], 'Step 02.5: Expect to see the following Advanced Chart menu.')
        time.sleep(3)
        """
            Step 05:Drag Unit Sales to the Measure column. Drag Product ID to the Group By column.
            Step 06:From the Charts Tab, select Funnel. Notice that there are no Unit Sales on the sector slices. Hover over provides that information.
        """
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        time.sleep(2)
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product ID', 1, 'Group By', 0)
        time.sleep(3)
        rollupobj.select_advance_chart('charttoolt1', 'funnel')
        time.sleep(3)
        expected_label_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        resobj.verify_riser_legends('wall2', expected_label_list, 'Step 05.1: Verify Funnel lablesList')
        utillobj.verify_chart_color("wall2", "riser!s0!g0!mriser", "bar_blue", "Step 05.2: Verify first Funnel bar color")
        miscelaneous_obj.verify_chart_title('wbody2_ft', 'Unit Sales by Product ID', 'Step 05.3: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['More Options', 'Column','Pie','Line', 'Scatter', 'Rollup','Advanced Chart', 'Original Chart'],"Step 05.4: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Aggregation'],"Step 05.5: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Sum'],"Step 05.6: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('wall2', 20, "Step 05.7: Verify number of pie", custom_css=".chartPanel g path[class*='riser!s']")    
        expected_tooltip_list=['F103', 'X: Unit Sales', 'Y: 630K']
        miscelaneous_obj.verify_active_chart_tooltip("wall2", "riser!s5!g0!mriser!", expected_tooltip_list, "Step 05.8: Verify bar value")
        utillobj.verify_object_visible("#wmenu2 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 05.9: toggleFiltLink Visible')
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step5', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        miscelaneous_obj.close_popup_dialog("2")
if __name__ == '__main__':
    unittest.main()
        
        