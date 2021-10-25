"""-------------------------------------------------------------------------------------------
Created on September 20, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2348918
Test Case Title =  Insight - Matrix with Fill Color 
-----------------------------------------------------------------------------------------------"""

import unittest, time
from common.wftools.login import Login
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.pages.webfocus_editor import WebfocusEditor
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2348918_TestClass(BaseTestCase):

    def test_C2348918(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        chart = Chart(self.driver)
        locator = WfMainPageLocators()
        editor = WebfocusEditor(self.driver)
        utils = UtillityMethods(self.driver)
        main_page = Wf_Mainpage(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        chart_css = "div#runbox_id"
        
        Step1 = """
            STEP 01 : Run C2348918_Base.fex using API calls.
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10660%252FG168204%252F&BIP_item=C2348918_Base.fex
            Chart displayed in run time without error.
        """
        chart.run_fex_using_api_url("P292_S10660/G168204", "C2348918_Base", mrid = "mrid", mrpass = "mrpass", run_chart_css = chart_css)
        chart.wait_for_visible_text(chart_css, "CAR")
        
#         insight.verify_insight_querybox_text_options(['Rows', 'Columns', 'Color'], "Step 01.01 : Chart displayed in run time without error")
        #Avoiding above function as we face import error for the module
        
        expected_query_list = ['Rows', 'Columns', 'Color']
        query_buckets = utils.validate_and_get_webdriver_objects(".header-box .query-box .bucket-label", 'query buckets')
        query_buckets_text =  [element.text for element in query_buckets]
        msg = "Step 01.01 : Chart displayed in run time without error"
        utils.verify_list_values(expected_query_list, query_buckets_text, msg)
        
#         insight.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Save', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 01.02 : Chart displayed in run time without error.")
        
        expected_options_list = ['Reset', 'Swap  Axis', 'Save', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options']
        option_buckets = utils.validate_and_get_webdriver_objects(".header-box .options-box .er-menu-button:not([style*='none'])", 'option buckets')
        option_buckets_text = [utils.get_element_attribute(element, 'title').strip() for element in option_buckets]
        msg = "Step 01.02 : Chart displayed in run time without error."
        utils.verify_list_values(expected_options_list, list(option_buckets_text), msg)
        
        chart.verify_x_axis_label_in_run_window(['CAR'], parent_css = chart_css, xyz_axis_label_css = "svg > g text[class^='rowHeader-label!']", msg = "Step 01.01 : Chart displayed in run time without error")
        chart.verify_y_axis_label_in_run_window(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], parent_css = chart_css, xyz_axis_label_css = "svg > g text[class^='rowLabel!']", msg = "Step 01.02 : Chart displayed in run time without error")
        chart.verify_x_axis_label_in_run_window(['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN'], parent_css = chart_css, xyz_axis_label_css = "svg > g text[class^='colLabel!']", msg = "Step 01.03 : Chart displayed in run time without error")
        chart.verify_y_axis_label_in_run_window(['BODYTYPE'], parent_css = chart_css, xyz_axis_label_css = "svg > g text[class^='colHeader-label!']", msg = "Step 01.04 : Chart displayed in run time without error")
        chart.verify_legends_in_run_window(['RETAIL_COST', '3.1K', '17K', '31K', '44.9K', '58.8K'], parent_css = chart_css, msg = "Step 01.05 : Chart displayed in run time without error")
        chart.verify_number_of_risers("#runbox_id rect", 1, 13, msg = "Step 01.06 : Chart displayed in run time without error")
        chart.verify_chart_color("runbox_id", "riser!s0!g0!mmarker!r8!c4!", "dark_red4", msg = "Step 01.07 : Chart displayed in run time without error")
        chart.verify_chart_color("runbox_id", "riser!s0!g0!mmarker!r2!c4!", "dark_green3", msg = "Step 01.08 : Chart displayed in run time without error")
        utils.capture_screenshot("01.01", Step1, expected_image_verify = True)
        
        Step2 = """
            STEP 02 : Close the run window.
        """
        chart.api_logout()
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Edit C2348918_Base.fex in text editor.
            The below code has been added under *GRAPH_JS_FINAL keyword.
        """
        login.invoke_home_page("mrid", "mrpass")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder("P292_S10660->G168204")
        utils.synchronize_with_visble_text("div.files-box-files", "C2348918_Base", 60)
        
        main_page.right_click_folder_item_and_select_menu("C2348918_Base", "Edit with text editor")
        chart.switch_to_new_window()
        time.sleep(15)
        text_editor_parent_obj = utils.validate_and_get_webdriver_object("div.ace_scroller", "Text editor css")
        utils.scroll_down_on_element(text_editor_parent_obj, number_of_scroll = 5)
        time.sleep(5)
        editor.verify_line_in_texteditor( [r'"series":     ['],  "03.01", comparison_type = "asin")
        editor.verify_line_in_texteditor([r'"series": "all",'], "03.02", comparison_type = "asin")
        editor.verify_line_in_texteditor([r'"marker": {'], "03.03", comparison_type = "asin")
        editor.verify_line_in_texteditor([r'"shape": "fill"'], "03.04", comparison_type = "asin")
        editor.verify_line_in_texteditor([r'"agnosticSettings": {'], "03.05", comparison_type = "asin")
        editor.verify_line_in_texteditor([r'"chartTypeFullName": "Marker"'], "03.06", comparison_type = "asin")
        chart.switch_to_previous_window()
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)
        
        Step4 = """
            STEP 04 : Close the Text editor window.
        """
        chart.api_logout()
        utils.capture_screenshot("04.01", Step4)
        
        Step5 = """
            STEP 05 : Restore C2348918_Base.fex using below API.
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2348918.fex
            Chart restore successfully without error.
        """
        chart.edit_fex_using_api_url("P292_S10660/G168204", fex_name = "C2348918_Base")
        chart.wait_for_visible_text("#pfjTableChart_1", "CAR")
        
        chart.verify_x_axis_label_in_preview(['CAR'], xyz_axis_label_css = "svg > g text[class^='rowHeader-label!']", msg = "Step 05.01 : Chart restore successfully without error.")
        chart.verify_y_axis_label_in_preview(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], xyz_axis_label_css = "svg > g text[class^='rowLabel!']", msg = "Step 05.02 : Chart restore successfully without error.")
        chart.verify_x_axis_label_in_preview(['CONVERTIBLE', 'COUPE', 'HARDTOP', 'ROADSTER', 'SEDAN'], xyz_axis_label_css = "svg > g text[class^='colLabel!']", msg = "Step 05.03 : Chart restore successfully without error.")
        chart.verify_y_axis_label_in_preview(['BODYTYPE'], xyz_axis_label_css = "svg > g text[class^='colHeader-label!']", msg = "Step 05.04 : Chart restore successfully without error.")
        chart.verify_legends_in_preview(['RETAIL_COST', '3.1K', '17K', '31K', '44.9K', '58.8K'], msg = "Step 05.05 : Chart restore successfully without error.")
        chart.verify_number_of_risers("#pfjTableChart_1 rect", 1, 13, msg = "Step 05.06 : Chart restore successfully without error.")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mmarker!r8!c4!", "dark_red4", msg = "Step 05.07 : Chart restore successfully without error.")
        chart.verify_chart_color("pfjTableChart_1", "riser!s0!g0!mmarker!r2!c4!", "dark_green3", msg = "Step 05.08 : Chart restore successfully without error.")
        utils.capture_screenshot("05.01", Step5, expected_image_verify = True)
        
        Step6 = """
            STEP 6 : Log out with API call
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart.api_logout()
        utils.capture_screenshot("06.01", Step6)

if __name__ == '__main__':
    unittest.main()  