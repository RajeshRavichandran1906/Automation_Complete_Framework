'''
Created on Sept'06

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053786
TestCase Name = Verify Rollup table is generated
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,  active_chart_rollup, visualization_resultarea
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2053786_TestClass(BaseTestCase):

    def test_C2053786(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = '2053786'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7074','mrid','mrpass')      
        time.sleep(8)      
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """Step 02:Select State > Chart > Pie > Category"""
        
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')
        time.sleep(5)
        
        #Verify that 'State By Product' pop up window for the chart is displayed.
        
        active_misobj.verify_popup_title('wall1', 'State by Category', 'Step 02: Verify that State By Product pop up window for the chart is displayed')
        
  
        """Step 03: Click Rollup icon from the toolbar"""
        #Verify Pie chart converted to table format where selected columns are displayed.  
        
        rollupobj.click_chart_menu_bar_items('wall1',5)
        time.sleep(5)
        parent_css="#IWindowBody1 tr:nth-child(3) td:nth-child(1)"
        resobj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        
        #utillobj.create_popup_data_set('wall1', 'ITableData1', 'C2053786_Ds01.xlsx')        
        
        utillobj.verify_popup_data_set('wall1', 'ITableData1', 'C2053786_Ds01.xlsx', 'Step 03:Verify Pie chart converted to table format where selected columns are displayed. ')
        
       


if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
