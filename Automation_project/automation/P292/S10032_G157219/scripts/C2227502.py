'''
Created on Nov 19, 2017

@author: BM13368
TestCase_Name : Verify InfoMini request with Report mode 
Testcase_ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227502
'''
import unittest,time, re
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_run
from common.lib import utillity

class C2227502_TestClass(BaseTestCase):

    def test_C2227502(self):
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227502'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
            Step 01 : Launch IA Chart mode:
            http://machine:port/ibi_apps/ia?tool=Chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """
            Step 02 : Double click "CAR", "SALES".
        """
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        """
            Step 03 : Select "Format" > "InfoMini" (dropdown) (Destination Group) > "Resources/Field Tab".
        """
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Resources/Field Tab")
        time.sleep(2)
        """
            Step 04 : Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        """
            Step 05 : Verify InfoMini application is displayed in a new window.
        """
#         ia_run_obj.create_table_data_set("table[summary='Summary']", 'C2227502_Ds01.xlsx', desired_no_of_rows=5)
        ia_run_obj.verify_table_data_set("table[summary='Summary']", "C2227502_Ds01.xlsx" , 'Step 05:01: Verify report dataset')
        """
            Step 06 : Dismiss InfoMini application.
        """
        driver.close()
        """
            Step 07 : Click "IA" > "Save".
            Step 08 : Enter Title = "C2227502".
            Step 09 : Click "Save".
        """
        utillobj.switch_to_window(0)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 10 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 11 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227502.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        """
            Step 12 : Select Format > Verify "Infomini" button is selected
        """
        ribbonobj.switch_ia_tab("Format")
        time.sleep(6)
        infomini_css=self.driver.find_element_by_css_selector("#FormatApplicationRibbonEnable")
        status=True if bool(re.match('.*menu-button-checked.*', infomini_css.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 12:01: Verify infomini is selected.")
        
        """
            Step 13 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
if __name__ == "__main__":
    unittest.main()