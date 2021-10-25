"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 22-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928110_TestClass(BaseTestCase):
    
    def test_C9928110(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        portal_name = "v5-navigation-test1"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/P406_S31920/G875202/" + portal_name
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right-click on 'v5-navigation-test1' > Edit
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select("Edit")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : 
            1.Verify dialog title appears as 'Edit Portal';
            2.Verify title and name appears as 'v5-navigation-test1';
            3.Banner switch is on;
            4.Alias is empty;
            5.Logo is Not Selected;
            6.Navigation is Two-level side;
            7.Theme should be 'Light';
            8.URL field shows : https://machinename:port/alias/domain_name/v5-navigation-test1
        """
        HomePage.ModalDailogs.V5Portal.verify_title("Edit Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text(portal_name, "04.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "04.03")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.04")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "04.05")
        HomePage.ModalDailogs.V5Portal.Logo.verify_text("", "04.06")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(['Two-level side'], "04.07")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Light", "04.08")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "04.09")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on cancel button
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Edit portal dialog closes.
        """
        HomePage.ModalDailogs.V5Portal.verify_closed("05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)