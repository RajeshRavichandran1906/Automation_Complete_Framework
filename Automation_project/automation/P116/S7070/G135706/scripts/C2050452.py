'''
Created on Aug 17, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050452
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2050452_TestClass(BaseTestCase):

    def test_C2050452(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Execute the attached repro - 143512.fex
        """
        utillobj.active_run_fex_api_login("143512.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the AR-RP-001.fex and Verify the Report Heading')
        column_list=['CAR','COUNTRY','SEATS']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the AR-RP-001.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','143512.xlsx','Step 01.3: Expect to see the  Active Report')
        time.sleep(3)
        """
        Step 02: From the drop down for Seats, locate the Hide column selection.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Hide Column')
        
        """
        Step 03: Expect to see the Seats column no longer displayed.
        """
        utillobj.verify_data_set('ITableData0','I0r','C2050452_Ds01.xlsx','Step 03: Expect to see the Seats column no longer displayed')
        """
        Step 04: Click either the CAR or the COUNTRY column, and locate the 'Show Columns->Show All option.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 1, 'Show Columns','Show All')
        
        """
        Step 05: Expect to see the Seats column returned to the report.
        """
        utillobj.verify_data_set('ITableData0','I0r','143512.xlsx','Step 05: Expect to see the Seats column returned to the report')
        
if __name__ == '__main__':
    unittest.main()           
              
        

        
        
        