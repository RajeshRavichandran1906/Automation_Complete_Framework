'''
Created on Sep 9, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055503
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest

class C2055503_TestClass(BaseTestCase):

    def test_C2055503(self):
        
        """
            Step 01: Execute 105103.fex form repro
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("140811.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 140811.fex")
        column_list=['COUNTRY','CAR','MODEL','SEATS']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 140811.fex')
        
        
        """
        Step 02: Verify it doesn't throws any error message and displayed the output properly.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', '140811.xlsx','Step 02: Verify it doesnt throws any error message and displayed the output properly')
        
        
if __name__ == '__main__':
    unittest.main()         