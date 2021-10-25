"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 11-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927977_TestClass(BaseTestCase):
    
    def test_C9927977(self):
        
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
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace from the resource tree > Click on 'G784912' folder
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double click on folder 'IA/Visualization' from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("IA/Visualization")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Chart_Context", 20)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click on report 'Report_Context' in the content area.
        """
        report = "Report_Context"
        HomePage.Workspaces.ContentArea.right_click_on_file(report)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule (Email/Printer/Report Library/Repository).
            4.Edit.
            5.Copy.
            6.Add to Favorites.
            7.Properties.
        """
        report_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(report_context, "05.01")
        HomePage.ContextMenu.verify(run_menu, "05.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file(report)
        HomePage.ContextMenu.verify(schedule_menu, "05.03", menu_path="Schedule")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on chart 'Chart_Context' in the content area.
        """
        chart = "Chart_Context"
        HomePage.Workspaces.ContentArea.right_click_on_file(chart)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule (Email/Printer/Report Library/Repository).
            4.Edit.
            5.Copy.
            6.Add to Favorites.
            7.Properties.
        """
        chart_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(chart_context, "06.01")
        HomePage.ContextMenu.verify(run_menu, "06.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file(chart)
        HomePage.ContextMenu.verify(schedule_menu, "06.03", menu_path="Schedule")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on item 'Visual_Context' in the content area.
        """
        visual = "Visual_Context"
        HomePage.Workspaces.ContentArea.right_click_on_file(visual)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window).
            3.Edit.
            4.Copy.
            5.Add to Favorites.
            6.Properties.
        """
        visual_context = ['Run', 'Run...', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(visual_context, "07.01")
        HomePage.ContextMenu.verify(['Run in new window'], "07.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on document 'Document_Context' in the content area.
        """
        document = "Document_Context"
        HomePage.Workspaces.ContentArea.right_click_on_file(document)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule (Email/Printer/Report Library/Repository).
            4.Edit.
            5.Copy.
            6.Add to Favorites.
            7.Properties.
        """
        document_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(document_context, "08.01")
        HomePage.ContextMenu.verify(run_menu, "08.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file(document)
        HomePage.ContextMenu.verify(schedule_menu, "08.03", menu_path="Schedule")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on 'Alert_Context' in the content area.
        """
        alert = "Alert_Context"
        HomePage.Workspaces.ContentArea.right_click_on_file(alert)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify context menu,
            1.Run.
            2.Run (Run in new window/Run deferred).
            3.Schedule (Email/Printer/Report Library/Repository).
            4.Edit.
            5.Copy.
            6.Add to Favorites.
            7.Properties.
        """
        alert_context = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(alert_context, "09.01")
        HomePage.ContextMenu.verify(run_menu, "09.02", menu_path="Run...")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Workspaces.ContentArea.right_click_on_file(alert)
        HomePage.ContextMenu.verify(schedule_menu, "09.03", menu_path="Schedule")
        HomePage.ContextMenu.close(location='bottom_middle', y=5)
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Right click on sample content 'centurysales' in the content area.
        """
        centurysales = "centurysales"
        HomePage.Workspaces.ContentArea.right_click_on_folder(centurysales)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify context menu,
            1.Open.
            2.Copy.
            3.Refresh.
            4.Properties.
        """
        centurysales_context = ['Open', 'Copy Ctrl+C', 'Refresh', 'Properties']
        HomePage.ContextMenu.verify(centurysales_context, "10.01")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)