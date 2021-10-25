'''
Created on Nov 30, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231274
TestCase Name : Verify Alert Assist save and restore 
'''
import unittest, time
from common.pages import visualization_metadata, ia_resultarea, wf_alert_assist, visualization_ribbon, visualization_resultarea
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2231274_TestClass(BaseTestCase):

    def test_C2231274(self):
        
        Test_Case_ID = "C2231274"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        alert_obj=wf_alert_assist.Wf_Alert_Assist(self.driver)
        ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
    
        """
            Step 01:Launch Alert Assist with car:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=Alert&master=ibisamp/car
        """
        utillobj.infoassist_api_login('Alert','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        alert_title=("Alert" in driver.title)
        utillobj.asequal(True, alert_title, "Step 01:01: Verify Alert page is displayed")
        
        """
            Step 02:Right-click "Test" component > "New" > "WebFOCUS Test"
        """
        alert_obj.select_aa_tree_item('Test', 1,'New', 'WebFOCUS Test')
        utillobj.switch_to_window(1)
        
        """ 
            Step 03:Select CAR.MAS
        """ 
        utillobj.select_masterfile_in_open_dialog("ibisamp", "car")
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """    
            Step 04:Double click "COUNTRY", "CAR" and "SALES"
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        """ 
            Step 05:Verify "Live Preview"
        """
        #ia_resultobj.create_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", "Step 05:01: Verify preview")
        """ 
            Step 06:Click "IA" > "Exit" > Click "Yes" to save
        """
        ribbon_obj.select_tool_menu_item('menu_exit')
        ia_resultobj.ia_exit_save("Yes")
        """
            Step 07:Right-click "Result" component > New > New Report > Report
        """
        utillobj.switch_to_window(0)
        alert_obj.select_aa_tree_item('Result', 1,'New', 'New Report', 'Report')
        utillobj.switch_to_window(1)
           
        """ 
            Step 08:Select CAR.MAS
        """
        utillobj.select_masterfile_in_open_dialog("ibisamp", "car")
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """ 
            Step 09:Double-click "MODEL" and "SEATS"
        """
        time.sleep(4)
        metaobj.datatree_field_click("MODEL", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SEATS", 2, 1)
        time.sleep(4)    
        """ 
            Step 10:Click "IA" > "Exit" > Click "Yes" to save
        """
        ribbon_obj.select_tool_menu_item('menu_exit')
        ia_resultobj.ia_exit_save("Yes")
        """ 
            Step 11:Click "AA" menu > "Save" > save as "C2231274" > Click Save
        """
        utillobj.switch_to_window(0)
        alert_obj.select_aa_tool_menu_item("menu_save_as")
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        """ 
            Step 12:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        """ 
            Step 13:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231274.fex&tool=Alert
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'alert', 'S10032_infoassist_4', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        """ 
            Step 14:Verify tool is launched
        """
        alert_title=("Alert" in driver.title)
        utillobj.asequal(True, alert_title, "Step 14:01: Verify Alert page is displayed")
        
        """ 
            Step 15:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()