"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 27 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927966_TestClass(BaseTestCase):
    
    def test_C9927966(self):
        
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
            Step 03.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Schedule".
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Schedule")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right click on "Schedule_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Schedule_Context")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify the following context menu:
            Edit.
            Run.
            View log.
            Disable.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective policy.../Owner...).
            Properties.
        """
        expected_menus = ['Edit', 'Run', 'View log', 'Disable', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "04.02", menu_path = "Security")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on "AccessList_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("AccessList_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify the following context menu:
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective policy.../Owner...).
            Properties.
        """
        expected_menus = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "05.02", menu_path = 'Security')
        HomePage.ContextMenu.close(location = "top_middle")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right click on "DistributionList_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DistributionList_Context")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """  
            Step 06.01 : Verify the following context menu:
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective policy.../Owner...).
            Properties.
        """
        expected_menus = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "05.02", menu_path = 'Security')
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main()