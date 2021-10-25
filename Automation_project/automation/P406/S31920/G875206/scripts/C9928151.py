"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 16th January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
import keyboard
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage
from common.lib.javascript import JavaScript


class C9928151_TestClass(BaseTestCase):
    
    def test_C9928151(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        j_script = JavaScript(self.driver)

        """
        TESTCASE VARIABLES
        """
        tooltip_css = "div[id^= 'BiPopup']:not([disabled='true'])[style*='inherit']"
        drop_down_css = "#ScheduleEditor_btnItemTasksNew div[id^='BiToolBarMenuButton']"
        final_save_css = "#IbfsOpenFileDialog7_btnOK"
        dialog_ok_css = "#OccurrenceDlg_btnOK"
        task_dialog_css = "#rcBiTaskDlg .bi-window"
        browse_button_css = "#TaskStandardReportPane_procBrowseButton"
        webfocus_report_css = ".bi-menu-table tbody tr:nth-child(2)"
        distribution_email_css = ".bi-menu[style*='inherit']  .bi-menu-table tbody tr:nth-child(2)"
        schedule_dialog_css = "#rcBiOccurrenceDlg"
        ibfs_css = "#dlgIbfsOpenFile7"
        password_dialog_css = "#rcBiTaskPasswordDlg"
        password_dialog_ok_css = "#TaskPasswordDlg_btnOK"
        password_css = "#TaskStandardReportPane_execpassButton"
        execution_id_css = "#TaskStandardReportPane_execidListComboBox"
        new_button_css = "#ScheduleEditor_btnItemRecurrenceNew"
        property_title_css = "#ScheduleEditor_nameTextField"
        task_dialog_ok_css = "#TaskDlg_btnOK"
        first_password_css = "#TaskPasswordDlg_firstPasswordField"
        confirm_password_css = "#TaskPasswordDlg_confirmPasswordField"
        distribution_dialog_css = "#rcBiDistributeDlg"
        distribution_dialog_ok_css = "#DistributeDlg_btnOK"
        save_and_close_css = "#ScheduleEditor_btnSaveClose"
        
        def editor_box_click(show_name):
            group_css="#ScheduleEditor_groupShowVBox [id*='ScheduleEditor']"
            total_objects = utils.validate_and_get_webdriver_objects(group_css, 'test')
            element_obj = total_objects[j_script.find_element_index_by_text(total_objects, show_name)]
            core_utils.left_click(element_obj)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        utils.capture_screenshot('01.00',Step_01)
        
        Step_02 = """
            Step 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot('02.00',Step_02)
        
        Step_03 = """
            Step 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9928151')
        utils.capture_screenshot('03.00',Step_03)
        
        Step_04 = """
            Step 04 :Click on 'Schedule' category button > Click on 'Schedule' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab("SCHEDULE")
        HomePage.Workspaces.ActionBar.select_tab_option("Schedule")
        HomePage.Workspaces.switch_to_default_content()
        core_utils.switch_to_new_window()
        utils.capture_screenshot('04.00',Step_04)
        
        Step_04_01  = """
            Verify that 'Untitled - Schedule' opens in a new tab
        """
        utils.verify_current_tab_name("Untitled - TIBCO WebFOCUS Schedule","Step 04.01 'Untitled - Schedule' opens in a new tab ")
        utils.capture_screenshot('04.01',Step_04_01,expected_image_verify=True)
        
        Step_05 = """
            Step 05 : Enter title as 'C9928151' in properties tab.
        """
        utils.set_text_to_textbox_using_keybord('C9928151', property_title_css)
        utils.capture_screenshot('05.00',Step_05)
        
        Step_06 = """
            Step 06 : Click on 'Recurrence' tab > Click on 'New' > Click OK
        """
        editor_box_click('Recurrences')
        new_button = utils.validate_and_get_webdriver_object(new_button_css, "new-button")
        core_utils.python_left_click(new_button)
        utils.synchronize_with_number_of_element(schedule_dialog_css, 1, 120)
        ok_button = utils.validate_and_get_webdriver_object(dialog_ok_css, "ok-button")
        core_utils.python_left_click(ok_button)
        utils.capture_screenshot('06.00',Step_06,expected_image_verify=True)
        
        Step_07 = """
            STEP 07 Click on 'Tasks' tab > Click on 'New' dropdown > WenFOCUS report > Click on browse button from 'Procedure' > 
            Double click on 'Report' folder > Select 'Sales Metrics YTD' > Click Open
        """
        editor_box_click('Tasks')
        drop_down_button = utils.validate_and_get_webdriver_object(drop_down_css,"drop-down")
        core_utils.left_click(drop_down_button)
        utils.synchronize_with_number_of_element(tooltip_css,1, 120)
        webreport_obj =utils.validate_and_get_webdriver_object(webfocus_report_css, "web-report")
        core_utils.left_click(webreport_obj)
        utils.synchronize_with_number_of_element(task_dialog_css, 1, 120)
        browse_button = utils.validate_and_get_webdriver_object(browse_button_css, 'browse-button')
        core_utils.left_click(browse_button )
        utils.synchronize_with_number_of_element(ibfs_css, 1, 120)
        utils.select_masterfile_in_open_dialog("Retail Samples->Reports", 'Sales Metrics YTD')
        utils.synchronize_with_number_of_element(task_dialog_css, 1, 120)
        utils.capture_screenshot('07.00',Step_07)
        
        Step_08 = """
        Enter 'Execution ID' as srvadmin and Password > Enter Password and Confirm Password as 'srvadmin' and Click OK.
        """
        utils.set_text_to_textbox_using_keybord('srvadmin', execution_id_css)
        password_button = utils.validate_and_get_webdriver_object(password_css, "password-css")
        core_utils.left_click(password_button)
        utils.synchronize_with_number_of_element(password_dialog_css, 1, 120)
        utils.set_text_to_textbox_using_keybord('srvadmin', first_password_css)
        keyboard.press('tab')
        utils.set_text_to_textbox_using_keybord('srvadmin', confirm_password_css)
        password_ok_button = utils.validate_and_get_webdriver_object(password_dialog_ok_css, "password-ok-css")
        core_utils.left_click(password_ok_button)
        utils.synchronize_with_number_of_element(task_dialog_css, 1,120)
        utils.capture_screenshot('08.00',Step_08)
        
        Step_09 = """
        Click OK.Then, Click on 'Distribution' tab Enter To: valid email ID (Eg: rcadmin1@ibi.com) and Click OK.
        """
        task_ok_button = utils.validate_and_get_webdriver_object(task_dialog_ok_css, "task-ok")
        core_utils.left_click(task_ok_button)
        editor_box_click('Distributions')
        drop_down_button = utils.validate_and_get_webdriver_object(drop_down_css,"drop-down")
        core_utils.python_left_click(drop_down_button)
        utils.synchronize_with_number_of_element(tooltip_css,1, 120)
        email_obj =utils.validate_and_get_webdriver_object(distribution_email_css, "email")
        core_utils.left_click(email_obj)
        utils.synchronize_with_number_of_element(distribution_dialog_css, 1 , 120)
        utils.set_text_to_textbox_using_keybord('rcadmin1@ibi.com', '#DistributeEmailPane_mailToTextField')
        utils.set_text_to_textbox_using_keybord('rcadmin1@ibi.com', '#DistributeEmailPane_mailReplyTextField')
        distribution_ok_button = utils.validate_and_get_webdriver_object(distribution_dialog_ok_css, "distribution-ok-css")
        core_utils.left_click(distribution_ok_button)
        utils.capture_screenshot('09.00',Step_09)

        Step_10 = """
        Click 'Save&Close' button > Click 'Save'
        """
        save_close_button = utils.validate_and_get_webdriver_object(save_and_close_css, "save-close-css")
        core_utils.left_click(save_close_button)
        utils.synchronize_with_visble_text(final_save_css, 'Save', 15)
        save_button = utils.validate_and_get_webdriver_object(final_save_css, "save-css")
        core_utils.left_click(save_button)
        core_utils.switch_to_previous_window(window_close=False)
        utils.capture_screenshot('10.00',Step_10)
        
        Step_10_01 = """
        Verify that 'C9928151' schedule is created
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(["C9928151"],'10.01')
        utils.capture_screenshot('10.01',Step_10_01,expected_image_verify=True)
    
        Step_11 = """
        Right click on 'C9928151' > Delete
        """
        HomePage.Workspaces.ContentArea.delete_file('C9928151')
        utils.capture_screenshot('11.00',Step_11)
        
        Step_11_01 = """
        Verify that 'C9928151' schedule gets deleted
        """
        HomePage.Workspaces.ContentArea.verify_files(["C9928151"],'11.01',assert_type="asnotin")
        utils.capture_screenshot('11.00',Step_11_01)
        
        Step_12 = """
            Step 12 : In the banner link, Click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('12.00',Step_12)
 
if __name__ == "__main__":
    unittest.main()