'''
Created on Aug 8, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203641
Test Case name = AHTML:Highlight Row- wrong row after sorting performed (Act-437)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity


class C2203641_TestClass(BaseTestCase):

    def test_C2203641(self):
        """
            Step 01: Execute the attached repro - Act-437.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_mis= active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.active_run_fex_api_login("Act-437.fex", "S7068", 'mrid', 'mrpass')
        header_css="table[id='IWindowBody0'] .arGridBar table>tbody table tbody tr td:nth-child(2)"
        utillobj.synchronize_with_visble_text(header_css, "18of18records,Page1of1", 45, 1)
        active_mis.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Verify Page Summary of Act-437.fex")
        active_mis.verify_column_heading('ITableData0', ['COUNTRY','CAR','MODEL','SALES'], "Step 01.2: Verify Column heading of ACT-437.fex")
        utillobj.verify_data_set('ITableData0','I0r','Act-437.xlsx', "Step 01.3: Verify Act-437.fex dataset")
         
        """
        Step 02: Select Sort descending from CAR column dropdown.
        """
        active_mis.select_menu_items('ITableData0', 1, 'Sort Descending')
        utillobj.verify_data_set('ITableData0','I0r','C2050566_Ds01.xlsx', "Step 02: Verify sorted descending using dataset")
        
        """
        Step 03: Left click on 'TR7" from model column and select Highlight row option.
        """
        active_mis.select_field_menu_items('ITableData0', 3, 2,'Highlight Row',original_rownum=0)
        
        """
        Step 04: Verify whether exact row is highlighted.
        """   
        utillobj.verify_data_set('ITableData0','bgcolor','C2050566_Ds02.xlsx',"Step 04: Verify dataset highlighted with navy color", color='navy')
         
        
if __name__ == '__main__':
    unittest.main()