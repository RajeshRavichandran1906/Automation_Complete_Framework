"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 30-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928020_TestClass(BaseTestCase):
    
    def test_C9928020(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        trees = ['Web Content', 'Global Resources']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Collapse Workspaces from the resource tree if workspaces is expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that Workspaces and Global Resources are available as main nodes under resource tree.
        """
        HomePage.Workspaces.ResourcesTree.verify_items(['Workspaces', 'Global Resources'], "03.01", "asequal")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Collapse Workspaces from the resource tree if workspaces is expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that Web Content and Global Resources are not available under resource tree.
        """
        HomePage.Workspaces.ResourcesTree.verify_items(trees, "07.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Collapse Workspaces from the resource tree if workspaces is expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that Web Content and Global Resources are not available under resource tree.
        """
        HomePage.Workspaces.ResourcesTree.verify_items(trees, "11.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Collapse Workspaces from the resource tree if workspaces is expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that Web Content and Global Resources are not available under resource tree.
        """
        HomePage.Workspaces.ResourcesTree.verify_items(trees, "15.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)