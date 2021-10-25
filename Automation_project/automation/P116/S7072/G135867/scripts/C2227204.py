import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C2227204_TestClass(BaseTestCase):

    def test_C2227204(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 1. Execute the AR-AHTML-001.fex
        Expect to see the missing data represented by the SET NODATA=MISSING value.
        """
        utillobj.active_run_fex_api_login("act-179jschart.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '3of3records,Page1of1', 'Step 01.a: Verify the Page Summary')
        column_list=['COL1', 'SALES']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.b: Verify Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','act-179jschart.xlsx',"Step 01.c: Verify Data Set")
    
if __name__ == '__main__':
    unittest.main()