"""-------------------------------------------------------------------------------------------
Created on June 10, 2019
@author: Aftab/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6735628
Test Case Title =  Optional (_FOC_NULL) prompting fields
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.lib import global_variables

class C6735628_TestClass(BaseTestCase):

    def test_C6735628(self):
        
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
        
        """
            STEP 1 : Create new IA report using wf_retail_lite mas file using API:
        """
        report_obj.invoke_ia_tool_using_new_api_login(master = 'baseapp/wf_retail_lite')
        report_obj.wait_for_visible_text(live_preview_css, "Drag and drop")

        """
            STEP 2 : Double click add "Product,Category" and "Revenue" fields.
        """
        report_obj.double_click_on_datetree_item("Product,Category", 1)
        report_obj.wait_for_visible_text(qwery_css, "Product,Category")
        
        report_obj.double_click_on_datetree_item("Revenue", 1)
        report_obj.wait_for_visible_text(qwery_css, "Revenue")

        """
            STEP 3 : Drag "Product,Subcategory" field to the Filter pane
        """
        report_obj.drag_and_drop_from_data_tree_to_filter("Product,Subcategory", 1)
        report_obj.wait_for_visible_text(cancel_css, "Cancel")
        
        """
            STEP 4 : Select Parameter in Type dropdown.
        """
        report_obj.open_filter_where_value_dialog()
        report_obj.select_filter_type("Parameter")
        
        """
            STEP 5 : Check Optional checkbox and click OK
        """
        report_obj.select_filter_parameter_checkbox(ParamOptional = True)
        report_obj.close_filter_where_value_popup_dialog()
        
        """
            STEP 6 : Click OK in filtering condition dialog
        """
        report_obj.close_filter_dialog()
 
        """
            STEP 7 : Click Run in toolbar
        """
        report_obj.run_report_from_toptoolbar()
        
        """
            STEP 7.01 : Verify report appears as below
        """
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(resultarea_css, "Revenue")
        #report_obj.create_html_report_dataset(DATA_SET_NAME1)
        report_obj.verify_html_report_dataset(DATA_SET_NAME1, "STEP 7.01 : Verify report appears as below")
        report_obj.switch_to_default_content()
        
        """
            STEP 8 : Close IA without saving
        """
        report_obj.close_ia_without_save()
 
        """
            STEP 9 : Logout WF using API:
        """

if __name__ == '__main__':
    unittest.main()
        