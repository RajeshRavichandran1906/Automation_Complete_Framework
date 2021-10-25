"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 18-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927791_TestClass(BaseTestCase):
    
    def test_C9927791(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
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
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace > 'G784912' folder
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G784912")
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that 'P406_S31920' workspace and 'G784912' folder gets expanded. Also, verify the breadcrumb trail as 'Workspaces > P406_S31920 > G784912'
        """
        HomePage.Workspaces.ResourcesTree.verify_expanded("P406_S31920->G784912", "03.01")
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G784912", "03.02")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User (autoadvuser62).
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that by default 'Retail_Samples' workspace gets expanded. Also, verify the breadcrumb trail as 'Workspaces > Retail_Samples'
        """
        HomePage.Workspaces.ResourcesTree.verify_expanded("Retail Samples", "05.01")
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>Retail Samples", "05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User (autodevuser208).
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.infoassist_api_logout()
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("07", STEP_07, True)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Collapse 'G784912' folder under 'P406_S31920' workspace and 'P406_S31920' workspace to revert back the Paris Homepage content area by its default state.
        """
        HomePage.Workspaces.ResourcesTree.verify_expanded("P406_S31920->G784912", "07.01")
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs("Workspaces>P406_S31920>G784912", "07.02")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Collapse 'G784912' folder under 'P406_S31920' workspace and 'P406_S31920' workspace to revert back the Paris Homepage content area by its default state.
        """
        #HomePage.Workspaces.ResourcesTree
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)
        
        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)