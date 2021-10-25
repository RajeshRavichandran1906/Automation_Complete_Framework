"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 10 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928007_TestClass(BaseTestCase):
    
    def test_C9928007(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        REPORT_EXPECTED_MENUS     = ['Run', 'Run...','Add to Favorites','Properties']
        REPORT_EXPECTED_SUB_MENUS = ['Run in new window', 'Run deferred']
        CHART_EXPECTED_MENUS      = ['Run', 'Run...','Add to Favorites','Properties']
        CHART_EXPECTED_SUB_MENUS  = ['Run in new window', 'Run deferred']
        VISUAL_EXPECTED_MENUS     = ['Run', 'Run...','Add to Favorites','Properties']
        VISUAL_EXPECTED_SUB_MENUS = ['Run in new window']
        DOC_EXPECTED_MENUS        = ['Run', 'Run...','Add to Favorites', 'Properties']
        DOC_EXPECTED_SUB_MENUS    = ['Run in new window', 'Run deferred']
        ALERT_EXPECTED_MENUS      = ['Run', 'Run...','Add to Favorites','Properties']
        ALERT_EXPECTED_SUB_MENUS  = ['Run in new window', 'Run deferred']
        CEUNTURY_EXPECTED_MENUS   = ['Open', 'Refresh', 'Properties']
        
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "IA/Visualization".
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("IA/Visualization")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right click on report Report_Context in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Report_Context")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        HomePage.ContextMenu.verify(REPORT_EXPECTED_MENUS, "04.01")
        HomePage.ContextMenu.verify(REPORT_EXPECTED_SUB_MENUS, "04.02", menu_path = "Run...")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on chart "Chart_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Chart_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        
        HomePage.ContextMenu.verify(CHART_EXPECTED_MENUS, "05.01")
        HomePage.ContextMenu.verify(CHART_EXPECTED_SUB_MENUS, "05.02", menu_path = "Run...")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right-click on item Visual_Context in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Visual_Context")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify context menu,
            Run.
            Run (Run in new window).
            Add to Favorites.
            Properties.
        """
        
        HomePage.ContextMenu.verify(VISUAL_EXPECTED_MENUS, "06.01")
        HomePage.ContextMenu.verify(VISUAL_EXPECTED_SUB_MENUS, "06.02", menu_path = "Run...")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Right click on document "Document_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Document_Context")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        
        HomePage.ContextMenu.verify(DOC_EXPECTED_MENUS, "07.01")
        HomePage.ContextMenu.verify(DOC_EXPECTED_SUB_MENUS, "07.02", menu_path = "Run...")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : Right click on alert "Alert_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Alert_Context")
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            Step 08.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        HomePage.ContextMenu.verify(ALERT_EXPECTED_MENUS, "08.01")
        HomePage.ContextMenu.verify(ALERT_EXPECTED_SUB_MENUS, "08.02", menu_path = "Run...")
        HomePage.ContextMenu.close(location = "top_middle")
        utils.capture_screenshot("08.01", STEP_08_01, expected_image_verify = True)
        
        STEP_09 = """
            Step 09.00 : Right click on sample content "centurysales" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("centurysales")
        utils.capture_screenshot("09.00", STEP_09)
        
        STEP_09_01 = """
        Verify context menu,
        Open.
        Refresh.
        Properties.
        """ 
        
        HomePage.ContextMenu.verify(CEUNTURY_EXPECTED_MENUS, "09.01")
        utils.capture_screenshot("09.01", STEP_09_01, expected_image_verify = True)
        
        STEP_10 = """
            Step 10.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("10.00", STEP_10)

if __name__ == "__main__":
    unittest.main() 