
'''
Created on Aug 9, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050546
Test CaseName = AHTML_CACHE:Filter Calculation-`Filtered Sum 0(0%)`displayed (103440)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050546_TestClass(BaseTestCase):

    def test_C2050546(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(25) #Intializing common implicit wait for throughout the test
        
        """
        Step 01: Execute the 103440.fex 
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('103440.fex','S7068','mrid','mrpass')
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18 records')
        column=['COUNTRY', 'DEALER_COST','RETAIL_COST']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Verify Column heading")
        utillobj.verify_data_set('ITableData0','I0r','103440.xlsx',"Step 01.3: Verify entire Data set of 103440.fex ")
                
        """
        Step 02: click on DEALER_COST dropdown menu and select Calculate -> SUM
        """ 
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', '1', 'Calculate', 'Sum')
        time.sleep(10)
        active_misobj.verify_calculated_value(2,2, "Total Sum 143,794", True, "Step 02: Verify Total Sum 143,794")
        
        """
        Step 03: Once again click on DEALER_COST dropdown menu and select FILTER option
        """
        active_misobj.select_menu_items('ITableData0', '1', 'Filter','Not equal')
        
        """
        Step 04: Select the filter condition as 'Not Equal' and value as 4,631. Click FILTER button
        """
        time.sleep(5)
        filterobj.create_filter(1, 'Not equal', value1='4,631')
        filterobj.filter_button_click('Filter')
        """Verify Filtered Sum is displayed when filter is applied to Total Sum"""
        active_misobj.verify_page_summary('0','17of18records,Page1of1', 'Step 04.1: Verify Page summary 18of18 records')
        filterobj.verify_filter_selection_dialog(True,'Step 04.2: Verify filter menu DEALER_COST appears',['DEALER_COST','Not equal','4,631'])
        active_misobj.verify_calculated_value(2,2, "Filtered Sum 139,163(96.78%)\nTotal Sum 143,794", True, "Step 04.3: Verify Filtered Sum 139,163(96.78%)\nTotal Sum 143,794")
        utillobj.verify_data_set('ITableData0','I0r','C2050546_Ds01.xlsx',"Step 04.4: Verify data set after filter")
         
        
if __name__ == '__main__':
    unittest.main()

