"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 14/2/2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928005_TestClass(BaseTestCase):
    
    def test_C9928005(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
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
            Step 03.00 : Right-click on "P406_S31920" workspace from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify Context Menu,
            Expand/Collapse.
            Refresh.
            Properties..
        """
        expected_menus = ['Expand','Refresh','Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Click "Expand" option.
        """
        HomePage.ContextMenu.select("Expand")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : From the Resource Tree > Right click on "My Content" folder under "P406_S31920" workspace
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->My Content")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify Context Menu,
            Expand/Collapse.
            Paste (Grayed out).
            Delete.
            Refresh.
            Properties.
        """
        expected_menus = ['Expand', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Paste Ctrl+V']
        HomePage.ContextMenu.verify_disabled_options(expected_menus, "05.02")
        HomePage.ContextMenu.close(location='top_right')
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
       
        STEP_06 = """
            Step 06.00 : Under Workspaces Tree >> Right-click on G784912 folder underneath 'P406_S31920' workspace.
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G784912")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify the Context Menu:
            Expand/Collapse.
            Refresh.
            Properties.
        """
        expected_menus = ['Expand', 'Refresh','Properties']
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)
        
if __name__ == "__main__":
    unittest.main() 