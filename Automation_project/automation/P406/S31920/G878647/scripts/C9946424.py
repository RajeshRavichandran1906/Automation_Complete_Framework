"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 16-September-2020
-------------------------------------------------------------------------------------------"""

from common.wftools.login import LoginPage
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946424_TestClass(BaseTestCase):
    
    def test_C9946424(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Login = LoginPage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        user_name = HomePage.Home._core_utils.parseinitfile("mridadv")
        old_password = HomePage.Home._core_utils.parseinitfile("mrpassadv")
        new_password = "Pass1"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
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
            STEP 04 : Enter a valid password in the 'Old Password' entry box i.e, 'Pass'
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
            STEP 05 - Expected : Verify that 'Cancel' and the 'Change Password' buttons get enabled
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
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text("Your password has been changed", "07.01")
        HomePage.Home._core_utils.update_config_file("mrpassadv", new_password)
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + Login._locators_.user_name[1], 45)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Enter a valid 'User name' as 'autoadvuser60' and 'Password' as 'admin' > Click on 'Sign in' button
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
            STEP 11 : Enter a valid 'User name' and a newly changed Password ie., 'Pass1'
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['WebFOCUS Home', 'My Workspace'], "11.01", "asin")
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
            STEP 14 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that alert prompt message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("15.01")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click on 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify the following:
            1.'The passwords you entered do not match' error message appears with the red background-color
            2.'Old Password' text box is in grey border-color
            3.'New Password' and 'Confirm New Password' text boxes highlighted in red border-color
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered do not match.', '16.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '16.02')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('gray80', "16.03")
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('crimson', '16.04')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('crimson', '16.05')
        HomePage.Home._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Clear 'Old Password', 'New Password' and 'Confirm New Password' entry boxes
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.UserName.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Enter 'Pass1' in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(old_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # To disable Firefox browser tooltip.
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text("Your password has been changed", "20.01")
        HomePage.Home._core_utils.update_config_file("mrpassadv", old_password)
        HomePage.Home._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("22", STEP_22)

        STEP_23 = """
            STEP 23 : Enter a valid 'User name' and a newly changed Password ie., 'Pass'
        """
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + Login._locators_.user_name[1], 45)
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("23", STEP_23)

        STEP_23_EXPECTED = """
            STEP 23 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['WebFOCUS Home', 'My Workspace'], "23.01", "asin")
        HomePage.Home._utils.capture_screenshot("23 - Expected", STEP_23_EXPECTED, True)

        STEP_24 = """
            STEP 24 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("24", STEP_24)