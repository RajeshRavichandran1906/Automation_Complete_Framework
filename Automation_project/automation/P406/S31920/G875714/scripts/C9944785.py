"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 26 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944785_TestClass(BaseTestCase):
    
    def test_C9944785(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login('mridadv','mrpassadv')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on the 'User' icon in the Banner link.
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on the 'Change Password' option.
        """
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the 'Change Password' dialog box opens with the following:
            1.User name text box should be readable only
            2.Cursor is in the Old Password text box and the border is highlighted in blue color
            3.'New Password' and 'Confirm New Password' entry boxes should be empty with a default border-color
            4.By default, cancel button is enabled and Change Password button gets disabled
            5.X button should within the margin.
        """
        HomePage.ModalDailogs.ChangePassword.UserName.verify_read_only('03.01')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('malibu', '03.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_text('', '03.03')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('gray80', '03.04')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_text('', '03.05')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('gray80', '03.06')
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('03.07')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_disabled('03.08')
        HomePage.ModalDailogs.ChangePassword.verify_close_icon_displayed('03.09')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Click on the X button
        """
        HomePage.ModalDailogs.ChangePassword.close()
        HomePage.ModalDailogs.ChangePassword.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify the 'Change Password' dialog box gets closed
        """
        HomePage.ModalDailogs.ChangePassword.verify_closed('04.01')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click on the 'User' icon in the Banner link > Click on the 'Change Password' option.
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on the Cancel button
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.click()
        HomePage.ModalDailogs.ChangePassword.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify the 'Change Password' dialog box gets closed
        """
        HomePage.ModalDailogs.ChangePassword.verify_closed('06.01')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)