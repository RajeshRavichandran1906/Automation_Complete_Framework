'''
Created on Sep 6, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053795
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_chart_rollup
from common.lib import utillity
import unittest
import time


class C2053795_TestClass(BaseTestCase):

    def test_C2053795(self):
        
        """
            Step 01: Execute the AR-RP-001A.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        utillobj.active_run_fex_api_login("AR-RP-001A.fex", "S7074", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01.1: Execute the AR-RP-001A.fex")
        column_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report AR-RP-001A.fex')
        
        """
        STep 02: Select Dollar Sales > Chart > Pie > Category
        """
        miscelanousobj.select_menu_items('ITableData0', 5, 'Chart','Pie','Category')
        miscelanousobj.verify_popup_appears('wall1', 'Dollar Sales by Category', 'Step 02.1: Verify that Dollar Sales By Category pop up window for the Bar chart is displayed')
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053795_pic01', image_type='actual_images')
        miscelanousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mwedge', ['Coffee','Dollar Sales: 17.2M','37.3% of 46.2M'],  'Step 02.2: Verify chart tooltip')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 02.2b: Verify Chart piebevel Color ")
        rollupobj.verify_arChartMenu('wall1', 'Step 02.3: Verify that chart toolbar is present with all the options')
        
        """
        Step 03: Click aggregation icon from SUM(default state) to AVG
        """
        rollupobj.select_aggregate_function('wall1', 0, 'Avg', verify=True)
        
        time.sleep(5)
        element1 = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element1, 'C2053795_pic02', image_type='actual_images')
        miscelanousobj.verify_active_chart_tooltip('wall1', 'riser!s0!g0!mwedge', ['Coffee','Dollar Sales: 574K','42.2% of 1.4M'],  'Step 03.1: Verify chart tooltip')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 03.2b: Verify Chart piebevel Color ")
if __name__ == '__main__':
    unittest.main() 
        
        
        
        
        
        
        
        
        
