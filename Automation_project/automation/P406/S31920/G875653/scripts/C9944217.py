"""-------------------------------------------------------------------------------------------
Author Name : Vpriya
Automated On : 6th December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944217_TestClass(BaseTestCase):
    
    def test_C9944217(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        expected_portal_menus = ['Run', 'Delete DEL', 'Add to Favorites', 'Properties']
        expected_page_menus =['Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mradvid", "mradvpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Right click on V4-Collaborative portal V4PortalContext.
        """
        HomePage.MyWorkspace.right_click_on_item("V4_Portal_Context")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Verify context menu,
            Run.
            Delete DEL.
            Add to Favorites.
            Properties.
            """
        
        HomePage.ContextMenu.verify(expected_portal_menus, "03.01")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Right click on portal page Page_Context.
        """
        HomePage.MyWorkspace.right_click_on_item("Page_Context")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify context menu,
            Duplicate.
            Delete DEL.
            Share
            Share with...
            Properties.
        """
        HomePage.ContextMenu.verify(expected_page_menus, "04.01")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05= """
            Step 05.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)

if __name__ == "__main__":
    unittest.main()