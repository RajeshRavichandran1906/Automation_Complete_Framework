"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 24 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930506_TestClass(BaseTestCase):
    
    def test_C9930506(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        HELP_MENU_ITEM="TIBCO Software Inc."
        IBI_URL = "https://www.tibco.com/"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Help ribbon
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Select TIBCO Software Inc.
        """
        HomePage.ContextMenu.select(HELP_MENU_ITEM)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify Tibco Home web page comes up
        """
        HomePage.Home._core_utils.switch_to_new_window()
        ACTUAL_URL = self.driver.current_url
        
        HomePage.Home._utils.asequal(IBI_URL, ACTUAL_URL, "Step 03.01 : Verify Tibco page is opened")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.sign_out()
        
