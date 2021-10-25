"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 23 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930504_TestClass(BaseTestCase):
    
    def test_C9930504(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        HELP_MENU_ITEM="About WebFOCUS"
        HELP_ABOUT_LABEL_CSS=".help-about-text-field .ibx-label-text"
        HELP_ABOUT_TITLE_CSS = ".ibx-dialog-title-box .ibx-title-bar-caption .ibx-label-text"
        HELP_ABOUT_OKBTN_CSS = ".about-webfocus .ibx-dialog-ok-button"
        EXPECTED_LABEL = ['Edition', 'Product release', 'Service pack', 'Package name', 'Release ID', 'Build/GEN number', 'Build/GEN date', 'Application Server']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Help ribbon
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Select About WebFOCUS
        """
        HomePage.ContextMenu.select(HELP_MENU_ITEM)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify About WebFOCUS window comes up and everything is displayed correctly
        """
        LABEL_ELEMS=HomePage.Home._utils.validate_and_get_webdriver_objects(HELP_ABOUT_LABEL_CSS, 'HELP_ABOUT_LABEL_CSS')
        LABEL_LIST = [label_item.text for label_item in LABEL_ELEMS]
        HomePage.Home._utils.as_List_equal(EXPECTED_LABEL, LABEL_LIST, "Step 03.01 : Verify labels in the about window")
        
        ACTUAL_TITLE_ELEM = HomePage.Home._utils.validate_and_get_webdriver_object(HELP_ABOUT_TITLE_CSS, 'HELP_ABOUT_TITLE_CSS')
        ACTUAL_TITLE_TEXT = ACTUAL_TITLE_ELEM.text
        
        HomePage.Home._utils.asequal(ACTUAL_TITLE_TEXT, HELP_MENU_ITEM, "Step 03.02 : Verify About WebFOCUS title")
        
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        OK_BTN_ELEM = HomePage.Home._utils.validate_and_get_webdriver_object(HELP_ABOUT_OKBTN_CSS, 'HELP_ABOUT_OKBTN_CSS')
        OK_BTN_ELEM.click()
                
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.sign_out()
        
