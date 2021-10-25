'''
Created on Sep 15, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055519
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest

class C2055519_TestClass(BaseTestCase):

    def test_C2055519(self):
        
        """
            Step 01: Execute the attached fex.
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("108268.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 01.1: Execute the 108268.fex")
        column_list=['COUNTRY','CAR','SWCB_HRS','SWCB_DOL']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 108268.fex')
        utillobj.verify_data_set('ITableData0', 'I0r', '108268.xlsx','Step 01.3: Verify data set')
        
        """
        Step 02: Select SWCB_HRS dropdown and click Rollup ->COUNTRY.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Rollup','COUNTRY')
        miscelanousobj.verify_popup_title('wall1', 'SWCB_HRS by COUNTRY', 'Step 02: Verify popup appears')
        
        """
        Step 03: Select SWCB_HRS dropdown and click Calculate -> Avg.
        """

        miscelanousobj.select_menu_items('ITableData1', 1, 'Calculate','Avg')

        """
        Step 04: Verify the Average Value generated from SWCB_HRS column.
        """
        miscelanousobj.verify_calculated_value(3, 2, 'Total Avg 12.4960', True, 'Step 04: Verify the Average Value generated from SWCB_HRS column', table_id="ITableData1")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()