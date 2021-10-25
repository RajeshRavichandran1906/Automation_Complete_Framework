'''
Created on Sep 1, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7078&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053845
'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_tools
from common.lib import utillity
from selenium.webdriver import ActionChains


class C2053845_TestClass(BaseTestCase):

    def test_C2053845(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053845'
        """
        Step 01: Execute the attached repro - Pivot.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        pivobj=active_pivot_comment.Active_Pivot_Comment(self.driver)
        toolobj=active_tools.Active_Tools(self.driver)
        utillobj.active_run_fex_api_login('Pivot.fex','S7078','mrid','mrpass')      
        misobj.verify_page_summary('0','1000of1000records,Page1of18', 'Step 01.1: Verify Page summary 1000of1000')
        column=['Store Code', 'Unit Price', 'Product', 'Store Code', 'Vendor ID', 'Unit Price']
        misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Dataset title")        
        utillobj.verify_data_set('ITableData0','I0r','Pivot.xlsx',"Step 01.3: Verify Dataset of Pivot.fex")        
        
        """
        Step 02: Select the first D10.2 Unit Price column and then pick Pivot(Cross Tab). 
        Select the first ALPHA Store Code field as the Group By field and then Product as the Across column.
        """
        time.sleep(5)
        misobj.select_menu_items('ITableData0', 0, 'Pivot (Cross Tab)','Store Code','Product')        
        utillobj.verify_data_set('ITableData0','I0r','C2053845_Ds01.xlsx',"Step 02.1: Verify Dataset ALPHA Store Code field as the Group By field and then Product as the Across")
       

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
