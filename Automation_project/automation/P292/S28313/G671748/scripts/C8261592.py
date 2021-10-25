'''
Created on January 03, 2019

@author: KK14897

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261592
Testcase Name : Verify action Bar options are all functional, Dev user Folder
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261592_TestClass(BaseTestCase):

    def test_C8261592(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        TESTCASE CSS
        """
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Domains->Retail Samples'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'Retail Samples' from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Common', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3.1: Verify by default 'Common' category button is selected
        """
        main_page_obj.verify_selected_action_bar_tab(['Common'], "Step 3.1: Verify that still 'Data' category is selected")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Folder' action bar
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        
        """
        Step 4.1: Verify that the 'New Folder' prompt is displayed 
        """
        main_page_obj.verify_new_folder_caption_title(step_number='4.1')
        
        """
        Step 5: Enter Title 'C6667539_0'
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(title_value='C6667539_0')
        
        """
        Step 5.1: Verify the Name will be inherited from the title
        Also, Verify 'OK' button got enable after title is being entered
        """
        main_page_obj.verify_new_folder_name_in_popup_dialog(name_value='C6667539_0', msg="Step 5.1: Verify the Name will be inherited from the title")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(button_name='OK', msg="Step 5.2: Also, Verify 'OK' button got enable after title is being entered")
        
        """
        Step 6: Click on 'Ok' button in new folder prompt
        """
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        
        """
        Step 6.1: Verify that the 'C6667539_0' is displayed in Content area
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'C6667539_0', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view(['C6667539_0'], 'asin', "Step 6.1:")
        
        """
        Step 7: Right Click on the 'C6667539_0' > Delete > yes in the 'Delete' dialog box
        """
        main_page_obj.right_click_folder_item_and_select_menu(item_name='C6667539_0', context_menu_item_path='Delete')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        
        """
        Step 7.1: Verify that the 'C6667539_0' is not displayed in Content area
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'C6667539_0', main_page_obj.home_page_long_timesleep, condition_type='asnotin')
        main_page_obj.verify_folders_in_grid_view(['C6667539_0'], 'asnotin', "Step 7.1:")
        
        """
        Step 8: Click on 'Other' category button
        """
        main_page_obj.select_action_bar_tab('Other')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Click on 'Folder' action bar under 'Other' category
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        
        """
        Step 9.1: Verify that the 'New Folder' prompt is displayed  
        """
        main_page_obj.verify_new_folder_caption_title(step_number='9.1')
        
        """
        Step 10: Enter Title 'C6667539_1'
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(title_value='C6667539_1')
        
        """
        Step 10.1: Verify the Name will be inherited from the title
        Also, Verify 'OK' button got enable after title is being entered
        """
        main_page_obj.verify_new_folder_name_in_popup_dialog(name_value='C6667539_1', msg="Step 10.1: Verify the Name will be inherited from the title")
        main_page_obj.verify_button_enable_or_disable_on_popup_dialog(button_name='OK', msg="Step 10.2: Also, Verify 'OK' button got enable after title is being entered")
        
        """
        Step 11: Click on 'Ok' button in new folder prompt
        """
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        
        """
        Step 11.1: Verify that the 'C6667539_1' is displayed in Content area
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'C6667539_1', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view(['C6667539_1'], 'asin', "Step 11.1:")
        
        """
        Step 12: Right Click on the 'C6667539_1' > Delete > yes in the 'Delete' dialog box
        """
        main_page_obj.right_click_folder_item_and_select_menu(item_name='C6667539_1', context_menu_item_path='Delete')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog(button_name='OK')
        
        """
        Step 12.1: Verify that the 'C6667539_1' is not displayed in Content area
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'C6667539_1', main_page_obj.home_page_medium_timesleep, condition_type='asnotin')
        main_page_obj.verify_folders_in_grid_view(['C6667539_1'], 'asnotin', "Step 12.1:")
        
        """
        Step 13: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()