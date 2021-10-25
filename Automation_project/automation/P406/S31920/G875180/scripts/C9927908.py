"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 16 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927908_TestClass(BaseTestCase):
    
    def test_C9927908(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """ 
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right-click on 'V5 Context Menu Testing' from the content area
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - Verify the following context menu:
        """
        expected_menus = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05_01 = """
            Step 05.00 : Hover over Customization menu
            Step 05.01 : Verification - Verify the following context menu:
        """
        expected_menus = ['Remove my customizations', 'Remove customizations for all users']
        HomePage.ContextMenu.verify(expected_menus, "05.01", menu_path = "Customizations")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06_01 = """
            Step 06 : Hover over Security Menu
            Step 06.01 : Verify the following context menu:
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "06.01", menu_path = "Security")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main() 