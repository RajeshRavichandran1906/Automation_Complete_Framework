"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 27 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930505_TestClass(BaseTestCase):
    
    def test_C9930505(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        HELP_MENU_ITEM="License"
        
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
            STEP 03.00 : Select License
        """
        HomePage.ContextMenu.select(HELP_MENU_ITEM)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify License dialogue comes up
        """
        HomePage.Home._core_utils.switch_to_new_window()
        
        page_title = self.driver.title
        HomePage.Home._utils.asequal(page_title, "Product End User License Agreement", "Step 03.01 : Verify Licence Page Title")
        
        page_url = self.driver.current_url
        
        HomePage.Home._utils.asin("docs.tibco.com/pub/ibi/webfocus/tibco-eula.pdf", page_url, "Step 03.02 : Verify Licence Page URL")
        
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()

        HomePage.Banner.sign_out()
        
