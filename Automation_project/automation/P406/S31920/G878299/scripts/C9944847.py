"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 07-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944847_TestClass(BaseTestCase):
    
    def test_C9944847(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        folder_name = "My Content - Shortcut"
        user_name = "~" + HomePage.Home._utils.parseinitfile("mriddev")
        folder = "P406_S31920"
        target_path = "IBFS:/WFC/Repository/{0}/{1}".format(folder, user_name)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > Click on 'P406_S31920' Workspace from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select(folder)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(folder_name)
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.ModalDailogs.Shortcut.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on the 'Browse' button > Select 'My Content' folder
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.ModalDailogs.Resources._locators_.base[1] + ".pop-top", "Content", 60)
        HomePage.ModalDailogs.Resources.GridView.Folders.click("My Content")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that 'Title' should be 'My Content' and 'Name' should be '~autodevuser204'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text("My Content", "05.01")
        HomePage.ModalDailogs.Resources.Name.verify_text(user_name, "05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following:
            1. Target path = IBFS:/WFC/Repository/P406_S31920/~autodevuser204
            2. Title - My Content - Shortcut
            3. Summary should be empty
            4. Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text(target_path, "06.01")
        HomePage.ModalDailogs.Shortcut.Title.verify_text("My Content - Shortcut", "06.02")
        HomePage.ModalDailogs.Shortcut.Summary.verify_text("", "06.03")
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled("06.04")
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled("06.06")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click OK
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, folder_name, 60)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that 'My Content - Shortcut' folder shortcut created with the shortcut icon
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_folders([folder_name], "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right-click on 'My Content - Shortcut' > Delete
        """
        HomePage.Workspaces.ContentArea.delete_folder(folder_name)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that 'My Content - Shortcut' folder shortcut gets deleted
        """
        HomePage.Workspaces.ContentArea.verify_folders([folder_name], "08.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)