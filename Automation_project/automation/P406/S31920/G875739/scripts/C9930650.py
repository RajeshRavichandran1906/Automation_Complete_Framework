"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 15-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import LoginPage as Login
from common.wftools.paris_home_page import ParisHomePage

class C9930650_TestClass(BaseTestCase):
    
    def test_C9930650(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        username = HomePage.Home._core_utils.parseinitfile('mriddev')
        password = HomePage.Home._core_utils.parseinitfile('mrpassdev')
        
        STEP_01 = """
            STEP 01 : Open a browser session > Enter the URL for WF
        """
        url = HomePage.Home._utils.get_setup_url().replace("8206", "")
        HomePage.Home._core_utils.update_current_working_area_browser_specification()
        self.driver.get(url)
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + LoginPage._locators_.user_name[1], 30)
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Enter a valid Username and invalid Password
        """
        LoginPage.UserName.enter_text(username)
        LoginPage.Password.enter_text(password + "test")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on Sign in button
        """
        LoginPage.SignInButton.click()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the following:
            1.Username and Password text box outline changes into red color
            2.'Incorrect username or password' error message appears
        """
        LoginPage.UserName.verify_border_color('crimson', '03.01')
        LoginPage.Password.verify_border_color('crimson', '03.02')
        LoginPage.ErrorMessage.verify_text('Incorrect username or password', '03.03')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Clear the Username and Password text box.
        """
        LoginPage.UserName.clear()
        LoginPage.Password.clear()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05 : Enter an invalid Username and a valid Password
        """
        LoginPage.UserName.enter_text(username + "test")
        LoginPage.Password.enter_text(password)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify that the outline changes to blue and the error message get disappear
        """
        LoginPage.UserName.verify_border_color('gray80', '05.01')
        LoginPage.Password.verify_border_color('dodger_blue', '05.02')
        LoginPage.ErrorMessage.verify_text('', '05.03')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 03 : Click on Sign in button
        """
        LoginPage.SignInButton.click()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify the following:
            1.Username and Password text box outline changes into red color
            2.'Incorrect username or password' error message appears
        """
        LoginPage.UserName.verify_border_color('crimson', '06.01')
        LoginPage.Password.verify_border_color('crimson', '06.02')
        LoginPage.ErrorMessage.verify_text('Incorrect username or password', '06.03')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Clear the Username and Password text box.
        """
        LoginPage.UserName.clear()
        LoginPage.Password.clear()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """
            STEP 08 : Enter a valid Username and Password
        """
        LoginPage.UserName.enter_text(username)
        LoginPage.Password.enter_text(password)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that the outline changes to blue and the error message get disappear
        """
        LoginPage.UserName.verify_border_color('gray80', '08.01')
        LoginPage.Password.verify_border_color('dodger_blue', '08.02')
        LoginPage.ErrorMessage.verify_text('', '08.03')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Click on Sign in button
        """
        LoginPage.SignInButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Home.Favorites.__locators__.favorites_section_css, "FAVORITES", 120)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['My Workspace'], '09.01', 'asin')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)