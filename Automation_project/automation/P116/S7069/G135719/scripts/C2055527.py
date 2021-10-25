
'''
Created on July 29, 2016
@author: Gobi/niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7069
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055525
'''
__author__ = "Gobi for Niranjan"
__copyright__ = "IBI"

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from common.lib import utillity


class C2055527_TestClass(BaseTestCase):

    def test_C2055527(self):

        driver = self.driver #Driver reference object created
        Test_Case_ID = 'C2055527'
        
        """Step 01:  Execute the attached repro - 108268.fex"""
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login('108268.fex','S7069','mrid','mrpass')
        time.sleep(10)  
        active_misobj.verify_page_summary('0','5of5records,Page1of1', 'Step 01a: Verify Page summary')
        
        utillobj.verify_data_set('ITableData0','I0r','108268.xlsx',"Step 01:Verify fex data table ")
        
        #utillobj.create_data_set('ITableData0','I0r','108268.xlsx')    
                
        """Step 02: Select SWCB_HRS dropdown and click Rollup ->COUNTRY..""" 
        miscelanousobj.select_menu_items('ITableData0', 1, 'Rollup', 'COUNTRY')
        time.sleep(4)

        """Step 03: Select SWCB_HRS dropdown and click Calculate -> Avg."""
        utillobj.verify_data_set('ITableData1','I1r',"C2055527_Ds01.xlsx","Step 03: Verify table of active pop up") 
#         utillobj.create_data_set('ITableData1','I1r',"C2055527_Ds01.xlsx")
      
        miscelanousobj.select_menu_items('ITableData1', 1, 'Calculate','Avg')
        time.sleep(4)
        
        """Step 04: Verify the Average Value generated from SWCB_HRS column."""
        
        miscelanousobj.verify_calculated_value(3, 2, "Total Avg 12.4960", True, "Step 02: Expect to see Total Avg 12.4960", table_id='ITableData1') 
        

if __name__ == '__main__':
    unittest.main()

