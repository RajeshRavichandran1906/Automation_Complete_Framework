"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 03 August 2020
-----------------------------------------------------------------------------------------------"""

from common.wftools.login import LoginPage
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929921_TestClass(BaseTestCase):
    
    def test_C9929921(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Login = LoginPage(self.driver)
        
        """
        TESTCASE VAIABLES
        """
        user = HomePage.Home._core_utils.parseinitfile('mridauth')
        password = "password"
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Author user
        """
        HomePage.invoke_with_login('mridauth','mrpassauth')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'User' from the banner link
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify the following options:
            1. Preferences
            2. Change Password
            3. Sign Out
        """
        HomePage.ContextMenu.verify(['Preferences', 'Change Password', 'Sign Out'], '02.01')
        HomePage.Home._utils.capture_screenshot('02.01', STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Click on 'Change Password'
        """
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the 'Change Password' dialog box opens with the following:
            1.User name text box should be readable only
            2.'Old Password', 'New Password' and 'Confirm New Password' entry boxes should be empty with a default border-color
            3.By default, cancel button is enabled
            4.X button should within the margin.
        """
        HomePage.ModalDailogs.ChangePassword.UserName.verify_read_only('03.01')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_text('', '03.02')
        HomePage.ModalDailogs.ChangePassword.OldPassword.verify_border_color('gray80', '03.03')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_text('', '03.04')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('gray80', '03.05')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_text('', '03.06')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('gray80', '03.07')
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('03.08')
        HomePage.ModalDailogs.ChangePassword.verify_close_icon_displayed('03.09')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Enter the following:
            Old Password: (leave it as empty)
            New Password: password
            Confirm New Password: password
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(password)
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(password)
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05 : Click Change Password
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '05.01')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06_07 = """
            STEP 06 : Click on 'User' from the banner link
            STEP 07 : Click 'Sign Out'
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + Login._locators_.user_name[1], 20)
        HomePage.Home._utils.capture_screenshot('06_07', STEP_06_07)
        
        STEP_08 = """
            STEP 08 : From the Sign In Page, enter the valid username and new password
        """
        Login.UserName.enter_text(user)
        Login.Password.enter_text(password)
        Login.SignInButton.click()
        HomePage.Home._utils.wait_for_page_loads(60)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Banner.locators.top_banner_css, "Workspace", 120)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify user able to log in with the new password
        """
        HomePage.Banner.verify_top_bar_menus_title(['My Workspace', 'Shared with Me'], '08.01', 'asin')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Click on 'User' from the banner link > Click on 'Change Password'
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_10 = """
            STEP 10 : Enter the following:
            Old Password: password
            New Password: (leave it as empty)
            Confirm New Password: (leave it as empty)
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(password)
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_11 = """
            STEP 11 : Click Change Password
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '11.01')
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)