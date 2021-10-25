"""-------------------------------------------------------------------------------------------
Author Name : Vpriya
Automated On : 6th December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944216_TestClass(BaseTestCase):
    
    def test_C9944216(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        expected_Sub_menus = ['Run in new window', 'Run deferred']
        expected_menu_DF_Page = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mradvid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Right click on chart DF_Chart.
        """
        HomePage.MyWorkspace.right_click_on_item("DF_Chart")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify context menu,
            Run.
            Run... (Run in new window)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        
        HomePage.ContextMenu.verify(expected_menus, "03.01")
        HomePage.ContextMenu.verify(expected_Sub_menus, "03.02", menu_path = "Run...")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Right click on workbook DF_Report.
        """
        HomePage.MyWorkspace.right_click_on_item("DF_Report")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify context menu,
            Run.
            Run... (Run in new window)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        HomePage.ContextMenu.verify(expected_Sub_menus, "04.02", menu_path = "Run...")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on page DF_Page.
        """
        HomePage.MyWorkspace.right_click_on_item("DF_Page")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify context menu,
            Run.
            Run in new window
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        HomePage.ContextMenu.verify(expected_menu_DF_Page, "05.01")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06= """
            Step 06.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == "__main__":
    unittest.main()