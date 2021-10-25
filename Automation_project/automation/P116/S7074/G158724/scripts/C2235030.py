'''
Created on JUN 18, 2017

@author: Pavithra

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235030
TestCase Name = PIE Charts show gray areas when a slice is clicked.Proj 159195
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup,ia_run,active_tools
from common.lib import utillity

class C2235030_TestClass(BaseTestCase):

    def test_C2235030(self):
        
        Test_Case_ID="C2235030"
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
            Step 01:Execute attached repro - ahtml_chart.fex.
        """
        utillobj.active_run_fex_api_login("ahtml_chart.fex", "S7074", 'mrid', 'mrpass')
        time.sleep(6)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Top'] img"
        resobj.wait_for_property(parent_css, 1)
        miscelaneous_obj.verify_page_summary('0','10of10records,Page1of1', 'Step 01.1: Verify Page summary')
#         ia_runobj.create_table_data_set("table[id='ITableData0']", "C2235030_Ds01.xlsx")
        ia_runobj.verify_table_data_set("table[id='ITableData0']", 'C2235030_Ds01.xlsx',"Step 01.2: ahtml_chart.fex data verification")
        time.sleep(2)
     
        """
            Step 02:From any field drop down control, 
            select the Chart Rollup Tool.
        """ 
        miscelaneous_obj.select_menu_items("ITableData0", "0", "Chart/Rollup Tool")
        time.sleep(6)
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 1,['Columns', 'Category', 'Product ID', 'Unit Sales', 'Dollar Sales'], 'Step 02.1: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 2,['Group By', 'Drag Column Here'], 'Step 02.2: Expect to see the following Advanced Chart menu.')
        active_toolsobj.chart_rollup_tool_verify_columns('charttoolt1', 'tpanel_0_1_0', 3,['Measure', 'Drag Column Here'], 'Step 02.3: Expect to see the following Advanced Chart menu.')
        time.sleep(3)
        """
            Step 03:Drag Unit Sales to the Measure column.Drag Product ID to the Group By column.
        """
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        time.sleep(2)
        active_toolsobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product ID', 1, 'Group By', 0)
        time.sleep(3)
        
        """
            Step 04:Click the Charts tab and select the first PIE chart.
        """
        rollupobj.select_advance_chart('charttoolt1', 'piebevel')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('wall2', ['Unit Sales'], "Step 04.1:",custom_css="text[class*='pieLabel']",same_group=True)
        expected_label_list=['C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        resobj.verify_riser_legends('wall2', expected_label_list, 'Step 04.2: Verify pie lablesList')
        utillobj.verify_chart_color("wall2", "riser!s0!g0!mwedge", "bar_blue", "Step 04.3: Verify first bar color")
        miscelaneous_obj.verify_chart_title('wbody2_ft', 'Unit Sales by Product ID', 'Step 04.4: Verify Chart Title')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['More Options', 'Column','Pie','Line', 'Scatter', 'Rollup','Advanced Chart', 'Original Chart'],"Step 04.5: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Aggregation'],"Step 04.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('wmenu2', ['Sum'],"Step 04.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('wall2', 10, "Step 04.8: Verify number of pie", custom_css=".chartPanel g path[class*='riser!s']")    
        expected_tooltip_list=['C142', 'Unit Sales: 878K', '23.8% of 3.7M']
        miscelaneous_obj.verify_active_chart_tooltip("wall2", "riser!s1!g0!mwedge", expected_tooltip_list, "Step 03.9: Verify bar value")
        time.sleep(2)
        utillobj.verify_object_visible("#wmenu2 .arChartMenuBar div[onclick*='toggleFiltLink']", True, 'Step 03.10 toggleFiltLink Visible')
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step4', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
        
        