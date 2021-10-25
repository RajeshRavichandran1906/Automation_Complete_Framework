"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 03-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9945006_TestClass(BaseTestCase):
    
    def test_C9945006(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        choose_col_css = "div[title^='Choose']"
        default_sort_css = "div.content-title-btn-name:not([style*='none'])"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as a Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Retail_Samples' from the repository tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click the toggle button to switch to List view
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on the Choose Columns button
        """
        choose_columns = HomePage.Home._utils.validate_and_get_webdriver_object(choose_col_css, "Home page grid view default sort")
        HomePage.Home._core_utils.left_click(choose_columns)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)
        
        STEP_05 = """
            STEP 05 : Click Tags in the drop-down list
        """
        HomePage.ContextMenu.select("Tags")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click the toggle button to switch to Grid view
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on the 'Default Sort' button
        """
        default_sort = HomePage.Home._utils.validate_and_get_webdriver_object(default_sort_css, "Home page list view choose column")
        HomePage.Home._core_utils.left_click(default_sort)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Tags appears in drop down list:
        """
        HomePage.ContextMenu.verify(["Tags"], "07.01", "asin")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click the toggle button to switch to List view
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click the Choose Columns button
        """
        choose_columns = HomePage.Home._utils.validate_and_get_webdriver_object(choose_col_css, "Home page grid view default sort")
        HomePage.Home._core_utils.left_click(choose_columns)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click Tags in the drop-down list to deselect
        """
        HomePage.ContextMenu.select("Tags")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on the toggle button to switch to Grid view
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on the 'Default Sort' button
        """
        default_sort = HomePage.Home._utils.validate_and_get_webdriver_object(default_sort_css, "Home page list view choose column")
        HomePage.Home._core_utils.left_click(default_sort)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that Tags does not appear in the drop-down list
        """
        HomePage.ContextMenu.verify(["Tags"], "07.02", "asnotin")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : In the banner link, Click on the 'User' button > Click SignOut
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)