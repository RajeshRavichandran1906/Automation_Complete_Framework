'''
Created on April 13, 2019

@author: Varun
Testcase Name : Move folder from My Content to parent Domain in content tree and content area
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261753
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import core_utility,utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.pages.wf_mainpage import Wf_Mainpage

class C8261753_TestClass(BaseTestCase):
    
    def test_C8261753(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        folder_css = "div[data-ibxp-text=\"Folders\"]"
     
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 3: Click on Domains node and select Domain tile
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Workspace')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Workspace', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Enter title as 'Move-test' and click ok.
        """
        main_page_obj.create_new_folder('Move-test')
        util_obj.synchronize_with_visble_text(".files-box .files-box-files", 'Move-test', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on 'Move-test' domain -> 'My Content' folder and select Folder tile;
        Enter title as 'aaa' and click ok
        """
        main_page_obj.expand_repository_folder('Move-test')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.double_click_folder_item_and_select_menu('My Content')
        main_page_obj.select_action_bar_tabs_option('Folder')
        main_page_obj.create_new_folder('aaa')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Click on 'Move-test' domain -> 'My Content' folder and select Folder tile;
        Enter title as 'bbb' and click ok
        """
        main_page_obj.expand_repository_folder('Move-test')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.double_click_folder_item_and_select_menu('My Content')
        main_page_obj.select_action_bar_tabs_option('Folder')
        main_page_obj.create_new_folder('bbb')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: Drag and drop 'aaa' folder from 'My Content' folder to 'Move-test' domain from content tree.
        Verify message dialog appears as 'do you wish to move this resource'
        """
        verify_message = "Are you sure you wish to move these resources?"
        drag_obj = main_pages_obj.get_domain_folder_item('aaa')
        drag_portal = core_util_obj.get_web_element_coordinate(drag_obj)
        drop_obj = main_pages_obj.get_repository_folder('Move-test')
        drop_portal = core_util_obj.get_web_element_coordinate(drop_obj)
        util_obj.drag_drop_on_screen(sx_offset=drag_portal['x'], sy_offset=drag_portal['y'], tx_offset=drop_portal['x'], ty_offset=drop_portal['y'])
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", "Warning", main_page_obj.home_page_short_timesleep)
        observed_warning = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"message\"]",'message').text.strip()
        util_obj.asequal(verify_message, observed_warning, "Step 7.1: Verify the warning message")
        
        """
        Step 8: Click yes.
        Verify 'aaa' folder is now moved under 'Move-test' domain
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['aaa'], 'asin', 'Step 8.1: Verify aaa folder is present')
        
        """
        Step 9: Drag and drop 'bbb' from 'My Content' folder to 'Move-test' domain from content area to content tree.
        Verify message dialog appears as 'do you wish to move this resource'
        """
        main_page_obj.double_click_folder_item_and_select_menu('My Content')
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        drag_obj = main_pages_obj.get_domain_folder_item('bbb')
        drag_portal = core_util_obj.get_web_element_coordinate(drag_obj)
        drop_obj = main_pages_obj.get_repository_folder('Move-test')
        drop_portal = core_util_obj.get_web_element_coordinate(drop_obj)
        util_obj.drag_drop_on_screen(sx_offset=drag_portal['x'], sy_offset=drag_portal['y'], tx_offset=drop_portal['x'], ty_offset=drop_portal['y'])
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", "Warning", main_page_obj.home_page_short_timesleep)
        observed_warning = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"message\"]",'message').text.strip()
        util_obj.asequal(verify_message, observed_warning, "Step 9.1: Verify the warning message")
        
        """
        Step 10: Click yes.
        Verify 'bbb' folder is now moved under 'Move-test' domain
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text(folder_css, 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['bbb'], 'asin', 'Step 10.1: Verify aaa folder is present')
        
        """
        Step 11: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()