"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 27 April 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944219_TestClass(BaseTestCase):
    
    def test_C9944219(self):
        
        """
            TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
    
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mradvid", "mradvpass")
        utils.capture_screenshot("01.00", STEP_01)
 
        STEP_02 = """
            STEP 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on uploaded image Image_Context
        """
        HomePage.MyWorkspace.right_click_on_item('Image_Context')
        utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify context menu,
            View.
            View in new window.
            Duplicate.
            Delete DEL.
            Share
            Share with...
            Properties.
        """
        context_menu = ['View', 'View in new window', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'03.01')
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04 : Right click on URL_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('URL_Context')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify context menu,
            View.
            View in new window.
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share.
            Share with...
            Properties.
        """
        context_menu = ['View', 'View in new window', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'04.01')
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            STEP 05.00 : Right click on Blog_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('Blog_Context')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Edit.
            Comments (View comments).
            Duplicate.
            Delete DEL.
            Share
            Share with...
            Properties.
        """
        context_menu = ['Edit', 'Comments', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'05.01')
        HomePage.ContextMenu.close()
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            STEP 06 : Right click on TextEditor_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('TextEditor_Context')
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify context menu,
            Run.
            Run (Run in new window).
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        context_menu = ['Run', 'Run...', 'Schedule', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'06.01')
        context_submenu = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(context_submenu, "06.02", menu_path = "Run...")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07: Right click on IA_Report - Shortcut.
        """
        HomePage.MyWorkspace.right_click_on_item('IA_Report - Shortcut')
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07_01 Verify context menu,
            Run.
            Run... (Run in new window)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        
        context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu,'07.01')
        context_submenu = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(context_submenu, "07.02", menu_path = "Run...")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        
        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00', STEP_08)

if __name__ == "__main__":
    unittest.main()