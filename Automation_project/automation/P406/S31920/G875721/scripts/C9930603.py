"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 12-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930603_TestClass(BaseTestCase):
    
    def test_C9930603(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = "Explore Sales Data"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click inside the Search dialogue
        """
        HomePage.Banner.Search.SearchBox.click()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the Search dialogue is highlighted with blue color
        """
        HomePage.Banner.Search.SearchBox.verify_border_color("malibu", "02.01")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Type 'Explore Sales Data'
        """
        HomePage.Banner.Search.SearchBox.enter_text(file_name)
        HomePage.Banner.Search.Results.wait_for_visible()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify it brings up the flyout serach result it displayed 'Explore Sales Data' Tag:Example
        """
        HomePage.Banner.Search.Results.verify(['Explore Sales Data Tag : Example Summary : Explore data interactively using the "Run with Insight" feature'], "03.01", include_tag=True)
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on the Search button
        """
        HomePage.Banner.Search.SearchButton.click()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify 'SEARCH RESULTS' window opens with the 'Explores Sales Data' item in list view
        """
        HomePage.SearchResuls.verify_list_view_displayed("04.01")
        HomePage.SearchResuls.verify_items([file_name], "04.02")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on back arrow to move on to Home view
        """
        HomePage.SearchResuls.click_left_arrow()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 'WebFOCUS Home' view dislpayed and still search bar is filled with 'Explore Sales Data'
        """
        HomePage.Home.verify_sections(["GETTING STARTED", "FAVORITES"], "05.01", "asin")
        HomePage.Banner.Search.SearchBox.verify_text(file_name, "05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click 'X' inside the search text box to clear search text
        """
        HomePage.Banner.Search.ClearButton.click()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that 'Search' text box gets cleared and it displayed 'Search' as a text by default
        """
        HomePage.Banner.Search.SearchBox.verify_placeholder("", "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)