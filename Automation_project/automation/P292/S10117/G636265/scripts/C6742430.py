'''
Created on June 11, 2018

@author: Varun/Prasanth
Testcase Name : Different jQuery control
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6742430
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.lib import utillity
from common.pages import visualization_metadata

class C6742430_TestClass(BaseTestCase):
    
    def test_C6742430(self):
        """
        Test_case variables
        """
        report_obj= report.Report(self.driver)
        utility_obj=utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 1: Create new IA report using wf_retail_lite mas file using API:
        http://machine_name:port/alias/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report_obj.invoke_ia_tool_using_new_api_login(master="baseapp/wf_retail_lite")
        report_obj.wait_for_visible_text("#singleReportLayout", "Drag and drop")
        
        """
        Step 2: Double click add "Product,Category" and "Revenue" fields.
        """

        report_obj.double_click_on_datetree_item(field_name="Product,Category", field_position=1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Product,Category")
        report_obj.double_click_on_datetree_item(field_name="Revenue", field_position=1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Revenue")
        
        """
        Step 3: Drag "Product,Subcategory" field to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Subcategory", field_position=1)
        report_obj.wait_for_visible_text("#dlgWhere", "Create a filtering condition")
        
        """
        Step 4: Select Parameter in Type drop down and select Dynamic radio button;
        Check "Select multiple values at run time" and click OK
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.wait_for_visible_text("#dlgWhereValue", "Type")
        report_obj.select_filter_type("Parameter")
        report_obj.select_filter_parameter_type("Dynamic")
        report_obj.select_filter_parameter_checkbox(ParamMultiple=True)
        report_obj.close_filter_where_value_popup_dialog()
        
        """
        Step 5: Click OK in filtering condition dialog
        """
        report_obj.close_filter_dialog()
        
        """
        Step 6: Click Run in toolbar
        """
        report_obj.run_report_from_toptoolbar()
        
        """
        Step 6 Expected: Verify auto prompt window appears as below
        """
        report_obj.switch_to_frame()
        expected_field_label_list=["Product Subcategory:"]
        report_obj.verify_autoprompt_field_labels_using_asequal(expected_field_label_list, "Step 06.01 : Verify autoprompt field labels")
        expected_value_list="All Values"
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("Product Subcategory:", expected_value_list, "Step 06.02 : Verify selected drop down value")
        
        """
        Step 7: Click Product Subcategory: dropdown.
        """
        report_obj.select_field_filter_values_dropdown_in_auto_prompt("Product Subcategory:")
        
        """
        Step 7 Expected: Verify drop down is visible and All Values is selected as below
        """
        report_obj.verify_all_values_button_selected_autoprompt(step_num="07.01")
        
        """
        Step 8: Click Select Values.
        """
        report_obj.select_radio_button_in_auto_prompt_values('Select Values')
        
        """
        Step 8 Expected : Verify Search and available values are enabled as below
        """
        enabled_status = len(self.driver.find_elements_by_css_selector(".autop-sav-values-container.ui-state-disabled"))
        utility_obj.asequal(0, enabled_status, "Step 08.01 : Verify Search and available values are enabled")
        
        """
        Step 9: Enter 'S' in Search box.
        """
        report_obj.enter_value_search_textbox_popup_in_auto_prompt('S')
        
        """
        Step 9 Expected: Verify only matching values are filtered as below
        """
        expected_value_list=['Smartphone', 'Speaker Kits', 'Standard', 'Streaming']
        report_obj.verify_input_type_field_filter_values_in_auto_prompt(expected_value_list, "Step 09.01 : Verify only matching values are filtered")
        
        """
        Step 10: Click "All" in control
        """
        report_obj.select_value_button_in_auto_prompt("All")
        
        """
        Step 10 Expected: Verify all available values are selected as below
        """
        report_obj.verify_field_filter_values_checked_property_in_auto_prompt(expected_value_list, "Step 10.01 : Verify selected values are checked", 'checked')
        
        """
        Step 11: Click None in control.
        """
        report_obj.select_value_button_in_auto_prompt("None")
        
        """
        Step 11 Expected: Verify selected values are unchecked as below
        """
        report_obj.verify_field_filter_values_checked_property_in_auto_prompt(expected_value_list, "Step 11.01 : Verify selected values are unchecked", 'unchecked')
        report_obj.select_auto_prompt_value_back_button()
        
        """
        Step 12 : Click Run with filter values
        """
        report_obj.run_auto_prompt_report()
        report_obj.switch_to_frame("iframe[name='wfOutput']")
        
        """
        Step 12 Expected: Verify report appears as below
        """
        report_obj.create_table_data_set("table[summary='Summary']", "C6742430_DataSet_01.xlsx")
        report_obj.verify_html_report_dataset("C6742430_DataSet_01.xlsx", "Step 12.01 : Verify report")
        
        """
        Step 13 : Close IA without saving
        """
        report_obj.switch_to_default_content()
        
        """
        Step 14 :Logout WF using API:
        http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report_obj.close_ia_without_save()
        
if __name__ == '__main__':
    unittest.main()
