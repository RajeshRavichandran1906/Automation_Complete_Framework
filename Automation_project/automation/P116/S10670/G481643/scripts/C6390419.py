'''
Created on Jun 29, 2018

@author: Bhagavathi

Test Case =  http://172.19.2.180/testrail/index.php?/cases/view/6390419&group_by=cases:section_id&group_id=481643&group_order=asc
TestCase Name = AHTML_CACHE:Calculate on aphanumeric fls-IE ERROR - 91551
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_run
from common.lib import utillity

class C6390419_TestClass(BaseTestCase):

    def test_C6390419(self):
        
        Test_Case_ID="C6390419"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        
        fex_name="91551.fex"
        
        """
            Step 01 : Login to WebFOCUS environment using the below link:
            http://machine:port/{alias}
            Step 02 : Run the 91551.fex using the below API link:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S10032/G481643&BIP_item=91551.fex
        """  
        utillobj.active_run_fex_api_login(fex_name, "S10670", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "ALFA ROMEO", 65)
        
        miscelaneous_obj.verify_page_summary(0, '18of18records,Page1of1', 'Step 01:01: Verify the Report Heading')
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+"_Ds01.xlsx")
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+"_Ds01.xlsx","Step 01:02: Verify entire Data set in Page 1")
        
        """
            Step 03:In report from Car field click dropdown and select calculate->Count/Distinct
        """
        miscelaneous_obj.select_menu_items('ITableData0', 0, 'Calculate', 'Count')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Total Cnt 18", 15)
        
        miscelaneous_obj.verify_page_summary(0, '18of18records,Page1of1', 'Step 03:01: Verify the Report Heading')
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+"_Ds02.xlsx")
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+"_Ds02.xlsx","Step 03:02: Verify entire Data set in Page 1")
        
        """
            Step 04:Verify report gets displayed properly without throwing IE error or getting hanged.
        """
        miscelaneous_obj.select_menu_items('ITableData0', 0, 'Calculate', 'Distinct')
        utillobj.synchronize_with_visble_text("#ITableData0 tr:nth-child(2) td:nth-child(1)", "Total Cnt Dist 10", 15)
        
        miscelaneous_obj.verify_page_summary(0, '18of18records,Page1of1', 'Step 04:01: Verify the Report Heading')
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+"_Ds03.xlsx")
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+"_Ds03.xlsx","Step 04:02: Verify entire Data set in Page 1")
        
        
        """
            Step 05:Launch below IA API to logout.
            http://machine:port/alias/service/wf_security_logout.jsp
        """
            
if __name__ == '__main__':
    unittest.main()