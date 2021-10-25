"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 10-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946221_TestClass(BaseTestCase):
    
    def test_C9946221(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context"
        PORTAL_BANNER_CSS = ".pvd-portal-banner"
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5 Context Menu Testing' > Select 'Run'
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that 'V5 Context Menu Testing' runs in a new tab
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(PORTAL_BANNER_CSS, PORTAL_NAME, 120)
        actual_title = self.driver.title
        msg = "Step 03.01 : Verify that 'V5 Context Menu Testing' runs in a new tab"
        HomePage.Home._utils.asequal(PORTAL_NAME, actual_title, msg)
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04.00 : Close the 'V5 Context Menu Testing' run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)

        STEP_05 = """
            STEP 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
