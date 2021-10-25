"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 18-September-2020
-------------------------------------------------------------------------------------------"""
from common.wftools.login import LoginPage
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930649_TestClass(BaseTestCase):
    
    def test_C9930649(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Login = LoginPage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        analytic_url = "https://www.ibi.com/analytics-platform/"
        kb_link = "https://kb.informationbuilders.com/"
        
        STEP_01 = """
            STEP 01 : Open a browser session > Enter the URL for WF
            (Example: http://machine_name:port/alias/signin)
        """
        Login.invoke()
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Tour WebFOCUS' link
        """
        Login.click_tour_webfocus()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Should open in a new browser tab with the below URL:
            https://www.ibi.com/analytics-platform/
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(15, pause_time=5)
        HomePage.Home._utils.asequal(analytic_url, self.driver.current_url, "Step 02.01 : Verify https://www.ibi.com/analytics-platform/ opened in new window")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Close 'WebFOCUS BI and Analytics | Information Builders' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Visit the Knowledge Base' link
        """
        Login.click_visit_knowledge_base()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Should open in a new browser tab with the below URL:
            https://kb.informationbuilders.com/
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.asequal(kb_link, self.driver.current_url, "Step 04.01 : Verify https://kb.informationbuilders.com/ opened in new window")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Close 'WebFOCUS KnowledgeBase' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06_07 = """
            STEP 06 : Enter with suitable credentials
            STEP 07 : Click on Sign in button
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("06_07", STEP_06_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify 'WebFOCUS Homepage Paris' appears
        """
        HomePage.Banner.verify_top_bar_menus_title(['WebFOCUS Home', 'My Workspace', 'Shared with Me'], "07.01", "asin")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)