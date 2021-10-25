"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 04 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927953_TestClass(BaseTestCase):
    
    def test_C9927953(self):
        
        """
            TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 :Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login("mradvid", "mradvpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
        Right-click on 'V5 Context Menu Testing2' and click 'Add to Favorites'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('V5 Context Menu Testing2')
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 ="""
        Verify that Favorite added popup opens with a background transparent green layer over the popup.
        """
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.NotifyPopup.verify_text("Favorite added",'04.01')
        HomePage.NotifyPopup.verify_background_color('04.02')
        HomePage.NotifyPopup.verify_transparent('04.03')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """
        Click on 'WebFOCUS Home' tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing2'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_home()
        HomePage.Home.Favorites.right_click_on_item('V5 Context Menu Testing2')
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Verify that 'V5 Context Menu Testing2' appears
        Run
        Remove from Favorites
        Properties
        """
        HomePage.ContextMenu.verify(['Run', 'Remove from Favorites', 'Properties'],'05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Right-click on 'V5 Context Menu Testing2' > Click Remove from Favorites
        """
        HomePage.Home.Favorites.right_click_on_item('V5 Context Menu Testing2')
        HomePage.ContextMenu.select('Remove from Favorites')
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 ="""
        Verify that 'Portal for Context Menu Testing2' favorite has been removed
        """
        HomePage.Home.Favorites.verify_items(["V5 Context Menu Testing2"],'06.01',assert_type='asnotin')
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01,expected_image_verify=True)
        
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main() 