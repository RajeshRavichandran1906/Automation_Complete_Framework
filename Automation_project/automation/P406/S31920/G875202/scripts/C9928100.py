"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 15-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928100_TestClass(BaseTestCase):
    
    def test_C9928100(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        portal_name = "v5-alias-test1"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/P406_S31920/G875202/" + portal_name
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on 'v5-alias-test1' portal and Select 'Edit' option.
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select("Edit")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : 'Edit portal' dialog appears.
        """
        HomePage.Home._utils.wait_for_page_loads(3, pause_time=3)
        HomePage.ModalDailogs.V5Portal.verify_title("Edit Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text(portal_name, "04.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "04.03")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "04.04")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.05")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("04.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_browse_button_displayed("04.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("04.08")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(["Two-level side"], "04.09")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("04.10")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_unchecked("04.11")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.12")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Midnight", "04.13")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "04.14")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("04.15")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click 'Cancel' button.
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the 'Portal' dialog disappears.
        """
        HomePage.ModalDailogs.V5Portal.verify_closed("05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)
        