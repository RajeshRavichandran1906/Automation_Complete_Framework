'''
Created on Sep 27, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203736

verify is max value on numeric field contain comma

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity

import time

class C2203736_TestClass(BaseTestCase):

    def test_C2203736(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute the 92330.fex
        """
        
        #Verify AHTML report is displayed.
        
        utillobj.active_run_fex_api_login("92330.fex", "S7072", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-886-report.fex and Verify the Report Heading')
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        column_list=['CAR','RETAIL_COST', 'DEALER_COST']
        
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2:Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '92330.xlsx', 'Step 01.3: Execute the 92330.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '92330.xlsx')

        """
        Step 02:Select calculation "MAX" option from Retail_cost drop down 
        """
        
        miscelanousobj.select_menu_items("ITableData0", "1", "Calculate","Max")
        time.sleep(6)
            
        """Step 03: verify max value get generated with comma"""
        
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 03.1:Verify the Report Heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '92330.xlsx', 'Step 03.2:verify report')
        
        miscelanousobj.verify_calculated_value(2, 2, 'Total Max 58,762',True, "Step 03: verify max value get generated with comma")
        
        
        
            
        
if __name__ == "__main__":
    unittest.main()