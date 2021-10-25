'''
Created on Nov 15, 2018

@author: KK14897

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/28313&group_by=cases:section_id&group_order=asc&group_id=671767
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261703
TestCase Name = Verify UnShared personal page does not shows share icon inside the My Content folder 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261703_TestClass(BaseTestCase):

    def test_C8261703(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        folder_name_path="Domains->P292_S19901_G520454"
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')

        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_number_of_element(crumb_css, '1', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run')
        util_obj.wait_for_page_loads(10)
        core_utility_obj.switch_to_new_window() 
        """
        Step 4: Click on Share button from the personal page toolbar.
        Verify 'Share with Others' dialog opens with the following options:
        1.X button is displays at the top right corner of the dialog box
        2.Enter users and groups' search box with the dropdown control is empty
        3.Under shared with it shows 'autobaseuser08' user
        4.Share with everyone checkbox
        5.OK button is disabled
        6.Cancel button is enabled
        """
        share_css="div[class^='pd-page-header'] div[class^='pd-header-buttons'] div[class*='button-share']"
        share_button_obj=util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        core_utility_obj.left_click(share_button_obj)
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(".share-with-others-dialog", "Share", main_page_obj.home_page_medium_timesleep)
        
        x_button_obj = util_obj.validate_and_get_webdriver_object("div[class^='ibx-title-bar-close-button']", "x button css")
        actual_output = x_button_obj.is_displayed()
        msg = "Step 4.1 : X button is displays at the top right corner of the dialog box"
        util_obj.asequal(True, actual_output, msg)
        
        seachbox_obj = util_obj.validate_and_get_webdriver_object(".share-with-txt-search input", "Search box css")
        actual_output = seachbox_obj.get_attribute('aria-label')
        msg = "Step 4.2 : Enter users and groups' search box with the dropdown control is empty"
        util_obj.asequal("Text Input", actual_output, msg)
        
        shared_obj = util_obj.validate_and_get_webdriver_object('.share-with-item .sw-item-desc', "shared css")
        actual_output = shared_obj.text
        msg = "Step 4.3 : Under shared with it shows 'autobaseuser08' user"
        util_obj.asequal("autobasuser08", actual_output, msg)
        
        checkbox_obj = util_obj.validate_and_get_webdriver_object(".share_with_everyone .ibx-check-box-simple-marker-uncheck", "check box css")
        actual_output = checkbox_obj.is_displayed()
        msg = "Step 4.4 : Share with everyone checkbox"
        util_obj.asequal(True, actual_output, msg)
        
        ok_button = util_obj.validate_and_get_webdriver_object('.ibx-dialog-ok-button.ibx-widget-disabled', 'ok button css')
        actual_output = ok_button.is_displayed()
        msg = "Step 4.5 : OK button is disabled"
        util_obj.asequal(True, actual_output, msg)
        
        cancel_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-cancel-button", "cancel button css")
        actual_output = cancel_button.is_enabled()
        msg = "Step 4.6 : Cancel button is enabled"
        util_obj.asequal(True, actual_output, msg)
        
        """
        Step 5: Click X button under Shared with 'autobaseuser08' textbox to unshare the already shared 'autobaseuser08' user > Click OK
        Verify 'Share with Others' window gets closed and Share button appears in grey color
        """
        share_dialog_css='div[class*="sw-item-name"]'
        util_obj.synchronize_with_number_of_element(share_dialog_css, 1, main_page_obj.home_page_medium_timesleep)
        close_obj=util_obj.validate_and_get_webdriver_object('div[class*="sw-close-button"]','Close_button_css')
        core_utility_obj.left_click(close_obj)
        OK_obj=util_obj.validate_and_get_webdriver_object('div[class*="ibx-dialog-ok-button"]','Ok_button_css')
        core_utility_obj.left_click(OK_obj)
        util_obj.synchronize_with_visble_text(".pd-page-header", "Page", main_page_obj.home_page_short_timesleep)
        
        util_obj.verify_picture_using_sikuli("share_button.png", "Step 5.1 : Verify 'Share with Others' window gets closed and Share button appears in grey color")
        
        """
        Step 6: Hover the mouse to the Share button
        Verify Share button shows as 'Share'
        """
        obj = util_obj.validate_and_get_webdriver_object(".pd-header-button-share", 'share button')
        actual_output = obj.get_attribute('title')
        msg = "Step 6.1 : Verify Share button shows as 'Share'"
        util_obj.asequal('Share', actual_output, msg)
       
        """
        Step 7: Close the portal run window.
        """
        core_utility_obj.switch_to_previous_window()
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()