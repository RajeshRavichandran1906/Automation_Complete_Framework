'''
Created on Sep 13, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055506
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import unittest

class C2055506_TestClass(BaseTestCase):

    def test_C2055506(self):
        
        """
            Step 01: Execute 110336b.fex form repro
        """
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.active_run_fex_api_login("110336b.fex", "S7215", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '288of288records,Page1of15', "Step 01.1: Execute the 110336b.fex")
        column_list=['City','Date','Budget Dollars','Budget Units','TOTAL']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report')
        utillobj.verify_data_set('ITableData0', 'I0r', '110336b.xlsx','Step 01.3: Verify data set')
        """
        Step 02: Select Visualize from Row total column.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Visualize')
        
        """
        Step 03: Verify Visualize is displayed when selected from row total column.
        """
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'black', 'Step 03: Verify Visualize is displayed when selected from row total column')
        
        
if __name__ == '__main__':
    unittest.main()               
        
        
        