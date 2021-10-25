"""--------------------------------------------------------------------------------------
Author : Prabhakaran
Automated On : 08-August-2019
--------------------------------------------------------------------------------------"""
from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods

class C7935404_TestClass(BaseTestCase):

    def test_C7935404(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            COMMON VARIABLES
        """
        CASE_ID = "C7935404"
        PREVIEW_CSS = "#TableChart_1"
        DATA_SET01 = CASE_ID + "_DataSet01.xlsx"
        
        """
            STEP 01 : Create new IA report using wf_retail_lite mas file using API:
            http://machine_name:port/alias/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report.invoke_ia_tool_using_new_api_login(master='baseapp/wf_retail_lite')
        report.wait_for_visible_text(PREVIEW_CSS, "Drag and", report.report_medium_timesleep)
        
        """
            STEP 02 : Double click "Product Category" and "Revenue"
        """
        report.double_click_on_datetree_item("Product,Category")
        report.wait_for_visible_text(PREVIEW_CSS, "Product", report.report_medium_timesleep)
        
        report.double_click_on_datetree_item("Revenue")
        report.wait_for_visible_text(PREVIEW_CSS, "Revenue", report.report_medium_timesleep)
        
        """
            STEP 03 : Click on Data tab -> Define
        """
        report.select_ia_ribbon_item("Data", "detail_define")
        report.wait_for_visible_text("[id^='QbDialog']", "Detail", report.report_short_timesleep)
        
        """
            STEP 04 : Click on Format button and select 'Date-time' from field type
        """
        report.define_compute_dialog().click_format()
        date_time = self.driver.find_element_by_xpath("//div[@id='format-types-list']//div[normalize-space()='Date-Time']")
        core_utils.left_click(date_time)
        
        """
            STEP 05 : Expand Year First under Date format and select YYMD and time format as Hour:Minute
        """
        expand_year_first = self.driver.find_element_by_xpath("//div[@id='dateFormat']//td[normalize-space()='Year First']/img")
        core_utils.left_click(expand_year_first)
        
        yymd = self.driver.find_element_by_xpath("//div[@id='dateFormat']//td[normalize-space()='YYMD']")
        core_utils.left_click(yymd)
        
        hour_minute = self.driver.find_element_by_xpath("//div[@id='timeFormat']//td[normalize-space()='Hour:Minute']")
        core_utils.left_click(hour_minute)
          
        """
            STEP 06 : Click OK
        """
        ok_button = self.driver.find_element_by_id("fmtDlgOk")
        core_utils.left_click(ok_button)
        
        """
            STEP 07 : Double click add sale date from under Sales_Related -> Sale_Day -> Sale Date Details and click OK
        """
        report.define_compute_dialog().double_click_on_data_field("Sale,Date")
        report.define_compute_dialog().click_ok_button()
        utils.synchronize_until_element_disappear("#fldCreatorOkBtn", 30)
        
        """
            STEP 08 : Drag Define_1 to filter pane
        """
#         time.sleep(4) # Giving time to settle element 
        report.drag_and_drop_from_data_tree_to_filter("Dimensions->Sales_Related->Transaction Date, Simple->Sale,Day->Attributes->Define_1")
        report.wait_for_visible_text("#dlgWhere", "Create a", report.report_medium_timesleep)
        
        """
            STEP 09 : Select type as Parameter and click OK
        """
        report.open_where_value_popup_in_filter_dialog(1)
        report.select_filter_type("Parameter")
        report.close_filter_where_value_popup_dialog()
        
        """
            STEP 10 : Click OK in filtering condition dialog
        """
        report.close_filter_dialog()
        
        """
            STEP 11 : Click Run
            Verify auto prompt appears as below
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text("#mainPage", "Filter Values", report.report_medium_timesleep)
        report.verify_autoprompt_field_labels_using_asequal(['Define_1:'], "Step 11.01 : Verify Auto prompt appears")
        
        """
            STEP 12 : Select March 10,2016 and click Run with filter values
            Verify report appears as below
        """
        report.select_year_in_calendardatepicker_dialog_in_run_window("2016")
        report.select_month_in_calendardatepicker_dialog_in_run_window("Mar")
        report.select_date_in_calendardatepicker_dialog_in_run_window("10")
        report.run_auto_prompt_report()
        report.switch_to_frame("iframe[name='wfOutput']")
        report.wait_for_visible_text("table[summary]", "Revenue", report.report_medium_timesleep)
        #report.create_report_dataset_using_start_end_rowcolumn(DATA_SET01)
        report.verify_report_dataset_using_start_end_rowcolumn(DATA_SET01, "table[summary]", "Step 12.01 : Verify report appears")
        report.switch_to_default_content()
        
        """
            STEP 13 : Close IA > Close > No
        """
        report.close_ia_without_save()
        
        """
            STEP 14 : Logout WF using API
        """
        