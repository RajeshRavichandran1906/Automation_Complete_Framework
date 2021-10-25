"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 30 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927993_TestClass(BaseTestCase):
    
    def test_C9927993(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Click on "Workspaces" in the Resource Tree.
        """
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Designer".
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Designer_Framework")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Right click on chart "DF_Chart" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify the context menu:
            Verify the context menu:
            Run.
            Run (Run in new window/Run deferred/Run with SQL trace).
            Schedule Email
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Edit with text editor.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        HomePage.ContextMenu.verify(expected_menus, "05.02", menu_path = "Run...")
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        expected_menus = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(expected_menus, "05.03", menu_path = "Schedule")
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "05.04", menu_path = "Security")
        navigator_element = utils.validate_and_get_webdriver_object('.toolbar-spacer',"navigator_css")
        HomePage.ContextMenu.close(element_object=navigator_element,location="middle")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right click on page "DF_Page" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Page")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify the context menu:
            Run.
            Run in new window.
            Edit.
            Download translations.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "06.02", menu_path = "Security")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        HomePage.ContextMenu.close(element_object=navigator_element,location="middle")
        
        STEP_07 = """
            Step 07.00 : Right click on chart "DF_Report" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Report")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify the context menu:
            Run.
            Run (Run in new window/Run deferred/Run with SQL trace).
            Schedule Email
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Edit with text editor.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "07.01")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "07.02", menu_path = "Security")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)

if __name__ == "__main__":
    unittest.main() 