'''
Created on Jun 10, 2019

@author: Sudhan/Pearlson Joyal

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6693931
TestCase Name = Report with simple prompt
'''
import unittest
from common.wftools import report
from common.lib.basetestcase import BaseTestCase


class C6693931_TestClass(BaseTestCase):

    def test_C6693931(self):
        """
            CLASS OBJECTS 
        """
        report_ = report.Report(self.driver)
        
        """
            TESTCASE ID Variable 
        """
        case_id = 'C6693931'
        table_css="table[summary='Summary']"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        tablechart_css = "#TableChart_1"
        querypane_css = " #queryBoxColumn"
        cancel_css = "#dlgWhere_btnCancel"
        
        """
            STEP 1 : Create new IA report using WF_retail_lite mas file using API:
            http://machine_name:port/alias/ia?tool=Report&master=baseapp/WF_RETAIL_LITE&item=IBFS:/WFC/Repository/P292_S10117/G636265
        """
        report_.invoke_ia_tool_using_new_api_login(master='baseapp/wf_retail_lite')
        report_.wait_for_visible_text(tablechart_css, "Drag and drop")

        """
            STEP 2 : Double click on "Product,Category" and "Revenue" fields
        """      
        report_.double_click_on_datetree_item('Product,Category', 1)
        report_.wait_for_visible_text(querypane_css, "Product,Category")
        
        report_.double_click_on_datetree_item('Revenue', 1)
        report_.wait_for_visible_text(querypane_css, "Revenue")
        
        """
            STEP 3 : Drag "Product,Category" field into the Filter pane
        """
        report_.drag_and_drop_from_data_tree_to_filter('Product,Category',1)
        report_.wait_for_visible_text(cancel_css, "Cancel")
        
        """
            STEP 4 : Double click on Value;
            Click on Type drop down and select Parameter (Simple) and click OK
        """
        report_.open_filter_where_value_dialog()
        report_.select_filter_type("Parameter")
        report_.select_filter_parameter_type("Simple")
        report_.close_filter_where_value_popup_dialog()
 
        """
            STEP 5 : Click OK
        """
        report_.close_filter_dialog()

        """
            STEP 6 : Click Run in toolbar
        """
        report_.run_report_from_toptoolbar()
        report_.wait_for_number_of_element("[id^='ReportIframe']",1)
        
        """
            STEP 6.01 : Verify Auto prompt window appears with simple filter prompt as below
        """
        report_.switch_to_frame()
        report_.verify_autoprompt_field_labels_using_asequal(['Product Category:'], 'Step 6.01 : Verify autoprompt field labels') 
        report_.verify_field_textbox_value_in_autoprompt("Product Category:", "Product Category:","Step 6.01 : Verify Auto prompt window appears with simple filter prompt")
        
        """
            STEP 7 : Type "Computers" under Filter Values text box (Product Category) and click Run with filter values
        """
        report_.enter_value_field_textbox_in_auto_prompt("Product Category:", "Computers")
        report_.run_auto_prompt_report()
        report_.wait_for_number_of_element("iframe[name='wfOutput']",1)
        
        """
            STEP 7.01 : Verify results displayed without error in Auto prompt window as below
        """
        report_.switch_to_frame("iframe[name='wfOutput']")
        report_.wait_for_visible_text(table_css, "Revenue")
        #report_.create_html_report_dataset(DATA_SET_NAME1)
        report_.verify_html_report_dataset(DATA_SET_NAME1,"Verify results displayed without error in Auto prompt window")
        report_.switch_to_default_content()

        """
            STEP 8 : Close IA without saving
`       """
        report_.close_ia_without_save()
 
        """
            STEP 9 : Logout WF using API:
            http://machine_name:port/alias/service/wf_security_logout.jsp
        """       
        report_.api_logout()
        
if __name__ == '__main__':
    unittest.main()