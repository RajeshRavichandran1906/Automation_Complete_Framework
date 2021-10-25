"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 08 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944214_TestClass(BaseTestCase):
    
    def test_C9944214(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
    
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
 
        STEP_02 = """
            STEP 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on uploaded image Image_Context
        """
        HomePage.MyWorkspace.right_click_on_item('Image_Context')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
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
        image_context_menu = ['View', 'View in new window', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(image_context_menu,'03.01')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04 : Right click on URL_Context.
        """
        HomePage.Home._core_utils.python_click_with_offset(900,200)
        HomePage.MyWorkspace.right_click_on_item('URL_Context')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
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
        url_context_menu = ['View', 'View in new window', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(url_context_menu,'04.01')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            STEP 05.00 : Right click on Blog_Context.
        """
        HomePage.Home._core_utils.python_click_with_offset(900,200)
        HomePage.MyWorkspace.right_click_on_item('Blog_Context')
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Edit.
            Comments (View comments/Remove all comments).
            Duplicate.
            Delete DEL.
            Share
            Share with...
            Properties.
        """
        blog_context_menu = ['Edit', 'Comments', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(blog_context_menu,'05.01')
        comments_submenu = ['View comments', 'Remove all comments']
        HomePage.ContextMenu.verify(comments_submenu, '05.02', menu_path = 'Comments')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            STEP 06 : Right click on TextEditor_Context.
        """
        HomePage.Home._core_utils.python_click_with_offset(900,200)
        HomePage.MyWorkspace.right_click_on_item('TextEditor_Context')
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify context menu,
            Run.
            Run (Run in new window).
            Schedule Email
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties
        """
        text_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(text_context_menu,'06.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], "06.02", menu_path = "Run...")
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('TextEditor_Context')
        HomePage.ContextMenu.verify(schedule_submenu, "06.03", menu_path = "Schedule")
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
