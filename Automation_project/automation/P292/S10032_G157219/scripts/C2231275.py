'''
Created on Nov 8, 2017

@author: BM13368
Testcase_Name : Verify Report mode Join, Define and Compute
Testcase_ID : http://172.19.2.180/testrail/index.php?/cases/view/2231275
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, ia_run, define_compute, ia_ribbon, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2231275_TestClass(BaseTestCase):

    def test_C2231275(self):
        
        Test_Case_ID = "C2231275"
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomp_obj=define_compute.Define_Compute(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        """ 
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/EMPDATA&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 02 : Select "Data" > "Join" > Click "Add New" > TRAINING.MAS > "Open"
        """
        ia_ribbonobj.create_join("training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 02:01: Verify join link color")
        
        """
            Step 03: Click "Filter" button > Verify filter is EMPDATA.EMPDATA.PIN Equal To TRAINING.TRAINING.PIN > Click "OK"
        """
        ia_ribbonobj.select_join_menu_buttons("filter")
        time.sleep(2)
        ia_ribbonobj.verify_join_filter_Condition("EMPDATA.EMPDATA.PIN Equal to TRAINING.TRAINING.PIN", "Step 03:01: Verify filter condition")
        ia_ribbonobj.close_filter_dialog(btn='ok')
        time.sleep(1)
        ia_ribbonobj.select_join_menu_buttons("ok")
        
        """
            Step 04 : Click "Add New" > LOCATOR.MAS > "Open"
        """
        ia_ribbonobj.create_join("locator")
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 04:01: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 04:02: verify Join link color 'red' for second join")
        
        """
            Step 05: Click "Filter" button > Verify filter is EMPDATA.EMPDATA.PIN Equal To LOCATOR.LOCATOR.PIN > Click "OK"
            Step 06: Verify the following is displayed in the Join window
        """
        ia_ribbonobj.select_join_menu_buttons("filter")
        time.sleep(2)
        ia_ribbonobj.verify_join_filter_Condition("EMPDATA.EMPDATA.PIN Equal to LOCATOR.LOCATOR.PIN", "Step 05:01: Verify filter condition")
        time.sleep(1)
          
        """
            Step 07: Click OK to save Join
        """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        time.sleep(1)
        ia_ribbonobj.select_join_menu_buttons("ok")
        
        """
            Step 08 : Click "Define" in the Data Tab
        """
        defcomp_obj.invoke_define_compute_dialog('define')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 09 : Type NEWSITE for Field and A25 for Format
            Step 10 : Double-click "SITE" field to add it to the Define expression
        """
        defcomp_obj.enter_define_compute_parameter("NEWSITE", 'A25', 'SITE', 1)
        
        """
            Step 11: Click OK > Verify "NEWSITE" and Joined fields in the Data pane 
        """
        defcomp_obj.close_define_compute_dialog('ok')
        
        """
            Step 12: Double-click fields "NEWSITE", "LASTNAME", "COURSECODE", "EXPENSES"
        """
        metaobj.datatree_field_click("NEWSITE", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("COURSECODE", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(5)
        
        """
            Step 13: Click "Compute" in the Data Tab
        """
        defcomp_obj.invoke_define_compute_dialog('compute')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
            Step 14: Type NEWEXPENSES for the Field name
        """
        defcomp_obj.enter_define_compute_parameter("NEWEXPENSES", 'D12.2', 'EXPENSES', 1)
        
        """
            Step 15: Double-click "EXPENSES" from the Fields List > Then type * .10 using dialog's keypad
        """
        defcomp_obj.select_calculation_btns(btn_series="mult->dot->one->zero")
          
        """
            Step 16: Click OK > Verify Preview
        """
        defcomp_obj.close_define_compute_dialog('ok')
        time.sleep(4)
        coln_list = ['NEWSITE', 'LASTNAME', 'COURSECODE', 'EXPENSES', 'NEWEXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 19:01: Verify column titles")
        
        """
            Step 17: Select "Single Window" in the output location shortcut in the Status bar
        """
        ia_ribbonobj.select_report_output_window('Single Window')
        time.sleep(2)
        
        """
            Step 18: Click "Run"
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        time.sleep(9)
        utillobj.switch_to_window(1)
        time.sleep(12)
        
        """
            Step 19: Verify the report is displayed in a new window with expected output
        """
#         ia_runobj.create_table_data_set("html table", "C2231275_Ds01.xlsx", desired_no_of_rows=5)
        ia_runobj.verify_table_data_set("html table", "C2231275_Ds01.xlsx", "Step 19:02 verify preview data")
        
        """
            Step 20: Close the output window
        """
        driver.close()
        time.sleep(2)
        
        """
            Step 21: Click "IA" > "Save" > Enter Title = "C2231275" > Click "Save"
        """
        utillobj.switch_to_window(0)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 22: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
            Step 23: Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231275.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
            Step 24: Verify Report on "Live Preview"
        """
        coln_list = ["NEWSITE", "LASTNAME", "COURSECODE",'EXPENSES','NEWEXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 24:01: Verify column titles")
        
        """
            Step 25: Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
    if __name__ == "__main__":
        unittest.main()      
        
        
        