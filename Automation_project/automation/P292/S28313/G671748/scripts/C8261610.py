'''
Created on December 14, 2018

@author: varun
Testcase Name : Verify action Bar URL for Dev User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261610
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261610_TestClass(BaseTestCase):
    
    def test_C8261610(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        
        """bi.co
        Test case CSS
        """
        url_popup_css = ".ibx-root .create-new-url"
        action_bar_tab_options_css = "div:not([class*='tpg-hidden'])>div>div.create-new-item[role='button']"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
        """
        Test case variables
        """
        test_case_id = 'C6667557'
        test_case_id_two = 'C6667557_1'
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on the Content Sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Other' category button
        """
        main_page_obj.select_action_bar_tab('Other')
        
        """
        Step 5: Click on 'URL' action bar
        Verify New URL dialog box opens
        Also, Verify Ok button is disabled
        """
        util_obj.synchronize_with_number_of_element(action_bar_tab_options_css, 8, base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('URL')
        util_obj.synchronize_with_number_of_element(url_popup_css , 1 , base_obj.home_page_medium_timesleep)
        main_page_obj.verify_popup_dialog_caption('New URL', "Step 5.1: Verify New URL box is opened")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('OK', 'Step 5.2: Verify the ok button is disabled', enable=False)
    
        """
        Step 6: Enter title 'C6667557' and enter "www.ibi.com" in URL
        Verify Ok button is Enabled
        """
        main_page_obj.enter_url_title_in_popup_dialog(test_case_id)
        main_page_obj.enter_url_in_popup_dialog("www.ibi.com")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('OK', 'Step 5.2: Verify the ok button is enabled')
        
        """
        Step 7: Click Ok button in New URL dialog box
        Verify 'IBI URL' is displayed in content area
        """
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, test_case_id, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([test_case_id],'asin', "Step 7.1: Url is presnt in the content area")
        
        """
        Step 8: Right click on 'C6667557' > Edit        
        Verify Edit URL dialog box opens
        Also, Verify Update button is disabled
        """
        main_page_obj.right_click_folder_item_and_select_menu(test_case_id, 'Edit')
        util_obj.synchronize_with_number_of_element(url_popup_css , 1 , base_obj.home_page_medium_timesleep)
        main_page_obj.verify_popup_dialog_caption('Edit URL', "Step 8.1: Verify New URL box is opened")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('Update', 'Step 8.2: Verify the ok button is disabled', enable=False)
        
        """
        Step 9: Change the title as 'C6667557_1'
        """
        main_page_obj.enter_url_title_in_popup_dialog(test_case_id_two)
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog('Update', 'Step 9.1: Verify the ok button is enabled')
        
        """
        Step 10: Click 'Update' in Edit URL dialog box
        Verify that the title edited 'C6667557_1' is displayed in the Content area
        """
        main_page_obj.click_button_on_popup_dialog('Update')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, test_case_id_two, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([test_case_id_two],'asin', "Step 10.1:Verify Url in the content area")
        
        """
        Step 11: Right click on 'C6667557_1' > Delete > Ok
        """
        main_page_obj.right_click_folder_item_and_select_menu(test_case_id_two, 'Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        
        """
        Step 12: In the banner link, click on the top right username > Click Sign Out.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Other', main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()