"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 16-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928107_TestClass(BaseTestCase):
    
    def test_C9928107(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mriddev")
        portal_name = "v5-navigation-test1"
        portal_canvas_css = "div.pvd-canvas-container"
        light_theme_xpath = "//div[contains(@class,'pop-top')]//*[contains(text(),'Light')]"
        
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
            STEP 05 : Enter title as 'v5-navigation-test1' .
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Name input box is filled automatically as 'v5-navigation-test1'
        """
        HomePage.ModalDailogs.V5Portal.Name.verify_text(portal_name, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        

        STEP_06 = """
            STEP 06 : Click on Theme dropdown; Select 'Light' theme.
        """
        HomePage.ModalDailogs.V5Portal.Theme.click()
        HomePage.Home._utils.wait_for_page_loads(60)
        elem=self.driver.find_element_by_xpath(light_theme_xpath)
        elem.click()
        #HomePage.ContextMenu.select("Light")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)


        STEP_07 = """
            STEP 07 : Choose Two-level side navigation if not selected by default.
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Two-level side")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click 'Create'.
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 60)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : 
            1) Verify 'New Portal' dialog is closed;
            2) Portal title appears in Italic;
            3) Portal is unpublished.
        """
        HomePage.ModalDailogs.V5Portal.verify_closed("08.01")
        portal_title = self.driver.find_element_by_xpath("//div[contains(@class, 'home-tree-node')]/div[text()='{}']".format(portal_name))
        title_font_style = portal_title.value_of_css_property("font-style")
        HomePage.Home._utils.asequal("italic", title_font_style, "Step 08.02: Portal title appears in Italic")
        HomePage.Workspaces.ContentArea.verify_unpublished_folders([portal_name], "08.03")
        HomePage.Home._utils.capture_screenshot("08- Expected", STEP_08_EXPECTED, True)

 
        STEP_09 = """
            STEP 09 : Right click on 'v5-navigation-test1' and select Run
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875202->" + portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "available", 80)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : 1) Verify portal run mode shows no banner and title as below;
                                 2) Verify top navigation bars appears as below
        """
        title = self.driver.find_element_by_css_selector("div.pvd-portal-title").text.strip()
        left_banner = self.driver.find_element_by_css_selector("div.pvd-container div.bundle-folder-wrapper")
        HomePage.Home._utils.asequal(portal_name, title, "Step 09.01: Verify portal title")
        HomePage.Home._utils.asequal(False, left_banner.is_displayed(), "Step 09.02: left banner is not displayed")
        logo = self.driver.find_element_by_css_selector("div.pvd-banner-logo")
        logo_status = (logo.is_displayed() and "IB_logo.png" in logo.value_of_css_property("background-image")) # Verify portal logo
        user = self.driver.find_element_by_css_selector("div.pvd-menu-admin").text.strip()
        user_status = True if user_name == user else False # Verify user name in top navigation bar
        portal_theme = self.driver.find_element_by_css_selector("link.portal-theme").get_attribute("href")
        portal_theme_status = True if "Light/theme.css" in portal_theme else False # Verify portal light theme
        top_navigation_bar = all([logo_status, user_status, portal_theme_status])
        HomePage.Home._utils.asequal(top_navigation_bar, True, "Step 09.03 : Verify top navigation bars appears as below")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)
        
        STEP_10 = """
            STEP 10 : Close portal run mode
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)