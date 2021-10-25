"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 11 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928008_TestClass(BaseTestCase):
    
    def test_C9928008(self):
        
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
            Step 03.00 : Click on "Workspaces" in the Resource Tree.
        """
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Designer_Framework" in the content area
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Designer_Framework")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Right click on chart DF_Chart.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Chart")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        expected_menus = ['Run', 'Run...','Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_sub_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_sub_menus, "05.02", menu_path = "Run...")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Right click on chart DF_Report.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Report")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        HomePage.ContextMenu.verify(expected_sub_menus, "06.02",menu_path = "Run...")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Right click on page DF_Page.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("DF_Page")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify context menu,
            Run.
            Run (Run in new window).
            Add to Favorites.
            Properties.
        """
        HomePage.ContextMenu.verify(['Run', 'Run in new window', 'Add to Favorites', 'Properties'], "07.01")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)

if __name__ == "__main__":
    unittest.main() 