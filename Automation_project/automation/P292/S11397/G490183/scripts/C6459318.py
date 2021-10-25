"""-------------------------------------------------------------------------------------------
Created on July 10, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459318
Test Case Title =  Create and Open Distribution List 
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.lib import global_variables
import time


class C6459318_TestClass(BaseTestCase):

    def test_C6459318(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_run = Run(self.driver)
        
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        browser_name =global_variables.Global_variables.browser_name
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        expected_email_value='ibiqaauto@amtexsystems.com'
        expected_text_header=["Burst Value","E-mail",' ']
        
        
        def enter_distribution_list_title(title):
            title_textbox_elem=utils.validate_and_get_webdriver_object("input#AddrbookEditor_nameTextField", "Text_box_title_value")
            utils.set_text_to_textbox_using_keybord(title,text_box_elem=title_textbox_elem)
            
        def click_ribbon_icon_distribution_list(section_name,item_name):
            ribbon_css="#AddrbookEditor_tabPage #AddrbookEditor_group{0}VBox #AddrbookEditor_btn{1}Members".format(section_name,item_name)
            button_elem=utils.validate_and_get_webdriver_object(ribbon_css,"ribbon_item_in_schedule")
            core_utils.python_left_click(button_elem)
        
        def enter_email_addr_in_addnew_member(Email_addr):
            email_textbox_elem=utils.validate_and_get_webdriver_object("input#AddrbookItem_addressTextField", "Email_text_box")
            utils.set_text_to_textbox_using_keybord(Email_addr,text_box_elem=email_textbox_elem)
        
        """
        STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
        Step 4:Click on 'Distribution List' action tile from under Schedule category;
        Enter Title as 'Email DList' and Method as 'Email'
        """
        main_page.select_action_bar_tab('Schedule')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Distribution List', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Distribution List')
        core_utils.switch_to_new_window()
        utils.synchronize_until_element_is_visible("input#AddrbookEditor_nameTextField",main_page.home_page_medium_timesleep)
        enter_distribution_list_title("Email DList")
        
        
        """
        Step 5:Click on Add New icon.
        Verify that the Add New Member dialog opens as below
        """
        click_ribbon_icon_distribution_list("Members","AddNew")
        utils.synchronize_until_element_is_visible("#rcBiAddrbookItemDlg",main_page.home_page_medium_timesleep)

        """
        Step 6:Give Email Address: as {email account}@ibi.com (any valid email address there is the access to. Ex, report_broker@ibi.com) and click OK.
        Verify correct Email Address is displayed in the list as below
        """
        enter_email_addr_in_addnew_member("ibiqaauto@amtexsystems.com")
        ok_elem=utils.validate_and_get_webdriver_object("div#AddrbookItem_btnOK","Ok_button_in_add_new_mem_dlg")
        core_utils.python_left_click(ok_elem)
        e_mail_value_text=self.driver.find_element_by_css_selector(".bi-tree-view-body-content table>tbody>tr>td:nth-child(2)").text
        utils.asequal(e_mail_value_text,expected_email_value,"Step 6.1 verify the email value")
        utils.verify_object_visible(".bi-tree-view-body-content  table>tbody>tr>td>img[src*='Silver/images/file.gif']", True,"Step 6.1 verify the images of burst")
        headers_elem=utils.validate_and_get_webdriver_objects(".bi-tree-view-headers table>tbody>tr>td","header_schedule_elem")
        for x in headers_elem:
            actual_text_header=x.text
            utils.asin(actual_text_header,expected_text_header,"Step 6.3 verify the text header in schedule")
    
        """
        Step 7:Click on RC icon > Save > Click Save button.
        """
        
        save_button_toolbar=utils.validate_and_get_webdriver_object("#AddrbookEditor_btnSave","save_button")
        core_utils.python_left_click(save_button_toolbar)
        utils.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_btnOK",main_page.home_page_medium_timesleep)
        save_button=utils.validate_and_get_webdriver_object("#IbfsOpenFileDialog7_btnOK","Save_button")
        time.sleep(3)
        core_utils.python_move_to_element(save_button)
        core_utils.python_left_click(save_button)
        application_button=utils.validate_and_get_webdriver_object("img[src*='reportcaster']","Rc_application_button")
        core_utils.python_left_click(application_button)
 
        """
        Step 8:Click on RC icon> Close.
        Verify Email DList' is created and listed under G490183 folder
        """
        utils.select_or_verify_bipop_menu("Close")
        
        """
        Step 9:Double click on 'Email DList'.
        Verify that the Email DList Distribution List opens in a new tab.
        """
        core_utils.switch_to_previous_window(window_close=False)
        if browser_name=="chrome":
            main_page_run.switch_to_frame()
            pd_design.switch_to_container_frame("Panel 1")
        main_page.double_click_on_content_area_items("Email DList")
        core_utils.switch_to_new_window()
        e_mail_value_text=self.driver.find_element_by_css_selector(".bi-tree-view-body-content table>tbody>tr>td:nth-child(2)").text
        utils.asequal(e_mail_value_text,expected_email_value,"Step 10 verify the email value")
        utils.verify_object_visible(".bi-tree-view-body-content  table>tbody>tr>td>img[src*='Silver/images/file.gif']", True,"Step 10.1 verify the images of burst")
        headers_elem=utils.validate_and_get_webdriver_objects(".bi-tree-view-headers table>tbody>tr>td","header_schedule_elem")
        for x in headers_elem:
            actual_text_header=x.text
            utils.asin(actual_text_header,expected_text_header,"Step 10.3 verify the text header in schedule")
        
        """
        Step 10:Click RC icon > Exit.
        """
        
        application_button=utils.validate_and_get_webdriver_object("img[src*='reportcaster']","Rc_application_button")
        core_utils.python_left_click(application_button)
        utils.select_or_verify_bipop_menu("Close")
        core_utils.switch_to_previous_window(window_close=False)
        
        """
        Step 11:Close the 'Explorer widget' page run window.
        Verify Home page is displayed and 'Email DList' is listed under G490183 folder
        """
        if browser_name=="chrome":
            main_page_run.switch_to_frame()
            pd_design.switch_to_container_frame("Panel 1")
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(["Email DList"],"asin","Step 11.1 Verify 'Distribution_list' is available under 'G490183' folder in content area as below")

        
        """
        Step 12:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 