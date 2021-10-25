'''
Created on Aug 18, 2016

@author: Niranjan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7070&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055764
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
import time

class C2055764_TestClass(BaseTestCase):

    def test_C2055764(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        """
        1. Run the attached act-80.fex. Note that under the first column Compute_1 the first value is $0.00. 
        """
        utillobj.active_run_fex_api_login("act-80.fex", "S7070", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01.1: Execute the act-80.fex and Verify the Report Heading')
        column_list=['Compute_1', 'COUNTRY', 'CAR', 'RETAIL_COST', 'DEALER_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Execute the act-80.fex and Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055764_Ds01.xlsx', 'Step 01.3: Execute the act-80.fex and Verify the entire data, first column Compute_1 the first value is $0.00 .')
        """
        2. Click on the Compute_1 column dropdown and select Sort Ascending. The value that was $0.00 should still be $0.00. 
        The erroneous behavior is that the value is converted to $.00, without the leading zero. 
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Sort Ascending')
        time.sleep(5)
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2055764_Ds02.xlsx', 'Step 02.1: After Sort Ascending verify entire table and make sure the value that was $0.00 should still be $0.00.')
        
if __name__ == '__main__':
    unittest.main()
        
