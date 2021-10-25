'''
Created on Sept'06

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053786
TestCase Name = Verify Rollup table is generated
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_chart_rollup, visualization_resultarea
from common.lib import utillity

class C2053785_TestClass(BaseTestCase):

    def test_C2053785(self):
        """
            TESTCASE VARIABLES
        """
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass')      
        time.sleep(8)      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """Step 02:Select State > Chart > Pie > Category"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(5)
        
        
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02: Verify that State By Product pop up window for the chart is displayed')
    
#         Verify that chart toolbar is present with following options:
#         - New icon (dropdown)
#         - Bar
#         - Pie
#         - Line
#         - Scatter
#         - Rollup
#         - Advanced chart
#         - Original chart
#         - Freeze icon
#         - Aggregation icon See attached screenshot.
        #Menu
        rollupobj.verify_arChartMenu('wall1',"Step 02.1: Verify the chart Menu")
        
  
        """Step 03: Click Scatter icon from the toolbar"""
        #Verify Pie chart converted to Scatter chart. See attached screenshot. 
        
        rollupobj.click_chart_menu_bar_items('wall1',4)
        time.sleep(6)
        
        #screenshot
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053785_Actual_Step03', image_type='actual')
        
        expected=['State','X: Coffee','Y: 30']
        
        active_misobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mmarker',expected,"Step 03a: Verify correct/selected chart type is displayed ")
        time.sleep(2)
        
        #label
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '10', '20', '30', '40', '50']
        resobj.verify_riser_chart_XY_labels('wall1', expected_xval_list, expected_yval_list, 'Step 03: Verify the label values in scatter chart-mandatory verification')

        #title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 03.3: Verify that State By Product pop up window for the chart is displayed for top 5')
 
 
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
