'''
Created on Aug 28, 2019

@author: Niranjan

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925883
Test case name: Context Menu:Verify Homepage Context menu for Designer items as Developer.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C9925883_TestClass(BaseTestCase):

    def test_C9925883(self):
        
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
        folder_path = "P292_S10660->G671733->Designer"
        designerchart_context = 'DesignerChart_Context'
        designerpage_context = 'DesignerPage_Context'
        workbook_context = 'Workbook_Context'
        v5portal_context = "V5Portal_Context"
        
        """
            STEP 01 :
            Sign into WebFOCUS Home Page as Developer User.
        """
        login.invoke_home_page("mrid", "mrpass")
 
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Designer.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text("#files-box-area", "DesignerChart_Context", main_page.home_page_long_timesleep)
        
        """
            STEP 03 : Right click on chart DesignerChart_Context.
            Verify context menu,
            Run.
            Run (Run in new window/Run deferred/Run with SQL trace).
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Edit with text editor.
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
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(designerchart_context, expected_context_menu, msg="Step 03.01")
        main_page.verify_repository_folder_item_context_submenu(designerchart_context, "Run...", expected_run_submenu, msg="Step 03.02", close_context_menu_css = 'div.left-main-panel')
        main_page.verify_repository_folder_item_context_submenu(designerchart_context, "Schedule", expected_schedule_submenu, msg="Step 03.03", close_context_menu_css = 'div.left-main-panel')
        main_page.verify_repository_folder_item_context_submenu(designerchart_context, "Security", expected_security_submenu, msg="Step 03.04", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 4 :
            Right click on workbook Workbook_Context.
            Verify context menu,
            Run.
            Run in new window.
            Edit.
            Download translations.
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
        expected_context_menu = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(designerpage_context, expected_context_menu, msg="Step 04.01")
        main_page.verify_repository_folder_item_context_submenu(designerpage_context, "Security", expected_security_submenu, msg="Step 04.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 5 :
            Right click on page DesignerPage_Context.
            Verify context menu,
            Run.
            Run in new window.
            Edit.
            Download translations.
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
        expected_context_menu = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(workbook_context, expected_context_menu, msg="Step 05.01")
        main_page.verify_repository_folder_item_context_submenu(workbook_context, "Security", expected_security_submenu, msg="Step 05.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 6 :
            Right click on Designer portal V5Portal_Context
            Verify context menu,
            Open.
            Run.
            Edit.
            Customizations (Remove my customizations/Remove customizations for all users).
            Paste.
            Delete.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource/Effective Policy/Owner).
            Properties.
        """
        expected_context_menu = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_customizations_menu = ['Remove my customizations', 'Remove customizations for all users']
        expected_security_submenu = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        main_page.verify_repository_folder_item_context_menu(v5portal_context, expected_context_menu, msg="Step 06.01")
        main_page.verify_repository_folder_item_context_submenu(v5portal_context, "Customizations", expected_customizations_menu, msg="Step 06.02", close_context_menu_css = 'div.left-main-panel')
        main_page.verify_repository_folder_item_context_submenu(v5portal_context, "Security", expected_security_submenu, msg="Step 06.03", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 7 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()   