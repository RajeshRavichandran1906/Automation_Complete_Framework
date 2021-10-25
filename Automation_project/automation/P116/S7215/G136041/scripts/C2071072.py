'''
Created on Sep 20, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2071072
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest

class C2071072_TestClass(BaseTestCase):

    def test_C2071072(self):
        
        """
            Step 01: Execute the attached repro - act-73.fex
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("act-73.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', "Step 01.1: Execute the act-73.fex")
        column_list=['COUNTRY','CLS_MKT_CAP_AMT']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report act485t.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', 'act-73.xlsx','Step 01.3: Expect to see the Active Report, displaying Packed decimal numbers for each of 5 Countries')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()