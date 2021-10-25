"""-------------------------------------------------------------------------------------------
Created on November 20, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6742419
Test Case Title =  Verify Date prompting
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report

class C6742419_TestClass(BaseTestCase):

    def test_C6742419(self):
        
        """
            CLASS OBJECTS 
        """
        report = Report(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        TESTCASE_ID = "C6742419"
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 60
        SHORT_WAIT_TIME = 30
        DATASET_NAME = TESTCASE_ID + ".DS01.xlsx"
        
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
            STEP 03 : Drag "Sale,Date" field into the Filter pane.
        """
        report.drag_and_drop_from_data_tree_to_filter('Sale,Date', 1)
        report.wait_for_visible_text("#dlgWhere #dlgWhere_btnOK", 'OK', LONG_WAIT_TIME)
         
        """
            STEP 03.1 : Verify Create a filtering condition window opens.
            STEP 04 : Select Parameter in Type dropdown and click OK and OK.
        """
        report.open_filter_where_value_dialog()
        report.select_filter_type('Parameter')
        report.close_filter_where_value_popup_dialog()
        report.close_filter_dialog()
        report.wait_for_visible_text("#qbFilterBox", 'Sale,Date Equal to Simple Parameter (Name: TIME_DATE)', MEDIUM_WAIT_TIME)
        
        """
            STEP 05 : Click Run in toolbar.
        """
        report.run_report_from_toptoolbar()
        report.switch_to_frame()
        report.wait_for_visible_text("#ui-datepicker-div span[title='Monday']", 'Mo', LONG_WAIT_TIME)
        
        """
            STEP 05.1 : Verify autoprompt window appears successfully without error.
        """
        report.verify_autoprompt_field_labels_using_asequal(['Date:'], 'Step 05.01 : Verify autoprompt window appears successfully without error')
        
        """
            STEP 06 : Select September 11, 2016 in Date: control and click submit
        """
        report.select_year_in_calendardatepicker_dialog_in_run_window('2016')
        report.select_month_in_calendardatepicker_dialog_in_run_window('Sep')
        report.select_date_in_calendardatepicker_dialog_in_run_window('11')
        report.run_auto_prompt_report()
        report.switch_to_frame("iframe.autop-wf-output")
        report.wait_for_visible_text("table[Summary]>tbody>tr:nth-child(2)>td:nth-child(2)", '$117,107.04', MEDIUM_WAIT_TIME)
        
        """
            STEP 06.1 : Verify report run successfully.
        """
        #report.create_table_data_set(None, DATASET_NAME)
        report.verify_table_data_set(None, DATASET_NAME, 'Step 06.01 : Verify report run successfully')
        
        """
            STEP 07 : Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        report.api_logout()

if __name__ == '__main__':
    unittest.main()