"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 11-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9948778_TestClass(BaseTestCase):
    
    def test_C9948778(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        columns_heading = ['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown', '']
        
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
            STEP 04 : Double-click on the 'Portals' folder from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("Portals")
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the items appears as same as below in grid view and by default 'Default sort' button with up arrow is selected
        """
        folders = ['Published_and_show_folder', 'Unpublished_and_hide_folder', 'Unpublished_and_show_folder', 'V4 portal Resources']
        files = ['Blog test', 'Portal page', 'V4 portal']
        HomePage.Workspaces.ContentArea.verify_folders(folders, "04.01", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "04.02", "asequal")
        sorting_arrow = self.driver.find_element(*HomePage.Workspaces.ContentArea.locators.grid_view_sorted_arrow).text.strip()
        HomePage.Home._utils.asequal("arrow_upward", sorting_arrow, "Step 04.03 : Verify Default sort button with up arrow is selected as default")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on toggle 'Switch to list view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the follwoing:
            1.Items appears as same as below in list view
            2.'Default sort' button is not displayed
            3.'Choose Columns' button is displayed
        """
        HomePage.Workspaces.ContentArea.verify_folders(folders, "05.01", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "05.02", "asequal")
        default_sort = self.driver.find_elements(*HomePage.Workspaces.ContentArea.locators.grid_view_sorting)
        is_default_sort_displayed = (len(default_sort)>0) and (default_sort[0].is_displayed())
        HomePage.Home._utils.asequal(False, is_default_sort_displayed, "Step 05.03 : Verify 'Default sort' button is not displayed")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on Title heading
        """
        title = "Title"
        HomePage.Workspaces.ContentArea.click_listview_column_heading(title)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify sort arrow appears next to Title pointing down and the items are sorted alphabetically in descending order.
        """
        title_sorted_folders = ['V4 portal Resources', 'Unpublished_and_show_folder', 'Unpublished_and_hide_folder', 'Published_and_show_folder']
        title_sorted_files = ['V4 portal', 'Portal page', 'Blog test']
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(title).text.strip()
        HomePage.Home._utils.asequal("arrow_downward\nTitle", arrow, "Step 06.01 : Verify sort arrow appears next to Title pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(title_sorted_folders, "06.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(title_sorted_files, "06.03", "asequal")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on Title heading
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(title)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify sort arrow appears next to Title pointing up, and the item are sorted in ascending order.
        """
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(title).text.strip()
        HomePage.Home._utils.asequal("arrow_upward\nTitle", arrow, "Step 07.01 : Verify sort arrow appears next to Title pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "07.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "07.03", "asequal")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on Title heading again
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(title)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that sort arrow is not appears anywhere in the headings and by default items are displayed as same as below:
        """
        HomePage.Workspaces.ContentArea.verify_list_view_columns_heading(columns_heading, "08.01")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "08.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "08.03", "asequal")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on 'Choose Columns' button
        """
        HomePage.Workspaces.ContentArea.click_choose_columns_icon()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that 'Published' and 'Shown columns' gets check-off
        """
        HomePage.ContextMenu.verify_selected_options(["Published", "Shown"], "09.01", "asin")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click anywhere outside drop down list
        """
        HomePage.Workspaces.ActionBar.select_tab("DATA")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on Published heading
        """
        published = "Published"
        HomePage.Workspaces.ContentArea.click_listview_column_heading(published)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify sort arrow appears next to Published pointing down and the items are sorted by published items in descending order as same as below:
        """
        published_sorted_folder = ['Published_and_show_folder', 'V4 portal Resources', 'Unpublished_and_hide_folder', 'Unpublished_and_show_folder']
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(published).text.strip()
        HomePage.Home._utils.asequal("arrow_downward\nPublished", arrow, "Step 11.01 : Verify sort arrow appears next to Title pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(published_sorted_folder, "11.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "11.03", "asequal")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click on Published heading
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(published)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify sort arrow appears next to Published pointing up and the items are sorted by published items in ascending order as same as below:
        """
        published_sorted_folder = ['Unpublished_and_hide_folder', 'Unpublished_and_show_folder', 'Published_and_show_folder', 'V4 portal Resources']
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(published).text.strip()
        HomePage.Home._utils.asequal("arrow_upward\nPublished", arrow, "Step 12.01 : Verify sort arrow appears next to Title pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(published_sorted_folder, "12.03", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "12.03", "asequal")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on Published heading
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(published)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify that sort arrow is not appears anywhere in the headings and by default items are displayed as same as below:
        """
        HomePage.Workspaces.ContentArea.verify_list_view_columns_heading(columns_heading, "13.01")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "13.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "13.03", "asequal")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on Shown heading
        """
        shown = "Shown"
        HomePage.Workspaces.ContentArea.click_listview_column_heading(shown)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify sort arrow appears next to Shown pointing down and the items are sorted by shown/hide items in descending order as same as below:
        """
        shown_sorted_folders = ['Published_and_show_folder', 'Unpublished_and_show_folder', 'Unpublished_and_hide_folder', 'V4 portal Resources']
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(shown).text.strip()
        HomePage.Home._utils.asequal("arrow_downward\nShown", arrow, "Step 14.01 : Verify sort arrow appears next to Shown pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(shown_sorted_folders, "14.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "14.03", "asequal")
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on Shown heading
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(shown)
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify sort arrow appears next to Published pointing down and the items are sorted by shown/hide items in descending order as same as below:
        """
        shown_sorted_folders = ['Unpublished_and_hide_folder', 'V4 portal Resources', 'Published_and_show_folder', 'Unpublished_and_show_folder']
        arrow = HomePage.Workspaces.ContentArea._get_listview_column_heading_obj(shown).text.strip()
        HomePage.Home._utils.asequal("arrow_upward\nShown", arrow, "Step 15.01 : Verify sort arrow appears next to Title pointing down")
        HomePage.Workspaces.ContentArea.verify_folders(shown_sorted_folders, "15.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "15.03", "asequal")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)
        
        STEP_16 = """
            STEP 16 : Click on Shown heading
        """
        HomePage.Workspaces.ContentArea.click_listview_column_heading(shown)
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify that sort arrow is not appears anywhere in the headings and by default items are displayed as same as below:
        """
        HomePage.Workspaces.ContentArea.verify_list_view_columns_heading(columns_heading, "16.01")
        HomePage.Workspaces.ContentArea.verify_folders(folders, "16.02", "asequal")
        HomePage.Workspaces.ContentArea.verify_files(files, "16.03", "asequal")
        HomePage.Home._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Click on toggle 'Switch to grid view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("18", STEP_18)