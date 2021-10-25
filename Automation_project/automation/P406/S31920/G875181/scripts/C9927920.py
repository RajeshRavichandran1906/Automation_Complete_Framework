"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 16 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927920_TestClass(BaseTestCase):
    
    def test_C9927920(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)

        """
        TESTCASE VARIABLES
        """
        CONTEXT_MENUS = ['Expand', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        CUSTOMIZATION_MENU = ['Remove my customizations', 'Remove customizations for all users']
        SECURITY_MENU = ['Rules on this resource...', 'Effective policy...', 'Owner...']
    
        
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Right-click on 'V5 Context Menu Testing' from the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875179->V5 Context Menu Testing")
        utils.capture_screenshot("04.00", STEP_04)

        STEP_04_01 = """Verification - Verify the following context menu:
        """
        HomePage.ContextMenu.verify(CONTEXT_MENUS,'Step 04.01')
        utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        """
            Step 05 : Hover over Customization menu
        """
        STEP_05_01 = """
        Step 05.00 Verify the following context menu:
        """
        HomePage.ContextMenu.verify(CUSTOMIZATION_MENU,'Step 05.01',menu_path='Customizations')
        utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
    
        """
        Hover over Security Menu
        """
        STEP_06_01 ="""Verify the following context menu:
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875179->V5 Context Menu Testing")
        HomePage.ContextMenu.verify(SECURITY_MENU,'Step 06.01',menu_path='Security')
        utils.capture_screenshot('06.01', STEP_06_01, expected_image_verify=True)
        HomePage.Workspaces.switch_to_default_content()
        
        STEP_07 = """
            Step 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main()  