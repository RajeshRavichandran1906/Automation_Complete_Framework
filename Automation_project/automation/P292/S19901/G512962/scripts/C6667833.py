'''
Created on December 10, 2018

@author: varun
Testcase Name : Verify the Category Buttons and Action Tiles for Admin User Under the Global Resources Node
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667833
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6667833_TestClass(BaseTestCase):
    
    def test_C6667833(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        crumb_css = ".crumb-box"
        folders_available = ['Page Templates (Legacy)','Page Templates','Themes']
        page_template_folders = ['Standard','Custom']
        items_css = "div[data-ibxp-text=\"Items \"]"
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css,1,45)
        
        """
        Step 3: Click on Global Resources from the resource tree
        Verify that Page Templates, Page Templates (Legacy) and Themes folders are displayed
        Also, Verify NO action bar is displayed
        """
        main_page_obj.expand_repository_folder('Global Resources')
        util_obj.synchronize_with_number_of_element(locator_obj.FOLDER_ITEM_PUBLISHED,3,60)
        main_page_obj.verify_folders_in_grid_view(folders_available, 'asequal', 'Step 3.1: Verify 3 given folders are present')
        main_page_obj.verify_action_bar_is_not_visible("Step 3.2: Verify No Action bar is visible")
        
        """
        Step 4: Double click on 'Page Templates' folder in content area 
        Verify that 'Standard' and 'Custom' folders are displayed
        Also, Verify NO action bar is displayed
        """
        main_page_obj.double_click_folder_item_and_select_menu('Page Templates')
        util_obj.synchronize_with_number_of_element(locator_obj.FOLDER_ITEM_PUBLISHED,2,60)
        main_page_obj.verify_folders_in_grid_view(page_template_folders, 'asequal', 'Step 4.1: Verify 2 given folders are present')
        main_page_obj.verify_action_bar_is_not_visible("Step 4.2: Verify No Action bar is visible")
        
        """
        Step 5: Double click on 'Standard' folder in content area
        Verify NO action bar is displayed
        """
        main_page_obj.double_click_folder_item_and_select_menu('Standard')
        util_obj.synchronize_with_visble_text(items_css, 'Items', 60)
        main_page_obj.verify_action_bar_is_not_visible("Step 5.1: Verify No Action bar is visible")
        
        """
        Step 6: Click on 'Custom' folder under Page Templates from the resource tree
        Verify that the 'Folder' and 'Page' action bars are displayed
        """
        main_page_obj.expand_repository_folder('Page Templates->Custom')
        util_obj.synchronize_with_visble_text(action_bar_css, 'Action Bar', 60)
        main_page_obj.verify_ribbon_button(['Folder','Page'], 'Step 6.1: Verify Folder and Page buttons are present ', repository_section_area='global resources')
        
        """
        Step 7: Click on 'Page Templates (Legacy)' from the resource tree
        Verify that 'Standard' and 'Custom' folders are displayed
        Also, Verify NO action bar is displayed
        """
        main_page_obj.expand_repository_folder('Page Templates (Legacy)')
        util_obj.synchronize_with_number_of_element(locator_obj.FOLDER_ITEM_PUBLISHED,2,60)
        main_page_obj.verify_folders_in_grid_view(page_template_folders, 'asequal', 'Step 7.1: Verify folders under Page Template(Legacy)')
        main_page_obj.verify_action_bar_is_not_visible("Step 7.2: Verify No Action bar is visible")
        
        """
        Step 8: Double click on 'Standard' folder in content area
        Verify NO action bar is displayed
        """
        main_page_obj.double_click_folder_item_and_select_menu('Standard')
        util_obj.synchronize_with_visble_text(folders_text_css,'Folders', 60)
        main_page_obj.verify_action_bar_is_not_visible("Step 8.1: Verify No Action bar is visible")
        
        """
        Step 9: Click on 'Custom' folder under Page Templates (Legacy) from the resource tree
        Verify that the 'Folder' and 'Portal Page' action bars are displayed
        """
        main_page_obj.expand_repository_folder('Page Templates (Legacy)->Custom')
        util_obj.synchronize_with_visble_text(action_bar_css, 'Action Bar', 60)
        main_page_obj.verify_ribbon_button(['Folder','Portal Page'], 'Step 9.1: Verify Folder and Page buttons are present ', repository_section_area='global resources')
        
        """
        Step 10: Click on 'Themes' from the resource tree
        Verify that 'Standard' and 'Custom' folders are displayed
        Also, Verify NO action bar is displayed
        """
        main_page_obj.expand_repository_folder('Themes')
        util_obj.synchronize_with_number_of_element(locator_obj.FOLDER_ITEM_PUBLISHED,2,60)
        main_page_obj.verify_action_bar_is_not_visible("Step 10.1: Verify No Action bar is visible")
        
        """
        Step 11: Double click on 'Standard' folder in content area
        Verify NO action bar is displayed
        """
        main_page_obj.double_click_folder_item_and_select_menu('Standard')
        util_obj.synchronize_with_visble_text(folders_text_css,'Folders', 60)
        main_page_obj.verify_action_bar_is_not_visible("Step 11.1: Verify No Action bar is visible")
        
        """
        Step 12: Click on 'Custom' folder under Themes from the resource tree
        Verify that the 'Folder' and 'Text Editor' action bars are displayed
        """
        main_page_obj.collapse_repository_folder('Page Templates')
        main_page_obj.collapse_repository_folder('Page Templates (Legacy)')
        main_page_obj.expand_repository_folder('Themes->Custom')
        util_obj.synchronize_with_visble_text(action_bar_css, 'Action Bar', 60)
        main_page_obj.verify_ribbon_button(['Folder','Text Editor'], 'Step 12.1: Verify Folder and Text Editor buttons are present ', repository_section_area='global resources')
        
        """
        Step 13: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()