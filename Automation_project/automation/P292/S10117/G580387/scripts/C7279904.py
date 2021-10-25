"""-------------------------------------------------------------------------------------------
Created on June 17, 2019
@author: magesh/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268774
Test Case Title =  Breadcrumbs - Have two hierarchy sorts from different dimensions - HTML format 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib import utillity
from common.wftools import report
from common.lib import global_variables
from common.lib.basetestcase import BaseTestCase

class C7279904_TestClass(BaseTestCase):

    def test_C7279904(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        global_var_obj = global_variables.Global_variables()
      
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        report_css = "#TableChart_1"
        format_css = "#FormatTab"
        report_frame_css = "table[summary]"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        """
            STEP 1 : Reopen the saved fex using API link:
        """
        report_obj.edit_fex_using_api_url("IA-Shell")
        report_obj.wait_for_visible_text(report_css, "Sale")
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
        
        """
            STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
        report_obj.select_ia_ribbon_item("Format", "auto_drill")
    
        """
            STEP 02.01 : Verify auto Drill button is selected as below.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "02.01")
    
        """
            STEP 3 : Click "Run" in toolbar.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.switch_to_frame(frame_css="body > iframe")
        report_obj.wait_for_visible_text(report_frame_css, "Sale")
        
        """
            STEP 4 : Click on "2016" in the "ACROSS" labels and Click "Drill down to Sale Year/Quarter".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 1, 2, "Drill down to Sale Year/Quarter")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "2016")
        
        """
            STEP 5 : Click on "2016 Q4" and Click "Drill down to Sale Year/Month".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Drill down to Sale Year/Month")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "2016 Q4")
        
        """
            STEP 6 : Click on "2016/12" and Click "Drill down to Sale Day".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Drill down to Sale Day")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "2016/12")
        
        """
            STEP 06.01 : Check the Breadcrumb and following Output.
        """
#         report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1, "STEP 06.01 : Check Breadcrumb appears as below")
        
        """
            STEP 7 : Click on "2016/12/31" and Click "Drill up to Sale Year/Month".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Go up to Sale Year/Month")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "2016 Q4")
        
        """
            STEP 8 : Click on "2016/12" and Click "Drill up to Sale Year/Quarter".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Go up to Sale Year/Quarter")
        report_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "2016")

        """
            STEP 9 : Click on "2016 Q4" and Click "Drill up to Sale Year".
        """
        report_obj.select_report_autolink_tooltip_runtime("table[summary='Summary']", 3, 2, "Go up to Sale Year")
        report_obj.wait_for_visible_text(report_frame_css, "Sale")
        
        """
            STEP 09.01 : Check the following output.
        """
        #report_obj.create_html_report_dataset(DATA_SET_NAME2)
        report_obj.verify_html_report_dataset(DATA_SET_NAME2, "STEP 09.01 : Check Breadcrumb appears as below")
        report_obj.switch_to_default_content()
        
        """
            STEP 10 : Click "IA" menu and Select "Save As" option.
            STEP 11 : Enter "C7279904" in Title textbox and Click "Save" button.
        """
        report_obj.save_as_from_application_menu_item("C7279904", target_table_path="P292_S10117->G580387")
     
        """
            STEP 12 : Logout
        """
        report_obj.api_logout()
        
        """
            STEP 13 : Reopen the saved fex using API link
        """
        report_obj.edit_fex_using_api_url("C7279904")
        report_obj.wait_for_visible_text(report_css, "Sale")
        utils.wait_for_page_loads(report_obj.home_page_long_timesleep) #firefox its required
    
        """
            STEP 14 : Click "Format tab".
        """
        report_obj.switch_ia_ribbon_tab('Format')
        report_obj.wait_for_visible_text(format_css, "Features")
        
        """
            STEP 14.01 : Check" Auto Drill" is still selected.
        """
        report_obj.verify_ribbon_item_selected("format_auto_drill", "14.01")
        
        """
            STEP 15 : Logout
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()