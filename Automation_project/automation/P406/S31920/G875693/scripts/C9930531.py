"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 10-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930531_TestClass(BaseTestCase):
    
    def test_C9930531(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        portal_name  = "Test"
        portal_title_css = "div.pvd-portal-title"
        portal_canvas_css = "div.pvd-canvas-container"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand Workspaces>My Workspaces>My Content from the tree
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace->My Content")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : From the Action Bar, click the Application tab>Launch Portal
        """
        HomePage.Workspaces.ActionBar.select_tab_option('Portal')
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify New Portal dialogue comes up
        """
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal", "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Enter a Title in dialogue - Exp:Test
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click 'Create'
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 40)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Portal has been successfully created under Folders
        """
        HomePage.Workspaces.ContentArea.verify_folders([portal_name], "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right-click on created Portal
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify right-click menu
        """
        portal_context_menu = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(portal_context_menu, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Select 'Run'
        """
        HomePage.ContextMenu.select('Run')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "There", 40)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify created Portal opens up
        """
        HomePage.Home._utils.verify_element_text(portal_title_css, portal_name, "Step 08.01 : Verify created Portal opens up")
        HomePage.Home._utils.verify_element_text(portal_canvas_css, "There are no pages available", "Step 08.02 : Verify created Portal canvas text")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)
        
        STEP_09 = """
            STEP 09 : Close run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)