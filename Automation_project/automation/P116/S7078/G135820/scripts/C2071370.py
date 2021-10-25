'''
Created on Sept 01, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2071370

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_chart_rollup, visualization_resultarea, active_tools
from common.lib import utillity


class C2071370_TestClass(BaseTestCase):

    def test_C2071370(self):
        """
        Step 01: Execute the attached repro - act-246
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        toolobj= active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('ACT-639.fex','S7078','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary 107of107')
        column=['Category','Product', 'State', 'Unit Sales','Dollar Sales']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.a: Verify Column heading of act-246.fex")
        utillobj.verify_data_set('ITableData0','I0r','C2071370_Ds01.xlsx',"Step 01.b: Verify act-639.fex dataset")        
        #utillobj.create_data_set('ITableData0','I0r','C2071370_Ds01.xlsx')
        
        """
        Step 02: From the drop down control for Unit Sales, select the Chart/Rollup Tool.
                Place Unit Sales and Dollar Sales in the Measure area. 
                Place Product an Category in the Group By area,
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart/Rollup Tool')
        time.sleep(5)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Product', 1, 'Group By', 0)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Category', 1, 'Group By', 1)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)
        toolobj.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Dollar Sales', 1, 'Measure', 1)
        """Expect to see the Chart/Rollup menu with the following values."""
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 2,['Group By', 'Product', 'Category'], 'Step 03a: Verify Group By column')
        toolobj.chart_rollup_tool_verify_columns('charttoolt1','tpanel_0_1_0', 3,['Measure', 'Sum:', 'Unit Sales', 'Sum:', 'Dollar Sales'], 'Step 03b: Verify Measure column')
        
        """
        Step 03: Click OK to generate the default Bar Chart.
        """
        driver.find_element_by_css_selector("#charttoolt1 td[onclick*=dochart]").click()
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2071370_Actual_Step08', image_type='actual')
           
        rollobj.verify_arChartMenu("wall2", "Step 03.a Verify the Chart Menu bar labels displayed on Run chart")
        x_val_list=['Biscotti/F...', 'Capuccin...', 'Coffee Gri...', 'Coffee Po...', 'Croissant...', 'Espresso...', 'Latte/Coffee', 'Mug/Gifts', 'Scone/Food', 'Thermos/...']
        y_val_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        
        resobj.verify_riser_chart_XY_labels('wall2', x_val_list, y_val_list, 'Step 03.b: Verify XY Label')
        
        expected_tooltip=['Dollar Sales: 5.3M', 'X: Biscotti/Food']
        active_misobj.verify_active_chart_tooltip('wall2', 'riser!s1!g0!mbar!', expected_tooltip,"Step 03.c: verify the chart tooltip")
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mbar!', 'bar_blue', 'Step 03.d: verify the chart first fill color')
        resobj.verify_legends(['Unit Sales', 'Dollar Sales']  , '#wbody2_f', msg='Step 03.d : Verify legends text')
        utillobj.verify_chart_color('wall2', 'legend-markers!s0!', 'bar_blue', 'Step 03.d: verify the first legend fill color')
        utillobj.verify_chart_color('wall2', 'legend-markers!s1!', 'pale_green', 'Step 03.d: verify the second legend fill color')
        
        
        """
        Step 04: Click on the sixth icon at the top, for Rollup.
        """
        rollobj.click_chart_menu_bar_items("wall2", 5)
        time.sleep(5)
        active_misobj.verify_page_summary('1','10of10records,Page1of1', 'Step 04: Verify Page summary 10of10')
        column=['Product', 'Category', 'Unit Sales','Dollar Sales']
        active_misobj.verify_column_heading('ITableData1', column, "Step 04.a: Verify Column heading of Rollup report")
        utillobj.verify_data_set('ITableData1','I1r','C2071370_Ds02.xlsx',"Step 04.b: Verify all the matching records for rollup report")
        #utillobj.create_data_set('ITableData1','I1r','C2071370_Ds02.xlsx')
        
if __name__ == '__main__':
    unittest.main()
