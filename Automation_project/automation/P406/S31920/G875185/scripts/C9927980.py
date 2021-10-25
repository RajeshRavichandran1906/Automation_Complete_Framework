"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 10-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927980_TestClass(BaseTestCase):
    
    def test_C9927980(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace from the resource tree > Click on 'G784912' folder > Double click on folder 'ReportingObject'.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("ReportingObject")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "ReportingObject_Context", 20)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on 'ReportingObject_Context' in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("ReportingObject_Context")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify context menu:
            1.Copy.
            2.New (InfoAssist[Report/Chart/Document]).
            3.Properties.
        """
        context_menu = ['Copy Ctrl+C', 'open_in_new New', 'Properties']
        HomePage.ContextMenu.verify(context_menu, "04.01")
        HomePage.ContextMenu.verify(['Report', 'Chart', 'Document'], "04.02",  menu_path="New->InfoAssist")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)