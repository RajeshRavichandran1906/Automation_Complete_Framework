"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 17-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C9930090_TestClass(BaseTestCase):
    
    def test_C9930090(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Author
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on My Workspace button
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify My Workspace is empty
        """
        HomePage.MyWorkspace.verify_items([ ], "2.01")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click the <----Back to Home button
        """
        back_button=utils.validate_and_get_webdriver_object('div[title="Back to Home"]', "Back to Home button")
        core_utils.left_click(back_button)
        utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify user is taken back to main page after sign in
        """
        HomePage.Home.verify_sections(['GETTING STARTED', 'FAVORITES'], 03.01, assert_type='asin')
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

