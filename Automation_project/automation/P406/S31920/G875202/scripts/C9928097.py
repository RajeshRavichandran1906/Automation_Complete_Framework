"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 07-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928097_TestClass(BaseTestCase):
    
    def test_C9928097(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mriddev")
        portal_name = "v5-mypages-with-alias"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/12345"
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
            STEP 04 : Click the 'Application' category button and click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name) #Delete portal if already exits.
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Enter 'v5-mypages-with-alias' in Title text box.
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Enter '12345' in the Alias text box.
        """
        HomePage.ModalDailogs.V5Portal.Alias.enter_text("12345")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Check the 'URL' text box : Check the "URL" text box. http://machine_name:port/alias/portal/12345
        """
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Check off 'Create My Pages menu'
        """
        HomePage.ModalDailogs.V5Portal.CreateMyPagesMenu.check()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click 'Create' button.
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Workspaces.locators.page_load_completed_css, 120)    
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 60)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Double click 'v5-mypages-with-alias' from the Repository tree.
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder(portal_name)
        grid_folder_css=HomePage.Workspaces.ContentArea.locators.grid_view_folders[1]+str(":not(.folder-item-published)")
        HomePage.Home._utils.synchronize_with_visble_text(grid_folder_css, 'My Pages', 60)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 'My Pages' folder created in the content area in an unpublished state
        """
        HomePage.Workspaces.ContentArea.verify_unpublished_folders(['My Pages'], "09.01", "asequal")
        HomePage.Workspaces.ContentArea.verify_folders(['My Pages'], "09.02", "asequal")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right-click 'v5-mypages-with-alias' > Select 'Run'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875202->" + portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "available", 120)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following:
            1.Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/12345
            2.'TIBCO' logo appears at the top left corner of the portal banner area
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

        STEP_11 = """
            STEP 11 : Close the Portal run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)