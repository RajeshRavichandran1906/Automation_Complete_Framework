"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 10-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9948779_TestClass(BaseTestCase):
    
    def test_C9948779(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        sort_button_css= HomePage.Workspaces.ContentArea.locators.grid_view_sorting
#         sort_button_css = ".content-title-btn-name .ibx-label-text"
        sort_arrow_locator = HomePage.Workspaces.ContentArea.locators.grid_view_sorted_arrow
        folders = ["Published_and_show_folder", "Unpublished_and_hide_folder", "Unpublished_and_show_folder", "V4 portal Resources"]
        published_folder_sort_order = [folders[2], folders[1], folders[3], folders[0]]
        shown_folder_sort_order = [folders[1], folders[3], folders[2], folders[0]]
        files = ["Blog test", "Portal page", "V4 portal"]
        sort_options = ["Default sort", "Title", "Summary", "Last modified", "Size", "Published", "Shown"]
        
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Developer User.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view > Click on 'Workspaces from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace > Click on 'G878308' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G878308")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Double-click on 'Portals' folder from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder('Portals')
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the items appears as same as below in grid view and by default 'Default sort' button with pointing up arrow button
        """
        HomePage.Home._utils.wait_for_page_loads(60)
        HomePage.Home._utils.synchronize_with_visble_text(sort_button_css[1], sort_options[0], 30)
        HomePage.Workspaces.ContentArea.verify_grid_view_displayed("04.01")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "04.02")
        HomePage.Workspaces.ContentArea.verify_files(files, "04.03")
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[0], sort_title, "Step 04.04: Verify Default sort is selected")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 04.05: Verify pointing up arrow button is displayed")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'Default sort' button
        """
        HomePage.driver.find_element_by_css_selector(sort_button_css[1]).click()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the following options displayed:
        """
        HomePage.ContextMenu.verify(sort_options, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on 'Title' option
        """
        HomePage.ContextMenu.select(sort_options[1])
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following:
            1. 'Title' button is displayed and Pointing up arrow button is displayed next to the 'Title' button
            2. Folders and Items are sorted alphabetically in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(sort_button_css[1], sort_options[1], 30)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[1], sort_title, "Step 06.01: Verify 'Title' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 06.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "06.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "06.04")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click the ponting up arrow button next to the 'Title' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following:
            1. Pointing down arrow button is displayed next to the 'Title' button
            2. Folders and Items are sorted alphabetically in descending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[1], sort_title, "Step 07.01: Verify 'Title' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_downward", "Step 07.02: Verify pointing down arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(folders[::-1], "07.03")
        HomePage.Workspaces.ContentArea.verify_files(files[::-1], "07.04")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click the ponting down arrow button next to the 'Title' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the following:
            1. Pointing up arrow button is displayed next to the 'Title' button
            2. Folders and Items are sorted alphabetically in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[1], sort_title, "Step 08.01: Verify 'Title' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 08.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "08.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "08.04")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on 'Title' button > Select 'Published' option
        """
        HomePage.driver.find_element_by_css_selector(sort_button_css[1]).click()
        HomePage.ContextMenu.select(sort_options[5])
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following:
            1. 'Published' button is displayed and Pointing up arrow button is displayed next to the 'Title' button
            2. Folders and Items are sorted by published items in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(sort_button_css[1], sort_options[5], 30)
        
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[5], sort_title, "Step 09.01: Verify 'Published' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 09.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(published_folder_sort_order, "09.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "09.04")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click the ponting up arrow button next to the 'Published' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following:
            1. Pointing down arrow button is displayed next to the 'Published' button
            2. Folders and Items are sorted by published items in descending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[5], sort_title, "Step 10.01: Verify 'Published' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_downward", "Step 10.02: Verify pointing down arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(published_folder_sort_order[::-1], "10.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "10.04")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click the ponting down arrow button next to the 'Published' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the following:
            1. Pointing up arrow button is displayed next to the 'Published' button
            2. Folders and Items are sorted by published items in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[5], sort_title, "Step 11.01: Verify 'Published' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 11.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(published_folder_sort_order, "11.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "11.04")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on 'Title' button > Select 'Shown' option
        """
        HomePage.driver.find_element_by_css_selector(sort_button_css[1]).click()
        HomePage.ContextMenu.select(sort_options[6])
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the following:
            1. 'Shown' button is displayed and Pointing up arrow button is displayed next to the 'Shown' button
            2. Folders and Items are sorted by shown items in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(sort_button_css[1], sort_options[6], 30)
        
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[6], sort_title, "Step 12.01: Verify 'Shown' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 12.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(shown_folder_sort_order, "12.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "12.04")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click the ponting up arrow button next to the 'Shown' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the following:
            1. Pointing down arrow button is displayed next to the 'Shown' button
            2. Folders and Items are sorted by shown items in descending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[6], sort_title, "Step 13.01: Verify 'Shown' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_downward", "Step 13.02: Verify pointing down arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(shown_folder_sort_order[::-1], "13.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "13.04")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click the ponting down arrow button next to the 'Shown' button
        """
        self.driver.find_element(*sort_arrow_locator).click()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following:
            1. Pointing up arrow button is displayed next to the 'Shown' button
            2. Folders and Items are sorted by shown items in ascending order same as below:
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[6], sort_title, "Step 14.01: Verify 'Shown' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 14.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(shown_folder_sort_order, "14.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "14.04")
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on 'Shown' button > Select 'Default sort' option
        """
        HomePage.driver.find_element_by_css_selector(sort_button_css[1]).click()
        HomePage.ContextMenu.select(sort_options[0])
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify the items appears as same as below in grid view and by default 'Default sort' button with pointing up arrow button
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(sort_button_css[1], sort_options[0], 30)
        
        sort_title = HomePage.driver.find_element_by_css_selector(sort_button_css[1]).text.strip()
        HomePage.Home._utils.asequal(sort_options[0], sort_title, "Step 15.01: Verify 'Default sort' button is displayed")
        sort_arrow = self.driver.find_element(*sort_arrow_locator).text.strip()
        HomePage.Home._utils.asequal(sort_arrow, "arrow_upward", "Step 15.02: Verify pointing up arrow button is displayed")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "15.03")
        HomePage.Workspaces.ContentArea.verify_files(files, "15.04")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

