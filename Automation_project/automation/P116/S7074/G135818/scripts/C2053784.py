'''
Created on Sep 06, 2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053784

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_chart_rollup, visualization_resultarea,\
    active_tools
from common.lib import utillity


class C2053784_TestClass(BaseTestCase):

    def test_C2053784(self):

        """
        Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.a: Verify Page summary 107of107')
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        active_misobj.verify_column_heading('ITableData0', column_list, "Step 01.b: Verify the Run Report column heading")
        
        """
        Step 02: Select State > Chart > Bar > Category
            Verify that 'State By Category' pop up window for the Bar chart is displayed.
            Verify that chart toolbar is present with all the options. See attached screenshot.
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Column','Category')
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053784_Actual_Step02', image_type='actual')
        rollobj.verify_arChartMenu("wall1", "Step 02.a Verify the Chart Menu bar labels displayed on Run chart")
        x_val_list=['Coffee', 'Food', 'Gifts']
        y_val_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels('wall1', x_val_list, y_val_list, "Step 02.b")
        expected_tooltip=['State: 30','X: Coffee']
        active_misobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mbar', expected_tooltip,  "Step 02.c: verify the chart tooltip with fill color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mbar','cerulean_blue',"Step 02.d: Verify Chart piebevel Color ")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02.d: Verify the dialog title')
        
        #Legend
        resobj.verify_riser_legends('wall1', ['State'],"Step 02.e: Verify Chart Legend")
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
