'''
Created on Nov 1, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203733

verify conditional styling works fine with cache ON

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2203733_TestClass(BaseTestCase):

    def test_C2203733(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute the 103365.fex with cache ON command
        SET WEBVIEWER=ON

        """
        #Verify WGERMAN in red color font as per conditional style
        
        utillobj.active_run_fex_api_login("103365.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(5)
        
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01.1: Execute the act-886-report.fex and Verify the Report Heading')
        
        column_list=['COUNTRY', 'CAR']
        
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act-886-report.fex and Verify the column heading')
        
        utillobj.verify_data_set('ITableData0', 'I0r', '103365.xlsx', 'Step 01.3: Execute the 97564.fex and Verify the entire data')
        
        #utillobj.create_data_set('ITableData0', 'I0r', '103365.xlsx')

        miscelanousobj.verify_cell_property("ITableData0", 9, 0, 'W GERMANY', 'Step 01: Verify WGERMAN in red color font as per conditional style',text_color='red')
        
        
            
        
if __name__ == "__main__":
    unittest.main()