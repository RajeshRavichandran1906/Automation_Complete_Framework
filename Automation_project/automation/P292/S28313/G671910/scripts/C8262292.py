"""-------------------------------------------------------------------------------------------
Created on July 04, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262292
Test Case Title =  Create multiple Optional parameters in a single WHERE clause with OR/AND
                   should generate -DEFAULT for each filter in the WHERE clasue
-----------------------------------------------------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report, utillobject

class C8262292_TestClass(BaseTestCase):

    def test_C8262292(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = utillobject(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        CASE_ID = "C8262292"
        DATASET = CASE_ID + "_DataSet_01.xlsx"
        QUERY_PANE_CSS = "#queryTreeColumn"
        FILTER_DIG_CSS = "#dlgWhere"
        SHORT_TIME = 30
        LONG_TIME = 120
        
        """
            STEP 01 : Launch IA Report with car file
            http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/car&item=IBFS:/WFC/Repository/P292_S28313/G671908
        """
        report.invoke_ia_tool_using_new_api_login(master='ibisamp/car')
        report.wait_for_visible_text(QUERY_PANE_CSS, "Sum", LONG_TIME)
        
        """
            STEP 02 : Double click COUNTRY and SALES
        """
        report.double_click_on_datetree_item('COUNTRY')
        report.wait_for_visible_text(QUERY_PANE_CSS, "COUNTRY", SHORT_TIME)
        
        report.double_click_on_datetree_item('SALES')
        report.wait_for_visible_text(QUERY_PANE_CSS, "SALES", SHORT_TIME)
        
        """
            STEP 03 : Drag COUNTRY into the Filter pane
        """
        report.drag_and_drop_from_data_tree_to_filter('COUNTRY')
        report.wait_for_visible_text(FILTER_DIG_CSS, "Create a", SHORT_TIME)
        
        """
            STEP 04 : Select Type:Parameter > Optional > OK
        """
        report.open_where_value_popup_in_filter_dialog(1)
        report.select_filter_type("Parameter")
        report.select_filter_parameter_checkbox(True)
        report.close_filter_where_value_popup_dialog()
        
        """
            STEP 05 : Select 'Insert After'
        """
        insert_after = self.driver.find_element_by_id("dlgWhere_btnInsertAfter")
        core_utils.left_click(insert_after)
        
        """
            STEP 06 : Select field CAR > Type:Parameter > Optional > OK
        """
        report.double_click_field_in_filter_tree('CAR')
        report.open_where_value_popup_in_filter_dialog(3)
        report.select_filter_type("Parameter")
        report.select_filter_parameter_checkbox(True)
        report.close_filter_where_value_popup_dialog()
        
        """
            STEP 07 : Click OK to save the filters
        """
        report.close_filter_dialog()
        report.wait_for_visible_text("#qbFilterBox", "COUNTRY", SHORT_TIME)
        
        """
            STEP 08 : Click on the View Source button. Verify -DEFAULT syntax for each Optional filter
            -DEFAULT &COUNTRY = FOCNULL;
            -DEFAULT &CAR = FOCNULL;
            STEP 09 : Close the source window
        """
        msg = "Step 08.01 : Verify -DEFAULT &COUNTRY = FOCNULL; -DEFAULT &CAR = FOCNULL; syntax displayed in source code dialog"
        report.verify_fexcode_syntax(['-DEFAULT &COUNTRY = _FOC_NULL;', '-DEFAULT &CAR = _FOC_NULL;'], msg)
        
        """
            STEP 10 : Click Run Verify output (No prompt should be displayed)
        """
        msg = "Step 10.01 : Verify report output"
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        #report.create_html_report_dataset(DATASET)
        report.verify_html_report_dataset(DATASET, msg)
        report.switch_to_default_content()
        
        """
            STEP 11 : Click IA > Save As > "C6984758" > Click Save
        """
        report.save_as_from_application_menu_item(CASE_ID)
        
        """
            STEP 12 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEP 13 : Reopen FEX - http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P292_S28313/G671908/C6984758.fex
        """
        report.edit_fex_using_api_url(CASE_ID)
        report.wait_for_visible_text(QUERY_PANE_CSS, "SALES", LONG_TIME)
        
        """
            STEP 14 : Click Run > Verify output (No prompt should be displayed)
        """
        msg = "Step 14.01 : Verify report output"
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.verify_html_report_dataset(DATASET, msg)
        report.switch_to_default_content()
        
        """
            STEP 15 : Click on the View Source button > Verify -DEFAULT syntax for each Optional filter
            -DEFAULT &COUNTRY = FOCNULL;
            -DEFAULT &CAR = FOCNULL;
            STEP 16 : Close the source window
        """
        msg = "Step 15.01 : Verify -DEFAULT &COUNTRY = FOCNULL; -DEFAULT &CAR = FOCNULL; syntax displayed in source code dialog"
        report.verify_fexcode_syntax(['-DEFAULT &COUNTRY = _FOC_NULL;', '-DEFAULT &CAR = _FOC_NULL;'], msg)
        
        """
            STEP 17 : Right click on the filter in the Filter pane > Edit
        """
        report.right_click_on_field_in_filterbox("COUNTRY Equal to Optional Simple Parameter (Name: COUNTRY) or CAR Equal to Optional Simple Parameter (Name: CAR)", context_menu_path='Edit')
        
        """
            STEP 18 : Verify both filters are "Optional"
        """
        msg = "Step 18.01 : Verify both filters are 'Optional'"
        expected_value = ['WHERE', 'COUNTRY Equal to Optional Simple Parameter (Name: COUNTRY)', 'OR', 'CAR Equal to Optional Simple Parameter (Name: CAR)', '']
        actual_value = [filter_row.text.strip() for filter_row in self.driver.find_elements_by_css_selector("#dlgWhereWhereTree table>tbody>tr")]
        utils.asequal(expected_value, actual_value, msg)
        
        """
            STEP 19 : Cancel
        """
        report.close_filter_dialog()
        
        """
            STEP 20 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        