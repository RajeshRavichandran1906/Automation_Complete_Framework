'''
Created on June 10, 2018

@author: Varun/Prasanth
Testcase Name : Multi-select dynamic prompting
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6694058
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.pages import visualization_metadata

class C6694058_TestClass(BaseTestCase):
    
    def test_C6694058(self):
        """
        Test_case variables
        """
        report_obj= report.Report(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 1: Create new IA report using wf_retail_lite mas file using API:
        http://machine_name:port/alias/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report_obj.invoke_ia_tool_using_new_api_login(master="baseapp/wf_retail_lite", wait_time=report_obj.chart_long_timesleep)
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
        #report_obj.drag_and_drop_from_data_tree_to_filter("Dimensions->Product->Product->Product,Subcategory", field_position=1)
        report_obj.wait_for_visible_text("#dlgWhere", "Create a filtering condition")
        
        """
        Step 4: Select Parameter in Type drop down
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.wait_for_visible_text("#dlgWhereValue", "Type")
        report_obj.select_filter_type("Parameter")
        
        """
        Step 5: Select Dynamic radio button;
        Select Product,Subcategory field in list;
        """
        report_obj.select_filter_parameter_type("Dynamic")
        report_obj.select_field_in_filter_tree("Dimensions->Product->Product->Product,Subcategory", 1)
        
        """
        Step 6: Select multiple values at runtime check boxes;
        Click OK
        """
        report_obj.select_filter_parameter_checkbox(ParamMultiple=True)
        report_obj.close_filter_where_value_popup_dialog()
        
        """
        Step 7: Click OK in filtering condition dialog
        """
        report_obj.close_filter_dialog()
        
        """
        Step 8: Click Run in toolbar
        """
        report_obj.run_report_from_toptoolbar()
        
        """
        Step 9: Click on Product Subcategory filter;
        Click on Select Values;
        Multi select Blu Ray, Charger and Tablet values
        Click anywhere in the report preview
        """
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text("div.autop-amper-ctrl-container", "Product")
        report_obj.select_field_filter_values_dropdown_in_auto_prompt("Product Subcategory:")
        report_obj.select_radio_button_in_auto_prompt_values('Select Values')
        report_obj.select_multiple_filter_values_from_field_auto_prompt(["Blu Ray", "Charger", "Tablet"])
        report_obj.select_auto_prompt_value_back_button()
        
        """
        Step 9 Expected: Verify filter selection appears as below
        """
        expected_value_list="Blu Ray, Charger, Tablet"
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("Product Subcategory:", expected_value_list, "Step 09.01 : Verify selected drop down value")
        report_obj.verify_selected_field_dropdown_value_count_in_autoprompt("Product Subcategory:", "3", "Step 09.02 : Verify selected field dropdown value count in auto prompt")
        
        """
        Step 10 : Click Run with filter values
        """
        report_obj.run_auto_prompt_report()
        report_obj.switch_to_frame("iframe[name='wfOutput']")
        """
        Step 10 Expected: Verify report appears as below
        """
        #report_obj.create_table_data_set("table[summary='Summary']", "C6694058_DataSet_01.xlsx")
        report_obj.verify_html_report_dataset("C6694058_DataSet_01.xlsx", "Step 10.01 : Verify report")
        
        """
        Step 11 : Close IA without saving
        """
        report_obj.switch_to_default_content()
        
        """
        Step 12 :Logout WF using API:
        http://machine_name:port/alias/service/wf_security_logout.jsp
        """
        report_obj.close_ia_without_save()
        
if __name__ == '__main__':
    unittest.main()
