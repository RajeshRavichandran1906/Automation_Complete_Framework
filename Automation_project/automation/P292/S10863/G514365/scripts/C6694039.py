'''
Created on Nov 14, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6694039&group_by=cases:section_id&group_id=514365&group_order=asc
Testcase Name : Verify combinations of filter prompt
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report

class C6694039_TestClass(BaseTestCase):

    def test_C6694039(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID="C6694039"
        report_obj=report.Report(self.driver)
        
        folder_name='P292_S10863/G514365'
        fex_name='C6694039'
        autoprompt_field_labels=['CAR:', 'MODEL:', 'Min MPG:', 'Max MPG:', 'COUNTRY:']
       
        """
            Step 01: Run uploaded C6694039.fex using API:
            http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10117%252FG456746%252F&BIP_item=C6694039.fex
        """

        report_obj.run_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass', run_table_css=".autop-pane div[class^='autop-navbar'] a[title^='Run']")
        
        """
            Verify report run successfully.
        """
        expected_selected_value1='ALFA ROMEO'
        expected_selected_value2='All Values'
        report_obj.verify_autoprompt_field_labels_using_asequal(autoprompt_field_labels, "Step 01:01: Verify ALFA ROMEO is displayed in auto prompt")
        report_obj.verify_selected_field_dropdown_value_in_autoprompt('CAR:', expected_selected_value1, "Step 01:01: Verify default selected value in CAR field drop down")
        report_obj.verify_selected_field_dropdown_value_in_autoprompt('MODEL:', expected_selected_value2, "Step 01:02: Verify default selected value in MODEL field drop down")
        report_obj.verify_field_textbox_value_in_autoprompt('Min MPG:', '10', "Step 01:03: Verify MIN value in auto prompt")
        report_obj.verify_field_textbox_value_in_autoprompt('Max MPG:', '20', "Step 01:04: Verify MAX value in auto prompt")
        report_obj.verify_field_textbox_value_in_autoprompt('COUNTRY:', 'COUNTRY:', "Step 01:05: Verify COUNTRY value in auto prompt")
        
        """
            Step 02: Click CAR: static dropdown.
        """
        report_obj.select_field_filter_values_dropdown_in_auto_prompt('CAR')
        
        """
            Verify list of values available.
        """
        expected_value_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'TOYOTA', 'TRIUMPH']
        report_obj.verify_option_type_field_filter_values_in_auto_prompt(expected_value_list, "Step 02:01:Verify filter values in field auto prompt")
        
        """
            Step 03: Select "BMW" in CAR dropdown.
        """
        report_obj.select_single_field_filter_value_in_auto_prompt(['BMW'])
        
        """
            Verify selected condition applied.
        """
        report_obj.verify_selected_field_dropdown_value_in_autoprompt('CAR:', 'BMW', "Step 03: Verify selected field CAR: drop down value BMW is selected")
        
        """
            Step 04: Select MODEL: dynamic dropdown.
        """
        report_obj.select_field_filter_values_dropdown_in_auto_prompt('MODEL')
        
        """
            Verify list of values available.
        """
        expected_value_list=['All Values', '2002 2 DOOR', '2002 2 DOOR AUTO', '3.0 SI 4 DOOR', '3.0 SI 4 DOOR AUTO', '530I 4 DOOR', '530I 4 DOOR AUTO']
        report_obj.verify_option_type_field_filter_values_in_auto_prompt(expected_value_list, "Step 04:01:Verify filter values in field auto prompt")
        
        """
            Step 05: Multi-select last four values in dropdown and click outside the dropdown.
        """
        multi_field_value_list=['530I 4 DOOR AUTO','530I 4 DOOR','3.0 SI 4 DOOR AUTO','3.0 SI 4 DOOR']
        report_obj.select_multiple_filter_values_from_field_auto_prompt(multi_field_value_list)
        report_obj.select_close_button_in_field_filter_values_in_auto_prompt()
        
        """
            Verify selected condition applied.
        """
        expected_selected_value='3.0 SI 4 DOOR, 3.0 SI 4 DOOR AUTO, 530I 4 DOOR, 530I 4 DOOR AUTO'
        report_obj.verify_selected_field_dropdown_value_in_autoprompt('MODEL:',expected_selected_value, "Step 05:01: Verify selected")
        
        """
            Step 06:Enter "W GERMANY" in COUNTRY:.
        """
        
        report_obj.enter_value_field_textbox_in_auto_prompt('COUNTRY:','W GERMANY')
        
        """
            Step 07:Click Run with filter values.
        """
        report_obj.run_auto_prompt_report()
        report_obj.wait_for_number_of_element("[name='wfOutput']", 1, 60)
        report_obj.switch_to_frame(frame_css="[name='wfOutput']")
#         report_obj.create_table_data_set("table", Test_Case_ID+"_Ds01.xlsx")
        
        """
            Verify report run successfully.
        """
        report_obj.verify_table_data_set("table", Test_Case_ID+"_Ds01.xlsx", "Step 07:01: Verify report data at runtime")
        
        """
            Step 08: Logout WF using API:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()