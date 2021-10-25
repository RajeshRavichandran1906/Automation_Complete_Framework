'''
Created on Jul 04, 2017
@author: Nasir
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2204936_TestClass(BaseTestCase):

    def test_C2204936(self):
        utillobj = utillity.UtillityMethods(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Execute C46036.fex
        """
        utillobj.active_run_fex_api_login("46036.fex", "S7074", 'mrid', 'mrpass')
        miscelaneousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01a: Execute the 46036.fex and Verify the Report Heading')
        column_list=['Category','Product ID','Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01b: Execute the 46036.fex and Verify the column heading')
        value = utillobj.validate_and_get_webdriver_object("[id^='THEAD_0_'] span", 'span').text.strip()
        utillobj.asequal('ABC COMPANY CONFIDENTIAL', value, 'Step 01c: Verify that the procedure contains a custom heading, ABC COMPANY CONFIDENTIAL')
        
if __name__ == '__main__':
    unittest.main()