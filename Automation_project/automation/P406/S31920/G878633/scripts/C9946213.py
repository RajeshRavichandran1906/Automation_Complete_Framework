"""----------------------------------------------------
Author Name  : Robert
Automated on : 08-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946213_TestClass(BaseTestCase):
    
    def test_C9946213(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context"
        EXPECTED_MENUS= ['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties']
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5 Context Menu Testing'
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the following context menu:
        """
        HomePage.ContextMenu.verify(EXPECTED_MENUS, "03.01")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        #HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)

        