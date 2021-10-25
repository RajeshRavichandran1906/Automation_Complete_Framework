"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 01-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927979_TestClass(BaseTestCase):
    
    def test_C9927979(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspace' view
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Under resource tree >> Navigate to 'P406_S31920' workspace >> G784912 >> Click on folder **Portal/Pages**.
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912->Portal/Pages")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on Collaborative portal **V4_Portal_Context**.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("V4_Portal_Context")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify context menu,
            1.Run.
            2.Remove my customizations.
            3.Copy.
            4.Add to Favorites.
            5.Properties.
        """
        v4_portal_context = ['Run', 'Remove my customizations', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(v4_portal_context, "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right click on portal page **Page_Context**.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Page_Context")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify context menu,
            1.Copy.
            2.Properties.
        """
        page_portal_context = ['Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(page_portal_context, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)