"""-------------------------------------------------------------------------------------------
Created on September 16, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9333214
Test Case Title =  Verify output formats HTML, Active Report, PDF
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.report import Report
from common.lib.global_variables import Global_variables
from common.wftools.active_report import Active_Report
import time

class C9333214_TestClass(BaseTestCase):

    def test_C9333214(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        global_var_obj = Global_variables()
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        act_report = Active_Report(self.driver)
      
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
            STEP 01 : Launch the API to create new Report with CAR.
            http://machine:port/{alias}/ia?is508=false&tool=report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S29835/G781455
        """
        report.invoke_ia_tool_using_new_api_login(master = "ibisamp/car")
        report.wait_for_visible_text(live_preview_css, "Drag and drop")
        utils.capture_screenshot("01.01", Step1)
         
        Step2 = """
            STEP 02 : Double click "COUNTRY", "CAR" and "DEALER_COST" in Data pane.
        """
        report.double_click_on_datetree_item("COUNTRY", 1)
        report.wait_for_visible_text(query_css, "COUNTRY")
         
        report.double_click_on_datetree_item("CAR", 1)
        report.wait_for_visible_text(query_css, "CAR")
         
        report.double_click_on_datetree_item("DEALER_COST", 1)
        report.wait_for_visible_text(query_css, "DEALER_COST")
        utils.capture_screenshot("02.01", Step2)
         
        Step3 = """
            STEP 03 : Click "Save" in toolbar Enter "C9333214" and Click "Save" button.
        """
        report.save_report_from_toptoolbar()
        report.wait_for_visible_text(cancel_css, "Cancel")
         
        report.save_file_in_save_dialog('C9333214')
        utils.synchronize_until_element_disappear(cancel_css, report.home_page_short_timesleep)
        utils.capture_screenshot("03.01", Step3)
        
        Step4 = """
            STEP 04 : Click "Run" from toolbar.
            Check the HTML formatted report is generated.
        """
        report.run_report_from_toptoolbar()
        time.sleep(5)
        report.switch_to_frame()
        time.sleep(15)
        #report.create_html_report_dataset(DATA_SET_NAME1)
        report.verify_html_report_dataset(DATA_SET_NAME1, "Step 04.01 : Check the HTML formatted report is generated.")
        report.switch_to_default_content()
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP 05 : Click "HTML" dropdown under Home tab and Select "HTML Analytic Document".
        """
        report.change_output_format_type("active_report")
        report.wait_for_visible_text('#HomeFormatType', "HTML Analytic Document")
        utils.capture_screenshot("05.01", Step5)
        
        Step6 = """
            STEP 06 : Click "Run" from toolbar.
            Check the HTML Analytic Document formatted report is generated.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text("#orgdivtable0", "ENGLAND")
        
        #act_report.create_active_report_dataset(DATA_SET_NAME2, desired_no_of_rows=11, starting_rownum=1)
        act_report.verify_active_report_dataset(DATA_SET_NAME2,table_css="#ITableData0", desired_no_of_rows=11, starting_rownum=1, msg= 'Step 06.01 : Check the HTML Analytic Document formatted report is generated.')
        report.switch_to_default_content()
        utils.capture_screenshot("06.01", Step6, expected_image_verify = True)
        
        Step7 = """
            STEP 07 : Click "HTML" dropdown under Home tab and Select "PDF".
        """
        report.change_output_format_type("pdf")
        report.wait_for_visible_text('#HomeFormatType', "PDF")
        utils.capture_screenshot("07.01", Step7)
 
        Step8 = """
            STEP 08 : Click "Run" from toolbar.
            Check the "PDF" formatted report is generated.
        """
        report.run_report_from_toptoolbar()
        time.sleep(5)
        report.switch_to_frame()
        time.sleep(15)
        
        if Global_variables.browser_name == "chrome":
            pdf_obj = utils.validate_and_get_webdriver_object("embed[src]", "PDF css")
            actual_result = pdf_obj.get_attribute("type")
            expected_result = "application/pdf"
            msg = "Step 08.01 : Check the 'PDF' formatted report is generated."
            utils.asin(expected_result, actual_result, msg)
        else:
            pdf_obj = utils.validate_and_get_webdriver_object("#viewer", "PDF css")
            actual_result = pdf_obj.is_displayed()
            msg = "Step 06.01 : Check it generated the PDF document."
            utils.asequal(actual_result, True, msg)
        report.switch_to_default_content()
        utils.capture_screenshot("08.01", Step8, expected_image_verify = True)
        
        Step9 = """
            STEP 09 : Click "Save" from toolbar and Click "OK" button.
        """
        report.save_report_from_toptoolbar()
        report.wait_for_visible_text("div[class*='bi-button button button-focus']", "OK")
        
        ok_button_css = utils.validate_and_get_webdriver_object("div[class*='bi-button button button-focus']", "OK button css")
        core_utils.python_left_click(ok_button_css)
        time.sleep(5)
        utils.capture_screenshot("09.01", Step9)
        
        Step10 = """
            STEP 10 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        utils.capture_screenshot("10.01", Step10)
        
        Step11 = """
            STEP 11 : Reopen the saved fex using API link
            http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/P292_S29835/G781455/C9333214.fex&tool=Report
            Check the output format is set to "PDF".
        """
        report.edit_fex_using_api_url("C9333214", folder_name = "P292_S29835/G781455", mrid = "mrid", mrpass = "mrpass")
        report.wait_for_visible_text("#singleReportLayout", "COUNTRY")
        
        pdf_obj = utils.validate_and_get_webdriver_object("#HomeFormatType", "Pdf css")
        actual_result = pdf_obj.text
        msg = "Step 11.01 : Check the output format is set to 'PDF'"
        utils.asequal(actual_result, "PDF", msg)
        utils.capture_screenshot("11.01", Step11, expected_image_verify = True)
        
        Step12 = """
            STEP 12 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        utils.capture_screenshot("12.01", Step12)
        
if __name__ == '__main__':
    unittest.main()