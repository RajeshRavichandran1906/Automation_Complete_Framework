"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 02-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929846_TestClass(BaseTestCase):
    
    def test_C9929846(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        env_url = HomePage.Home._utils.get_setup_url().replace("home8206", "")
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces tab
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that 'Workspaces' is available at the navigation bar and also in the top of the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.verify_items(['Workspaces'], '02.01')
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on 'Workspaces' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that the two 'Action Bars' such as Workspace' and 'Folder' are displayed
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(['Workspace', 'Folder'], '03.01')
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on 'Workspaces' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab_option('Workspace')
        HomePage.ModalDailogs.NewWorkspace.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that 'New Workspace' dialog displayed and in the type drop-down box it displayed 'Enterprise workspace'
        """
        HomePage.ModalDailogs.NewWorkspace.verify_title('New Workspace', '04.01')
        HomePage.ModalDailogs.NewWorkspace.Type.verify_text('Enterprise workspace', '04.01')
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'Type' drop-down
        """
        HomePage.ModalDailogs.NewWorkspace.Type.click()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that it displayed two workspaces are 'Enterprise workspace' and 'Tenant workspace'
        """
        HomePage.ContextMenu.verify(['Enterprise workspace', 'Tenant workspace'], '05.01')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click Cancel to close the 'New Workspace' dialog
        """
        HomePage.ModalDailogs.NewWorkspace.CancelButton.click()
        HomePage.ModalDailogs.NewWorkspace.wait_for_diappear()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on 'Settings' banner link > Select 'Administration Console' > Click on 'BI Portal'
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select("Administration Console")
        HomePage.Home._core_utils.switch_to_new_window()
        bi_portal = self.driver.find_element_by_xpath("//div[@id='_idConfigurationButton']//tr[normalize-space()='BI Portal']//img")
        HomePage.Home._core_utils.left_click(bi_portal)
        HomePage.Home._utils.synchronize_with_visble_text("#idApplicationSettingsPageView", "Open First Workspace", 30)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that the 'Open First Workspace' option gets displayed
        """
        open_first_workspace = self.driver.find_element_by_xpath("//div[@id='idApplicationSettingsPageView']//div[normalize-space()='Open First Workspace']")
        HomePage.Home._utils.asequal(True, open_first_workspace.is_displayed(), "Step 07.01 : Verify that the 'Open First Workspace' option gets displayed")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the admin console
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Launch Legacyhome using below API Link as:
            http://machine_name:port/alias/legacyhome
        """
        legacyhome_url = env_url + "legacyhome"
        self.driver.get(legacyhome_url)
        HomePage.Home._utils.wait_for_page_loads(60)
        HomePage.Home._utils.synchronize_with_visble_text("#bipTreePanel", "Workspaces", 120)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that 'Workspaces' appear in the tree instead of 'Domains'
        """
        workspaces = self.driver.find_element_by_xpath("//div[@id='bipTreePanel']//tr[normalize-space()='Workspaces']")
        HomePage.Home._utils.asequal(True, workspaces.is_displayed(), "Step 09.01 : Verify that 'Workspaces' appear in the tree instead of 'Domains'")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Switch back to Paris Homepage
        """
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on '+' icon > Select 'Assemble Visualizations' > Choose 'Blank' template
        """
        blank_css = ".pop-top [title='Blank']"
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualizations")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(blank_css, 60)
        blank_temp = self.driver.find_element_by_css_selector(blank_css)
        HomePage.Home._core_utils.left_click(blank_temp)
        HomePage.Home._utils.wait_for_page_loads(60)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on 'Content' from the sidebar > Click on '<' twice to move onto the resource tree
        """
        content_css = "div[data-ibx-type='pdTreeBrowserNode']>.tnode-label"
        HomePage.Home._utils.synchronize_with_visble_text(content_css, "My Content", 60)
        for node in ["My Workspace", "Workspaces"]:
            node_obj = self.driver.find_element_by_css_selector(content_css)
            HomePage.Home._core_utils.left_click(node_obj)
            HomePage.Home._utils.synchronize_with_visble_text(content_css, node, 60)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that 'Workspaces' appear in the resource tree instead of 'Domains'
        """
        workspaces = self.driver.find_element_by_css_selector(content_css).text.strip()
        HomePage.Home._utils.asequal("Workspaces", workspaces, "Step 12.01 : Verify that 'Workspaces' appear in the resource tree instead of 'Domains'")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close 'WebFOCUS Designer' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)