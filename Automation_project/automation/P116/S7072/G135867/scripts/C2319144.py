'''
Created on Nov 13, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2319144
TestCase Name = AHTML: Webviewer/Arcachemode SET command errors/bad output(ACT-299).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2319144_TestClass(BaseTestCase):

    def test_C2319144(self):
        
        Test_Case_ID="C2319144"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)

        """   
            Step 01: Execute the attached repro - act-299.fex.
        """
        utillobj.active_run_fex_api_login("act-299.fex", "S7072", 'mrid', 'mrpass')
        element_css="#IWindowBody0  span[title='Move to Bottom'] img"
        utillobj.synchronize_with_number_of_element(element_css, expected_number=1, expire_time=30)
        
        """
            Step 02:Expect to see the following Active report.Verify the correct page information, 
                    showing 4317 records and 76 Pages.
        """
        miscelaneousobj.verify_page_summary('0','4317of4317records,Page1of76', 'Step 01.1: Verify Page summary')        
        miscelaneousobj.verify_column_heading('ITableData0', ['Category','Product ID','Product','State','Unit Sales','Dollar Sales'], "Step 01.2: Verify Column heading of AR-RP-001.fex")
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID+'_Ds_01.xlsx', desired_no_of_rows=20)
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds_01.xlsx',"Step 01.3: Verify  Data set in Page 1")
        
if __name__ == '__main__':
    unittest.main()