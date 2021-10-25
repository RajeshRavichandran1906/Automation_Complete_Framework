"""-------------------------------------------------------------------------------------------
Created on September 12, 2019
@author: Vishnu Priya/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9335822
Test Case Title =  Verify activating Document mode from Home Tab
-----------------------------------------------------------------------------------------------"""
import unittest, time
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables 

class C9335822_TestClass(BaseTestCase):

    def test_C9335822(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        global_var_obj = Global_variables()
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        live_preview_css = "#TableChart_1"
        query_css = "#queryBoxColumn"
        cancel_css = "#IbfsOpenFileDialog7_btnCancel"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        Step1 = """
            STEP 01 :  Launch the API to create new Report with EMPLOYEE.
            http://machine:port/{alias}/ia?is508=false&tool=report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S29835/G781455
        """
        report.invoke_ia_tool_using_new_api_login(master = "ibisamp/employee")
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        utils.capture_screenshot("02.01", Step1)
        
        Step2 = """
            STEP 02 : Double click "EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY" in Data pane.
            Check the Live preview.
        """
        report.double_click_on_datetree_item("EMP_ID", 1)
        report.wait_for_visible_text(query_css, "EMP_ID")
        
        report.double_click_on_datetree_item("LAST_NAME", 1)
        report.wait_for_visible_text(query_css, "LAST_NAME")
        
        report.double_click_on_datetree_item("CURR_SAL", 1)
        report.wait_for_visible_text(query_css, "CURR_SAL")
        
        report.double_click_on_datetree_item("SALARY", 1)
        report.wait_for_visible_text(query_css, "SALARY")
        
        #report.create_acrossreport_data_set_in_preview("TableChart_1", 1, 4, 12, 4, DATA_SET_NAME1)
        report.verify_across_report_data_set_in_preview("TableChart_1", 1, 4, 12, 4, DATA_SET_NAME1, "Step 02.01 : Check the Live preview.")
        utils.capture_screenshot("02.01", Step2, expected_image_verify = True)
        
        Step3 = """
            STEP 03 : Click "Document" icon under Home tab.
            Check the Report Mode is converted to Document Mode.
        """
        report.select_ia_ribbon_item("Home", "Document")
        
        report.wait_for_visible_text('#iaCanvasCaptionLabel', 'Document')
        report.wait_for_visible_text("div#TableChart_1", "EMP_ID")
        #report.create_acrossreport_data_set_in_preview("canvasContainer #TableChart_1", 1, 4, 12, 4, DATA_SET_NAME2)
        report.verify_across_report_data_set_in_preview("canvasContainer #TableChart_1", 1, 4, 12, 4, DATA_SET_NAME2, "Step 03.01 : Check the Report Mode is converted to Document Mode.")
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)
        
        Step4 = """
            STEP 04 : Click "HTML Analytic Document" and Select "PDF" format.
        """
        report.change_output_format_type("pdf")
        report.wait_for_visible_text('#HomeFormatType', "PDF")
        utils.capture_screenshot("04.01", Step4)
        
        Step5 = """
            STEP 05 : Click "Save" in toolbar Enter "C9335822" and Click "Save" button.
        """
        report.save_report_from_toptoolbar()
        report.wait_for_visible_text(cancel_css, "Cancel")
        
        report.save_file_in_save_dialog('C9335822')
        utils.synchronize_until_element_disappear(cancel_css, report.home_page_short_timesleep)
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : Click "Run" from toolbar.
            Check it generated the PDF document.
        """
        report.run_report_from_toptoolbar()
        time.sleep(5)
        report.switch_to_frame()
        time.sleep(15)
        
        if Global_variables.browser_name == "chrome":
            pdf_obj = utils.validate_and_get_webdriver_object("embed[src]", "PDF css")
            actual_result = pdf_obj.get_attribute("type")
            expected_result = "application/pdf"
            msg = "Step 06.01 : Check it generated the PDF document."
            utils.asin(expected_result, actual_result, msg)
        else:
            pdf_obj = utils.validate_and_get_webdriver_object("#viewer", "PDF css")
            actual_result = pdf_obj.is_displayed()
            msg = "Step 06.01 : Check it generated the PDF document."
            utils.asequal(actual_result, True, msg)
            
        report.switch_to_default_content()
        utils.capture_screenshot("06.01", Step6)
        
        Step7 = """
            STEP 07 : Close the Run window.
        """
        close_button_obj = utils.validate_and_get_webdriver_object("#resultAreaWindowManager div[class*='window-close-button']", "Close button css")
        core_utils.python_left_click(close_button_obj)
        time.sleep(15)
        utils.capture_screenshot("07.01", Step7)
        
        Step8 = """
            STEP 08 : Click "IA" menu and Select "Close" option.
        """
        report.select_ia_application_menu("close")
        report.wait_for_visible_text("#TableChart_1", "EMP_ID")
        utils.capture_screenshot("08.01", Step8)
        
        Step9 = """
            STEP 09 : Click "IA" menu and Select "Close" option.
            Check the following Warning message.        
            """
#         report.close_ia_without_save()
        report.select_ia_application_menu("close")
        report.wait_for_visible_text("#btnCancel", "Cancel")
        
        warning_popup_obj = utils.validate_and_get_webdriver_object("#saveAllDlg", "Warning popup")
        actual_result = warning_popup_obj.text
        msg = "Step 09.01 : Check the following Warning message."
        utils.asin("Save Changes to 'Report1'?", actual_result, msg)
        utils.capture_screenshot("09.01", Step9, expected_image_verify = True)
        
        Step10 = """
            STEP 10 : Click "No" button.
            """
        no_obj = utils.validate_and_get_webdriver_object("#btnNo", "No")
        core_utils.python_left_click(no_obj)
        utils.capture_screenshot("10.01", Step10)

        Step11 = """
            STEP 11 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        utils.capture_screenshot("11.01", Step11)
        
        Step12 = """
            STEP 12 : Run the saved fex from BIP using API
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P292_S29835/G781455&BIP_item=C9335822.fex
            Check it generated the PDF document.
        """
        report.run_fex_using_api_url(folder_name = "P292_S29835/G781455", fex_name = "C9335822", mrid = "mrid", mrpass = "mrpass", run_table_css = "body")
        time.sleep(20)
        
        if Global_variables.browser_name == "chrome":
            pdf_obj = utils.validate_and_get_webdriver_object("body embed", "PDF css")
            actual_result = pdf_obj.get_attribute("type")
            expected_result = "application/pdf"
            msg = "Step 12.01 : Check it generated the PDF document."
            utils.asin(expected_result, actual_result, msg)
        else:
            pdf_obj = utils.validate_and_get_webdriver_object("#viewerContainer", "PDF css")
            actual_result = pdf_obj.is_displayed()
            msg = "Step 12.01 : Check it generated the PDF document."
            utils.asequal(actual_result, True, msg)
        utils.capture_screenshot("12.01", Step12, expected_image_verify = True)
        
        Step13 = """
            STEP 13 : Logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        utils.capture_screenshot("13.01", Step13)
        
        Step14 = """
            STEP 14 : Launch the API to create new Report with EMPLOYEE.
            http://machine:port/{alias}/ia?is508=false&tool=report&master=ibisamp/employee&item=IBFS:/WFC/Repository/P292_S29835/G781455
        """
        report.invoke_ia_tool_using_new_api_login(master = "ibisamp/employee")
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        utils.capture_screenshot("14.01", Step14)
        
        Step15 = """
            STEP 15 : Double click "EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY" in Data pane.
        """
        report.double_click_on_datetree_item("EMP_ID", 1)
        report.wait_for_visible_text(query_css, "EMP_ID")
        
        report.double_click_on_datetree_item("LAST_NAME", 1)
        report.wait_for_visible_text(query_css, "LAST_NAME")
        
        report.double_click_on_datetree_item("CURR_SAL", 1)
        report.wait_for_visible_text(query_css, "CURR_SAL")
        
        report.double_click_on_datetree_item("SALARY", 1)
        report.wait_for_visible_text(query_css, "SALARY")
        
        #report.create_acrossreport_data_set_in_preview("TableChart_1", 1, 4, 12, 4, DATA_SET_NAME1)
        report.verify_across_report_data_set_in_preview("TableChart_1", 1, 4, 12, 4, DATA_SET_NAME1, "Step 15.01 : Check the Live preview.")
        utils.capture_screenshot("15.01", Step15)
        
        Step16 = """
            STEP 16 : Click "View" tab and Click "Document" icon.
            Check the Report Mode is converted to Document Mode.
        """
        report.select_ia_ribbon_item("View", "Document")
        report.wait_for_visible_text('#iaCanvasCaptionLabel', 'Document')
        report.wait_for_visible_text("div#TableChart_1", "EMP_ID")
        #report.create_acrossreport_data_set_in_preview("canvasContainer #TableChart_1", 1, 4, 12, 4, DATA_SET_NAME2)
        report.verify_across_report_data_set_in_preview("canvasContainer #TableChart_1", 1, 4, 12, 4, DATA_SET_NAME2, "Step 16.01 : Check the Report Mode is converted to Document Mode.")
        utils.capture_screenshot("16.01", Step16, expected_image_verify = True)
        
        Step17 = """
            STEP 17 : Click "IA" menu and Select "Close" option.
            Check the following Warning message.
        """
        report.select_ia_application_menu("close")
        report.wait_for_visible_text("#btnCancel", "Cancel")
        
        warning_popup_obj = utils.validate_and_get_webdriver_object("#saveAllDlg", "Warning popup")
        actual_result = warning_popup_obj.text
        msg = "Step 17.01 : Check the following Warning message."
        utils.asin("Save Changes to 'Document1'?", actual_result, msg)
        utils.capture_screenshot("17.01", Step17, expected_image_verify = True)
        
        Step18 = """
            STEP 18 : Click "No" button.
        """
        no_obj = utils.validate_and_get_webdriver_object("#btnNo", "No")
        core_utils.python_left_click(no_obj)
        utils.synchronize_until_element_disappear("#btnNo", report.home_page_short_timesleep)
        utils.capture_screenshot("18.01", Step18)
        
        Step19 = """
            STEP 19 : Click "IA" menu and Select "Close" option.
            Check the following Warning message.
        """
        time.sleep(8)
        report.select_ia_application_menu("close")
        report.wait_for_visible_text("#btnCancel", "Cancel")
        
        warning_popup_obj = utils.validate_and_get_webdriver_object("#saveAllDlg", "Warning popup")
        actual_result = warning_popup_obj.text
        msg = "Step 19.01 : Check the following Warning message."
        utils.asin("Save Changes to 'Report1'?", actual_result, msg)
        utils.capture_screenshot("19.01", Step19, expected_image_verify = True)
        
        Step20 = """
            STEP 20 : Click "No" button
        """
        no_obj = utils.validate_and_get_webdriver_object("#btnNo", "No")
        core_utils.python_left_click(no_obj)
        utils.capture_screenshot("20.01", Step20)
        
        """
            STEP 21 : Logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
 
if __name__ == '__main__':
    unittest.main()