'''
Created on Aug 8, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203640
Test Case name = AHTML: 'Hightlight Value' twice changes sort order for BY HIGHEST (ACT-484)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2203640_TestClass(BaseTestCase):

    def test_C2203640(self):
        """
            Step 01: Execute the attached repro - act484.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_mis= active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("act484.fex", "S7068", 'mrid', 'mrpass')
        header_css="table[id='IWindowBody0'] .arGridBar table>tbody table tbody tr td:nth-child(2)"
        utillobj.synchronize_with_visble_text(header_css, "18of18records,Page1of1", 45, 1)
        active_mis.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary of act484.fex")
        active_mis.verify_column_heading('ITableData0', ['COUNTRY','CAR','RETAIL_COST','DEALER_COST'], "Step 01.2: Verify Column heading of act-484.fex")
        utillobj.verify_data_set('ITableData0','I0r','act-484.xlsx', "Step 01.3: Verify act-484.fex dataset")
         
        """
        Step 02: Hover the mouse over row1, on the value 5063;
        left click, select Highlight Value.
        """
        active_mis.select_field_menu_items('ITableData0', 0, 3,'Highlight Value')
        """The first row should be highlighted. The sort order should be the same."""
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2050610_Ds01.xlsx',"Step 02.1: Verify 5063 dataset highlighted with navy color", color='navy')
        utillobj.verify_data_set('ITableData0','I0r','act-484.xlsx', "Step 02.2: Verify sort order is same after Highlight")
        
        """
        Step 03: Hover the mouse over row2, on the value 5800;
        left click, select Highlight Value.
        """
        active_mis.select_field_menu_items('ITableData0', 1, 3,'Highlight Value')
        """The second row should be highlighted. The sort order should be the same."""
        utillobj.verify_data_set_old('ITableData0','bgcolor','C2050610_Ds02.xlsx',"Step 03.1: Verify 5800 dataset highlighted with navy color", color='navy')
        utillobj.verify_data_set('ITableData0','I0r','act-484.xlsx', "Step 03.2: Verify sort order is same after Highlight")
        
        
        
if __name__ == '__main__':
    unittest.main()