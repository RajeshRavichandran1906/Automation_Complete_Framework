'''
Created on June 11, 2018

@author: Varun/Prasanth
Testcase Name : Date prompting
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6742419
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report

class C6742419_TestClass(BaseTestCase):
    
    def test_C6742419(self):
        """
        Test_case variables
        """
        report_obj= report.Report(self.driver)
        
        """
        Step 1: Create new IA report using wf_retail_lite mas file using API:
        http://machine_name:port/alias/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report_obj.invoke_ia_tool_using_new_api_login(master="baseapp/wf_retail_lite")
        report_obj.wait_for_visible_text("#singleReportLayout", "Drag and drop")
        
        """
        Step 2: Double click add "Product,Category", "Sale,Date" and "Revenue" fields
        """
        report_obj.double_click_on_datetree_item(field_name="Product,Category", field_position=1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Product,Category")
        report_obj.double_click_on_datetree_item(field_name="Sale,Date", field_position=1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Sale,Date")
        report_obj.double_click_on_datetree_item(field_name="Revenue", field_position=1)
        report_obj.wait_for_visible_text("#queryTreeWindow", "Revenue")
        
        """
        Step 3: Drag "Sale,Date" field to the Filter pane
        """
        report_obj.drag_and_drop_from_data_tree_to_filter("Sale,Date", field_position=1)
        report_obj.wait_for_visible_text("#dlgWhere", "Create a filtering condition")
        
        """
        Step 4: Select Parameter in Type drop down and click OK
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.wait_for_visible_text("#dlgWhereValue", "Type")
        report_obj.select_filter_type("Parameter")
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
        expected_field_label_list=["Date:"]
        report_obj.verify_autoprompt_field_labels_using_asequal(expected_field_label_list, "Step 06.01 : Verify autoprompt field labels")
        expected_value_list="Date:"
        report_obj.verify_field_textbox_value_in_autoprompt("Date:", expected_value_list, "Step 06.02 : Verify selected drop down value")
        
        """
        Step 7 : Select September 11, 2016 in Date: control and click Run with filter values
        """
        report_obj.select_year_in_calendardatepicker_dialog_in_run_window("2016")
        report_obj.select_month_in_calendardatepicker_dialog_in_run_window("Sep")
        report_obj.select_date_in_calendardatepicker_dialog_in_run_window("11")
        report_obj.run_auto_prompt_report()
        report_obj.switch_to_frame("iframe[name='wfOutput']")
        
        """
        Step 7 Expected: Verify report appears as below
        """
        report_obj.create_table_data_set("table[summary='Summary']", "C6742419_DataSet_01.xlsx")
        report_obj.verify_html_report_dataset("C6742419_DataSet_01.xlsx", "Step 10.01 : Verify report")
        
        """
        Step 8 : Close IA without saving
        """
        """
        Step 9 :Logout WF using API:
        http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report_obj.switch_to_default_content()
        report_obj.close_ia_without_save()
        
if __name__ == '__main__':
    unittest.main()
