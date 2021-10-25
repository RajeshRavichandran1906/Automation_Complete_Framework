'''
Created on January 17, 2019

@author: KK14897

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315339
TestCase Name = Verify Active Report Options Advanced Tab
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import core_utility,utillity
from common.wftools import active_report
from common.wftools import report
from common.wftools import chart
from common.pages import ia_ribbon
import keyboard

class C2315339_TestClass(BaseTestCase):

    def test_C2315339(self):
        
        """
        Test case Object's
        """
        util_obj = utillity.UtillityMethods(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        report_obj=report.Report(self.driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(self.driver)
        chart_obj=chart.Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        '''
        Variables
        '''
        TestCase_ID='C2315339'
        table_css="TableChart_1"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        Folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        def verify_active_report_options_dialog_advanced_tab(self, exp_list, css, dropdown_name):
            dropdown_obj=util_obj.validate_and_get_webdriver_object(css, dropdown_name)
            util_obj.verify_combo_box_item(exp_list, combobox_dropdown_elem=dropdown_obj, msg="step 04")
            core_util_obj.left_click(dropdown_obj)
        
        def verify_default_active_report_options_dialog_advanced_tab(self, textbox_value, css, msg, itype=None, tbox="input_box", **kwargs): 
            if (tbox == "input_box"):
                actual_obj=util_obj.validate_and_get_webdriver_object(css, msg)
                actual_obj=util_obj.get_attribute_value(actual_obj, itype)
                util_obj.asequal(textbox_value, actual_obj[itype].strip(), msg)

            if kwargs['radio_button']==False:
                try:
                    actual_obj=util_obj.validate_and_get_webdriver_object("#advancedPane #securityDateRadioBtn input", "date button")
                    actual_obj=actual_obj.get_attribute("disabled")
                    util_obj.asequal('true', actual_obj, "Step 3.2 : Date Radio button disabled")
                except:
                    print ("Date Radio button enabled")
                try:
                    actual_obj=util_obj.validate_and_get_webdriver_object("#advancedPane #securityDaysRadioBtn input", "days button")
                    actual_obj=actual_obj.get_attribute("disabled")
                    util_obj.asequal('true', actual_obj, "Step 3.3 : Days Radio button disabled")
                except:
                    print ("Days Radio button enabled")
                    
            if 'advanced_expiration' in kwargs:
                if kwargs['advanced_expiration']==True:
                    status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                    util_obj.asequal(True, status, "Step 3.4 : Verify Expiration is unchecked previously.")
                if kwargs['advanced_expiration']==False:
                    status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                    util_obj.asequal(False, status, "Step 3.4 : Verify Expiration is checked previously.")
        '''
        Step 01 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Reportt&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7044/G168564
        '''
        ar_obj.invoke_report_tool_using_api("ibisamp/car", mrid="mriddev", mrpass="mrpassdev", repository_path=Folder_path)
        
        '''
        Step 02 :Select Active Report as the output option.
        Add fields COUNTRY, CAR, DEALER_COST & RETAIL_COST.
        Expect to see the following Active Report Preview pane.
        '''
        chart_obj.change_output_format_type("active_report")
        report_obj.double_click_on_datetree_item("COUNTRY", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 7, 20)
        report_obj.double_click_on_datetree_item("CAR", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 18, 20)
        report_obj.double_click_on_datetree_item("DEALER_COST", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 29, 20)
        report_obj.double_click_on_datetree_item("RETAIL_COST", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 40, 20)
#         report_obj.create_report_data_set_in_preview("TableChart_1", 9, 4, TestCase_ID+"_Ds_01.xlsx")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 9, 4, TestCase_ID+"_Ds_01.xlsx","Step 2.1 : Verify Preview")
        
        
        '''
        Step 03 : Click the Format tab at the top.
        Select Active Report Options.
        Click the Advanced row from the option list.
        Expect to see the following options for the Advanced settings.
        '''
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window"]', 1, 10)
        ia_ribbon_obj.active_report_options('Advanced')
        
        verify_default_active_report_options_dialog_advanced_tab(self,'100',"#advancedPane #rowsRetrievedCombo input[type='text']","Row_Retrieve",itype="value",advanced_expiration=False,radio_button=False)
        
        '''
        Step 04 : Click the drop down in the Active Cache area for 
        Rows Retrieved.
        Expect to see the following options for Rows Retrieved. The default value is 100. 
        Also verify that the Password is blank by default.
        The Expiration box should be unchecked.
        Step 05 : Change the value to 500.
        In the Security area, enter Password - 'pass500'.
        Check the box for Expiration.
        Expect to see the following options set for the Advanced tab.
        '''
        verify_default_active_report_options_dialog_advanced_tab(self,'',"#advancedPane #advSecurityPassHBox  input", "Row_Retrieve",itype="value")
        verify_default_active_report_options_dialog_advanced_tab(self,'100',"#advancedPane #rowsRetrievedCombo input[type='text']","Row_Retrieve",itype="value",advanced_expiration=False,radio_button=False)
        ia_ribbon_obj.active_report_options("Advanced",advanced_rows_retrieved="500")
        util_obj.set_text_to_textbox_using_keybord("pass500", text_box_css="#advancedPane #advSecurityPassHBox  input")
        ia_ribbon_obj.active_report_options("Advanced",advanced_expiration=True)
        
        '''
        Step 06 :Click OK for the Advanced options.
        Click the Run button.
        Expect to see the following Password text box appear.
        '''
        ia_ribbon_obj.active_report_options('Advanced', btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        
        '''
        Step 07 :Enter 'pass500' into the Password box.
        Expect to see the following Active Report.

        '''
        report_obj.switch_to_frame()
        util_obj.set_text_to_textbox_using_keybord("pass500", text_box_css="#PromptTable1 input")
        keyboard.press("ENTER")
        util_obj.switch_to_main_window()
        
        '''
        Step 08 : Click the Show Code button at the top.
        Scroll to the bottom of the code.
        Expect to see the Cachelines set to 500, via the line
        ON TABLE SET CACHELINES 500
        and the Password set to 'pass500' via the line
        ON TABLE SET ARPASSWORD pass500
        '''
        expected_syntax_list=["ON TABLE SET CACHELINES 500","ON TABLE SET ARPASSWORD pass500"]
        report_obj.verify_fexcode_syntax(expected_syntax_list, "STep 08 : Verify fex code")
        
        '''
        Step 09 : Click the Home tab.
        Click the Format tab.
        Click the Pages on Demand icon.
        Expect to see the Pages on Demand button highlighted, indicating that Cache has been activated.
        '''
        report_obj.switch_ia_ribbon_tab("Home")
        report_obj.select_ia_ribbon_item("Format", "pages_on_demand")
        web_element=self.driver.find_element_by_css_selector("#FormatReportPod[class*='checked']")
        util_obj.verify_checked_class_property(web_element,"Step 09: verify Page on demand is highlighted") 
        
        '''
        Step 10 :Click the Show Code button at the top.
        Expect to see Cache mode activated by the presence of the line at the top:
        SET WEBVIEWER=ON
        '''
        expected_syntax_list=["SET WEBVIEWER=ON"]
        report_obj.verify_fexcode_syntax(expected_syntax_list, "STep 10 : Verify fex code")
        
        '''
        Step 11 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        '''
        report_obj.api_logout()
         
        
if __name__ == '__main__':
    unittest.main()