"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 03-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946411_TestClass(BaseTestCase):
    
    def test_C9946411(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        old_password = HomePage.Home._core_utils.parseinitfile('mrpassadm')
        
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
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Enter a valid password in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on 'New Password' entry box > Enter 'New Password' as 'admin' (valid password)
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'admin' (valid password)
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that alert prompt message does not appears
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_not_displayed("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following:
            1. 'New password does not meet password policy' message appears with the red background-color
            2. 'Old Password', 'New Password' and 'Confirm New Password' text boxes are in gery border-color
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('New password does not meet password policy', '07.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '07.02')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('gray80', "07.03")
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('gray80', '07.04')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('gray80', '07.05')
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on the 'Cancel' button to close the 'Change Password' dialog
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)