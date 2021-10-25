'''
Created on January 16, 2019

@author: KK14897

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315316
TestCase Name = Verify Records per Page Default - 57 and Records Per Page values.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility,utillity, javascript
from common.wftools import active_report
from common.wftools import report
from common.wftools import chart
from common.pages import ia_ribbon
import keyboard

class C2315316_TestClass(BaseTestCase):

    def test_C2315316(self):
        
        """
        Test case Object's
        """
        util_obj = utillity.UtillityMethods(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        java_obj=javascript.JavaScript(self.driver)
        report_obj=report.Report(self.driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        '''
        Variables
        '''
        run_css="#ITableData0"
        TestCase_ID='C2315316'
        table_css="TableChart_1"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        Folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        def verify_active_report_options_dialog(self, exp_list, css, dropdown_name):
            dropdown_obj=util_obj.validate_and_get_webdriver_object(css, dropdown_name)
            util_obj.verify_combo_box_item(exp_list, combobox_dropdown_elem=dropdown_obj, msg="step 04")
            core_util_obj.left_click(dropdown_obj)
        
        def verify_default_active_report_options_dialog(self, exp_val, css, input_type, msg, dropdown_name):
            actual_text=util_obj.validate_and_get_webdriver_object(css, dropdown_name)
            actual_text=util_obj.get_attribute_value(actual_text, input_type)
            util_obj.asequal(exp_val, actual_text[input_type].strip(), msg)
                
        '''       
        Step 01 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/movies&item=IBFS:/WFC/Repository/P95/S10142
        '''
        ar_obj.invoke_report_tool_using_api("ibisamp/movies", mrid="mriddev", mrpass="mrpassdev", repository_path=Folder_path)
        
        '''
        Step 02 :Add fields MOVIECODE, TITLE, & LISTPR.
        Select Active Report as the output option.
        '''
        report_obj.double_click_on_datetree_item("MOVIECODE", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 64, 20)
        report_obj.double_click_on_datetree_item("TITLE", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 126, 20)
        report_obj.double_click_on_datetree_item("LISTPR", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 188, 20)
        chart_obj.change_output_format_type("active_report")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 10, 4, TestCase_ID+"_Ds_01.xlsx","Step 2 : Verify Preview")
        
        '''
        Step 03 : Click the Run button.
        Scroll to the bottom.
        Expect to see the following report page information.
        Page 1 of 2 and 60 Records.
        '''
        report_obj.select_ia_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        obj=self.driver.find_element_by_css_selector(run_css+" tbody tr:nth-child(58) td:nth-child(3)")
        java_obj.scrollIntoView(obj)
        ar_obj.verify_page_summary(0, '60of60records,Page1of2', "Step 03 : Verify Page Summary")
        
        '''
        Step 04 : Click the Next Page arrow at the bottom.
        Expect to see the last 3 Records on Page 2.
        '''
        ar_obj.navigate_page("next_page")
        ar_obj.verify_page_summary(0, '60of60records,Page2of2', "Step 04.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_02.xlsx", "Step 04.2 : Verify records", table_css=run_css)
        
        '''
        Step 05 : Click the Format tab and select Active Report Options.
        Expect to see the default Records Per Page at 57.
        '''
        util_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 10)
        verify_default_active_report_options_dialog(self, "57","#generalPane #recordsPerPageCombo input[type='text']","value","Step 5: Verify Pages Default", "Pages")
        
        '''
        Step 06 : Click the down arrow for Records Per Page and select 10.
        Click the OK button.
        Click the Run button.
        Expect to see Page 1 of 6, with 10 records on the first page.
        '''
        ia_ribbon_obj.active_report_options('General',general_record_per_page="10", btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        ar_obj.verify_page_summary(0, '60of60records,Page1of6', "Step 06.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_03.xlsx", "Step 06.2 : Verify records", table_css=run_css)
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 33, 10)
        
        '''
        Step 07 : Click the Format tab and select Active Report Options.
        Click the down arrow for Records Per Page and select 20.
        Click the OK button.
        Click the Run button.
        Scroll down to the bottom of the page.
        Expect to see Page 1 of 3, with 20 records on the page.
        '''
        util_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 10)
        ia_ribbon_obj.active_report_options('General',general_record_per_page="20", btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        ar_obj.verify_page_summary(0, '60of60records,Page1of3', "Step 07.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_04.xlsx", "Step 07.2 : Verify records", table_css=run_css)
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 63, 10)
        
        '''
        Step 08 : Click the Format tab and select Active Report Options.
        Click the down arrow for Records Per Page and select 50.
        Click the OK button.
        Click the Run button.
        Scroll down to the bottom of the page.
        Expect to see Page 1 of 2, with 50 records on the first page.
        '''
        util_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 10)
        ia_ribbon_obj.active_report_options('General',general_record_per_page="50", btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        ar_obj.verify_page_summary(0, '60of60records,Page1of2', "Step 08.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_05.xlsx", "Step 08.2 : Verify records", table_css=run_css)
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 153, 10)
        
        '''
        Step 09 : Click the Next Page arrow at the bottom of the page.
        Expect to see the last 10 Records on Page 2.
        '''
        ar_obj.navigate_page("next_page")
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 33, 10)
        
        '''
        Step 10 : Click the Format tab and select Active Report Options.
        Click in the number area and enter 15.
        Expect to see the custom value of 15 for Records Per Page in the Records Per Page menu.
        '''
        util_obj.switch_to_default_content()
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.set_text_to_textbox_using_keybord("15", text_box_css="#generalPane #recordsPerPageCombo")
        keyboard.press("ENTER")
        verify_default_active_report_options_dialog(self, "15","#generalPane #recordsPerPageCombo input[type='text']","value","Step 10.1: Verify Pages Default", "Pages")
        
        '''
        Step 11 : Click the OK button.
        Click the Run button.
        Expect to see Page 1 of 4, with 15 records on the first page.
        '''
        ia_ribbon_obj.active_report_options('General', btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        core_util_obj.switch_to_frame()
        ar_obj.verify_page_summary(0, '60of60records,Page1of4', "Step 11.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_07.xlsx", "Step 11.2 : Verify records", table_css=run_css)
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 48, 10)
        
        '''
        Step 12 : Click the Last Page arrow at the bottom of the page.
        Expect to see the last page, Page 4, with 15 records.
        '''
        ar_obj.navigate_page('last_page')
        ar_obj.verify_page_summary(0, '60of60records,Page4of4', "Step 12.1 : Verify Page Summary")
        ar_obj.verify_active_report_dataset(TestCase_ID+"_Ds_08.xlsx", "Step 12.2 : Verify records", table_css=run_css)
        util_obj.synchronize_with_number_of_element('[onmouseover*="setCurCell"]', 48, 10)
        
        '''
        Step 13 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        '''
        
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()