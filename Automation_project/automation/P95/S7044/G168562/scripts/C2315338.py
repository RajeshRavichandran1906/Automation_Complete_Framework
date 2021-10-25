'''
Created on Jan 17, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7044
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2315338
TestCase_Name : Verify Analyst User - Promote to Document
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_report
from common.lib import utillity

class C2315338_TestClass(BaseTestCase):

    def test_C2315338(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        active_reportobj = active_report.Active_Report(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        report_parent_css="TableChart_1"
        run_report_css="ITableData0"
        file_name="C2315338"
        
        def verify_default_active_report_options_dialog(self, label_css, active_report_options_dialog_label_name, msg, bool_val=True):
            input_css = "#userOptions div[id*='"+label_css+"'] input"
            checkbox_obj=utillobj.validate_and_get_webdriver_object(input_css, active_report_options_dialog_label_name)
            act_val=checkbox_obj.is_selected()
            utillobj.asequal(act_val, bool_val, msg)
        
        """
        Step 01: Launch IA Report  using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(master='ibisamp/car', mrid="mriddev", mrpass="mrpassdev", report_css='#resultArea', no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
         
        """
        Step 02: Add fields COUNTRY, CAR & SEATS.
        Select Active Report as the output option.
        """
        report_obj.double_click_on_datetree_item('COUNTRY', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(4)", 'COUNTRY', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('CAR', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(5)", 'CAR', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('SEATS', 1)
        report_obj.wait_for_visible_text("#queryTreeColumn tr:nth-child(3)", 'SEATS', MEDIUM_WAIT_TIME)
        
        """
        Step 02.1: Expect to see the following Active Report preview pane.
        """
        coln_list=['COUNTRY', 'CAR', 'SEATS']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 02.1: Verify column titles")
#         report_obj.create_report_data_set_in_preview(report_parent_css, 10, 3, file_name+"_Ds_01.xlsx")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, file_name+"_Ds_01.xlsx", msg="Step 02.2: Verify report dataset")
        
        """
        Step 03: Click the Format tab. Select Active Report Options.
        Select the Menu Options entry.
        """
        report_obj.change_output_format_type("active_report")
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        report_obj.wait_for_number_of_element('[class*="bi-window active window "]', 1, 10)
        active_reportobj.active_report_options('Menu Options')
        
        """
        Step 03.1: Expect to see the following Active Report Options for User Type of Power.
        """
        verify_default_active_report_options_dialog(self, label_css='showRecordsCheckBox', active_report_options_dialog_label_name='Show Records', msg='Step 03.1: Expect to see Show Records is checked')
        verify_default_active_report_options_dialog(self, label_css='filterCheckBox', active_report_options_dialog_label_name='Filter', msg='Step 03.2: Expect to see Filter is checked')
        verify_default_active_report_options_dialog(self, label_css='freezeCheckBox', active_report_options_dialog_label_name='Freeze', msg='Step 03.3: Expect to see Freeze is checked')
        verify_default_active_report_options_dialog(self, label_css='calcsCheckBox', active_report_options_dialog_label_name='Calculations', msg='Step 03.4: Expect to see Calculations is checked')
        verify_default_active_report_options_dialog(self, label_css='hideUnhideCheckBox', active_report_options_dialog_label_name='Hide/Unhide', msg='Step 03.5: Expect to see Hide/Unhide is checked')
        verify_default_active_report_options_dialog(self, label_css='chartCheckBox', active_report_options_dialog_label_name='Chart', msg='Step 03.6: Expect to see Chart is checked')
        verify_default_active_report_options_dialog(self, label_css='exportCheckBox', active_report_options_dialog_label_name='Export', msg='Step 03.7: Expect to see Export is checked')
        verify_default_active_report_options_dialog(self, label_css='visualizeCheckBox', active_report_options_dialog_label_name='Visualize', msg='Step 03.8: Expect to see Visualize is checked')
        verify_default_active_report_options_dialog(self, label_css='sortingCheckBox', active_report_options_dialog_label_name='Sorting', msg='Step 03.9: Expect to see Sorting is checked')
        verify_default_active_report_options_dialog(self, label_css='rollupCheckBox', active_report_options_dialog_label_name='Rollup', msg='Step 03.10: Expect to see Rollup is checked')
        verify_default_active_report_options_dialog(self, label_css='pivotCheckBox', active_report_options_dialog_label_name='Pivot', msg='Step 03.11: Expect to see Pivot is checked')
        verify_default_active_report_options_dialog(self, label_css='commentsCheckBox', active_report_options_dialog_label_name='Comments', msg='Step 03.12: Expect to see Comments is checked')
        verify_default_active_report_options_dialog(self, label_css='windowTypeCheckBox', active_report_options_dialog_label_name='Window Type', msg='Step 03.13: Expect to see Window Type is checked')
        verify_default_active_report_options_dialog(self, label_css='restoreOrigCheckBox', active_report_options_dialog_label_name='Restore Original', msg='Step 03.14: Expect to see Restore Original is checked')
        verify_default_active_report_options_dialog(self, label_css='sendAsEmailCheckBox', active_report_options_dialog_label_name='Send as Email', msg='Step 03.15: Expect to see Send as Email is checked')
        verify_default_active_report_options_dialog(self, label_css='saveChangesCheckBox', active_report_options_dialog_label_name='Save Changes', msg='Step 03.16: Expect to see Save Changes is checked')
        verify_default_active_report_options_dialog(self, label_css='printCheckBox', active_report_options_dialog_label_name='Print', msg='Step 03.17: Expect to see Print is checked')
        verify_default_active_report_options_dialog(self, label_css='accordionCheckBox', active_report_options_dialog_label_name='Accordion', msg='Step 03.18: Expect to see Accordion is checked')
        verify_default_active_report_options_dialog(self, label_css='advToolsCheckBox', active_report_options_dialog_label_name='Advanced Tools', msg='Step 03.19: Expect to see Advanced Tools is checked')
        verify_default_active_report_options_dialog(self, label_css='gridToolCheckBox', active_report_options_dialog_label_name='Grid Tool', msg='Step 03.20: Expect to see Grid Tool is checked')
        
        """
        Step 04: Change the User Type to Analyst.
        """
        active_reportobj.active_report_options('Menu Options',menu_options=True, menu_value='Analyst')
        
        """
        Step 04.1: Expect to see the following Active Report Options for User Type of Analyst.
        """
        verify_default_active_report_options_dialog(self, label_css='showRecordsCheckBox', active_report_options_dialog_label_name='Show Records', msg='Step 04.1: Expect to see Show Records is checked')
        verify_default_active_report_options_dialog(self, label_css='filterCheckBox', active_report_options_dialog_label_name='Filter', msg='Step 04.2: Expect to see Filter is checked')
        verify_default_active_report_options_dialog(self, label_css='freezeCheckBox', active_report_options_dialog_label_name='Freeze', msg='Step 04.3: Expect to see Freeze is checked')
        verify_default_active_report_options_dialog(self, label_css='calcsCheckBox', active_report_options_dialog_label_name='Calculations', msg='Step 04.4: Expect to see Calculations is checked')
        verify_default_active_report_options_dialog(self, label_css='hideUnhideCheckBox', active_report_options_dialog_label_name='Hide/Unhide', msg='Step 04.5: Expect to see Hide/Unhide is checked')
        verify_default_active_report_options_dialog(self, label_css='chartCheckBox', active_report_options_dialog_label_name='Chart', msg='Step 04.6: Expect to see Chart is checked')
        verify_default_active_report_options_dialog(self, label_css='exportCheckBox', active_report_options_dialog_label_name='Export', msg='Step 04.7: Expect to see Export is checked')
        verify_default_active_report_options_dialog(self, label_css='visualizeCheckBox', active_report_options_dialog_label_name='Visualize', msg='Step 04.8: Expect to see Visualize is checked')
        verify_default_active_report_options_dialog(self, label_css='sortingCheckBox', active_report_options_dialog_label_name='Sorting', msg='Step 04.9: Expect to see Sorting is checked')
        verify_default_active_report_options_dialog(self, label_css='rollupCheckBox', active_report_options_dialog_label_name='Rollup', msg='Step 04.10: Expect to see Rollup is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='pivotCheckBox', active_report_options_dialog_label_name='Pivot', msg='Step 04.11: Expect to see Pivot is checked')
        verify_default_active_report_options_dialog(self, label_css='commentsCheckBox', active_report_options_dialog_label_name='Comments', msg='Step 04.12: Expect to see Comments is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='windowTypeCheckBox', active_report_options_dialog_label_name='Window Type', msg='Step 04.13: Expect to see Window Type is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='restoreOrigCheckBox', active_report_options_dialog_label_name='Restore Original', msg='Step 04.14: Expect to see Restore Original is checked')
        verify_default_active_report_options_dialog(self, label_css='sendAsEmailCheckBox', active_report_options_dialog_label_name='Send as Email', msg='Step 04.15: Expect to see Send as Email is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='saveChangesCheckBox', active_report_options_dialog_label_name='Save Changes', msg='Step 04.16: Expect to see Save Changes is checked')
        verify_default_active_report_options_dialog(self, label_css='printCheckBox', active_report_options_dialog_label_name='Print', msg='Step 04.17: Expect to see Print is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='accordionCheckBox', active_report_options_dialog_label_name='Accordion', msg='Step 04.18: Expect to see Accordion is checked')
        verify_default_active_report_options_dialog(self, label_css='advToolsCheckBox', active_report_options_dialog_label_name='Advanced Tools', msg='Step 04.19: Expect to see Advanced Tools is unchecked', bool_val=False)
        verify_default_active_report_options_dialog(self, label_css='gridToolCheckBox', active_report_options_dialog_label_name='Grid Tool', msg='Step 04.20: Expect to see Grid Tool is unchecked', bool_val=False)
        
        """
        Step 05: Click the OK button.
        Click the Run button.
        Click the drop down for COUNTRY.
        Step 05.1: Expect to see the following Active Report with the User Type options for Analyst.
        """
        active_reportobj.active_report_options('Menu Options', btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element('#ITableData0 > tbody > tr', 11, 10)
        active_reportobj.verify_page_summary(0, '10of10records,Page1of1', "Step 05.1 : Verify Page Summary")
#         active_reportobj.create_active_report_dataset(file_name+"_Ds_02.xlsx", desired_no_of_rows=11, table_css="#ITableData0")
        active_reportobj.verify_active_report_dataset(file_name+"_Ds_02.xlsx", msg="Step 05.2 : Verify runtime report", table_css="#ITableData0", desired_no_of_rows=11)
        expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Pivot (Cross Tab)', 'Hide Column', 'Show Records', 'Save Changes', 'Export', 'Restore Original']
        active_reportobj.verify_menu_items(run_report_css, 0, None, expected_menu_list, msg='Step 05.3: Expect to see the following Active Report with the User Type options for Analyst.')
        report_obj.switch_to_default_content()
        
        """
        Step 06: Close the Run time Report.
        Click the Home tab at the top.
        Click the Document icon.
        """
        report_obj.select_ia_ribbon_item("Home", "document")
        
        """
        Step 06.1: Expect to see the Active Report converted into an Active Document.
        """
        coln_list=['COUNTRY', 'CAR', 'SEATS']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 06.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, file_name+"_Ds_01.xlsx", msg="Step 06.2: Verify report dataset")
        
        """
        Step 07: Click the Run button.
        Click the drop down for COUNTRY.
        Step 07.1: Expect to see the following Active Document with the User Type options for Analyst.
        """
        report_obj.select_ia_toolbar_item('toolbar_run')
        report_obj.switch_to_frame()
        report_obj.wait_for_number_of_element('#ITableData0 > tbody > tr', 11, 10)
        active_reportobj.verify_page_summary(0, '10of10records,Page1of1', "Step 07.1 : Verify Page Summary")
        active_reportobj.verify_active_report_dataset(file_name+"_Ds_02.xlsx", msg="Step 07.2 : Verify runtime report", table_css="#ITableData0", desired_no_of_rows=11)
        expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Pivot (Cross Tab)', 'Hide Column', 'Show Records', 'Save Changes', 'Export', 'Restore Original']
        active_reportobj.verify_menu_items(run_report_css, 0, None, expected_menu_list, msg='Step 07.3: Expect to see the following Active Report with the User Type options for Analyst.')
        report_obj.switch_to_default_content()
        
        """
        Step 08: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()