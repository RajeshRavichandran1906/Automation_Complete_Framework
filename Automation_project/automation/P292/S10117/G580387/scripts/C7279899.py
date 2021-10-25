"""-------------------------------------------------------------------------------------------
Created on June 13, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268774
Test Case Title =  Breadcrumbs - Have two hierarchy sorts from different dimensions - HTML format 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase
from common.lib import global_variables,utillity, core_utility

class C7279899_TestClass(BaseTestCase):

    def test_C7279899(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        global_var_obj = global_variables.Global_variables()
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        report_css = "#TableChart_1"
        format_css = "#FormatTab"
        report_frame_css = "table[summary]"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        DATA_SET_NAME3 = case_id + '_DataSet_03.xlsx'
        
        """
            STEP 1 : Reopen the saved fex using API link:
        """
        report_obj.edit_fex_using_api_url("IA-Shell")
        report_obj.wait_for_visible_text(report_css, "Sale")
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep)
        
        """
            STEP 2 : Click "Format tab" and Click "Auto Drill"option
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
        
        """
            STEP 3 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        core_utils.switch_to_frame(frame_css="body > iframe", timeout = report_obj.home_page_long_timesleep) # Giving more time to switch frame
#         report_obj.switch_to_frame(frame_css="body > iframe")
        report_obj.wait_for_visible_text(report_frame_css, "Sale")
        
        """
            STEP 4 : Click on "Stereo Systems" under "North America" and Click "Drill down to Product Subcategory".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 16, 2, "Drill down to Product Subcategory")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)","Stereo Systems")
        
        """
            STEP 04.01 : Check Breadcrumb appears as below.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1, "STEP 04.01 : Check Breadcrumb appears as below")
         
        """
            STEP 5 : Click on "North America" and Click "Drill down to Store Business Sub Region".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 5, 1, "Drill down to Store Business Sub Region")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "North America")
        
        """
            STEP 05.01 : Check Breadcrumb appears as below.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME2)
        report_obj.verify_html_report_dataset(DATA_SET_NAME2, "STEP 05.01 : Check Breadcrumb appears as below")
        
        """
            STEP 6 : Click on "Home Theater Systems" under "West" and Click "Drill down to Model".
        """
        report_obj.select_report_autolink_tooltip_using_actionchains(43, 2, "Drill down to Model")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "Home Theater Systems")
        
        """
            STEP 06.01 : Check Breadcrumb appears as below.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME3)
        report_obj.verify_html_report_dataset(DATA_SET_NAME3, "STEP 06.01 : Check Breadcrumb appears as below")
        report_obj.switch_to_default_content()
        
        """
            STEP 7 : Click "IA" menu and Select "Save As" option.
            STEP 8 : Enter "C7279899" in Title textbox and Click "Save" button.
        """
        report_obj.save_as_from_application_menu_item("C7279899", target_table_path="P292_S10117->G580387")

        """
            STEP 9 : Logout
        """
        report_obj.api_logout()
        
        """
            STEP 10 : Reopen the saved fex using API link
        """
        report_obj.edit_fex_using_api_url("C7279899")
        report_obj.wait_for_visible_text(report_css, "Sale")
        
        """
            STEP 11 : Click "Format tab".
        """
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep)
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 11.01 : Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "11.01")
        
        """
            STEP 12 : Logout
        """
        report_obj.api_logout()
    
if __name__ == '__main__':
    unittest.main()