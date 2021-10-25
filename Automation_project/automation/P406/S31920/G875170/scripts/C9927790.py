"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 23-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927790_TestClass(BaseTestCase):
    
    def test_C9927790(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User (autodevuser208).
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that the resource tree gets expanded and it is in full view.
        """
        resources_tree = self.driver.find_element_by_css_selector(HomePage.Workspaces.ResourcesTree.locators.resources_tree_css)
        HomePage.Home._utils.asequal(True, resources_tree.is_displayed(), "Step 02.01 : Verify that the resource tree gets expanded")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on Collapse resources tree icon.
        """
        collapse = self.driver.find_element(*HomePage.Workspaces.ResourcesTree.locators.collapse)
        HomePage.Home._core_utils.left_click(collapse)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that the resource tree gets collapsed and there are no workspaces or folders displayed.
        """
        resources_tree = self.driver.find_element_by_css_selector(HomePage.Workspaces.ResourcesTree.locators.resources_tree_css)
        HomePage.Home._utils.asequal(False, resources_tree.is_displayed(), "Step 03.01 : Verify that the resource tree gets collapsed")
        HomePage.Workspaces.ResourcesTree.verify_items([],"03.02", assert_type="asequal")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Sign back into WebFOCUS Home Page as Advanced User (autoadvuser62).
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that the resource tree gets expanded and it is in full view.
        """
        resources_tree = self.driver.find_element_by_css_selector(HomePage.Workspaces.ResourcesTree.locators.resources_tree_css)
        HomePage.Home._utils.asequal(True, resources_tree.is_displayed(), "Step 06.01 : Verify that the resource tree gets expanded")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User (autodevuser208).
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that the resource tree still in collapsed state and there are no workspaces or folders displayed.
        """
        resources_tree = self.driver.find_element_by_css_selector(HomePage.Workspaces.ResourcesTree.locators.resources_tree_css)
        HomePage.Home._utils.asequal(False, resources_tree.is_displayed(), "Step 08.01 : Verify that the resource tree still in collapsed state")
        HomePage.Workspaces.ResourcesTree.verify_items([],"08.02", assert_type="asequal")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on Expand resources tree icon to revert back the Paris Homepage by its default state.
        """
        expand = self.driver.find_element(*HomePage.Workspaces.ResourcesTree.locators.expand)
        HomePage.Home._core_utils.left_click(expand)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)