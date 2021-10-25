# coding: latin-1
"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 07 Aug 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.login import Login

class C9946032_TestClass(BaseTestCase):
    
    def test_C9946032(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage  = ParisHomePage(self.driver)
        LoginPage = Login(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        LANG_LIST = ['English', 'Deutsch', 'English - Australian', 'English - Canadian', 'English - United Kingdom', 'Español', 'Français - Canada', 'Français - France']
         
        STEP_01 = """
            STEP 01 : Access WebFOCUS Cloud Trial Environment
        """
        
        environment_url=LoginPage.create_setup_url().replace("home8206", "")
        self.driver.get(environment_url)
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=1)
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : On the Sign in Page, Click on the language Dropdown list
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object(".language-div .dm-caret-down", "LANGUAGE_DROPDOWN")
        webelem.click()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify the following languages are listed.
                (English, Deutsch, English-AU, English-Canadian, English-United Kingdom, Espanol, French-Canada, French-France)
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_objects("ul.show-menu li[role='menuitem']", "LANGUAGE_LIST")
        ACTUAL_LIST = [i.text.strip() for i in webelem]
        HomePage.Home._utils.as_List_equal(LANG_LIST,ACTUAL_LIST,"Step 02.01 : Verify the Language list in the dropdown")
        HomePage.Home._utils.capture_screenshot('02.01', STEP_02_01, True)
        self.driver.close()
