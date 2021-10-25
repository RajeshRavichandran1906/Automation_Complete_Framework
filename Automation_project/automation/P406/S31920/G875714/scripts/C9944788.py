"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 30 Mach 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.login import LoginPage as Login
from common.wftools.paris_home_page import ParisHomePage

class C9944788_TestClass(BaseTestCase):
    
    def test_C9944788(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage  = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        user_name    = HomePage.Home._core_utils.parseinitfile('mridadv')
        old_password = HomePage.Home._core_utils.parseinitfile('mrpassadv')
        new_password = 'Pass1'
         
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
              
        STEP_04 = """
            STEP 04 : Enter a valid password in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        HomePage
        STEP_04_01 = """
            STEP 04.01 : Verify the 'Cancel' button gets enabled and the 'Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('04.01')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('04.02')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click on 'New Password' entry box > Enter 'New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify still the 'Cancel' button gets enabled and the 'Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.CancelButton.verify_enabled('05.01')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('05.02')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify the following:
            1.'The passwords you entered match.' message appears with the green background-color
            2.'New Password' and 'Confirm New Password' text boxes highlighted in green border-color
            3.Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered match.', '06.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('green', '06.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('green', '06.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('green', '06.03')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('06.04')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '07.01')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + LoginPage._locators_.sign_in[1], 20)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_09 = """
            STEP 09 : Enter a valid 'User name' and 'Password' as 'adv' > Click on 'Sign in' button
        """
        LoginPage.UserName.enter_text(user_name)
        LoginPage.Password.enter_text(old_password)
        LoginPage.SignInButton.click()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify 'Incorrect username or password' error message appears
        """
        LoginPage.ErrorMessage.verify_text('Incorrect username or password', '09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Clear the 'User name' and 'Password' entry boxes    
        """
        LoginPage.UserName.clear()
        LoginPage.Password.clear()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_11 = """
            STEP 11 : Enter a valid 'User name' and 'Password' as 'Pass1'
        """
        LoginPage.UserName.enter_text(user_name)
        LoginPage.Password.enter_text(new_password)
        LoginPage.SignInButton.click()
        HomePage.Home._utils.wait_for_page_loads(120, pause_time=3)
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Banner.locators.user[1], 30)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['User'], '11.01', assert_type='asin')
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Click on the 'User' icon in the Banner link > Click on the 'Change Password' option.
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_13 = """
            STEP 13 : Enter 'Pass1' in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_14 = """
            STEP 14 : Click on 'New Password' entry box > Enter 'New Password' as 'adv'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_15 = """
            STEP 15 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'Pass1'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)
        
        STEP_15_01 = """
            STEP 15.01 : Verify the following:
            1.'The passwords you entered do not match.' error message appears with the red background-color
            2.'New Password' and 'Confirm New Password' text boxes highlighted in red border-color
            3.Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered do not match.', '15.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '15.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('crimson', '15.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('crimson', '15.03')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('15.04')
        HomePage.Home._utils.capture_screenshot('15.01', STEP_15_01, True)
        
        STEP_16 = """
            STEP 16 : Clear 'Old Password', 'New Password' and 'Confirm New Password' entry boxes
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.clear()
        HomePage.ModalDailogs.ChangePassword.NewPassword.clear()
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.clear()
        HomePage.Home._utils.capture_screenshot('16.00', STEP_16)
        
        STEP_17 = """
            STEP 17 : Enter 'Pass1' in the 'Old Password' entry box
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(new_password)
        HomePage.Home._utils.capture_screenshot('17.00', STEP_17)
         
        STEP_18 = """
            STEP 18 : Click on 'New Password' entry box > Enter 'New Password' as 'adv'
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(old_password)
        HomePage.Home._utils.capture_screenshot('18.00', STEP_18)
        
        STEP_19 = """
            STEP 19 : Click on 'Confirm New Password' entry box > Enter 'Confirm New Password' as 'adv'
        """
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(old_password)
        HomePage.ModalDailogs.ChangePassword.UserName.click() # Click again on UserName text to dismiss Firefox tooltip
        HomePage.Home._utils.capture_screenshot('19.00', STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify the following:
            1.'The passwords you entered match.' message appears with the green background-color
            2.'New Password' and 'Confirm New Password' text boxes highlighted in green border-color
            3.Change Password' button gets enabled
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered match.', '19.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('green', '19.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('green', '19.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('green', '19.03')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.verify_enabled('19.04')
        HomePage.Home._utils.capture_screenshot('19.01', STEP_19_01, True)
        
        STEP_20 = """
            STEP 20 : Click on the 'Change Password' button
        """
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.Home._utils.capture_screenshot('20.00', STEP_20)
        
        STEP_20_01 = """
            STEP 20.01 : Verify 'Your password has been changed' prompt appears
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '20.01')
        HomePage.Home._utils.capture_screenshot('20.01', STEP_20_01, True)
        
        STEP_21 = """
            STEP 21 : Click on the 'User' icon in the Banner link > Click on the 'Change Password' option.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('21.00', STEP_21)