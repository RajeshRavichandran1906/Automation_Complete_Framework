"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 19 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927976_TestClass(BaseTestCase):
    
    def test_C9927976(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand "P406_S31920" workspace from the resource tree > Click on "My Content" folder
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->My Content")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify items Report, Portal, Shortcut & HTML page items are available under My Content folder.
        """
        expected_files = ['V4_Portal_Context', 'HTML_Content', 'IA_Report', 'IA_Report - Shortcut']
        HomePage.Workspaces.ContentArea.verify_files(expected_files, "03.01")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Right click on report "IA_Report" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("IA_Report")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify the following context menu:
            Run.
            Run (Run in new window/Run deferred).
            Schedule (Email/Printer/Report Library/Repository).
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Add to Favorites.
            Share.
            Share with.
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        expected_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_menus, "04.02", menu_path = "Run...")
        HomePage.Workspaces.ContentArea.right_click_on_file("IA_Report")    
        expected_menus = ['Email', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(expected_menus, "04.02", menu_path = "Schedule")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on portal "V4_Portal_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("V4_Portal_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify the following context menu:
            Run.
            Customizations (Remove my customizations).
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Add to Favorites.
            Share.
            Share with.
            Properties.
        """
        expected_menus = ['Run', 'Customizations', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Remove my customizations']
        HomePage.ContextMenu.verify(expected_menus, "05.02", menu_path = 'Customizations')
        HomePage.ContextMenu.close(location = "top_middle")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right click on HTML "HTML_Content" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("HTML_Content")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify the following context menu:
            View.
            View in new window.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Add to Favorites.
            Share.
            Share with.
            Properties.
        """
        expected_menus = ['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Right click on Shortcut "IA_Report - Shortcut" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("IA_Report - Shortcut")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify the following context menu:
            Run.
            Run... (Run in new window/Run deferred).
            Schedule (Email/Printer/Report Library/Repository).
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Add to Favorites.
            Share.
            Share with.
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "07.01")
        expected_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_menus, "07.02", menu_path = "Run...")
        HomePage.Workspaces.ContentArea.right_click_on_file("IA_Report - Shortcut")
        expected_menus = ['Email', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(expected_menus, "07.03", menu_path = "Schedule")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)
        
if __name__ == "__main__":
    unittest.main() 