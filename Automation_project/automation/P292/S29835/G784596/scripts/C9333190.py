"""-------------------------------------------------------------------------------------------
Created on September 11, 2019
@author: Vishnu Priya/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9333190
Test Case Title =  Verify changing output Format and Location
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.report import Report
from common.lib import global_variables
from common.pages.ia_ribbon import IA_Ribbon
import time

class C9333190_TestClass(BaseTestCase):

    def test_C9333190(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        global_var_obj = global_variables.Global_variables()
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        ia_ribbon = IA_Ribbon(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        live_preview_css = "#TableChart_1"
        query_css = "#queryBoxColumn"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
            
        Step1 = """
            STEP 01 : Launch the API to create new Report.
            http://machine:port/{alias}/ia?tool=Report&item=IBFS:/WFC/Repository/P292_S29835/G781455
        """
        report.invoke_report_without_master_file_by_api()
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Select "ibisamp" folder and Select "car.mas" > Click "Open" button.
        """
        utils.select_masterfile_in_open_dialog("ibisamp", "car")
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Double click "CAR" and "SALES" in Data pane.
        """
        report.double_click_on_datetree_item("CAR", 1)
        report.wait_for_visible_text(query_css, "CAR")
        
        report.double_click_on_datetree_item("SALES", 1)
        report.wait_for_visible_text(query_css, "SALES")
        utils.capture_screenshot("03.01", Step3)
        
        Step4 = """
            STEP 04 : Click "Output Location shortcut" in the lower right corner.
            Check the following menu.
        """
        output_location_obj = utils.validate_and_get_webdriver_object("#sbpTargetOutputPanel", "Output Location")
        core_utils.python_left_click(output_location_obj)
        report.wait_for_visible_text("div.bi-menu", "New Tab")
        time.sleep(5)
        
        output_location_content_obj = utils.validate_and_get_webdriver_objects("div.bi-menu table tr", "Output Location content")
        actual_list = []
        for x in output_location_content_obj:
            actual_list.append(x.text)
        msg = "Step 04.01 : Check the following menu."
        expected_list = ['', 'Single Tab  ', 'New Tab  ', 'Single Window  ', 'New Window  ']
        utils.as_List_equal(actual_list, expected_list, msg)
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP 05 : Select "New Window" option.
            Check the "New window" selection option.
        """
        new_window_option_obj = utils.validate_and_get_webdriver_object("div.bi-menu table tr:nth-child(5)", "New window css")
        core_utils.python_left_click(new_window_option_obj)
        time.sleep(3)
        
        selection_obj = utils.validate_and_get_webdriver_object("#sbpTargetOutput", "Selection css")
        actual_result = selection_obj.text
        msg = "Step 05.01 : Check the 'New window' selection option."
        utils.asequal(actual_result, "New Window", msg)
        utils.capture_screenshot("05.01", Step5, expected_image_verify = True)
        
        Step6 = """
            STEP 06 : Click "Output Format shortcut" in the lower right corner.
            Check the following menu.
        """
#         output_format_obj = utils.validate_and_get_webdriver_object("#sbpOutputFormatPanel", "output format css")
#         core_utils.python_left_click(output_format_obj)
#         report.wait_for_visible_text("#HomeFormatTypeMenu", "HTML")
        
        expected_output_list1 = ['HTML', 'HTML Analytic Document', 'PDF', 'PDF Analytic Document', 'Excel (xlsx)', 'PowerPoint (pptx)']
        ia_ribbon.select_or_verify_output_type(launch_point='bottom_tool_bar', selected_format='HTML', expected_output_list1= expected_output_list1, msg1 ="Step06.01 : Check the following menu.")
        utils.capture_screenshot("06.01", Step6, expected_image_verify = True)
        
        Step7 = """
            STEP 07 : Select "HTML Analytic Document" option.
            Check the "HTML Analytic Document" selection option.
        """
        html_analytic_obj = utils.validate_and_get_webdriver_object("#menu_ahtml_btn", "HTML Analytic Document Css")
        core_utils.python_left_click(html_analytic_obj)
        time.sleep(10)
        output_format_obj2 = utils.validate_and_get_webdriver_object("#sbpOutputFormatPanel", "Output format css")
        actual_result = output_format_obj2.text
        msg = "Step 07.01 : Check the 'HTML Analytic Document' selection option."
        utils.asequal(actual_result, "HTML Analytic Document", msg)
        utils.capture_screenshot("07.01", Step7, expected_image_verify = True)
        
        Step8 = """
            STEP 08 : Click "IA" menu and Select "Run" option.
            Check the following Output in a New window.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_new_window()
        report.wait_for_visible_text("#MAINTABLE_wbody0 table[id='ITableData0']", "CAR")
        
        #report.create_html_report_dataset(DATA_SET_NAME1, table_css = "#ITableData0")
        report.verify_html_report_dataset(DATA_SET_NAME1, table_css = "#ITableData0", msg = "Step 08.01 : Check the following Output in a New window.")
        utils.capture_screenshot("08.01", Step8, expected_image_verify = True)
        
        Step9 = """
            STEP 9 : Close the Output window.
        """
        report.switch_to_previous_window()
        report.wait_for_visible_text("#TableChart_1", "CAR")
        utils.capture_screenshot("09.01", Step9, expected_image_verify = True)
        
        Step10 = """
            STEP 10 : Click "IA" menu and Select "New" option.
        """
        report.select_new_from_toptoolbar()
        report.wait_for_visible_text("#splash_options", "Getting")
        utils.capture_screenshot("10.01", Step10)
        
        Step11 = """
            STEP 11 : Select "Build a Report" in the Splash Screen.
        """
        report_build_obj = utils.validate_and_get_webdriver_object("#splash_options_report", "Report build obj")
        core_utils.python_left_click(report_build_obj)
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        utils.capture_screenshot("11.01", Step11)
        
        Step12 = """
            STEP 12 : Select "ibisamp" folder and Select "car.mas" > Click "Open" button.
            Check the following Status bar.
        """
        utils.select_masterfile_in_open_dialog("ibisamp", "car")
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        
        reports_obj = utils.validate_and_get_webdriver_object("#sbpSwitchReportPanel", "Report")
        actual_result = reports_obj.text
        msg = "Step 12.01 : Check the following Status bar."
        utils.asequal("2 Reports", actual_result, msg)
        
        output_format_obj3 = utils.validate_and_get_webdriver_object("#sbpOutputFormat", "Output Format css")
        actual_result = output_format_obj3.text
        msg = "Step 12.02 : Check the following Status bar."
        utils.asequal("HTML", actual_result, msg)
        
        output_tab_obj = utils.validate_and_get_webdriver_object("#sbpTargetOutputPanel", "Output tab css")
        actual_result = output_tab_obj.text
        msg = "Step 12.03 : Check the following Status bar."
        utils.asequal("Single Tab", actual_result, msg)
        utils.capture_screenshot("12.01", Step12, expected_image_verify = True)
        
        Step13 = """
            STEP 13 : Click "2 Reports" shortcut.
            Check the following menu.
        """
        reports_obj = utils.validate_and_get_webdriver_object("#sbpSwitchReportPanel", "Report")
        core_utils.python_left_click(reports_obj)
        report.wait_for_visible_text("div[class='bi-menu'][style*='visibility: inherit']", "Report1")
        
        reports_verify_obj = utils.validate_and_get_webdriver_objects("div[class='bi-menu'][style*='visibility: inherit'] table tr", "Reports verify css")
        actual_list = []
        for x in reports_verify_obj:
            actual_list.append(x.text)
        expected_list = ['', 'Report1  ', 'Report2  ']
        msg = "Step 13.01 : Check the following menu."
        utils.as_List_equal(actual_list, expected_list, msg)
        utils.capture_screenshot("13.01", Step13, expected_image_verify = True)
        
        Step14 = """
            STEP 14 : Select "Report1" option.
            Check the options for "Report 1".
        """
        report1_obj = utils.validate_and_get_webdriver_object("div[class='bi-menu'][style*='visibility: inherit'] table tr:nth-child(2)", "Report1 css")
        core_utils.python_left_click(report1_obj)
        report.wait_for_visible_text("#TableChart_1", "CAR")
        
        reports_obj = utils.validate_and_get_webdriver_object("#sbpSwitchReportPanel", "Report")
        actual_result = reports_obj.text
        msg = "Step 14.01 : Check the following Status bar."
        utils.asequal("2 Reports", actual_result, msg)
        
        output_format_obj3 = utils.validate_and_get_webdriver_object("#sbpOutputFormat", "Output Format css")
        actual_result = output_format_obj3.text
        msg = "Step 14.02 : Check the following Status bar."
        utils.asequal("HTML Analytic Document", actual_result, msg)
        
        output_tab_obj = utils.validate_and_get_webdriver_object("#sbpTargetOutputPanel", "Output tab css")
        actual_result = output_tab_obj.text
        msg = "Step 14.03 : Check the following Status bar."
        utils.asequal("Single Tab", actual_result, msg)
        utils.capture_screenshot("14.01", Step14, expected_image_verify = True)
        
        Step15 = """
            STEP 15 : Click "IA" menu and Select "Close" option.
        """
        report.select_ia_application_menu("close")
        report.wait_for_visible_text("#btnCancel", "Cancel")
        utils.capture_screenshot("15.01", Step15, expected_image_verify = True)
        
        Step16 = """
            STEP 16 : Click "NO" option.
        """
        no_obj = utils.validate_and_get_webdriver_object("#btnNo", "No")
        core_utils.python_left_click(no_obj)
        utils.synchronize_until_element_disappear("#btnNo", report.home_page_short_timesleep)
        utils.capture_screenshot("16.01", Step16, expected_image_verify = True)
        
        Step17 = """
            STEP 17 : Click "IA" menu and Select "Close" option.
        """
        report.select_ia_application_menu("close")
        utils.capture_screenshot("17.01", Step17, expected_image_verify = True)
        
        Step18 = """
            STEP 18 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        utils.capture_screenshot("18.01", Step18)

if __name__ == '__main__':
    unittest.main()