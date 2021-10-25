"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 23 June 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.login import LoginPage as Login
from common.wftools.paris_home_page import ParisHomePage

class C9946031_TestClass(BaseTestCase):
    
    def test_C9946031(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage  = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        USER_NAME    = HomePage.Home._core_utils.parseinitfile('mrid')
        OLD_PASSWORD = HomePage.Home._core_utils.parseinitfile('mrpass')
        WRONG_OLD_PASSWORD = "wrong"
        NEW_PASSWORD1 = 'test'
        NEW_PASSWORD2 = "#1QAibiibi"
         
        STEP_01 = """
            STEP 01 : Sign in to Cloud Trial Environment
        """
        HomePage.invoke_with_login('mrid','mrpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on your User name
        """
        HomePage.Banner.click_user()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify drop down menu list
        """
        HomePage.ContextMenu.verify(['Preferences', 'Change Password', 'Sign Out'], "02.01")
        HomePage.Home._utils.capture_screenshot('02.01', STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Click on "Change Password"
        """
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify Change Password Dialog is invoked
        """
        HomePage.ModalDailogs.ChangePassword.verify_title("Change Password", "03.01")
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Type in "incorrect" Old Password
            New Password -> test
            Confirm New Password -> test
            Click on Change Password
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(WRONG_OLD_PASSWORD)
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(NEW_PASSWORD1)
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(NEW_PASSWORD1)
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify "Incorrect username or password" msg
        """
        
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text("Incorrect username or password", "04.01")
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color("persian_red4", "04.02")
        '''QA-4794 Clarifiction ticket has been opened'''
        '''Need to update the color to gray80'''
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('gray80', '04.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('gray80', '04.04')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Type in "correct" Old Password
            Old Password -> ibiibi#1QA
            New Password -> #1QAibiibi
            Confirm New Password->test
            Type in
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(OLD_PASSWORD)
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(NEW_PASSWORD2)
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(NEW_PASSWORD1)
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify "The passwords you entered do not match"
            Verify New Password and Confirm New Passwords input areas are highlighted
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered do not match.', '05.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '05.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('crimson', '05.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('crimson', '05.04')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 06.00 : Type in new Password.
            For example,
            Old Password -> ibiibi#1QA
            New Password -> #1QAibiibi
            Confirm New Password -> #1QAibiibi
            Click on "Change Password
        """
        HomePage.ModalDailogs.ChangePassword.OldPassword.enter_text(OLD_PASSWORD)
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text(NEW_PASSWORD2)
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text(NEW_PASSWORD2)
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.click()
        HomePage.Home._core_utils.update_config_file('mrpass', NEW_PASSWORD2)
        
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify change password dialog closes and 'Your password has been changed popup displayed.
        """
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_text('The passwords you entered do not match.', '06.01')
        HomePage.ModalDailogs.ChangePassword.ErrorMessage.verify_background_color('persian_red4', '06.02')
        HomePage.ModalDailogs.ChangePassword.NewPassword.verify_border_color('crimson', '06.03')
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.verify_border_color('crimson', '06.04')
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        
        STEP_07 = """
            STEP 07.00 : Click on User Name -> Click on "Sign Out""
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + LoginPage._locators_.sign_in[1], 20)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)

        STEP_07_01 = """
            STEP 07.01 : Verify user is directed to Sign In Page
        """
        HomePage.Home._utils.verify_object_visible("#" + LoginPage._locators_.sign_in[1], True, "Step 07.01 : Verify Signin page is displayed")
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Enter Username and new Password on Sign in Page
            ->ibiwfqa001@gmail.com
            ->#1QAibiibi
        """
        HomePage.invoke_with_login('mrid','mrpass')
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08_01 : Verify user logs in successfully
        """
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Banner.locators.user[1], 30)
        HomePage.Banner.verify_top_bar_menus_title(['User'], '08.01', assert_type='asin')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Sign out -> Close Browser
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)