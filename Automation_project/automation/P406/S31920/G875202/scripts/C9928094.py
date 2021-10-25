"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 05-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928094_TestClass(BaseTestCase):
    
    def test_C9928094(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/P406_S31920/G875202"
        
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
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the following:
            1.'New Portal' dialog opens. Title, Name, and Alias should be empty.
            2.Cursor for input stays in the 'Title' text box by default.
            3.Banner toggle button is on
            4.Show portal title in banner checkbox is checked
            5.Logo is enabled with the text Not Selected and Browse button is on the right of the logo
            6.Two-level side navigation is selected
            7.Show top navigation in banner with a checkbox is disabled
            8.Maximum width text box is available and 100% is set by default
            9.'Designer 2018' theme is selected by default.
            10.URL as 'http://machinename:port/alias/portal/P406_S31920/G8751...' and it is read-only
            11.Create button is disabled and the Cancel button is enabled by default.
        """
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text("", "04.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text("", "04.03")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "04.04")
        HomePage.ModalDailogs.V5Portal.Title.verify_border_color("malibu", "04.05")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.06")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("04.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_browse_button_displayed("04.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("04.08")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(["Two-level side"], "04.09")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("04.10")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_unchecked("04.11")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.12")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "04.13")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "04.14")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("04.15")
        HomePage.ModalDailogs.V5Portal.CreateButton.verify_disabled("04.16")
        HomePage.ModalDailogs.V5Portal.CancelButton.verify_enabled("04.17")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Hover over 'Navigation types' one by one.
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Two-level side")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Check the tool tip appears as 'Two-level side', 'Three-level' and 'Two-level top' respectively.
        """
        HomePage.ModalDailogs.V5Portal.Navigation.verify("05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Maximum width' text box and Enter '1500px'
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.enter_text("1500px")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the 'Maximum width' text box in as below.
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_text("1500px", "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on 'Theme' dropdown.
        """
        HomePage.ModalDailogs.V5Portal.Theme.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the dropdown value 'Designer 2018', 'Light' and 'Midnight', 'Vivid' themes are available for selection.
        """
        themes = ['Designer 2018', 'Light', 'Midnight', 'Vivid', 'Custom Theme2']
        HomePage.ContextMenu.verify(themes, "07.01", "asin")
        HomePage.ContextMenu.close(x=-10)
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Hover over 'X' icon right side top in Portal dialog.
        """
        close_icon = self.driver.find_element(*HomePage.ModalDailogs.V5Portal._locator_.close_icon)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Check it brings up 'Close' tool tip.
        """
        HomePage.Home._utils.asequal("Close", close_icon.get_attribute("title"), "Step 08.01 : Verify close icon displayed tooltip")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click 'X' icon to close the Portal page.
        """
        HomePage.ModalDailogs.V5Portal.close()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Check the 'Portal' dialog disappears.
        """
        HomePage.ModalDailogs.V5Portal.verify_closed("09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)