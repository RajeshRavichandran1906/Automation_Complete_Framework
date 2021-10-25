"""-------------------------------------------------------------------------------------------
Author Name  : Prabhakaran
Automated On : 22 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930501_TestClass(BaseTestCase):
    
    def test_C9930501(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        
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
            STEP 03 : Select WebFOCUS Online Help
        """
        HomePage.ContextMenu.select('WebFOCUS Online Help')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify WebFOCUS Online Help website is available
        """
        HomePage.Home._core_utils.switch_to_frame("#indexFrameset frame[name='HelpFrame']")
        HomePage.Home._core_utils.switch_to_frame("#helpFrameset frame[name='NavFrame']")
        HomePage.Home._core_utils.switch_to_frame("#navFrameset frame[name='ViewsFrame']")
        HomePage.Home._core_utils.switch_to_frame("iframe[name='toc']")
        HomePage.Home._core_utils.switch_to_frame("#viewFrameset frame[name='tocViewFrame']")
        actual_text = self.driver.find_element_by_css_selector("a[title*='Online Help']").text.strip()
        HomePage.Home._utils.asin("TIBCO WebFOCUS", actual_text, "Step 03.01 : Verify WebFOCUS Online Help website is available")
        HomePage.Home._utils.asin("Online Help", actual_text, "Step 03.01 : Verify WebFOCUS Online Help website is available")
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)