'''
Created on Feb 02, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227195

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By



class C2227195_TestClass(BaseTestCase):

    def test_C2227195(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 1. Execute the attached repro- act-163.fex
        
        """
        utillobj.active_run_fex_api_login("act-163.fex", "S7072", 'mrid', 'mrpass')
        utillobj._validate_page((By.ID,'ITableData0'))
        miscelanousobj.verify_page_summary(0, '41of41records,Page1of1', 'Step 01.a: Verified the Page Summary')
        column_list=['PIN', 'LASTNAME','DEPT','SALARY','HIREDATE']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','act-163.xlsx','Step 01.c : Data set verified and The HIREDATE column data in DD-Mon-YYYY format ')
        

if __name__=='__main__' :
    
    unittest.main()