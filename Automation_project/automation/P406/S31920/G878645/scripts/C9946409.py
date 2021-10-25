"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 14-September-2020
-------------------------------------------------------------------------------------------"""

from common.wftools.login import LoginPage
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946409_TestClass(BaseTestCase):
    
    def test_C9946409(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Login = LoginPage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mridadm")
        old_password = HomePage.Home._core_utils.parseinitfile("mrpassadm")
        new_password = "Pass1"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'User' icon in the Banner link.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on the 'Change Password' option.
        """
        HomePage.ContextMenu.select("Change Password")
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
        HomePage.ModalDailogs.ChangePassword.UserName.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that alert prompt message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._core_utils.update_config_file("mrpassadm", new_password)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.NotifyPopup.verify_text("Your password has been changed", "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + Login._locators_.user_name[1], 45)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Enter a 'User name' and an 'Old Password' > Click on 'Sign in' button
        """
        Login.UserName.enter_text(user_name)
        Login.Password.enter_text(old_password)
        Login.SignInButton.click()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 'Incorrect username or password' error message appears
        """
        Login.ErrorMessage.verify_text("Incorrect username or password", "09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Clear the 'User name' and 'Password' entry boxes
        """
        Login.UserName.clear()
        Login.Password.clear()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Enter a 'User name' and a newly changed Password ie., 'Pass1'
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(["WebFOCUS Home", "Settings"], "11.01", "asin")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on the 'User' icon in the Banner link > Click on the 'Change Password' option.
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select("Change Password")
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Enter 'Pass1' in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click on 'New Password' entry box > Enter 'New Password' as 'admin'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that alert prompt message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("15.01")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Clear 'Old Password', 'New Password' and 'Confirm New Password' entry boxes
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Enter 'Pass1' in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Click on 'New Password' entry box > Enter 'New Password' as 'admin'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'admin'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(old_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._core_utils.update_config_file("mrpassadm", old_password)
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.NotifyPopup.verify_text("Your password has been changed", "20.01")
        HomePage.Home._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + Login._locators_.user_name[1], 60)
        HomePage.Home._utils.capture_screenshot("21", STEP_21)

        STEP_22 = """
            STEP 22 : Enter a valid 'User name' and a newly changed Password ie., 'admin'
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(["WebFOCUS Home", "Settings"], "22.01", "asin")
        HomePage.Home._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("23", STEP_23)