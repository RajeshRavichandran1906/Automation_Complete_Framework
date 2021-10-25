'''
Created on Jun 12, 2019

@author: Varun/Prasanth
Testcase Name : Auto drill for non-hierarchy field used as a sorting field in report
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279871

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools import report
from common.lib import global_variables

class C7279871_TestClass(BaseTestCase):
    
    def test_C7279871(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        global_var_obj=global_variables.Global_variables()
        
        """
        Test case variables
        """
        case_id=global_var_obj.current_test_case
        
        """
        STEP 1: Reopen the saved fex using API link:
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(fex_name="IA-Shell")
        report_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2: Double click "Brand" in Data pane.
        """
        report_obj.double_click_on_datetree_item("Brand", 1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Brand")
        
        """
        STEP 3 : Click "Format" tab and Click "Auto Drill" button.
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """
        STEP 4: Click Run in toolbar
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.switch_to_frame("iframe")
        report_obj.wait_for_visible_text("table[summary]", "Brand" )
        
        """
        STEP 4.01 Expected: Check"Brand" doesn't have drill down links.
        """
        brand_columns = self.driver.find_elements_by_css_selector("table[summary]>tbody>tr>td:nth-child(3)")[1:49] #
        status = False not in [column.find_elements_by_css_selector("a[href]")==[] for column in brand_columns]
        UtillityMethods.asequal(self, True, status, "Step 04.01 : Verify 'Brand' doesn't have drill down links.")
        
        """
        STEP 5: Click "IA" menu and Click "Save As" option.
        """
        """
        STEP 6: Enter "C7279871" in Tittle textbox and Click "Save" button.
        """
        report_obj.switch_to_default_content()
        report_obj.save_as_from_application_menu_item(case_id)
        
        """
        STEP 7: Click "IA" menu and Select "Close" option.
        """
        report_obj.select_ia_application_menu("close")
        
        """
        STEP 8: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
        """
        STEP 9:Reopen the saved fex using API link
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279871.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url(case_id)
        report_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 10:Click "Format" tab
        """
        report_obj.switch_ia_ribbon_tab("Format")
        
        """
        STEP 10.01 Expected : Check "Auto Drill" button is active.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "10.01")
        
        """
        STEP 11: Click "IA" menu and Select "Close" option.
        """
        report_obj.select_ia_application_menu("close")
        
        """
        STEP 12: Logout
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()
    
        