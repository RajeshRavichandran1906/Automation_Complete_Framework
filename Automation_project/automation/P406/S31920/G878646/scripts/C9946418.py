"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 09-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.login import LoginPage as Login
from common.wftools.paris_home_page import ParisHomePage

class C9946418_TestClass(BaseTestCase):
    
    def test_C9946418(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name    = HomePage.Home._core_utils.parseinitfile('mriddev')
        old_password = HomePage.Home._core_utils.parseinitfile('mrpassdev')
        new_password = "Pass1"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'User' icon in the Banner link.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the 'Change Password' option.
        """
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Enter a valid password in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that 'Cancel' and the 'Change Password' buttons get enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled("04.01")
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled("04.02")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that still 'Cancel' and the 'Change Password' buttons get enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled("05.01")
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled("05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password)
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=3)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that alert prompt message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
        
        
            
        STEP_07 = """
            STEP 07 : Clear 'Old Password', 'New Password' and 'Confirm New Password' entry boxes
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.clear()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)
        
        STEP_08 = """
            STEP 08 : Click on the 'Cancel' button to close the 'Change Password' dialog box
        """
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.ModalDailogs.ChangePassword.CancelButton.click()
        HomePage.ModalDailogs.ChangePassword.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + LoginPage._locators_.sign_in[1], 20)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Enter a valid 'User name' and the 'Password' as 'Pass1' > Click on 'Sign in' button
        """
        LoginPage.UserName.enter_text(user_name)
        LoginPage.Password.enter_text(new_password)
        LoginPage.SignInButton.click()
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=3)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 'Incorrect username or password' error message appears
        """
        LoginPage.ErrorMessage.verify_text("Incorrect username or password", "10.01")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Enter a valid 'User name' and a valid 'Password' i.e, 'admin' > Click on 'Sign in' button
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['WebFOCUS Home'], "11.01", "asin")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)