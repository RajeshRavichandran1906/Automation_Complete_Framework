'''
Created on December 27, 2018

@author: varun
Testcase Name : Verify action Bar Schedule for Dev User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261608
'''
import unittest
import keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.lib.javascript import JavaScript

class C8261608_TestClass(BaseTestCase):
    
    def test_C8261608(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        j_script = JavaScript(self.driver)
        
        """
        Test case CSS
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
        schedule_tab_css = "div[id^='BiTabBar'] .bi-tab-button .bi-button-label"
        action_tab_options_css = "div:not([class*='tpg-hidden'])>div>div.create-new-item[role='button']"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        first_password_css = "#TaskPasswordDlg_firstPasswordField"
        confirm_password_css = "#TaskPasswordDlg_confirmPasswordField"
        distribution_dialog_css = "#rcBiDistributeDlg"
        distribution_dialog_ok_css = "#DistributeDlg_btnOK"
        save_and_close_css = "#ScheduleEditor_btnSaveClose"
        
        """
        Test case variables
        """
        new_tab_text = 'Untitled - Schedule'
        schedule_text = 'Schedule'
        folders_text = 'Folders'
        
        def editor_box_click(show_name):
            group_css="#ScheduleEditor_groupShowVBox [id*='ScheduleEditor']"
            total_objects = util_obj.validate_and_get_webdriver_objects(group_css, 'test')
            element_obj = total_objects[j_script.find_element_index_by_text(total_objects, show_name)]
            core_util_obj.left_click(element_obj)
        
        """
        Step 1: Sign into WebFOCUS as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Domains > Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Domains->Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """
        Step 4: Click on 'Schedule' category button > Click on 'Schedule' action bar
        Verify that 'Untitled - Schedule' opens in a new tab
        """
        main_page_obj.select_action_bar_tab(schedule_text)
        util_obj.synchronize_with_number_of_element(action_tab_options_css, 3, base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(schedule_text)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(schedule_tab_css,schedule_text, base_obj.home_page_medium_timesleep)
        obtained_title_text = self.driver.title
        util_obj.asequal(new_tab_text, obtained_title_text, "Step 4.1: Verify that 'Untitled - Schedule' opens in a new tab")
        
        """
        Step 5: Enter title as 'C6667555' in properties tab.
        """
        util_obj.set_text_to_textbox_using_keybord('C6667555', property_title_css)
        
        """
        Step 6: Click on 'Recurrence' tab > Click on 'New' > Click OK
        """
        editor_box_click('Recurrences')
        new_button = util_obj.validate_and_get_webdriver_object(new_button_css, "new-button")
        core_util_obj.python_left_click(new_button)
        util_obj.synchronize_with_number_of_element(schedule_dialog_css, 1, base_obj.home_page_short_timesleep)
        ok_button = util_obj.validate_and_get_webdriver_object(dialog_ok_css, "ok-button")
        core_util_obj.python_left_click(ok_button)
        
        """
        Step 7: Click on 'Tasks' tab > Click on 'New' dropdown > WenFOCUS report > Click on browse button from 'Procedure' > 
        Double click on 'Report' folder > Select 'Sales Metrics YTD' > Click Open
        """
        editor_box_click('Tasks')
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css,"drop-down")
        core_util_obj.left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(tooltip_css,1, base_obj.home_page_short_timesleep)
        webreport_obj =util_obj.validate_and_get_webdriver_object(webfocus_report_css, "web-report")
        core_util_obj.left_click(webreport_obj)
        util_obj.synchronize_with_number_of_element(task_dialog_css, 1, base_obj.home_page_short_timesleep)
        browse_button = util_obj.validate_and_get_webdriver_object(browse_button_css, 'browse-button')
        core_util_obj.left_click(browse_button )
        util_obj.synchronize_with_number_of_element(ibfs_css, 1, base_obj.home_page_short_timesleep)
        util_obj.select_masterfile_in_open_dialog("Retail Samples->Reports", 'Sales Metrics YTD')
        util_obj.synchronize_with_number_of_element(task_dialog_css, 1, base_obj.home_page_short_timesleep)
        
        """
        Step 8: Enter 'Execution ID' as srvadmin and Password > Enter Password and Confirm Password as 'srvadmin' and Click OK.
        """
        util_obj.set_text_to_textbox_using_keybord('srvadmin', execution_id_css)
        password_button = util_obj.validate_and_get_webdriver_object(password_css, "password-css")
        core_util_obj.left_click(password_button)
        util_obj.synchronize_with_number_of_element(password_dialog_css, 1, base_obj.home_page_short_timesleep)
        util_obj.set_text_to_textbox_using_keybord('srvadmin', first_password_css)
        keyboard.press('tab')
        util_obj.set_text_to_textbox_using_keybord('srvadmin', confirm_password_css)
        password_ok_button = util_obj.validate_and_get_webdriver_object(password_dialog_ok_css, "password-ok-css")
        core_util_obj.left_click(password_ok_button)
        util_obj.synchronize_with_number_of_element(task_dialog_css, 1, base_obj.home_page_short_timesleep)
        
        """
        Step 9 : Click OK.Then, Click on 'Distribution' tab Enter To: valid email ID and Click OK.
        """
        task_ok_button = util_obj.validate_and_get_webdriver_object(task_dialog_ok_css, "task-ok")
        core_util_obj.left_click(task_ok_button)
        editor_box_click('Distributions')
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css,"drop-down")
        core_util_obj.python_left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(tooltip_css,1, base_obj.home_page_short_timesleep)
        email_obj =util_obj.validate_and_get_webdriver_object(distribution_email_css, "email")
        core_util_obj.left_click(email_obj)
        util_obj.synchronize_with_number_of_element(distribution_dialog_css, 1 , base_obj.home_page_short_timesleep)
        util_obj.set_text_to_textbox_using_keybord('ibiqaauto@amtexsystems.com', '#DistributeEmailPane_mailToTextField')
        util_obj.set_text_to_textbox_using_keybord('ibiqaauto@amtexsystems.com', '#DistributeEmailPane_mailReplyTextField')
        distribution_ok_button = util_obj.validate_and_get_webdriver_object(distribution_dialog_ok_css, "distribution-ok-css")
        core_util_obj.left_click(distribution_ok_button)
        
        """
        Step 10: Click 'Save&Close' button > Click 'Save'
        Verify that 'C6667555' schedule
        """
        save_close_button = util_obj.validate_and_get_webdriver_object(save_and_close_css, "save-close-css")
        core_util_obj.left_click(save_close_button)
        util_obj.synchronize_with_visble_text(final_save_css, 'Save', 15)
        save_button = util_obj.validate_and_get_webdriver_object(final_save_css, "save-css")
        core_util_obj.left_click(save_button)
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(".content-box", "C6667555", main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['C6667555'], 'asin', 'Step 10.1: Verify schedule in the content area')
        
        """
        Step 11: In the banner link, Click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()