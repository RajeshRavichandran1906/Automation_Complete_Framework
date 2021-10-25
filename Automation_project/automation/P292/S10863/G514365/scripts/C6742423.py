"""-------------------------------------------------------------------------------------------
Created on November 21, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6742423
Test Case Title =  Verify chaining feature for variables within a dimensional hierarchy
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C6742423_TestClass(BaseTestCase):

    def test_C6742423(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        TESTCASE_ID = self.__class__.__name__.strip().split('_')[0]
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 60
        SHORT_WAIT_TIME = 30
        DATASET_NAME1 = TESTCASE_ID + "_DS01.xlsx"
        DATASET_NAME2 = TESTCASE_ID + "_DS02.xlsx"
        
        """
            STEP 01 : Create new IA report using WF_retail_lite
            http://machine:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10863%2FG514365&tool=report&master=baseapp/wf_retail_lite
        """
        report.invoke_ia_tool_using_new_api_login(master='baseapp/wf_retail_lite')
        report.wait_for_visible_text("#queryTreeColumn table>tbody>tr:nth-child(2)", 'Sum', LONG_WAIT_TIME)
        
        """
            STEP 02 : Double click "Product,Category" and "Revenue" fields.
        """
        report.double_click_on_datetree_item('Product,Category', 1)
        report.wait_for_visible_text("#queryTreeColumn table>tbody>tr:nth-child(4)", 'Product,Category', SHORT_WAIT_TIME)
        
        report.double_click_on_datetree_item('Revenue', 1)
        report.wait_for_visible_text("#queryTreeColumn table>tbody>tr:nth-child(3)", 'Revenue', SHORT_WAIT_TIME)
        
        """
            STEP 02.1 : Verify the following report is displayed.
        """
        #report.create_report_data_set_in_preview('TableChart_1', 8, 2, DATASET_NAME1)
        report.verify_report_data_set_in_preview('TableChart_1', 8, 2, DATASET_NAME1, 'Step 02.01 : Verify the report is displayed')
        report.verify_report_column_titles_on_preview(4, 4, ['Product', '', 'Category', 'Revenue'], msg='Step 02.02 : Verify report column title')
        
        """
            STEP 03 : Drag "Product,Category" field into the Filter pane.
        """
        report.drag_and_drop_from_data_tree_to_filter('Product,Category', 1)
        report.wait_for_visible_text("#dlgWhere #dlgWhere_btnOK", 'OK', LONG_WAIT_TIME)
         
        """
            STEP 04 : Select Parameter in Type dropdown and select Dynamic radio button and click OK and OK.
        """
        report.open_filter_where_value_dialog()
        report.select_filter_type('Parameter')
        report.select_filter_parameter_type('Dynamic')
        report.close_filter_where_value_popup_dialog()
        report.close_filter_dialog()
        report.wait_for_visible_text("#qbFilterBox", 'Product,Category Equal to Dynamic Parameter (Name: PRODUCT_CATEGORY, Field: PRODUCT_CATEGORY in WF_RETAIL_LITE) Sort Ascending', MEDIUM_WAIT_TIME)
        
        """
            STEP 05 : Drag "Product,Subcategory" field into the Filter pane.
        """
        report.drag_and_drop_from_data_tree_to_filter('Product,Subcategory', 1)
        report.wait_for_visible_text("#dlgWhere #dlgWhere_btnOK", 'OK', LONG_WAIT_TIME)
        
        """
            STEP 06 : Select Parameter in Type dropdown and select Dynamic radio button and click OK and OK.
        """
        report.open_filter_where_value_dialog(rownum=3)
        report.select_filter_type('Parameter')
        report.select_filter_parameter_type('Dynamic')
        report.close_filter_where_value_popup_dialog()
        report.close_filter_dialog()
        report.wait_for_number_of_element("#qbFilterBox table tr", 3, MEDIUM_WAIT_TIME)
        
        """
            STEP 07 : Drag "Model" field into the Filter pane.
        """
        report.drag_and_drop_from_data_tree_to_filter('Model', 1)
        report.wait_for_visible_text("#dlgWhere #dlgWhere_btnOK", 'OK', LONG_WAIT_TIME)
        
        """
            STEP 08 : Select Parameter in Type dropdown and select Dynamic radio button and click OK and OK.
        """
        report.open_filter_where_value_dialog(rownum=4)
        report.select_filter_type('Parameter')
        report.select_filter_parameter_type('Dynamic')
        report.close_filter_where_value_popup_dialog()
        report.close_filter_dialog()
        report.wait_for_number_of_element("#qbFilterBox table tr", 4, MEDIUM_WAIT_TIME)
        
        """
            STEP 09 : Click Run in toolbar.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text("#promptPanel .autop-amper-select label", 'Product Category:', LONG_WAIT_TIME)
        
        """
            STEP 09.1 : Verify Autoprompt window appears successfully with chaining feature enabled.
        """
        report.verify_autoprompt_field_labels_using_asequal(['Product Category:', 'Product Subcategory:', 'Product Model:'], 'Step 09.01 : Verify autoprompt filed labels')
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Category:', 'Accessories', 'Step 09.02 : Verify default selected value for Product Category')
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Subcategory:', 'Charger', 'Step 09.03 : Verify default selected value for Product Subcategory')
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Model:', 'B00D7MOHDO', 'Step 09.04 : Verify default selected value for Product Product Model')
        report.verify_filter_chained_group_icon_is_visible_in_autoprompt('Step 09.05 : Verify Autoprompt window appears successfully with chaining feature enabled')
        
        """
            STEP 10 : Select "Computers" in Product Category: dropdown.
        """
        report.select_field_filter_values_dropdown_in_auto_prompt('Product Category:')
        report.select_single_field_filter_value_in_auto_prompt(['Computers'])
        
        """
            STEP 10.1 : Verify both Product Subcategory: and Product Model: dropdowns are updated with fields related to Computers.
        """
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Category:', 'Computers', 'Step 10.01 : Verify dropdown selected value for Product Category')
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Subcategory:', 'Smartphone', 'Step 10.02 : Verify dropdownselected value for Product Subcategory')
        report.verify_selected_field_dropdown_value_in_autoprompt('Product Model:', 'C6506B', 'Step 10.03 : Verify dropdown selected value for Product Product Model')
        
        """
            STEP 11 : Click Run with filter values.
        """
        report.run_auto_prompt_report()
        report.switch_to_frame("iframe.autop-wf-output")
        report.wait_for_visible_text("table[Summary]>tbody>tr:nth-child(2)>td:nth-child(2)", '$8,159,907.03', MEDIUM_WAIT_TIME)
        
        """
            STEP 11.1 : Verify report run successfully.
        """
        #report.create_table_data_set(None, DATASET_NAME2)
        report.verify_table_data_set(None, DATASET_NAME2, 'Step 11.01 : Verify report run successfully')
        
        """
            STEP 12 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()

if __name__ == '__main__':
    unittest.main()