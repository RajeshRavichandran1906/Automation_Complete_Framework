'''
Created on Dec 3, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2235445
TestCase Name : Verify Aggregation Function
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase


class C2235445_TestClass(BaseTestCase):

    def test_C2235445(self):
        
        Test_Case_ID = "C2235445"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Double click "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        ia_resultobj.verify_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds01.xlsx", "Step 02:01: Verofy report dataset")
        
        """ 
            Step 03:Click on Cost of Goods" in the Query pane > Click "Aggregation" in the Field Tab ribbon
        """
        metaobj.querytree_field_click("Cost of Goods", 1, 0)
        time.sleep(1)
        ribbonobj.select_ribbon_item('Field', "Aggregation")
        time.sleep(1)
        
        """ 
            Step 04:Select Aggregation > Average
        """
        utillobj.select_or_verify_bipop_menu("Average")
        time.sleep(2)
        """ 
            Step 05:Verify AVE prefix displayed in the Query pane and Preview
        """
        metaobj.verify_query_pane_field("Sum", "AVE.Cost of Goods", 1, "Step 05:01:")
        ia_resultobj.verify_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds02.xlsx", "Step 05:02: Verify report dataset")
        
        """ 
            Step 06:Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        
        """ 
            Step 07:Verify output
        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds03.xlsx", "Step 07:01: Verify report data at runtime")
          
        """
            Step 08:Click "Save" > save as "C2235445" > Click Save
        """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        """ 
            Step 09:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 10:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235445.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 11:Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field("Sum", "AVE.Cost of Goods", 1, "Step 11:01:")
        ia_resultobj.verify_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds02.xlsx", "Step 11:02: Verify report data at preview")
        
        """ 
            Step 12:Click on Cost of Goods" in the Query pane > Select Aggregation > Percent
        """
        metaobj.querytree_field_click("AVE.Cost of Goods", 1, 0)
        time.sleep(1)
        ribbonobj.select_ribbon_item('Field', "Aggregation")
        time.sleep(1) 
        utillobj.select_or_verify_bipop_menu("Percent")
        """ 
            Step 13:Verify Query pane and Preview display PCT prefix
        """
        metaobj.verify_query_pane_field("Sum", "PCT.Cost of Goods", 1, "Step 13:01:")
        ia_resultobj.verify_across_report_data_set("TableChart_1", 2, 2, 7, 2, Test_Case_ID+"_Ds04.xlsx", "Step 13:01: Verofy report dataset")
        
        """ 
            Step 14:Logout and do not save changes:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == "__main__":
    unittest.main()