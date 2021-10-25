"""-------------------------------------------------------------------------------------------
Author Name  : Prabhakaran
Automated On : 23 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930502_TestClass(BaseTestCase):
    
    def test_C9930502(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        CSS = ".m-feature-title" 
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Auther user.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Help ribbon
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Select Technical Resources
        """
        HomePage.ContextMenu.select('Technical Resources')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(CSS, 'WebFOCUS', 80)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify Technical Resources website comes up
        """
        actual_text = self.driver.find_element_by_css_selector(CSS).text.strip()
        HomePage.Home._utils.asin("KnowledgeBase", actual_text, "Step 03.01 : Verify Technical Resources website comes ups")
        HomePage.Home._utils.asin("TIBCO WebFOCUS", actual_text, "Step 03.01 : Verify Technical Resources website comes ups")
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)