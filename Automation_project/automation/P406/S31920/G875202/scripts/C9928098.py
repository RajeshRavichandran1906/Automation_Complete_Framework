"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 29-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928098_TestClass(BaseTestCase):
    
    def test_C9928098(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mriddev")
        portal_name = "v5-mypages-with-alias1"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/123"
        portal_canvas_css = "div.pvd-canvas-container"
        
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
            STEP 04 : Right-click on 'v5-mypages-with-alias' portal > Select 'Edit'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select("Edit")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the 'Edit Portal' dialog box opened with the following options:
            1.Title displayed as 'v5-mypages-with-alias1'
            2.Name displayed 'v5-mypages-with-alias1'
            3.Alias should be 123
            4.Banner toggle button is on
            5.'Show portal title in banner' checkbox gets checked
            6.Logo gets disabled with the text Not Selected and Browse button is on the right side of the logo
            7.Two-level side navigation is selected by default
            8.'Show top navigation in banner' checkbox is disabled by default
            9.Maximum width text box is set to 100% by default Theme should be 'Designer 2018'
            10.URL should be in read-only and it is displayed as, 'http://machine_name:port/alias/portal/P406_S31920/G875202/v5-mypages-with-alias1'
            11.Save button is disabled and the Cancel button is enabled
        """
        HomePage.ModalDailogs.V5Portal.verify_title("Edit Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text(portal_name, "04.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "04.03")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.04")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("123", "04.05")
        HomePage.ModalDailogs.V5Portal.Logo.verify_text("", "04.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("04.07")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(['Two-level side'], "04.08")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("04.09")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_unchecked("04.98")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.10")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "04.11")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "04.12")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("04.13")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the 'Theme' dropdown > Choose 'Light' theme.
        """
        HomePage.ModalDailogs.V5Portal.Theme.click()
        HomePage.ContextMenu.select("Light")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Delete the 'Alias' name.
        """
        HomePage.ModalDailogs.V5Portal.Alias.clear()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the 'URL' - http://machine_name:port/alias/portal/P406_S31920/G875202/v5-mypages-with-alias1
        """
        _porta_url = base_url + "portal/P406_S31920/G875202/" + portal_name
        HomePage.ModalDailogs.V5Portal.URL.verify_text(_porta_url, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Enter '123' in Alias text box.
        """
        HomePage.ModalDailogs.V5Portal.Alias.enter_text("123")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Check the 'URL' - http://machine_name:port/alias/portal/123
        """
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "06.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click 'Save' button.
        """
        HomePage.ModalDailogs.V5Portal.SaveButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on 'WebFOCUS Home' view > Click on 'VIEW ALL' link in the 'Portals' section
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_home()
        HomePage.Home.Portals.click_view_all()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Right-click on 'v5-mypages-with-alias1' portal > select 'Run'
        """
        HomePage.Home.ViewAll.right_click_on_item(portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "available", 100)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following:
            1.Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/123
            2. 'TIBCO' logo appears at the top left corner of the portal banner area
            3.'v5-mypages-with-alias' portal title appears in the portal banner area
            4.'Users Name' appears at the top right corner of the portal banner area
            5.'My Pages' folder displayed with dropdown icon
            6.'There are no pages available' label displayed in the page canvas and Page Heading title is not available in the page canvas
        """
        HomePage.Home._utils.asequal(portal_url, self.driver.current_url, "Step 10.01 : Verify portal runs in a new window with the below URL: http://machine_name:port/alias/portal/12345")
        logo = self.driver.find_element_by_css_selector("div.pvd-banner-logo")
        
        log_status = (logo.is_displayed() and "IB_logo.png" in logo.value_of_css_property("background-image"))
        HomePage.Home._utils.asequal(log_status, True, "Step 10.02 : Verify 'Tibco' logo appears")
        title = self.driver.find_element_by_css_selector("div.pvd-portal-title").text.strip()
        HomePage.Home._utils.asequal(portal_name, title, "Step 10.03 : Verify 'v5-mypages-with-alias' portal title appears in the portal banner area")
        user = self.driver.find_element_by_css_selector("div.pvd-menu-admin").text.strip()
        HomePage.Home._utils.asequal(user_name, user, "Step 10.04 : Verify 'Users Name' appears at the top right corner of the portal banner area")
        page = self.driver.find_element_by_css_selector(portal_canvas_css).text.strip()
        HomePage.Home._utils.asequal("There are no pages available", page, "Step 10.04 : Verify 'There are no pages available' label displayed in the page canvas")
        left_side = self.driver.find_element_by_css_selector("div.pvd-left-main-panel").text.strip()
        HomePage.Home._utils.asequal("chevron_right\nMy Pages", left_side, "Step 10.05 : Verify 'My Pages' folder displayed with dropdown icon")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on 'TIBCO' logo
            URL redirect to www.tibco.com
        """
        HomePage.Home._core_utils.left_click(logo, yoffset=2)
        HomePage.Home._core_utils.switch_to_new_window()
        tibco_url = self.driver.current_url
        HomePage.Home._utils.asequal(tibco_url, 'https://www.tibco.com/', "Step 11.01: Verify tibco url")
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)
        
        STEP_12 = """
            STEP 12 : Close the portal run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)