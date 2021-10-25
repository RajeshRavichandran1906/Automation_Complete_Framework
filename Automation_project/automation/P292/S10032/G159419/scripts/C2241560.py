'''
Created on May 04, 2018

@author: Magesh 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2241560
TestCase Name = API > Run > Existing FEX
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase

class C2241560_TestClass(BaseTestCase):

    def test_C2241560(self):
        
        Test_Case_ID = "C2241560"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        iarun=ia_run.IA_Run(self.driver)
        
        """       
        Step 01:Launch Report mode with IA API:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02:Add field "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        resobj.wait_for_property(parent_css, 1, string_value='Product,Category', with_regular_exprestion=True,expire_time=50)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 1, 7, 1, Test_Case_ID+'_DataSet_01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,1,7,1,Test_Case_ID+'_DataSet_01.xlsx','Step 02 : Verify report')
        
        """
        Step 03:Click "Save" > save as "C2241560" > Click "Save" in the dialog
        """
        time.sleep(6)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID) 
        time.sleep(5)
        utillobj.wf_logout()
        
        """
        Step 04:Run saved request using API:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2241560.fex
        """
        time.sleep(5)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_infoassist_5', 'mrid', 'mrpass')
        parent_css="table[summary='Summary']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(5)
               
        """
        Step 05:Verify output is displayed
        """
#         iarun.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx",'Step 05: Verify HTML format report After Run') 
       
        """
        Step 06:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main() 