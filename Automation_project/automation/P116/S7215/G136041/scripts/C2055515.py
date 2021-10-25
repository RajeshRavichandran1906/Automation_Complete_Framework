'''
Created on Sep 14, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055515
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest,time


class C2055515_TestClass(BaseTestCase):

    def test_C2055515(self):
        
        """
            Step 01: Execute the fex attached.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("92382.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '12of12records,Page1of1', "Step 01.1: Execute the 92382.fex")
        column_list=['CURR_SAL', 'HIRE_DATE', 'EFFECT_DATE', 'LAST_NAME', 'LAST_NAME']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
#         utillobj.verify_data_set('ITableData0', 'I0r', '92382.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Select Calculate option using any dropdown from report.
        Step 03: Select Min from the calculate option.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Calculate','Min')
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 2, 'Total Min 80/06/02', True, 'Step 03: Verify Calculated value')
        
        """
        STep 04: Redo the 2nd step.
        Step 05: Select Max from the calculate option.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Calculate','Max')
        time.sleep(8)
        miscelanousobj.verify_calculated_value(4, 2, 'Total Min 80/06/02', True, 'Step 05.1: Verify Calculated value')
        time.sleep(4)
        miscelanousobj.verify_calculated_value(4, 3, 'Total Max 84/09/01', True, 'Step 05.2: Verify Calculated value')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()