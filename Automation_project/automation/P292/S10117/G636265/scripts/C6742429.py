'''
Created on June 10, 2018

@author: Varun/Prasanth
Testcase Name : Longer list prompts
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6742429
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.lib.global_variables import Global_variables
from common.pages import visualization_metadata
import time

class C6742429_TestClass(BaseTestCase):
    
    def test_C6742429(self):
        """
        Test_case variables
        """
        report_obj= report.Report(self.driver)
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

        report_obj.double_click_on_datetree_item("Product,Category")
        report_obj.wait_for_visible_text("#queryTreeWindow", "Product,Category")
        
        report_obj.double_click_on_datetree_item("Revenue")
        report_obj.wait_for_visible_text("#queryTreeWindow", "Revenue")
        
        """
        Step 3: Drag "Product,Subcategory" field to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Subcategory", field_position=1)
        report_obj.wait_for_visible_text("#dlgWhere", "Create a filtering condition")
        
        """
        Step 4: Select Parameter in Type drop down and select Dynamic radio button;
        Click OK
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.wait_for_visible_text("#dlgWhereValue", "Type")
        report_obj.select_filter_type("Parameter")
        time.sleep(3)
        report_obj.select_filter_parameter_type("Dynamic")
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
        Step 6 Expected: Verify report with Auto prompt appears as below    
        """
        report_obj.wait_for_number_of_element("[id^='ReportIframe']", 1)
        report_obj.switch_to_frame()
        time.sleep(3)
        expected_field_label_list=['Product Subcategory:']
        report_obj.verify_autoprompt_field_labels_using_asequal(expected_field_label_list, "Step 06.01: Verify autoprompt field labels")
        expected_value_list="Blu Ray"
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("Product Subcategory:", expected_value_list, "Step 06.02 : Verify selected drop down value")
        
        """
        Step 7: Click Product Subcategory: drop down
        """
        report_obj.select_field_filter_values_dropdown_in_auto_prompt("Product Subcategory:")
        
        """
        Step 7 Expected: Verify drop down is visible with longer list as below
        """
        expected_value_list=['Blu Ray', 'Boom Box', 'Charger', 'CRT TV', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'iPod Docking Station', 'Portable TV', 'Professional', 'Receivers']
        if Global_variables.browser_name in ['firefox']:
            expected_value_list=['Blu Ray', 'Boom Box', 'Charger', 'CRT TV', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'iPod Docking Station', 'Portable TV', 'Professional', 'Receivers']
#             expected_value_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone']
        else:
            expected_value_list=['Blu Ray', 'Boom Box', 'Charger', 'CRT TV', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'iPod Docking Station', 'Portable TV', 'Professional']
        report_obj.verify_input_type_field_filter_values_in_auto_prompt(expected_value_list, "Step 07.01 : Verify drop down is visible with longer list")
        
        """
        Step 8: Scroll down and select Smartphone in drop down
        """
        report_obj.select_single_field_filter_value_in_listbox_auto_prompt(["Smartphone"])
        
        """
        Step 9 : Click Run with filter values
        """
        report_obj.run_auto_prompt_report()
        report_obj.wait_for_number_of_element("iframe[name='wfOutput']", 1)

        """
        Step 9 Expected: Verify report appears as below
        """
        report_obj.switch_to_frame("iframe[name='wfOutput']")
#         report_obj.create_table_data_set("table[summary='Summary']", "C6742429_DataSet_01.xlsx")
        report_obj.verify_html_report_dataset("C6742429_DataSet_01.xlsx", "Step 09.01 : Verify report")
        
        """
        Step 10 : Close IA without saving
        """
        report_obj.switch_to_default_content()
        report_obj.close_ia_without_save()
        """
        Step 11 :Logout WF using API:
        http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
 
        
if __name__ == '__main__':
    unittest.main()