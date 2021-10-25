'''
Created on Jun 11, 2018

@author: BM13368
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity

class C5751533_TestClass(BaseTestCase):

    def test_C5751533(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        fex_name="91551.fex"
        Test_Case_ID="C5751533"
        
        """
            Step 01 : Run 91551.fex from following URL
            
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP116%252FS7215&BIP_item=91551.fex
        """
        utillobj.active_run_fex_api_login(fex_name, "S7215", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "ALFA ROMEO", 65)
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute the 108268.fex")
        column_list=['CAR', 'BODYTYPE', 'DEALER_COST']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.2: Verify all columns listed on the report 143860.fex')
#         utillobj.create_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds01.xlsx')
        utillobj.verify_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds01.xlsx', "Step 01:03:Verify dataset")
        
        
        """
            Step 02 : In report from Car field click dropdown and select calculate->Count/Distinct
            Step 03 : Verify report gets displayed properly without throwing IE error or getting hung.
        """
        miscelanousobj.select_menu_items('ITableData0', 0, 'Calculate','Count')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Total Cnt 18", 15)
#         utillobj.create_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds02.xlsx')
        utillobj.verify_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds02.xlsx', "Step 02:01:Verify dataset")
        
        miscelanousobj.select_menu_items('ITableData0', 0, 'Calculate','Distinct')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Total Cnt Dist 10", 15)
#         utillobj.create_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds03.xlsx')
        utillobj.verify_data_set("ITableData0", 'I0r', Test_Case_ID+'Ds03.xlsx', "Step 02:02:Verify dataset")
        
if __name__ == "__main__":
    unittest.main()