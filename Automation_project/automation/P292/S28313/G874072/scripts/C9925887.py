'''
Created on Aug 30, 2019

@author: Prabhakaran

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925887
Test case name: Context Menu:Verify Homepage Context menu for Image/URL/Blog/TextEditor items as Developer User.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C9925887_TestClass(BaseTestCase):

    def test_C9925887(self):
        
        """
        CLASS OBJECTS
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        
        """
        COMMON VARIABLES 
        """
        folder_path = "P292_S10660->G671733->Images/URL/Blog/TextEditor"
        blog_context = "Blog_Context"
        image_context = "Image_Context"
        texteditor_context = "TextEditor_Context"
        url_context = "URL_Context"
        
        """
            STEP 1 : Sign into WebFOCUS Home Page as Developer User.
        """
        login.invoke_home_page("mrid", "mrpass")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Image/URL/Blog/TextEditor.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text("#files-box-area", "Blog_Context", main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Right click on uploaded image Image_Context
            Verify context menu,
            View.
            View in new window.
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective Policy/Owner).
            Properties.
        """
        expected_context_menu = ['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(image_context, expected_context_menu, msg="Step 03.01")
        main_page.verify_repository_folder_item_context_submenu(image_context, "Security", expected_security_submenu, msg="Step 03.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 4 : Right click on URL_Context.
            Verify context menu,
            View.
            View in new window.
            Edit.
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective Policy/Owner).
            Properties.
        """
        expected_context_menu = ['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(url_context, expected_context_menu, msg="Step 04.01")
        main_page.verify_repository_folder_item_context_submenu(url_context, "Security", expected_security_submenu, msg="Step 04.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 5 : Right click on Blog_Context.
            Verify context menu,
            Edit.
            Comments (View comments/Remove all comments).
            Duplicate.
            Cut.
            Copy.
            Create shortcut.
            Delete.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective Policy/Owner).
            Properties.
        """
        expected_context_menu = ['Edit', 'Comments', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_comments_menu = ['View comments', 'Remove all comments']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(blog_context, expected_context_menu, msg="Step 05.01")
        main_page.verify_repository_folder_item_context_submenu(blog_context, "Comments", expected_comments_menu, msg="Step 05.02", close_context_menu_css = 'div.left-main-panel')
        main_page.verify_repository_folder_item_context_submenu(blog_context, "Security", expected_security_submenu, msg="Step 05.03", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 6 : Right click on TextEditor_Context.
            Verify context menu,
            Run.
            Run (Run in new window/Run deferred/Run with SQL trace).
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Duplicate.
            Cut.
            Copy.
            Create Shortcut.
            Delete.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective Policy/Owner).
            Properties.
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(texteditor_context, expected_context_menu, msg="Step 06.01")
        main_page.verify_repository_folder_item_context_submenu(texteditor_context, "Run...", expected_run_submenu, msg="Step 06.02")
        main_page.verify_repository_folder_item_context_submenu(texteditor_context, "Schedule", expected_schedule_submenu, msg="Step 06.03")
        main_page.verify_repository_folder_item_context_submenu(texteditor_context, "Security", expected_security_submenu, msg="Step 06.04")
        
        """
            STEP 7 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main() 
