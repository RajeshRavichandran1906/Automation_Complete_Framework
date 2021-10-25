'''
Created on Jun 19, 2019

@author: Varun/Prasanth
Testcase Name : Reset after AutoPrompt inside IA
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2509906

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.wftools import report
from common.lib import core_utility
from common.wftools.designer_chart import Designer_Insight

class C2509906_TestClass(BaseTestCase):
    
    def test_C2509906(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        report_obj= report.Report(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        insight_obj=Designer_Insight(self.driver)
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=ibisamp/car
        """
        chart_obj.invoke_chart_tool_using_api("ibisamp/car", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2 : Add "CAR"to Horizontal Axis and "DEALER_COST"to Vertical Axis
        """
        chart_obj.double_click_on_datetree_item("CAR", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "CAR")
        chart_obj.double_click_on_datetree_item("DEALER_COST", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel", "DEALER_COST")
        
        """
        STEP 3 : Create a simple parameter filter for "COUNTRY"
        """
        report_obj.drag_and_drop_from_data_tree_to_filter("COUNTRY",1)
        chart_obj.wait_for_visible_text("#dlgWhere", "Create a filtering condition")
        report_obj.open_filter_where_value_dialog()
        chart_obj.wait_for_visible_text("#dlgWhereValue", "Type")
        report_obj.select_filter_type("Parameter")
        report_obj.close_filter_where_value_popup_dialog()
        report_obj.close_filter_dialog()
        
        """
        STEP 4 : Verify following chart with filter displayed
        """
        chart_obj.verify_x_axis_title_in_preview(["CAR"], msg='Step 04.01')
        chart_obj.verify_y_axis_title_in_preview(["DEALER_COST"], msg='Step 04.02')
        expected_x_axis_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg='Step 04.03')
        expected_y_axis_label_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg='Step 04.04')
        
        """
        STEP 5 : Select Format > Run with > Insight
        """
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 6: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """
        STEP 7: Type "ENGLAND" on the Auto Prompt screen 
        """
        chart_obj.enter_value_field_textbox_in_auto_prompt("COUNTRY:", "ENGLAND")
        
        """
        STEP 8: Select the Run icon on the Auto Prompt screen 
        """
        chart_obj.run_auto_prompt_report()
        chart_obj.switch_to_frame("iframe[name='wfOutput']")
        chart_obj.wait_for_visible_text(".main-box", "CAR")
        
        """
        STEP 9 : Verify following chart with filter displayed
        """
        chart_obj.verify_x_axis_title_in_run_window(["CAR"], parent_css=".main-box", msg='Step 09.01')
        chart_obj.verify_y_axis_title_in_run_window(["DEALER_COST"], parent_css=".main-box", msg='Step 09.02')
        expected_x_axis_label_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css=".main-box", msg='Step 09.03')
        expected_y_axis_label_list=['0', '4K', '8K', '12K', '16K', '20K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css=".main-box", msg='Step 09.04')
        
        insight_obj.verify_insight_querybox_text_options(['Vertical Axis', 'Group', 'Color'], "Step 09.05 : Verify_insight_querybox_text_options")
        insight_obj.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 09.06 :verify_insight_optionsbox_text")
        
        
        """
        STEP 10 : Click on the "Reset" button on the Option shelf
        """
        insight_obj.select_insight_optionsbox_in_preview("Reset")
        chart_obj.wait_for_visible_text(".main-box", "CAR")
        
        
        """
        STEP 11 : Verify following chart with filter displayed
        """
        chart_obj.verify_x_axis_title_in_run_window(["CAR"], parent_css=".main-box", msg='Step 11.01')
        chart_obj.verify_y_axis_title_in_run_window(["DEALER_COST"], parent_css=".main-box", msg='Step 11.02')
        expected_x_axis_label_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css=".main-box", msg='Step 11.03')
        expected_y_axis_label_list=['0', '4K', '8K', '12K', '16K', '20K']
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css=".main-box", msg='Step 11.04')
        
        insight_obj.verify_insight_querybox_text_options(['Vertical Axis', 'Group', 'Color'], "Step 11.05 : Verify_insight_querybox_text_options")
        insight_obj.verify_insight_optionsbox_text(['Reset', 'Swap  Axis', 'Change chart', 'Show Filter', 'Swap  Axis', 'More Options'], "Step 11.06 : Verify_insight_optionsbox_text")
        
        """
        STEP 12 : Click IA > Close > click No.
        """
        chart_obj.switch_to_default_content()
        chart_obj.close_ia_without_save()
        
        """
        STEP 13 :Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()
        