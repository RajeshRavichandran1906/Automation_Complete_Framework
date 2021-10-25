'''
Created on Aug 23, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053777
TestCase Name = Verify move to bottom icon moves pagination to the bottom
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, active_chart_rollup
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2053777_TestClass(BaseTestCase):

    def test_C2053777(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = '2053777'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_chart = active_chart_rollup.Active_Chart_Rollup(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass')      
              
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        active_misobj.verify_column_heading('ITableData0', ['Category','Product ID','Product','State','Unit Sales','Dollar Sales'], "Step 01.1: Verify Column heading of AR-RP-001.fex")
        utillobj.verify_data_set('ITableData0','I0r','C2053777_Ds_01.xlsx',"Step 01.3: Verify entire Data set in Page 1")
        
        #utillobj.create_data_set('ITableData0','I0r','C2053777_Ds_01.xlsx')
        """Step 02: Select State > Chart > Pie > Category"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(6)
        
        # Verify that 'State By Category' pop up window for the chart is displayed.
        # Verify that chart toolbar is present with following options:
        # - New icon (dropdown)
        # - Bar
        # - Pie
        # - Line
        # - Scatter
        # - Rollup
        # - Advanced chart
        # - Original chart
        # - Freeze icon
        # - Aggregation icon See attached screenshot and save the fex.      
        
        active_chart.verify_arChartMenu('wall1', 'Step 02: Verify that chart toolbar is present with following all options')
        
    
        
        
        
        
        
        
        
        
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
