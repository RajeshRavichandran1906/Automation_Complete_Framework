"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 20-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928109_TestClass(BaseTestCase):
    
    def test_C9928109(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mriddev")
        portal_name = "v5-navigation-test3"
        portal_container_css = "div.pvd-container"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click the 'Application' category button and click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name) #Delete portal if already exits.
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Enter title as 'v5-navigation-test3'
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Name input box is filled automatically as 'v5-navigation-test3'
        """
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Select 'Two-level top' navigation type
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Two-level top")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Check 'Show top navigation in banner' checkbox.
        """
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.check()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click Create
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify 'New Portal' dialog is closed;
            Portal title appears in Italic, Portal is unpublished.
        """
        HomePage.ModalDailogs.V5Portal.verify_closed("08.01")
        HomePage.Workspaces.ContentArea.verify_unpublished_folders([portal_name], "08.02")
        HomePage.Workspaces.ResourcesTree.verify_unpublished_items([portal_name], "08.03", parent_folder="P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on 'v5-navigation-test3' and select Run from content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_container_css, "There", 60)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify portal run mode appears as below.
        """
        actual_text = self.driver.find_element_by_css_selector(portal_container_css).text.strip()
        HomePage.Home._utils.asequal("There are no pages available", actual_text, "Step 09.01 : Verify portal run with 'There are no pages available'")
        actual_header_text = self.driver.find_element_by_css_selector("div.pvd-portal-banner").text.strip().replace("\n", " ")
        expected_header_text = "{} {}".format(portal_name, user_name)
        HomePage.Home._utils.asequal(expected_header_text, actual_header_text, "Step 09.02 : Verify portal header'")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close portal run mode
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)