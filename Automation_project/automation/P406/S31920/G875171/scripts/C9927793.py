"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 17-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927793_TestClass(BaseTestCase):
    
    def test_C9927793(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User (autodevuser207).
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that workspaces available in the content area get displayed in Grid View.
        """
        HomePage.Workspaces.ContentArea.verify_grid_view_displayed("02.01")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on the 'Switch to list view' toggle button.
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that the content area displayed in list view.
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("03.01")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User (autoadvuser63)
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that workspaces available in the content area get displayed in Grid View.
        """
        HomePage.Workspaces.ContentArea.verify_grid_view_displayed("05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that the content area still displayed in list view.
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on the 'Switch to grid view' toggle button to revert back the Paris Homepage content area by its default state.
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)