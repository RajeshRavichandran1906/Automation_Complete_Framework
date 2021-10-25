"""-------------------------------------------------------------------------------------------
Created on June 11, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22268797
Test Case Title =  Static Filter with BY field
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.lib import global_variables

class C7922374_TestClass(BaseTestCase):

    def test_C7922374(self):
        
        """
            CLASS OBJECTS 
        """
        report_obj = report.Report(self.driver)
        global_var_obj = global_variables.Global_variables()
      
        """
            COMMON TEST CASE VARIABLES 
        """
        case_id = global_var_obj.current_test_case
        live_preview_css = "#TableChart_1"
        qwery_css = "#queryBoxColumn"
        cancel_css = "#dlgWhere_btnCancel"
        resultarea_css = "table[summary]"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        multiple_css = "#id_wv_param_list_mvalues"
        
        """
            STEP 1 : Create new IA report using CAR mas file using API:
        """
        report_obj.invoke_ia_tool_using_new_api_login(master = 'baseapp/car')
        report_obj.wait_for_visible_text(live_preview_css, "Drag and drop")

        """
            STEP 2 : Double click "COUNTRY", "CAR", "SALES"
        """
        report_obj.double_click_on_datetree_item("COUNTRY", 1)
        report_obj.wait_for_visible_text(qwery_css, "COUNTRY")
        
        report_obj.double_click_on_datetree_item("CAR", 1)
        report_obj.wait_for_visible_text(qwery_css, "CAR")
        
        report_obj.double_click_on_datetree_item("SALES", 1)
        report_obj.wait_for_visible_text(qwery_css, "SALES")
        
        """
            STEP 3 : Drag "CAR" to Filter pane
        """
        report_obj.drag_and_drop_from_data_tree_to_filter("CAR", 1)
        report_obj.wait_for_visible_text(cancel_css, "Cancel")

        """
            STEP 4 : Double-click <Value>, Select Type = "Parameter"
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.select_filter_type("Parameter")

        """
            STEP 5 : Select "Static" radio button
        """
        report_obj.select_filter_parameter_type("Static")

        """
            STEP 6 : Click on "Get Values" drop down and select "All"
            STEP 7 : Double click "AUDI", "BMW" and "JAGUAR" values and click OK
        """
        report_obj.select_static_fields_in_filter_dialog("All", ["AUDI", "BMW", "JAGUAR"])
        report_obj.wait_for_visible_text(multiple_css, "JAGUAR")
        
        report_obj.close_filter_where_value_popup_dialog()

        """
            STEP 8 : Click OK in filtering condition dialog
        """
        report_obj.close_filter_dialog()
 
        """
            STEP 9 :Click "Run"
        """
        report_obj.run_report_from_toptoolbar()

        """
            STEP 09.01 :Verify the following auto prompt (CAR = AUDI) is displayed
        """
        report_obj.switch_to_frame()
        report_obj.verify_selected_field_dropdown_value_in_autoprompt("CAR:", "AUDI", "STEP 09.01 :Verify the following auto prompt (CAR = AUDI) is displayed")

        """
            STEP 10 : Click on CAR values
        """
        report_obj.select_field_filter_values_dropdown_in_auto_prompt("CAR:")
        
        """
            STEP 10.01 : Verify only the selected values are available
        """
        
        report_obj.verify_option_type_field_filter_values_in_auto_prompt(["AUDI", "BMW", "JAGUAR"] , "STEP 10.01 : Verify only the selected values are available")
        
        """
            STEP 11 : Select "BMW", click "Run" and click Run with filter values
        """
        report_obj.select_single_field_filter_value_in_auto_prompt(["BMW"])
        report_obj.run_auto_prompt_report()
            
        """
            STEP 11.01 : Verify report appears as below
        """
        report_obj.switch_to_frame("iframe[name='wfOutput']")
        report_obj.wait_for_visible_text(resultarea_css, "COUNTRY")
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1, "STEP 11.01 : Verify report appears as below")
        report_obj.switch_to_default_content()

        """
            STEP 12 : Close IA without saving
        """
        report_obj.close_ia_without_save()

        """
            STEP 13 : Logout WF using API:
        """

if __name__ == '__main__':
    unittest.main()   