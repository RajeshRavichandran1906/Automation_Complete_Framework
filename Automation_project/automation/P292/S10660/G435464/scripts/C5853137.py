'''
Created on May 31, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5853137
TestCase Name = API > Launch InfoMini Application
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,ia_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase

class C5853137_TestClass(BaseTestCase):

    def test_C5853137(self):
        
        Test_Case_ID = "C5853137"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)  
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)  
        iarun=ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch Report mode with IA API:
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        time.sleep(2)   
 
        """
        Step 02: Add field "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#queryTreeWindow tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'Product,Category', 50)
        time.sleep(5)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 1, 7, 1, Test_Case_ID+'_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1',2,1,7,1,Test_Case_ID+'_Ds01.xlsx','Step 02 : Verify report')
 
        """
        Step 03: Select Format Tab > Click "InfoMini"
        """
        ribbonobj.select_ribbon_item('Format', 'infomini')
        time.sleep(3)
        
        """
        Step 04: Click "Save" > save as "C5853137" > Click "Save" in the dialog
        """
        time.sleep(6)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID) 
        time.sleep(5)
        utillobj.infoassist_api_logout()
        
        """
        Step 05: Launch InfoMini:
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C5853137.fex
        """
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10660_infoassist_2", 'mrid', 'mrpass')       
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        
        """
        Step 06:Verify InfoMini Application is launched
        """
        utillobj.verify_object_visible("div[id^='saveButton']", True, "Step 06.1:Verify InfoMini Application save button")
        utillobj.verify_object_visible("div[id^='showFexSettingsButton']", True, "Step 06.2:Verify InfoMini Application show FexSettings Button")
        utillobj.verify_object_visible("div[id^='runButton']", True, "Step 06.3:Verify InfoMini Application run Buttonn")
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
#         iarun.create_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx",'Step 07: Verify HTML format report After Run')
        
        """
        Step 07:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
 
if __name__ == '__main__':
    unittest.main() 

