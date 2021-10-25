"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 17-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color
from common.wftools.login import LoginPage as Login
from common.wftools.paris_home_page import ParisHomePage

class C9944753_TestClass(BaseTestCase):
    
    def test_C9944753(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        STEP_01 = """
            STEP 01 : Open a browser session > Enter the URL for WF
        """
        url = HomePage.Home._utils.get_setup_url().replace("8206", "")
        HomePage.Home._core_utils.update_current_working_area_browser_specification()
        self.driver.get(url)
        HomePage.Home._utils.synchronize_until_element_is_visible("#" + LoginPage._locators_.user_name[1], 30)
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify Sign in screen displayed as same below:
            1.Information Builders/WebFOCUS logo should be aligned at center
            2.'Sign in' label should be in white color with radial-gradient color (blue and purple)
            3.Username and Password text should be in purple color
            4.Username and Password should be mandatory represents by the symbol * in red color
            5.Username and Password text-box should be empty by default
            6.'Tour WebFOCUS' and 'Visit the Knowledge Base' should be as a link and it is in royal blue color
            7.Sign in button is at the right bottom corner of the login screen
            8."Copyright 2019 Information Builders. All rights reserved." text should at the bottom of the login screen with center alignment
        """
        left_value = int(float(self.driver.find_element_by_css_selector(".dm-login-wrap").value_of_css_property('left')[:-2]))
        center_value = self.driver.execute_script('return window.innerWidth')//2
        align_status = left_value in range((center_value-20), (center_value+10))
        HomePage.Home._utils.asequal(True, align_status, "Step 01.01 : Verify Information Builders/WebFOCUS logo should be aligned at center")
        
        bg_color = Color.from_string(LoginPage.SignInButton._object_.value_of_css_property('background-color')).rgba
        font_color = Color.from_string(LoginPage.SignInButton._object_.value_of_css_property('color')).rgba
        btn_color_status = all([bg_color=='rgba(52, 85, 219, 1)', font_color=='rgba(255, 255, 255, 1)'])
        HomePage.Home._utils.asequal(True, btn_color_status, "Step 01.02 : Verify 'Sign in' label should be in white color with radial-gradient color (blue and purple)")
        
        labels_obj = list(map(self.driver.find_element_by_css_selector, (".dm-username", ".dm-password")))
        labels = [label.text.strip() for label in labels_obj]
        HomePage.Home._utils.asequal(['Username*', 'Password*'], labels, "Step 01.03 : Verify Username and Password text")
        
        labels_color = []
        start_color = []
        for obj in labels_obj:
            label = obj.find_element_by_css_selector(".dm-label-name")
            star = obj.find_element_by_css_selector(".dm-star")
            labels_color.append(Color.from_string(label.value_of_css_property('color')).rgba)
            start_color.append(Color.from_string(star.value_of_css_property('color')).rgba)
        HomePage.Home._utils.asequal(['rgba(83, 12, 98, 1)', 'rgba(83, 12, 98, 1)'], labels_color, "Step 01.04 : Verify Username and Password text should be in purple color")
        HomePage.Home._utils.asequal(['rgba(191, 0, 0, 1)', 'rgba(191, 0, 0, 1)'], start_color, "Step 01.05 : Verify Username and Password should be mandatory represents by the symbol * in red color")
        
        LoginPage.UserName.verify_text('', '01.06')
        LoginPage.Password.verify_text('', '01.07')
        
        about_text = []
        about_color = []
        for about in self.driver.find_elements_by_css_selector(".dm-bottom-left div[class*='about']"):
            about_text.append(about.text.strip())
            about_color.append(Color.from_string(about.value_of_css_property('color')).rgba)
        HomePage.Home._utils.asequal(['Tour WebFOCUS', 'Visit the Knowledge Base'], about_text, "Step 01.08 : Verify 'Tour WebFOCUS' and 'Visit the Knowledge Base' should be as a link text")
        HomePage.Home._utils.asequal(['rgba(52, 85, 219, 1)', 'rgba(52, 85, 219, 1)'], about_color, "Step 01.09 : Verify 'Tour WebFOCUS' and 'Visit the Knowledge Base' should be as a link in royal blue color")
        
        container = self.driver.find_element_by_css_selector(".dm-body")
        btn_align = ((container.size['width']//2) + container.location['x']) < LoginPage.SignInButton._object_.location['x']
        HomePage.Home._utils.asequal(True, btn_align, "Step 01.10 : Verify Sign in button is at the right bottom corner of the login screen")
        
        copy_right = self.driver.find_element_by_css_selector(".dm-copyright")
        container_y = int(container.location['y']  + container.size['height'])
        copy_right_align = int(copy_right.location['y']) in range((container_y-35), container_y)
        HomePage.Home._utils.asequal(True, copy_right_align, "Step 01.11 : Verify Copyright 2019 Information Builders. All rights reserved text should at the bottom of the login screen with center alignment")
        HomePage.Home._utils.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02 : Click on 'Username' text box
        """
        LoginPage.UserName.click()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify 'Username' text box gets highlighted in blue color and 'Password' text box is not highlighted
        """
        LoginPage.UserName.verify_border_color('dodger_blue', '02.01')
        LoginPage.Password.verify_border_color('gray80', '02.02')
        HomePage.Home._utils.capture_screenshot('02.01', STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Click on 'Password' text box
        """
        LoginPage.Password.click()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify 'Password' text box gets highlighted in blue color and 'Username' text box is not highlighted
        """
        LoginPage.UserName.verify_border_color('gray80', '03.01')
        LoginPage.Password.verify_border_color('dodger_blue', '03.02')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Enter suitable credentials
        """
        LoginPage.UserName.enter_text("admin")
        LoginPage.Password.enter_text("admin")
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify text inside 'Username' is in blue color and 'Password' is in blue with encrypted format    
        """
        input_color = []
        for inpu_obj in [LoginPage.UserName._object, LoginPage.Password._object]:
            input_color.append(Color.from_string(inpu_obj.value_of_css_property('color')).rgba)
        HomePage.Home._utils.asequal(['rgba(52, 85, 219, 1)', 'rgba(52, 85, 219, 1)'], input_color, "Step 04.01 : Verify text inside 'Username' is in blue color and 'Password' is in blue")
        input_type = LoginPage.Password._object.get_attribute('type')
        HomePage.Home._utils.asequal('password', input_type, "Step 04.02 : Verify password input in encrypted format")
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click on empty space in the login screen
        """
        HomePage.Home._core_utils.python_click_with_offset(100, 300) #fixed
#         HomePage.Home._core_utils.python_left_click(container, 'top_middle')
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify both 'Username' and 'Password' text box are not gets highlighted
        """
        LoginPage.UserName.verify_border_color('gray80', '05.01')
        LoginPage.Password.verify_border_color('gray80', '05.02')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)