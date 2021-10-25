'''
Created on Aug 24, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053872

'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_chart_rollup
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators


class C2053872_TestClass(BaseTestCase):

    def test_C2053872(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053872'
        """
            Step 01: Execute the 131586.fex
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(25) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        utillobj.active_run_fex_api_login('131586.fex','S7076','mrid','mrpass')      
        active_misobj.verify_page_summary('0','10of10records,Page1of1', 'Step 01.1: Verify Page summary 10of10')
        column=['COUNTER','COL_1','COL_2']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of 131586.fex")
        utillobj.verify_data_set('ITableData0','I0r','131586.xlsx',"Step 01.3: Verify 131586.fex dataset")        
        
        """
        Step 02: Click on Col1 column and select Rollup>Counter
        """
        active_misobj.select_menu_items('ITableData0', 1, 'Rollup','COUNTER')
        time.sleep(5)
        column=['COUNTER','COL_1']
        active_misobj.verify_column_heading('ITableData1', column, "Step 02.1: Verify Column heading after rollup")
        active_misobj.verify_page_summary('1','10of10records,Page1of1', 'Step 02.2: Verify Page summary 10of10')
        """Verify nodata values are displayed with '.'"""
        utillobj.verify_data_set('ITableData1','I1r','C2053872_Ds01.xlsx',"Step 02.3:Verify nodata values are displayed with .")
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
