"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 25-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927794_TestClass(BaseTestCase):
    
    def test_C9927794(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        choose_col_css = HomePage.Workspaces.ContentArea.locators.list_view[1] + "div[title='Choose columns']"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User (autodevuser207).
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that workspaces available in the content area get displayed in Grid View.
        """
        HomePage.Workspaces.ContentArea.verify_grid_view_displayed("02.01")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on 'Switch to list view' toggle button.
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that the content area displayed in list view with the columns Title, Summary, Last modified, Size, Published and Shown.
        """
        expected_columns1 = ['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown', '']
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("03.01")
        actual_columns = [column.text.strip() for column in self.driver.find_elements_by_css_selector("div.grid-cell-title") if column.is_displayed()]
        HomePage.Home._utils.asequal(expected_columns1, actual_columns, "Step 03.01 : Verify that the content area displayed with the columns Title, Summary, Last modified, Size, Published and Shown")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click 'Choose column' option > Check off 'Name'
        """
        choose_col = self.driver.find_element_by_css_selector(choose_col_css)
        HomePage.Home._core_utils.left_click(choose_col)
        HomePage.ContextMenu.select("Name")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.list_view[1], "Name", 20)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that additionally 'Name' column added in the content area which is in list view
        """
        expected_columns2 = ['Title', 'Name', 'Summary', 'Last modified', 'Size', 'Published', 'Shown', '']
        actual_columns = [column.text.strip() for column in self.driver.find_elements_by_css_selector("div.grid-cell-title") if column.is_displayed()]
        HomePage.Home._utils.asequal(expected_columns2, actual_columns, "Step 04.01 : Verify that additionally 'Name' column added in the content area which is in list view")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User (autoadvuser63).
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that workspaces available in the content area get displayed in Grid View.
        """
        HomePage.Workspaces.ContentArea.verify_grid_view_displayed("06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on 'Switch to list view' toggle button.
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that the content area shows in list view and the 'Name' column is not showing.
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("07.01")
        actual_columns = [column.text.strip() for column in self.driver.find_elements_by_css_selector("div.grid-cell-title") if column.is_displayed()]
        HomePage.Home._utils.as_notin("Name", actual_columns, "Step 07.01 : Verify that the 'Name' column is not showing in list view.")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on 'Switch to grid view' toggle button to revert back the Paris Homepage content area by its default state.
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User (autodevuser207).
        """
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on Workspaces view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that the content area displayed in list view with the columns Title, Name, Summary, Last modified, Size, Published and Shown.
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("10.01")
        actual_columns = [column.text.strip() for column in self.driver.find_elements_by_css_selector("div.grid-cell-title") if column.is_displayed()]
        HomePage.Home._utils.asequal(expected_columns2, actual_columns, "Step 10.02 : Verify that the columns Title, Name, Summary, Last modified, Size, Published and Shown.")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click 'Choose column' option > Uncheck 'Name'
        """
        choose_col = self.driver.find_element_by_css_selector(choose_col_css)
        HomePage.Home._core_utils.left_click(choose_col)
        HomePage.ContextMenu.select("Name")
        HomePage.Home._utils.wait_for_page_loads(20, pause_time=2)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that the content area displayed in list view with the columns Title, Summary, Last modified, Size, Published and Shown.
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("11.01")
        actual_columns = [column.text.strip() for column in self.driver.find_elements_by_css_selector("div.grid-cell-title") if column.is_displayed()]
        HomePage.Home._utils.asequal(expected_columns1, actual_columns, "Step 11.02 : Verify that the columns columns Title, Summary, Last modified, Size, Published and Shown.")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on 'Switch to grid view' toggle button to revert back the Paris Homepage content area by its default state.
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)