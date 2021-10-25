"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 03-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946408_TestClass(BaseTestCase):
    
    def test_C9946408(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        old_password = HomePage.Home._core_utils.parseinitfile('mrpassadm')
        new_password = 'Pass1'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mridadm','mrpassadm')
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
            STEP 04 - Expected : Verify the 'Cancel' button gets enabled and the 'Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('04.01')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('04.02')
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify still the 'Cancel' button gets enabled and the 'Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('05.01')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('05.02')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'admin'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(old_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that alert prompt error message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following:
            1. 'The passwords you entered do not match' error message appears with the red background-color
            2. 'Old Password' text box is in grey border-color
            3. 'New Password' and 'Confirm New Password' text boxes highlighted in red border-color
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered do not match.', '07.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '07.02')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('gray80', "07.03")
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('crimson', '07.04')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('crimson', '07.05')
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Clear 'Old Password', 'New Password' and 'Confirm New Password' entry boxes
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.clear()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Enter an invalid password in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(old_password*2, False)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(new_password, False)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password, False)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the following:
            1. 'Incorrect username or password' error message appears with the red background-color
            2. 'Old Password'text box gets highlighted in red border-color
            3. 'New Password' and 'Confirm New Password' text boxes in grey border-color
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('Incorrect username or password', '12.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '12.02')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('crimson', "12.03")
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('gray80', '12.04')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('gray80', '12.05')
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the 'Cancel' button to close the 'Change Password' dialog
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.click()
        HomePage.ModalDailogs.ChangePassword.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)