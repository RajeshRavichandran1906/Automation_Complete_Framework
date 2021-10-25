"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 14-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927981_TestClass(BaseTestCase):
    
    def test_C9927981(self):
        
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
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace from the resource tree > Click on 'G784912' folder
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double click on folder 'Schedule' from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("Schedule")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Schedule_Context", 20)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click on 'Schedule_Context' in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Schedule_Context")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify context menu,
            1.Edit.
            2.Edit With Designer Scheduler
            3.Run.
            4.View log.
            5.Copy.
            6.Properties.
        """
        schedule_context = ['Edit', 'Run', 'View log', 'Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(schedule_context, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on 'AccessList_Context' in the content area.
        """
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("AccessList_Context")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify context menu,
            1.Edit.
            2.Copy.
            3.Properties.
        """
        accesslist_context = ['Edit', 'Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(accesslist_context, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on 'DistributionList_Context' in the content area.
        """
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("DistributionList_Context")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify context menu,
            1.Edit.
            2.Copy.
            3.Properties.
        """
        distributionlist_context = ['Edit', 'Copy Ctrl+C', 'Properties']
        HomePage.ContextMenu.verify(distributionlist_context, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)