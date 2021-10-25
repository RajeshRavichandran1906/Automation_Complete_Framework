"""--------------------------------------------------------------------------------------
Author : Prabhakaran
Automated On : 06-August-2019
--------------------------------------------------------------------------------------"""

from common.wftools.report import Report
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase

class C7922373_TestClass(BaseTestCase):

    def test_C7922373(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON VARIABLES
        """
        CASE_ID = "C7922373"
        PREVIEW_CSS = "#TableChart_1"
        DATA_SET01 = CASE_ID + "_DataSet01.xlsx"
        
        """
            STEP 01 : Create new IA report using wf_retail_lite mas file using API:
            http://machine_name:port/alias/ia?tool=Report&master=baseapp/dimensions/wf_retail_product&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report.invoke_ia_tool_using_new_api_login(master='baseapp/dimensions/wf_retail_product')
        report.wait_for_visible_text(PREVIEW_CSS, "Drag and", report.report_medium_timesleep)
        utils.wait_for_page_loads(report.report_medium_timesleep)
        
        """
            STEP 02 : Click on Data Tab -> Join
        """
        report.select_ia_ribbon_item("Data", "join")
        report.wait_for_visible_text('#dlgJoin_btnOK', 'OK')
        """
            STEP 03 : Click 'Add New' and select wf_retail_vendor under Dimensions sub folder 
        """
        report.join_dialog().add_new_data_file("baseapp->dimensions", "wf_retail_vendor")
    
        """
            STEP 04 : Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor
        """
        report.join_dialog().link_fields("baseapp/dimensions/wf_retail_product", "ID_VENDOR", "baseapp/dimensions/wf_retail_vendor", "ID_VENDOR")
        
        """
            STEP 05 : Click OK
        """
        report.join_dialog().click_ok_button()
        
        """
            STEP 06 : Select Data Tab -> Define
        """
        report.select_ia_ribbon_item("Data", "detail_define")
        report.wait_for_visible_text("[id^='QbDialog']", "Detail", report.report_short_timesleep)
        
        """
            STEP 07 : Enter Field name "Vendor", Format A30V, double-click field "Vendor Name"
        """
        report.define_compute_dialog().enter_values_in_field_textbox("Vendor")
        report.define_compute_dialog().enter_values_in_format_textbox("A30V")
        report.define_compute_dialog().double_click_on_data_field("Dimensions->Vendor Name")
        report.define_compute_dialog().click_ok_button()
        
        """
            STEP 08 : Double-click fields "Product,Category", "Vendor", "ID Geography" and "Product Cost"
        """
        report.double_click_on_datetree_item("Dimensions->Product,Category")
        report.wait_for_visible_text(PREVIEW_CSS, "Accessories", report.report_medium_timesleep)
        
        report.double_click_on_datetree_item("Dimensions->Vendor")
        report.wait_for_visible_text(PREVIEW_CSS, "Vendor", report.report_medium_timesleep)
        
        report.double_click_on_datetree_item("Measures/Properties->ID Geography")
        report.wait_for_visible_text(PREVIEW_CSS, "ID Geography", report.report_medium_timesleep)
        
        report.double_click_on_datetree_item("Measures/Properties->Product,Cost")
        report.wait_for_visible_text(PREVIEW_CSS, "Cost", report.report_medium_timesleep)
        
        """
            STEP 09 : Drag and drop field "Vendor" from the Data pane to the Filter pane
        """
        report.drag_and_drop_from_data_tree_to_filter("Dimensions->Vendor")
        report.wait_for_visible_text("#dlgWhere", "Create a", report.report_medium_timesleep)
        
        """
            STEP 10 : Double Click <Value> and select Type:Parameter
        """
        report.open_where_value_popup_in_filter_dialog(1)
        report.select_filter_type("Parameter")
        
        """
            STEP 11 : Click "Static" radio button
        """
        report.select_filter_parameter_type("Static")
        
        """
            STEP 12 : Click "Get Values" > All
            STEP 13 : Select Audio Technica, Canon, LG, Panasonic, Samsung, Sharp, Sony, Toshiba and Click >> Click OK
        """
        static_fields = ['Audio Technica', 'Canon', 'LG', 'Panasonic', 'Samsung', 'Sharp', 'Sony', 'Toshiba']
        report.select_static_fields_in_filter_dialog("All", static_fields)
        report.close_filter_where_value_popup_dialog()
        
        """
            STEP 14 : Click ok in filtering condition dialog
        """
        report.close_filter_dialog()
        report.wait_for_visible_text('#qbFilterBox', 'Vendor')
        
        """
            STEP 15 : Click Run
            Verify Auto prompt appears as below
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text("#mainPage", "Filter Values", report.report_medium_timesleep)
        report.verify_autoprompt_field_labels_using_asequal(['Vendor:'], "Step 15.01 : Verify Auto prompt appears")
        report.verify_selected_field_dropdown_value_in_autoprompt('Vendor:', 'Audio Technica', "Step 15.02 : Verify Auto prompt appears")
        
        """
            STEP 16 : Click values drop down (Vendor)
            Verify list of values from Static Filter appears as below
        """
        report.select_field_filter_values_dropdown_in_auto_prompt('Vendor:')
        report.verify_option_type_field_filter_values_in_auto_prompt(static_fields, "Step 16.01 : Verify list of values from Static Filter appears")
        
        """
            STEP 17 : Select "Samsung" and click Run with filter values
            Verify report appears as below
        """
        report.select_single_field_filter_value_in_auto_prompt(['Samsung'])
        report.run_auto_prompt_report()
        report.switch_to_frame("iframe[name='wfOutput']")
        report.wait_for_visible_text("table[summary]", "Samsung", report.report_medium_timesleep)
        #report.create_report_dataset_using_start_end_rowcolumn(DATA_SET01)
        report.verify_report_dataset_using_start_end_rowcolumn(DATA_SET01, "table[summary]", "Step 17.01 : Verify report appears")
        report.switch_to_default_content()
        
        """
            STEP 18 : Close IA without saving
        """
        report.close_ia_without_save()
        
        """
            STEP 19 : Logout WF using API
        """
        