'''
Created on Sep 2, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053782

'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, \
    active_chart_rollup, visualization_resultarea
from common.lib import utillity

class C2053782_TestClass(BaseTestCase):

    def test_C2053782(self):
        
        """
        Test case Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
       
        """
        Step 01: Execute the AR-RP-001.fex
        """
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7074','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.01: Verify Page summary 107of107')
        
        """
        Step 02: Select State > Chart > Pie > Category
        Verify that 'State By Category' pop up window for the Pie chart is displayed (default) 
        Verify that chart toolbar is present with following options: 
        - New icon (dropdown) 
        - Bar
        - Pie 
        - Line 
        - Scatter 
        - Rollup 
        - Advanced chart 
        - Original chart 
        - Freeze icon 
        - Aggregation icon See attached screenshot.
        """
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 02.01: Verify Chart piebevel Color")
        time.sleep(5)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 02.02: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 02.03: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02.04: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 02.05: Verify the chart Menu")
         
if __name__ == '__main__':
    unittest.main()