"""-------------------------------------------------------------------------------------------
Author Name : Vpriya
Automated On : 5th December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944215_TestClass(BaseTestCase):
    
    def test_C9944215(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        Visual_Expected_menu = ['Run', 'Run...', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        expected_Sub_menus = ['Run in new window', 'Run deferred']
        schedule_sub_menus = ['Email', 'Printer', 'Report Library', 'Repository']
        
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
            Step 04.00 : Right-click on report Report_Context.
        """
        HomePage.MyWorkspace.right_click_on_item("Report_Context")
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
        HomePage.MyWorkspace.right_click_on_item("Report_Context")
        HomePage.ContextMenu.verify(schedule_sub_menus, "03.03", menu_path = "Schedule")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Right click on chart "Chart_Context" 
        """
        HomePage.MyWorkspace.right_click_on_item("Chart_Context")
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
        HomePage.MyWorkspace.right_click_on_item("Chart_Context")
        HomePage.ContextMenu.verify(schedule_sub_menus, "04.03", menu_path = "Schedule")

        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on item "Visual_Context"
        """
        HomePage.MyWorkspace.right_click_on_item("Visual_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify context menu,
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
        HomePage.ContextMenu.verify(Visual_Expected_menu, "05.01")
        HomePage.ContextMenu.verify(['Run in new window'], "05.02", menu_path = "Run...")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right click on document "Document_Context" in the content area.
        """
        HomePage.MyWorkspace.right_click_on_item("Document_Context")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify context menu,
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
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        HomePage.ContextMenu.verify(expected_Sub_menus, "06.02", menu_path = "Run...")
        HomePage.MyWorkspace.right_click_on_item("Document_Context")
        HomePage.ContextMenu.verify(schedule_sub_menus, "06.03", menu_path = "Schedule")

        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Right click on alert "Alert_Context" in the content area.
        """
        HomePage.MyWorkspace.right_click_on_item("Alert_Context")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify context menu,
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
        HomePage.ContextMenu.verify(expected_menus, "07.01")
        HomePage.ContextMenu.verify(expected_Sub_menus, "07.02", menu_path = "Run...")
        HomePage.MyWorkspace.right_click_on_item("Alert_Context")
        HomePage.ContextMenu.verify(schedule_sub_menus, "07.03", menu_path = "Schedule")
        
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08= """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)

if __name__ == "__main__":
    unittest.main()