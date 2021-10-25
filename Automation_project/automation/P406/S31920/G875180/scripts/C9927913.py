"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 03 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927913_TestClass(BaseTestCase):
    
    def test_C9927913(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
                
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verification  - Verify that 'V5 Context Menu Testing' displayed as an item and NOT a folder from the content area
        """
        expected_files = ['V5 Context Menu Testing']
        HomePage.Workspaces.ContentArea.verify_files(expected_files, '03.01')
        HomePage.Workspaces.ContentArea.verify_folders(expected_files,'03.02', assert_type='asnotin')
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Right-click on 'V5 Context Menu Testing' from the content area
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("V5 Context Menu Testing")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - Verify the following context menu
        """
        expected_menus = ['Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '04.01')
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)

if __name__ == "__main__":
    unittest.main() 