"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 11-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930532_TestClass(BaseTestCase):
    
    def test_C9930532(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        folder_name = "Folder1"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand Workspaces>My Workspace>My Content from the tree
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace->My Content")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : From the Action Bar, click on Other tab>Folder
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(folder_name)
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        HomePage.ModalDailogs.Folder.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Folder dialogue comes up
        """
        HomePage.ModalDailogs.Folder.verify_title("New Folder", "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Enter a 'Title' - Exp:Folder1
        """
        HomePage.ModalDailogs.Folder.Title.enter_text(folder_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click 'OK'
        """
        HomePage.ModalDailogs.Folder.OKButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, folder_name, 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Folder1 has been successfully created
        """
        HomePage.Workspaces.ContentArea.verify_folders([folder_name], "06.01")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)