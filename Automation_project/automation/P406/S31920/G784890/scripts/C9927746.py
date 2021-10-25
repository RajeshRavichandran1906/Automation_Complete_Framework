"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 09-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927746_TestClass(BaseTestCase):
    
    def test_C9927746(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASe VARIABLES
        """
        user_options = ['Preferences', 'Change Password', 'Sign Out', 'New Start Page', 'Legacy Home Page']
        user_name_css = "#SignonUserName"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : In the banner link Hover over the Username.
        """
        user = self.driver.find_element(*HomePage.Banner.locators.user)
        HomePage.Home._core_utils.python_move_to_element(user)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify it shows 'User' in Tooltip.
        """
        HomePage.Home._utils.asequal("User", user.get_attribute("title"), "Step 02.01 : Verify it shows 'User' in Tooltip.")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on the 'Username'.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify the Following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "03.01")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click 'Sign out' and Sign into WebFOCUS Home Page as Devceloper User.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_name_css, 30)
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on the 'Username'.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the Following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click 'Sign out' and Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_name_css, 30)
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on the 'Username'.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the Following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click 'Sign out' and Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_name_css, 30)
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on the 'Username'.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the Following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click 'Sign out'.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)