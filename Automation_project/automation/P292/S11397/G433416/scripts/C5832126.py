'''
Created on April 09, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5832126
TestCase Name = Verify action tiles of sub folders under Web Content node
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages import wf_mainpage as pages_main
from common.locators import wf_mainpage_locators
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous

class C5832126_TestClass(BaseTestCase):

    def test_C5832126(self):
        
        """
        TESTCASE VARIABLES
        """
        page_misc_obj = pd_miscelaneous(self.driver)
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        ok_button_css = ".pop-top"
        
        """ 
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Right click on Web Content folder and select Expand.
        Verify that the folder is now expanded and all its content folders are shown (app folders).
        """
        main_page_obj.select_repository_folder_context_menu('Web Content', 'Expand', verification_state='collapse')
        main_page_obj.verify_repository_folder_icon_plus_minus('Web Content', 'collapse', 'Step 3.1: Verify the folder is expanded')
        main_pages_obj.verify_repository_folders('Web Content', ['baseapp', 'ibisamp'], "Step 3.2: Verify the folders present", verification_state='skip', comparion_type='asin')
        
        """
        Step 4: Click on "baseapp" sub-folder in resource tree.
        Verify that its contents appear on the content area on the right.
        Verify only three action tiles are present:
        Folder
        Upload File 
        Text Editor 
        """
        main_page_obj.expand_repository_folder('Web Content->baseapp')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_action_bar_tab_all_options(['Folder', 'Upload File', 'Text Editor'], 'Step 4.1: Verify 3 action tiles in the content area')
        content_area_items = util_obj.validate_and_get_webdriver_object(locator_obj.content_area_css, 'content area').text.strip()
        if 'New_Folder' in content_area_items:
            main_page_obj.right_click_folder_item_and_select_menu('New_Folder', 'Delete')
            util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
            main_page_obj.click_button_on_popup_dialog('OK')
            util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'New_Folder', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        if 'action_tile_test.fex' in content_area_items:
            main_page_obj.right_click_folder_item_and_select_menu('action_tile_test.fex', 'Delete')
            util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
            main_page_obj.click_button_on_popup_dialog('OK')
            util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'action_tile_test.fex', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        if 'babydeer.jpg' in content_area_items:
            main_page_obj.right_click_folder_item_and_select_menu('babydeer.jpg', 'Delete')
            util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
            main_page_obj.click_button_on_popup_dialog('OK')
            util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'babydeer.jpg', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
           
        """
        Step 5: Click on "baseapp" sub-folder in resource tree and click Folder action tile in Action Bar.
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        
        """
        Step 6: Enter "New folder" and click OK button.
        Verify that the "New folder" is created and it appeared on the content area and the tree.
        """
        main_page_obj.create_new_folder('New Folder')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'New_Folder', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['New_Folder'], 'asin', 'Step 6.1: Verify the folder present')
        
        """
        Step 7: Click on "baseapp" sub-folder in resource tree and click Text Editor action tile in Action Bar
        """
        main_page_obj.expand_repository_folder('Web Content->baseapp')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Text Editor', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Text Editor')
        
        """
        Step 8: Choose fex file icon
        Verify Text Editor window opens
        """
        fex_file = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value='fex']", 'choose-fex')
        core_util_obj.left_click(fex_file)
        core_util_obj.switch_to_new_window()
        new_page_title = self.driver.title
        util_obj.asequal('Editor', new_page_title, 'Step 8.1: Verify the tab opened in the new page')
        
        """
        Step 9: Click Save icon in toolbar then enter "Action tile test" and click Save button and close the editor window.
        Verify that the fex appears in the content area as below
        """
        save_button_obj=util_obj.validate_and_get_webdriver_object(".te-menu-bar div[title*='Save']",'save-button')
        core_util_obj.left_click(save_button_obj)
        page_misc_obj.page_designer_open_dialog_resources(title='Action tile test', ok_button=True)
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'action_tile_test.fex', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['action_tile_test.fex'], 'asin', 'Step 9.1: Verify the item fex')
        
        """
        Step 10: Click on "baseapp" sub-folder in resource tree and click Upload File action tile in Action Bar.
        """
        main_page_obj.expand_repository_folder('Web Content->baseapp')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Upload File', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Upload File')
        
        """
        Step 11: Select babydeer.jpg from \ibirisc2\bipgqashare\Images_and_Things and click open.
        Verify file uploaded successfully message appears and file has been available.
        """
        main_page_obj.upload_file_using_action_bar(['babydeer.jpg'], '\\\ibirisc2\\bipgqashare\\Images_and_Things\\')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'Upload completed', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_upload_message('babydeer.jpg', "babydeer.jpg Upload completed", "Step 11.1: Verify upload message appears")
        main_page_obj.verify_items_in_grid_view(['babydeer.jpg'], 'asin', 'Step 11.2: Verify content area')
        
        """
        Step 12: Right click on "Action tile test" fex and select Delete then right click on 'babydeer' and select Delete.
        Verify Action tile test.fex and babydeer.jpg are no longer available. 
        """
        main_page_obj.right_click_folder_item_and_select_menu('action_tile_test.fex', 'Delete')
        util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'action_tile_test.fex', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.right_click_folder_item_and_select_menu('babydeer.jpg', 'Delete')
        util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'babydeer.jpg', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.verify_items_in_grid_view(['action_tile_test.fex'], 'asnotin', 'Step 12.1: Verify content area')
        main_page_obj.verify_items_in_grid_view(['babydeer.jpg'], 'asnotin', 'Step 12.2: Verify content area')
        main_page_obj.right_click_folder_item_and_select_menu('New_Folder', 'Delete')
        util_obj.synchronize_with_visble_text(ok_button_css, 'OK', main_pages_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'New_Folder', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        
        """
        Step 13: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        