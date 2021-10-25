"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 31 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928009_TestClass(BaseTestCase):
    
    def test_C9928009(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User.
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
            Step 03:00 :Click on "Workspaces" in the Resource Tree.
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Portal/Pages".
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Portal/Pages")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Right click on chart "V4_Portal_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("V4_Portal_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
           Step 05.00 : Verify context menu,
            Run.
            Remove my customizations.
            Add to Favorites.
            Properties.
        """
        expected_menus = ['Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        HomePage.ContextMenu.close()
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step06 :Right click on V5 Portal V5Portal_Context.
        """
        
        HomePage.Workspaces.ContentArea.right_click_on_file("V5Portal_Context")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
        Verify context menu,
        Run.
        Remove my customizations.
        Add to Favorites.
        Properties.
        """
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        HomePage.ContextMenu.close()
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        
        STEP_07 = """
            Step 07.00 : Right click on chart "Page_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Page_Context")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
           Step 07.00 : Verify context menu,
            Properties.
        """
        expected_menus_page = ['Properties']
        HomePage.ContextMenu.verify(expected_menus_page, "07.01")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)

if __name__ == "__main__":
    unittest.main() 