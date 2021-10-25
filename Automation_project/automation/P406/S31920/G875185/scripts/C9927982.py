"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 08-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927982_TestClass(BaseTestCase):
    
    def test_C9927982(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as  Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace from the resource tree > Click on 'G784912' folder
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double Click on 'Image/URL/Blog/TextEditor' folder in the content area.
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("Images/URL/Blog/TextEditor")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Blog_Context", 30)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click on uploaded image **Image_Context**
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Image_Context")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify context menu,
            1.View.
            2.View in new window.
            3.Copy.
            4.Properties.
        """
        image_context_menu = ['View', 'View in new window', 'Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(image_context_menu, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on **URL_Context**.
        """
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("URL_Context")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify context menu,
            1.View.
            2.View in new window.
            3.Edit.
            4.Copy.
            5.Add to Favorites.
            6.Properties.
        """
        url_context_menu = ['View', 'View in new window', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(url_context_menu, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on **Blog_Context**.
        """
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("Blog_Context")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify context menu,
            1.Comments (View comments).
            2.Copy.
            3.Properties.
        """
        blog_context_menu = ['Comments', 'Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(blog_context_menu, "07.01")
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("Blog_Context")
        HomePage.ContextMenu.verify(['View comments'], "07.02",  menu_path="Comments")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on **TextEditor_Context**.
        """
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("TextEditor_Context")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule Email.
            4.Schedule (Email/Printer/Report Library/Repository).
            5.Copy.
            6.Add to Favorites.
            7.Properties.
        """
        text_context_menu = ['Run', 'Run...', 'Schedule', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(text_context_menu, "08.01")
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("TextEditor_Context")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], "08.02",  menu_path="Run...")
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("TextEditor_Context")
        HomePage.ContextMenu.verify(['Email', 'Printer', 'Report Library', 'Repository'], "08.03",  menu_path="Schedule")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)