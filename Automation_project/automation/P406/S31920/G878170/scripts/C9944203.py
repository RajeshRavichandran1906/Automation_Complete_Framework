"""-------------------------------------------------------------------------------------------
Author Name  : Prabhakaran
Automated On : 24 July 2020
-----------------------------------------------------------------------------------------------"""

import keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944203_TestClass(BaseTestCase):
    
    def test_C9944203(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        
        STEP_01 = """
            STEP 01 : Log into Cloud or a machine where this feature is configured
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Invite button
        """
        HomePage.Banner.click_invite_user()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Leave the first name empty but enter something valid for the rest of the fields
        """
        HomePage.ModalDailogs.InviteUser.LastName.enter_text("IBI")
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text("prabham@amtexsystems.com")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click Invite button.
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that the invite button is disabled until you fix the issue
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.verify_disabled('04.01')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : ESC out and Click the Invite button
        """
        keyboard.press_and_release('esc')
        HomePage.ModalDailogs.InviteUser.wait_for_diappear()
        HomePage.Banner.click_invite_user()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Leave the last name empty but enter something valid for the rest of the fields
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text("WebFOCUS")
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text("prabham@amtexsystems.com")
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Click Invite button.
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify you get the same image as before and same error message
            Verify that the invite button is disabled until you fix the issue
        """
        HomePage.ModalDailogs.InviteUser.ErrorMessage.verify_text('Enter all required fields.', '07.01')
        HomePage.ModalDailogs.InviteUser.InviteButton.verify_disabled('07.02')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Click outside of the dialog
        """
        dialog = self.driver.find_element_by_css_selector(HomePage.ModalDailogs.InviteUser._locator_.base_css)
        HomePage.Home._core_utils.python_left_click(dialog, element_location='top_middle', yoffset=-12)
        HomePage.ModalDailogs.InviteUser.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : verify it closes it
        """
        HomePage.ModalDailogs.InviteUser.verify_closed('08.01')
        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Click Invite button.
        """
        HomePage.Banner.click_invite_user()
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)
        
        STEP_10 = """
            STEP 10 : Enter a valid first and last name
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text("WebFOCUS")
        HomePage.ModalDailogs.InviteUser.LastName.enter_text("IBI")
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_11 = """
            STEP 11 : Enter test@com for the email
        """
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text('test@com')
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_12 = """
            STEP 12 : Click Invite button.
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Verify that the invite button is disabled until you fix the issue
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.verify_disabled('12.01')
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01, True)
        
        STEP_13 = """
            STEP 13.00 : Close the dialog
        """
        HomePage.ModalDailogs.InviteUser.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)