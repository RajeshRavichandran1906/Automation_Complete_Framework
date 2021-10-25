"""-------------------------------------------------------------------------------------------
Author Name  : Prabhakaran
Automated On : 24 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930503_TestClass(BaseTestCase):
    
    def test_C9930503(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Auther user.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Help ribbon
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Select Community
        """
        HomePage.ContextMenu.select('Community')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the URL of community: https://ibi.influitive.com/users/sign_in
        """
        
        url = "https://ibi.influitive.com/users/sign_in"
        HomePage.Home._utils.asequal(url, self.driver.current_url, "Step 03.01 : Verify the URL of community: https://ibi.influitive.com/users/sign_in]")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Close 'Community' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Close 'Community' window
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)