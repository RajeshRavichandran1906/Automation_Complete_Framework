"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 27 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927965_TestClass(BaseTestCase):
    
    def test_C9927965(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "ReportingObject".
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("ReportingObject")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_4 = """
            Step 04.00 : Right click on "ReportingObject_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("ReportingObject_Context")
        utils.capture_screenshot("04.00", STEP_4)
        
        STEP_04_01 = """
            Step 04.01 : Verify the context menu:
            Run.
            Run... (Run in new window/Run deferred).
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+V.
            Create shortcut.
            Delete DEL.
            New (Designer[Workbook/Chart], InfoAssist[Report/Chart/Document]).
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'open_in_new New', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        expected_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_menus, "04.02", menu_path = "Run...")
        HomePage.Workspaces.ContentArea.right_click_on_file("ReportingObject_Context")
        expected_menus = ['InfoAssist']
        HomePage.ContextMenu.verify(expected_menus, "04.03", menu_path = "New")
        expected_menus = ['Report', 'Chart', 'Document']
        HomePage.ContextMenu.verify(expected_menus, "04.04", menu_path = "InfoAssist")
        HomePage.Workspaces.ContentArea.right_click_on_file("ReportingObject_Context")
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "04.05", menu_path = "Security")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """        
            Step 05.00 : In the banner link, click on the top right username > Sign Out.
        """        
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)

if __name__ == "__main__":
    unittest.main()