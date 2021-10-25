"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 10-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927978_TestClass(BaseTestCase):
    
    def test_C9927978(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        run_menu = ['Run in new window', 'Run deferred']
        schedule_menu = ['Email', 'Printer', 'Report Library', 'Repository']
        
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
            STEP 03 : Click on 'Workspaces' in the Resource Tree.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Expand 'P406_S31920' workspace from the resource tree > Click on 'G784912' folder > Double click on folder 'Designer_Framework'.
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Designer_Framework")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "DF_Chart", 20)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click on chart 'DF_Chart' in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify context menu
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule Email.
            4.Schedule (Email/Printer/Report Library/Repository).
            5.Edit.
            6.Copy.
            7.Add to Favorites.
            8.Properties.
        """
        df_chart_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(df_chart_context, "05.01")
        HomePage.ContextMenu.verify(run_menu, "05.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        HomePage.ContextMenu.verify(schedule_menu, "05.03", menu_path="Schedule")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        STEP_06 = """
            STEP 06 : Right click on page 'DF_Page' in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Page")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify context menu,
            1.Run.
            2.Run in new window.
            3.Edit.
            4.Copy.
            5.Add to Favorites.
            6.Properties.
        """
        df_page_context = ['Run', 'Run in new window', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(df_page_context, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on chart 'DF_Report' in the content area.
        """
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Report")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule Email.
            4.Schedule (Email/Printer/Report Library/Repository).
            5.Edit.
            6.Copy.
            7.Add to Favorites.
            8.Properties.
        """
        df_report_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(df_report_context, "07.01")
        HomePage.ContextMenu.verify(run_menu, "07.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Report")
        HomePage.ContextMenu.verify(schedule_menu, "07.03", menu_path="Schedule")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)