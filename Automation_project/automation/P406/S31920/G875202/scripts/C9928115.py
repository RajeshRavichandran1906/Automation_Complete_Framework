"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 15-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928115_TestClass(BaseTestCase):
    
    def test_C9928115(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mriddev")
        portal_name = "v5-alias"
        base_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        portal_url = base_url + "portal/P406_S31920/G875202/v5-alias"
        portal_alias_url = base_url + "portal/testalias"
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
            STEP 05 : Enter title as 'v5-alias' in create portal dialog.
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)
        
        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify URL : http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias
        """
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        

        STEP_06 = """
            STEP 06 : Enter alias 'testalias'.
        """
        HomePage.ModalDailogs.V5Portal.Alias.enter_text("testalias")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify URL: http://machine_name:port/alias/portal/testalias
        """
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_alias_url, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'Create'.
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.wait_for_page_loads(60)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 60)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right click on 'v5-alias' and select Run'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875202->" + portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "available", 80)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify portal appears as following:
            1. Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/testalias
            2.'Information Builders' logo appears at the top left corner of the portal banner area
            3.'v5-alias' portal title appears in the portal banner area
            4.'Users Name' appears at the top right corner of the portal banner area
            5.'There are no pages available' label displayed in the page canvas and Page Heading title is not available in the page canvas
        """
        HomePage.Home._utils.asequal(portal_alias_url, self.driver.current_url, "Step 08.01 :Verify Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/testalias")
        logo = self.driver.find_element_by_css_selector("div.pvd-banner-logo")
        logo_status = (logo.is_displayed() and "IB_logo.png" in logo.value_of_css_property("background-image"))
        HomePage.Home._utils.asequal(logo_status, True, "Step 08.02 : Verify 'Information Builders' logo appears")
        title = self.driver.find_element_by_css_selector("div.pvd-portal-title").text.strip()
        HomePage.Home._utils.asequal(portal_name, title, "Step 08.03 : Verify 'v5-alias' portal title appears in the portal banner area")
        user = self.driver.find_element_by_css_selector("div.pvd-menu-admin").text.strip()
        HomePage.Home._utils.asequal(user_name, user, "Step 08.04 : Verify 'Users Name' appears at the top right corner of the portal banner area")
        page = self.driver.find_element_by_css_selector(portal_canvas_css).text.strip()
        HomePage.Home._utils.asequal("There are no pages available", page, "Step 08.05 : Verify 'There are no pages available' label displayed in the page canvas")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close portal
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Right click on 'v5-alias' and select Edit.
        """
        #HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_name, 60)
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875202->" + portal_name)
        #HomePage.Workspaces.ContentArea.right_click_on_folder(portal_name)
        HomePage.ContextMenu.select("Edit")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)
        
        STEP_11 = """
            STEP 11 : Remove alias.
        """
        HomePage.ModalDailogs.V5Portal.Alias.clear()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify URL : http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias
        """
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "11.01")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)
        
        STEP_12 = """
            STEP 12 : Click save.
        """
        HomePage.ModalDailogs.V5Portal.SaveButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)
        
        STEP_13 = """
            STEP 13 : Right click on 'v5-alias' and select Run'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875202->" + portal_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(portal_canvas_css, "available", 80)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify portal appears as following:
            1. Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/v5-alias
            2.'Information Builders' logo appears at the top left corner of the portal banner area
            3.'v5-alias' portal title appears in the portal banner area
            4.'Users Name' appears at the top right corner of the portal banner area
            5.'There are no pages available' label displayed in the page canvas and Page Heading title is not available in the page canvas
        """
        HomePage.Home._utils.asequal(portal_url, self.driver.current_url, "Step 13.01 :Verify Portal runs in a new window with the below URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias")
        logo = self.driver.find_element_by_css_selector("div.pvd-banner-logo")
        logo_status = (logo.is_displayed() and "IB_logo.png" in logo.value_of_css_property("background-image"))
        HomePage.Home._utils.asequal(logo_status, True, "Step 13.02 : Verify 'Information Builders' logo appears")
        title = self.driver.find_element_by_css_selector("div.pvd-portal-title").text.strip()
        HomePage.Home._utils.asequal(portal_name, title, "Step 13.03 : Verify 'v5-alias' portal title appears in the portal banner area")
        user = self.driver.find_element_by_css_selector("div.pvd-menu-admin").text.strip()
        HomePage.Home._utils.asequal(user_name, user, "Step 13.04 : Verify 'Users Name' appears at the top right corner of the portal banner area")
        page = self.driver.find_element_by_css_selector(portal_canvas_css).text.strip()
        HomePage.Home._utils.asequal("There are no pages available", page, "Step 13.05 : Verify 'There are no pages available' label displayed in the page canvas")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)
        
        STEP_14 = """
            STEP 14 : Close portal
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)