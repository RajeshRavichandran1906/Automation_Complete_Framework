"""--------------------------------------------------------------------------------------
Author : Prabhakaran
Automated On : 13-August-2019
--------------------------------------------------------------------------------------"""
import unittest, time
from common.wftools.login import Login
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.text_editor import wf_texteditor

class C6694034_TestClass(BaseTestCase):

    def test_C6694034(self):
        
        """ CLASS OBJECTS """
        report = Report(self.driver)
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        editor = wf_texteditor(self.driver)
        
        """ COMMON VARIABLES """
        CASE_ID = "C6694034"
        PREVIEW_CSS = "#TableChart_1"
        DATA_SET01 = CASE_ID + "_DataSet01.xlsx"
         
        """
            STEP 01 : Create new IA report using Car master file using API:
            http://machine_name:port/alias/ia?tool=Report&master=baseapp/car&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report.invoke_ia_tool_using_new_api_login(master='baseapp/car')
        report.wait_for_visible_text(PREVIEW_CSS, "Drag and", report.report_medium_timesleep)
         
        """
            STEP 02 : Double click "CAR", "MODEL" and "MPG" fields
        """
        report.double_click_on_datetree_item("CAR")
        report.wait_for_visible_text(PREVIEW_CSS, "CAR", report.report_medium_timesleep)
         
        report.double_click_on_datetree_item("MODEL")
        report.wait_for_visible_text(PREVIEW_CSS, "MODEL", report.report_medium_timesleep)
         
        report.double_click_on_datetree_item("MPG")
        report.wait_for_visible_text(PREVIEW_CSS, "MPG", report.report_medium_timesleep)
         
        """
            STEP 03 : Drag and drop MPG field into Filter pane
        """
        time.sleep(4) #giving time for firefox consistency
        report.drag_and_drop_from_data_tree_to_filter("MPG")
        report.wait_for_visible_text("#dlgWhere", "Create a", report.report_medium_timesleep)
         
        """
            STEP 04 : Click on Value drop down and select Parameter in Type drop down
        """
        report.open_where_value_popup_in_filter_dialog(1)
        report.select_filter_type("Parameter")
         
        """
            STEP 05 : Click on Optional checkbox
        """
        report.select_filter_parameter_checkbox(ParamOptional=True)
         
        """
            STEP 06 : Enter "MINMPG" in Name and click OK
        """
        report.enter_where_value_field_textbox_in_filter_dialog("MINMPG")
        report.close_filter_where_value_popup_dialog()
         
        """
            STEP 07 : Double click "Equal to" drop down and select "Greater than" condition and click OK
            Verify an optional Parameter filter control is created in filter pane as below
        """
        report.click_equal_to_condition_in_filter_dialog("Greater than")
        report.close_filter_dialog()
        report.wait_for_visible_text('#qbFilterBox', 'Greater')
        report.verify_filter_pane_field("MPG Greater than Optional Simple Parameter (Name: MINMPG)", 1, "Step 08.01 ")
         
        """
            STEP 08 : Drag and drop MPG field into the Filter pane again
        """
        report.drag_and_drop_from_data_tree_to_filter("MPG")
        report.wait_for_visible_text("#dlgWhere", "Create a", report.report_medium_timesleep)
         
        """
            STEP 09 : Click on Value drop down and select Parameter in Type drop down
        """
        report.open_where_value_popup_in_filter_dialog(2)
        report.select_filter_type("Parameter")
         
        """
            STEP 10 : Click on Optional checkbox
        """
        report.select_filter_parameter_checkbox(ParamOptional=True)
         
        """
            STEP 11 : Enter "MAXMPG" in Name and click OK.
        """
        report.enter_where_value_field_textbox_in_filter_dialog("MAXMPG")
        report.close_filter_where_value_popup_dialog()
         
        """
            STEP 12 : Double click "Equal to" dropdown and select "Less than or equal to" condition and click OK
            Verify two filter controls are available in Filter pane as below
        """
        report.click_equal_to_condition_in_filter_dialog("Less than")
        report.close_filter_dialog()
        report.wait_for_visible_text('#qbFilterBox', 'Less')
        report.verify_filter_pane_field("MPG Greater than Optional Simple Parameter (Name: MINMPG)", 1, "Step 12.01 ")
        report.verify_filter_pane_field("MPG Less than Optional Simple Parameter (Name: MAXMPG)", 2, "Step 12.02 ")
         
        """
            STEP 13 : Click Save and enter "C6694034" in Title and Save
        """
        report.select_ia_toolbar_item("toolbar_save")
        report.wait_for_visible_text("#dlgIbfsOpenFile7", "Save", report.report_short_timesleep)
        report.save_file_in_save_dialog(CASE_ID)
         
        """
            STEP 14 : Logout - http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEP 15 : Login to WF as Developer user. http://machine:port/ibi_apps/
        """
        loginpage.invoke_home_page("mrid", "mrpass")
        homepage.select_content_from_sidebar()
        
        """
            STEP 16 : Navigate to the following folder P292_S10117/
        """
        homepage.expand_repository_folder("P292_S10117->G636265")
        report.wait_for_visible_text(".files-box", CASE_ID, homepage.home_page_short_timesleep)
         
        """
            STEP 17 : Right click on "C6694034" report and select Edit with Text Editor
        """
        homepage.right_click_folder_item_and_select_menu(CASE_ID, "Edit with text editor")
        report.switch_to_new_window()
         
        """
            STEP 18 : Replace DEFAULT and WHERE condition in Editor with the following:
        """
        editor.replace_line_in_texteditor("-DEFAULT &MINMPG = _FOC_NULL;", ["-DEFAULT &MINMPG = 10;"])
        editor.replace_line_in_texteditor("-DEFAULT &MAXMPG = _FOC_NULL;", ["-DEFAULT &MAXMPG = 20;"])
        editor.replace_line_in_texteditor("WHERE CAR.SPECS.MPG GT &MINMPG.(|FORMAT=D6).MPG:.;", ["WHERE CAR.SPECS.MPG GT &MINMPG.(FROM 1 TO 29|FORMAT=D6).Min MPG:.;"])
        editor.replace_line_in_texteditor("WHERE CAR.SPECS.MPG LT &MAXMPG.(|FORMAT=D6).MPG:.;", ["WHERE CAR.SPECS.MPG LE &MAXMPG.(FROM 2 TO 30|FORMAT=D6).Max MPG:.;"])
         
        """
            STEP 19 : Save and Exit Editor.
        """
        editor.click_menu_bar_button("Save")
        report.switch_to_previous_window()
        
        """
            STEP 20 : Right click "C6694034" report and select Properties
        """
        homepage.right_click_folder_item_and_select_menu(CASE_ID, "Properties")
        report.wait_for_visible_text(".properties-tab-pane [data-ibx-type$='TabGroup']", visble_element_text='Advanced', time_out=report.home_page_medium_timesleep)
        """
            STEP 21 : Click on "Prompt for parameters" check box and click OK.
        """
        homepage.select_property_tab_value("Advanced")
        report.wait_for_visible_text(".properties-tab-pane [class*='advanced'].tpg-selected", visble_element_text='Prompt for parameters', time_out=report.home_page_medium_timesleep)
        homepage.edit_property_dialog_value("Prompt for parameters", "checkbox", "check", tab_name='Advanced')
        homepage.select_property_dialog_save_cancel_button("Save")
        report.wait_for_number_of_element("[class*='ok'].ibx-widget-disabled", expected_number=1, time_out=report.home_page_medium_timesleep)
        
        """
            STEP 22 : Logout WF using API - http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report.api_logout()
        
        """
            STEP 23 : Run C6694034 using API:
            http://machine_name:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/S9970/&BIP_item=C6694034.fex
            Verify Slider control prompt appears as below
        """
        report.run_fex_using_api_url("P292_S10117/G636265", CASE_ID, "mrid", "mrpass", run_table_css="#promptPanel .autop-title")
        report.verify_autoprompt_field_labels_using_asequal(['Min MPG:', 'Max MPG:'], "Step 23.01 : Verify Slider control prompt appears")
        
        """
            STEP 24 : Click Run with filter values
            Verify report appears as below
        """
        report.run_auto_prompt_report()
        report.switch_to_frame("iframe.autop-wf-output")
        report.wait_for_visible_text("table[summary]", "CAR", report.report_medium_timesleep)
        #report.create_report_dataset_using_start_end_rowcolumn(DATA_SET01)
        report.verify_report_dataset_using_start_end_rowcolumn(DATA_SET01, "table[summary]", "Step 24.01 : Verify report appears")
        
        """
            STEP 25 : Close run window
            STEP 26 : Logout WF using API:
        """
        
if __name__ == '__main__':
    unittest.main()