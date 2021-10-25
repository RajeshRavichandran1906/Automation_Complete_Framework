'''
Created on Feb 06, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2227198

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
import time


class C2227198_TestClass(BaseTestCase):

    def test_C2227198(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 1. Execute the attached repro- 73192543.fex
        
        """
        utillobj.active_run_fex_api_login("73192543.fex", "S7072", 'mrid', 'mrpass')
        utillobj._validate_page((By.ID,'ITableData0'))
        
        miscelanousobj.verify_page_summary(0, '4of4records,Page1of1', 'Step 01.a: Verified the Page Summary')
        column_list=['COUNTRY', 'CAR','MODEL','SEATS','TEST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Expect top see the following report with the last column labelled TEST')
        utillobj.verify_data_set('ITableData0','I0r','C2227198_DS01.xlsx','Step 01.c : Data set verified')
        
        
        """
        Step 2. From the dropdown for TEST, select Calculate/SUM
        
        """
        
        miscelanousobj.select_menu_items('ITableData0', 4, 'Calculate','Sum')
        time.sleep(2)
        miscelanousobj.verify_page_summary(0, '4of4records,Page1of1', 'Step 02.a: Verified the Page Summary')
        column_list=['COUNTRY', 'CAR','MODEL','SEATS','TEST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.b: Verify Column Heading')
        miscelanousobj.verify_calculated_value(2, 5, "Total Sum 210,273.415000",True,"Step 02.c : The correct total of the TEST column is 210,273.415000")
        utillobj.verify_data_set('ITableData0','I0r','C2227198_DS02.xlsx','Step 02.d : Data set verified')
        

if __name__=='__main__' :
    
    unittest.main()