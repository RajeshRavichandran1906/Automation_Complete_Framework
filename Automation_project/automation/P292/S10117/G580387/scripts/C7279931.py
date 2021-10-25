"""-------------------------------------------------------------------------------------------
Created on June 18, 2019
@author: Baasha/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268782
Test Case Title =  Auto Drill with Group created from a hierarchy field after setting Auto Drill 
-----------------------------------------------------------------------------------------------"""

import unittest, time
from common.lib import utillity
from common.lib import global_variables
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C7279931_TestClass(BaseTestCase):

    def test_C7279931(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
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
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/IA-Shell.fex&tool=Report
        """
        report.edit_fex_using_api_url("IA-Shell")
        report.wait_for_visible_text(report_css, "Sale")
        utils.wait_for_page_loads(report.home_page_long_timesleep) #firefox its required
        
        """
            STEP 2 : Click "Format tab" and Click "Auto Drill"option.
        """
#         time.sleep(10) #firefox- giving time for different page elements locating
        report.select_ia_ribbon_item("Format", "auto_drill")
        time.sleep(10)
        
        """
            STEP 3 : Right click "Store Business Region" in the canvas and Click "Create Group" option.
        """
        report.select_preview_report_context_menu(25, "Create Group...")
        report.wait_for_visible_text("#dynaGrpsCancelBtn", "Cancel")
        
        """
            STEP 4 : Enter "BUSINESS_GROUP" in Field Textbox and Multi select both" North America" and "South America".
        """
        report.group_dialog().enter_values_in_field_textbox("BUSINESS_GROUP")
        report.group_dialog().select_multiple_fields(["North America", "South America"])
        
        """
            STEP 5 : Click "Group" and Click "OK" button.
        """ 
        report.group_dialog().click_group_button()
        time.sleep(3) #added time for group to be processed
        report.group_dialog().click_ok_button()
        
        """
            STEP 6 : Right click "BUSINESS_GROUP" in the canvas and Click "Change Title" option..
        """
        report.select_preview_report_context_menu(25, "Change Title...")
        report.wait_for_visible_text("div[id^='BiOptionPane']", "Cancel")
 
        """
            STEP 7 : Enter "Store,Business,Group" and Click "OK" button.
        """
        title_textbox = self.driver.find_element_by_css_selector("[id^='BiDialog'] input.bi-text-field")
        title_textbox.clear()
        title_textbox.send_keys("Store,Business,Group")
        click_button = self.driver.find_element_by_xpath("//div[contains(@id, 'BiDialog')]//div[normalize-space() = 'OK']")
        core_utils.left_click(click_button)
        
        """
            STEP 8 : Click "Run" in toolbar.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.switch_to_frame(frame_css="body > iframe")
        report.wait_for_visible_text(report_frame_css, "Sale")
        
        """
            STEP 08.01 : Check the following Output.
        """
        #report.create_html_report_dataset(DATA_SET_NAME1)
        report.verify_html_report_dataset(DATA_SET_NAME1, "STEP 08.01 : Check the following Output")
        
        """
            STEP 9 : Click on "North America" and "South America" Group.
            STEP 09.01 : Check "Drill down to Store Business Region" is displayed.
            STEP 10 : Click "Drill down to Store Business Region".
        """
        expected_tooltip = ["Drill down to Store Business Region"]
        msg = "Step 10.01 : Click Drill down to Store Business Region"
        report.select_report_autolink_tooltip_runtime("table[summary='Summary']", 12, 1,"Drill down to Store Business Region", verify_tooltip=expected_tooltip, msg=msg, verify_type="asin")
        report.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "North America and South America")
        
        """
            STEP 10.01 : Check the Breadcrumb and following Output.
        """
#         report.create_html_report_dataset(DATA_SET_NAME2)
        report.verify_html_report_dataset(DATA_SET_NAME2, "STEP 10.01 : Check the Breadcrumb and following Output.")
        
        """
            STEP 11 : Click on "North America".
            STEP 11.01 : Check both "Drill up to Store Business Group" and "Drill down to Store Business Sub Region" are displayed.
        """
        expected_tooltip = ["Go up to Store Business Group", "Drill down to Store Business Sub Region"]
        msg = "STEP 11.01 : Check both 'Drill up to Store Business Group' and 'Drill down to Store Business Sub Region' are displayed."
        report.select_report_autolink_tooltip_runtime("table[summary='Summary']", 5, 1,"Drill down to Store Business Sub Region", verify_tooltip= expected_tooltip, msg=msg, verify_type="asin" )
        report.wait_for_visible_text("table[summary]>tbody>tr:nth-child(1)", "North America")
        
        """
            STEP 12 : Click "IA" menu and Select "Save As" option.
            STEP 13 : Enter "C7279931" in Title textbox and Click "Save" button.
        """
        report.switch_to_default_content()
        report.save_as_from_application_menu_item("C7279931", target_table_path="P292_S10117->G580387")
        
        """
            STEP 14 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()

        """
            STEP 15 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S10117/G580387/C7279931.fex&tool=Report
        """
        report.edit_fex_using_api_url("C7279931")
        report.wait_for_visible_text(report_css, "Sale")
        utils.wait_for_page_loads(report.home_page_long_timesleep) #firefox its required
        
        """
            STEP 16 : Click "Format tab".
        """
        report.switch_ia_ribbon_tab('Format')
        report.wait_for_visible_text(format_css, "Features")

        """
            STEP 16.01 : Check" Auto Drill" is still selected.
        """
        report.verify_ribbon_item_selected("format_auto_drill", "14.01")
        
        """
            STEP 17 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
if __name__ == '__main__':
    unittest.main()