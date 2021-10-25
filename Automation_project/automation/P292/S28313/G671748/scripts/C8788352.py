'''
Created on March 11, 2019

@author: Niranjan/Samuel
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788352
Testcase Name : Verify Admin User can Create new Folder
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
import time

class C8788352_TestClass(BaseTestCase):

    def test_C8788352(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        CSS
        """
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID='C8788352'
        domain_folder='Retail Samples'
        ok_button = 'OK'
        folder_name = 'New Folder'
        font = 'italic'
        
        """
        Step 1:Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_long_timesleep)
 
        """
        Step 2:Click Content View from the sidebar > Click on Domains from the navigation bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text('div.crumb-box', 'Workspaces', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        
        """
        Step 3:Click on 'Folder' action bar
        Verify that the folder_name prompt is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        main_page_obj.verify_new_folder_caption_title(step_number='03.01')
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 03.02: Verify popup dialog is displayed")
        main_page_obj.verify_popup_dialog_caption(folder_name, "Step 03.03: Verify that the folder name prompt is displayed")

        """
        Step 4:Enter Title 'C8788352'
        Verify the Name will be inherited from the title
        Also, Verify ok_button button got enable after the title is being entered
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(Testcase_ID)
        main_page_obj.verify_new_folder_name_in_popup_dialog(Testcase_ID, "Step 04.01: Verify the Name will be inherited from the title")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(ok_button, "Step 04.02: Verify ok_button button got enable after the title is being entered")

        """
        Step 5:Click on ok_button button in new folder prompt
        Verify that the 'C8788352' is displayed in the Content area as unpublished by default
        Verify that the 'C8788352' is displayed in the resource tree as italic by default

        """
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 05.01: Verify folder is displayed in the Content area")
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID,'unpublish','Step 05.02: Verify folder is unpublished in the Content area')
        main_page_obj.verify_repository_folder_font_style(Testcase_ID, font, 'Step 05.03: Verify font style is itlaic')
        
        """
        Step 6:Right click on 'C8788352'
        Verify that the 'C8788352' is displayed in the Content area as published
        Verify that the 'C8788352' is displayed in the resource tree as published
        """
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 06.01: Verify folder is displayed in the Content area")
        time.sleep(3)
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Publish', folder_path='Domains')
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID, 'publish','Step 06.02: Verify folder is published in the Content area')
        main_page_obj.verify_repository_folder_publish_or_unpublish(Testcase_ID, 'publish','Step 06.03: Verify folder is published in the resource tree')
        
        """
        Step 7:Right Click on the 'C8788352' > Delete > yes in the 'Delete' dialog box
        Verify that the 'C8788352' is not displayed in the Content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Delete', folder_path='Domains')
        util_obj.synchronize_with_visble_text(ok_btn_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_long_timesleep)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asnotin', "Step 07.01: Verify folder is not displayed in the Content area")
        
        """
        Step 8: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)   
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        
        """
        Step 9:Click on 'Folder' action bar
        Verify that the folder_name prompt is displayed
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        main_page_obj.verify_new_folder_caption_title(step_number='09.01')
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 09.02: Verify popup dialog is displayed")
        main_page_obj.verify_popup_dialog_caption(folder_name, "Step 09.03: Verify that the folder name prompt is displayed")

        """
        Step 10:Enter Title 'C8788352'
        Verify the Name will be inherited from the title
        Also, Verify ok_button button got enable after the title is being entered
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(Testcase_ID)
        main_page_obj.verify_new_folder_name_in_popup_dialog(Testcase_ID, "Step 10.01: Verify the Name will be inherited from the title")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(ok_button, "Step 10.02: Verify ok_button button got enable after the title is being entered")

        """
        Step 11:Click on ok_button button in new folder prompt
        Verify that the 'C8788352' is displayed in the Content area as unpublished by default
        Verify that the 'C8788352' is displayed in the resource tree as italic by default

        """
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 11.01: Verify folder is displayed in the Content area")
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID,'unpublish','Step 11.02: Verify folder is unpublished in the Content area')
        main_page_obj.verify_repository_folder_font_style(Testcase_ID, font, 'Step 11.03: Verify font style is itlaic')
        
        """
        Step 12:Right click on 'C8788352'
        Verify that the 'C8788352' is displayed in the Content area as published
        Verify that the 'C8788352' is displayed in the resource tree as published
        """
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 12.01: Verify folder is displayed in the Content area")
        time.sleep(3)
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Publish', folder_path=domain_folder)
#         time.sleep(30)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID,'publish','Step 12.02: Verify folder is published in the Content area')
        main_page_obj.verify_repository_folder_publish_or_unpublish(Testcase_ID,'publish','Step 12.03: Verify folder is published in the resource tree')
        
        """
        Step 13:Right Click on the 'C8788352' > Delete > yes in the 'Delete' dialog box
        Verify that the 'C8788352' is not displayed in the Content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Delete', folder_path=domain_folder)
        util_obj.synchronize_with_visble_text(ok_btn_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asnotin', "Step 13.01: Verify folder is not displayed in the Content area")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Other', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 14: Click on 'Other' category button > Click on 'Folder' action bar under 'Other' category
        Verify that the folder_name prompt is displayed
        """
        main_page_obj.select_action_bar_tab("Other")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option('Folder')
        main_page_obj.verify_new_folder_caption_title(step_number='14.01')
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 14.02: Verify popup dialog is displayed")
        main_page_obj.verify_popup_dialog_caption(folder_name, "Step 14.03: Verify that the folder name prompt is displayed")
        
        """
        Step 15:Enter Title 'C8788352'
        Verify the Name will be inherited from the title
        Also, Verify ok_button button got enable after the title is being entered
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(Testcase_ID)
        main_page_obj.verify_new_folder_name_in_popup_dialog(Testcase_ID, "Step 15.01: Verify the Name will be inherited from the title")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(ok_button, "Step 15.02: Verify ok_button button got enable after the title is being entered")

        """
        Step 16:Click on ok_button button in new folder prompt
        Verify that the 'C8788352' is displayed in the Content area as unpublished by default
        Verify that the 'C8788352' is displayed in the resource tree as italic by default

        """
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 16.01: Verify folder is displayed in the Content area")
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID,'unpublish','Step 16.02: Verify folder is unpublished in the Content area')
        main_page_obj.verify_repository_folder_font_style(Testcase_ID, font, 'Step 16.03: Verify font style is itlaic')
        
        """
        Step 17:Right click on 'C8788352'
        Verify that the 'C8788352' is displayed in the Content area as published
        Verify that the 'C8788352' is displayed in the resource tree as published
        """
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asin', "Step 17.01: Verify folder is displayed in the Content area")
        time.sleep(3)
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Publish', folder_path=domain_folder)
#         time.sleep(30)
        util_obj.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(Testcase_ID, 'publish','Step 17.02: Verify folder is published in the Content area')
        main_page_obj.verify_repository_folder_publish_or_unpublish(Testcase_ID, 'publish','Step 17.03: Verify folder is published in the resource tree')
        
        """
        Step 18:Right Click on the 'C8788352' > Delete > yes in the 'Delete' dialog box
        Verify that the 'C8788352' is not displayed in the Content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_ID, context_menu_item_path='Delete', folder_path=domain_folder)
        util_obj.synchronize_with_visble_text(ok_btn_css, ok_button, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(ok_button)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_ID, main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.verify_folders_in_grid_view([Testcase_ID], 'asnotin', "Step 18.01: Verify folder is not displayed in the Content area")
        
        """
        Step 19:In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == "__main__":
    unittest.main()