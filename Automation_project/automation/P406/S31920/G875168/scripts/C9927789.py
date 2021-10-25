"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 12-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927789_TestClass(BaseTestCase):
    
    def test_C9927789(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        folders = ["Chart types", "ED_RC_TEST", "IA items", "Page designer", "Portals", "RC items", "Shortcuts", "Text Editor", "Uploaded items" ,"URL"]
        files = ["3D chart", "Arc chart", "Area chart", "Bar Chart", "Bubble chart", "Choropleth chart", "Datagrid Chart", "Funnel Chart", "Gauge chart", "Heatmap Chart", "Insight1", "Insight2", "Line chart", "Pie chart", "Pyramid Chart", "Ring Pie chart", "Scatter chart", "Streamgraph chart", "Tagcloud chart", "Treemap Chart"]
        choose_column_list = ["Title", "Name", "Summary", "Tags", "Last modified", "Created on", "Size", "Owner", "Published", "Shown"]
        context_menu_css = ".pop-top div[role][data-ibx-type$='Item']"
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

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify all the subfolders appears in the grid view as same in the below screenshot
        """
        if HomePage.Workspaces.ContentArea._is_list_view_displayed_():
            HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Workspaces.ContentArea.verify_folders(folders, "03.01", "asequal")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Hover the mouse to the switch to list view toggle button
        """
        
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the tooltip as 'Switch to list view'
        """
        tootip_value = self.driver.find_element(*HomePage.Workspaces.NavigationBar.locators.list_view).get_attribute("title").strip()
        HomePage.Home._utils.asequal(tootip_value, 'Switch to list view', 'Step 04: Verify the tooltip as "Switch to list view"')
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on toggle 'Switch to list view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that all the subfolders are displayed in the list view as same in the screenshot
            private item/folder icons need to reflect the grayscale effects
        """
        HomePage.Workspaces.ContentArea.verify_published_folders(folders, "05.01", "asequal")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Hover the mouse to the 'Switch to grid view' toggle button
        """
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the tooltip as 'Switch to grid view'
        """
        tootip_value = self.driver.find_element(*HomePage.Workspaces.NavigationBar.locators.grid_view).get_attribute("title").strip()
        HomePage.Home._utils.asequal(tootip_value, 'Switch to tile view', 'Step 06: Verify the tooltip as "Switch to tile view"')
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on toggle 'Switch to grid view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify all the subfolders appears in the grid view as same in the below screenshot
        """
        HomePage.Workspaces.ContentArea.verify_folders(folders, "07.01", "asequal")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Double click 'Chart types' in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder(folders[0])
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that different types of charts appears in the grid view (3D chart, Arc chart, Area chart, Bar Chart, Bubble chart, Choropleth chart, Datagrid Chart, Funnel Chart, Gauge chart, Heatmap Chart, Insight1, Insight2, Line chart, Pie chart, Pyramid Chart, Ring Pie chart, Scatter chart, Streamgraph chart, Tagcloud chart, and Treemap Chart)
        """
        HomePage.Workspaces.ContentArea.verify_files(files, "08.01", "asequal")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on toggle 'Switch to list view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_list_view()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that different types of charts appears in the list view (3D chart, Arc chart, Area chart, Bar Chart, Bubble chart, Choropleth chart, Datagrid Chart, Funnel Chart, Gauge chart, Heatmap Chart, Insight1, Insight2, Line chart, Pie chart, Pyramid Chart, Ring Pie chart, Scatter chart, Streamgraph chart, Tagcloud chart, and Treemap Chart)
        """
        HomePage.Workspaces.ContentArea.verify_list_view_displayed("09.01")
        HomePage.Workspaces.ContentArea.verify_files(files, "09.02", "asequal")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on 'Choose columns' button.
        """
        HomePage.Workspaces.ContentArea.click_choose_columns_icon()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the following options appears with the check/uncheck symbol:
        """
        checked_menu_index = [0, 2, 4, 6, 8, 9]
        checked_menus = [choose_column_list[index] for index in checked_menu_index]
        HomePage.ContextMenu.verify_selected_options(checked_menus, "10.01", "asin")
        unchecked_menu_index = [1, 3, 5]
        unchecked_menus = [choose_column_list[index] for index in unchecked_menu_index]
        HomePage.ContextMenu.verify_selected_options(unchecked_menus, "10.02", "asnotin")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Uncheck Summary
        """
        HomePage.ContextMenu.select(choose_column_list[2])
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify Summary heading does not appear and drop down list remains open
        """
        HomePage.Workspaces.ContentArea.verify_list_view_columns_heading([choose_column_list[2]], "11.01", "notin")
        choose_column = self.driver.find_element_by_css_selector(context_menu_css).is_displayed()
        HomePage.Home._utils.asequal(True, choose_column, "Step 11.02: Verify drop down list remains open")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Check Summary
        """
        HomePage.ContextMenu.select(choose_column_list[2])
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Summary heading appears and drop down list remains open
        """
        HomePage.Home._utils.wait_for_page_loads(50)
        HomePage.Workspaces.ContentArea.verify_list_view_columns_heading([choose_column_list[2]], "12.01", "in")
        choose_column = self.driver.find_element_by_css_selector(context_menu_css).is_displayed()
        HomePage.Home._utils.asequal(True, choose_column, "Step 12.02: Verify drop down list remains open")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click anywhere outside drop down list
        """
        HomePage.ContextMenu.close()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify drop down list closes
        """
        choose_column_object = self.driver.find_elements_by_css_selector(context_menu_css)
        choose_column_status = choose_column_object[0].is_displayed() if choose_column_object != [] else False
        HomePage.Home._utils.asequal(False, choose_column_status, "Step 13.02: Verify drop down list closes")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on toggle 'Switch to grid view' button
        """
        HomePage.Workspaces.ContentArea.switch_to_grid_view()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

