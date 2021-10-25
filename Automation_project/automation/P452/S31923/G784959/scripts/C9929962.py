"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 23-September-2020
-------------------------------------------------------------------------------------------"""

from common.wftools.page_designer import Design
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_chart import Designer_Chart
from common.wftools.paris_home_page import ParisHomePage

class C9929962_TestClass(BaseTestCase):
    
    def test_C9929962(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = Designer_Chart(self.driver)
        Page = Design(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        preview_table_css = "table#IWindowBodyFTB_0_0"
        grid_col_css = "tr.arGridColumnHeading td[onclick]"
        grid_head_css = "td[id^='THEAD']"
        grid_columns = ['Product\nCategory', 'Product\nSubcategory', 'Cost of Goods', 'Gross Profit', 'Cost of Goods', 'Gross Profit', 'Cost of Goods', 'Gross Profit', 'Cost of Goods', 'Gross Profit']
        grid_heading = ['Customer,Business,Region', 'EMEA', 'North America', 'Oceania', 'South America']
        data_file_name = "C9929962.xlsx"
        scroll_div_css = "#IWindowBodyFB_0_0"
        file_name = "C9929962"
        
        STEP_01 = """
            STEP 01 : Launch WF Designer to create a new visualization:
            http://machine.ibi.com:port/alias/designer?&master=new_retail/wf_retail_lite&item=IBFS:/WFC/Repository/P452_S31923/G784931&tool=framework&startlocation=IBFS:/WFC/Repository
        """
        Designer.invoke_designer_using_api("retail_samples/wf_retail_lite", "mriddev", "mrpassdev")
        HomePage.Home._utils.synchronize_with_visble_text("div.messageTextWrapper", "Drop", 120)
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select the 'Standard Report' template
        """
        open_css = "div.wfc-chartpicker-next-button"
        report_css = "div[data-ibx-name='uttpExtendedContainer'] div[title='Standard Report']"
        open_btn = self.driver.find_element_by_css_selector(open_css)
        HomePage.Home._core_utils.left_click(open_btn)
        HomePage.Home._utils.synchronize_until_element_is_visible(report_css, 15)
        report = self.driver.find_element_by_css_selector(report_css)
        HomePage.Home._core_utils.left_click(report)
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=2)
        open_btn = self.driver.find_element_by_css_selector(open_css)
        HomePage.Home._core_utils.left_click(open_btn)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Double click following fields:
            Product,Category
            Product,Subcategory
            Cost of Goods
            Gross Profit
        """
        Designer.double_click_on_dimension_field("Product->Product,Category")
        HomePage.Home._utils.synchronize_with_visble_text("tr.arGridColumnHeading", "Product", 45)
        Designer.double_click_on_dimension_field("Product->Product,Subcategory")
        measure_tree = self.driver.find_element_by_css_selector("div.measure-tree-box")
        HomePage.Home._core_utils.python_move_to_element(measure_tree)
        HomePage.Home._utils.synchronize_with_visble_text("tr.arGridColumnHeading", "Subcategory", 45)
        Designer.double_click_on_measures_field("Sales->Cost of Goods")
        HomePage.Home._utils.synchronize_with_visble_text("tr.arGridColumnHeading", "Cost of Goods", 45)
        Designer.double_click_on_measures_field("Sales->Gross Profit")
        HomePage.Home._utils.synchronize_with_visble_text("tr.arGridColumnHeading", "Gross Profit", 45)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag 'Customer,Business,Region' into the Columns bucket
        """
        Designer.drag_dimension_field_to_query_bucket("Customer->Customer,Business,Region", "Columns")
        HomePage.Home._utils.synchronize_with_visble_text(grid_head_css, "Customer,Business,Region", 45)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify query bucket values
        """
        Designer.verify_values_in_querybucket("Rows", ['Product,Category', 'Product,Subcategory'], "Step 04.01 : Verify Rows bucket values")
        Designer.verify_values_in_querybucket("Columns", ['Customer,Business,Region'], "Step 04.02 : Verify Columns bucket values")
        Designer.verify_values_in_querybucket("Summary", ['Cost of Goods', 'Gross Profit'], "Step 04.03 : Verify Summary bucket values")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the report canvas
        """
        actual_grid_col = [grid.text.strip() for grid in self.driver.find_elements_by_css_selector(grid_col_css) if grid.is_displayed()]
        actual_grid_heading = [grid.text.strip() for grid in self.driver.find_elements_by_css_selector(grid_head_css) if grid.is_displayed()]
        HomePage.Home._utils.asequal(grid_columns[:-2], actual_grid_col[:-2], "Step 05.01 : Verify grid columns")
        HomePage.Home._utils.asequal(grid_heading, actual_grid_heading, "Step 05.02 : Verify grid heading")
        #HomePage.Home._utils.create_table_data_start_end_rowcolumn(data_file_name, table_css=preview_table_css)
        HomePage.Home._utils.verify_table_data_using_start_end_rowcolumn(data_file_name, preview_table_css, "Step 05.03 : Verify data grid")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on the 'Convert to page' button in the toolbar
        """
        conver_page = self.driver.find_element_by_css_selector("div[title='Convert to page']")
        HomePage.Home._core_utils.left_click(conver_page)
        HomePage.Home._utils.wait_for_page_loads(60, pause_time=4)
        HomePage.Home._utils.synchronize_with_visble_text("div.pd-page-canvas", "Cost of Goods", 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify page canvas, horizontal/vertical scroll bars should be visible
        """
        actual_grid_col = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_col_css))
        actual_grid_heading = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_head_css))
        HomePage.Home._utils.asequal(grid_columns, actual_grid_col, "Step 06.01 : Verify grid columns")
        HomePage.Home._utils.asequal(grid_heading, actual_grid_heading, "Step 06.02 : Verify grid heading")
        HomePage.Home._utils.verify_table_data_using_start_end_rowcolumn(data_file_name, preview_table_css, "Step 06.03 : Verify data grid")
        Page.verify_containers_title(['Visualization 1'], "Step 06.04 : Verify page containers")
        horizontal_scrollbar = HomePage.Home._javascript.check_element_has_horizontal_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        vertical_scrollbar = HomePage.Home._javascript.check_element_has_vertical_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        HomePage.Home._utils.asequal(True, horizontal_scrollbar, "Step 06.05 : Verify horizontal bar visible")
        HomePage.Home._utils.asequal(True, vertical_scrollbar, "Step 06.05 : Verify vertical bar visible")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the Preview button
        """
        run_win = self.driver.find_element_by_css_selector("div[title='Run in new window']")
        HomePage.Home._core_utils.left_click(run_win)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(60, pause_time=4)
        HomePage.Home._utils.synchronize_with_visble_text("div.pd-page-canvas", "Cost of Goods", 80)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify horizontal/vertical scroll bars are visible
        """
        actual_grid_col = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_col_css))
        actual_grid_heading = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_head_css))
        HomePage.Home._utils.asequal(grid_columns, actual_grid_col, "Step 07.01 : Verify grid columns")
        HomePage.Home._utils.asequal(grid_heading, actual_grid_heading, "Step 07.02 : Verify grid heading")
        HomePage.Home._utils.verify_table_data_using_start_end_rowcolumn(data_file_name, preview_table_css, "Step 07.03 : Verify data grid")
        Page.verify_containers_title(['Visualization 1'], "Step 07.04 : Verify page containers")
        horizontal_scrollbar = HomePage.Home._javascript.check_element_has_horizontal_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        vertical_scrollbar = HomePage.Home._javascript.check_element_has_vertical_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        HomePage.Home._utils.asequal(True, horizontal_scrollbar, "Step 07.05 : Verify horizontal bar visible")
        HomePage.Home._utils.asequal(True, vertical_scrollbar, "Step 07.06 : Verify vertical bar visible")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the Preview window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on 'Save' > C9929962 > Click on the Save button
        """
        save_btn = self.driver.find_element_by_css_selector("div.btn-save")
        HomePage.Home._core_utils.left_click(save_btn)
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.ModalDailogs.Resources.Title.enter_text(file_name)
        HomePage.ModalDailogs.Resources.SaveButton.click()
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=3)
        ok_btn = self.driver.find_elements_by_css_selector(".pop-top .ibx-dialog-ok-button")
        (len(ok_btn)>0) and HomePage.Home._core_utils.left_click(ok_btn[0])
        HomePage.ModalDailogs.Resources.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Close Designer
        """
        Designer.api_logout()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Edit the saved item:
            http://machine.ibi.com:port/alias/designer?&item=IBFS:/WFC/Repository/P452_S31923/G784931/c9929962&startlocation=IBFS:/WFC/Repository
        """
        Designer.edit_page_with_designer_using_api(file_name, "mriddev", "mrpassdev")
        HomePage.Home._utils.wait_for_page_loads(60, pause_time=4)
        HomePage.Home._utils.synchronize_with_visble_text("div.pd-page-canvas", "Cost of Goods", 60)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify the page canvas
        """
        actual_grid_col = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_col_css))
        actual_grid_heading = HomePage.Home._javascript.get_elements_text(self.driver.find_elements_by_css_selector(grid_head_css))
        HomePage.Home._utils.asequal(grid_columns, actual_grid_col, "Step 12.01 : Verify grid columns")
        HomePage.Home._utils.asequal(grid_heading, actual_grid_heading, "Step 12.02 : Verify grid heading")
        HomePage.Home._utils.verify_table_data_using_start_end_rowcolumn(data_file_name, preview_table_css, "Step 12.03 : Verify data grid")
        Page.verify_containers_title(['Visualization 1'], "Step 12.04 : Verify page containers")
        horizontal_scrollbar = HomePage.Home._javascript.check_element_has_horizontal_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        vertical_scrollbar = HomePage.Home._javascript.check_element_has_vertical_scrollbar(self.driver.find_element_by_css_selector(scroll_div_css))
        HomePage.Home._utils.asequal(True, horizontal_scrollbar, "Step 12.05 : Verify horizontal bar visible")
        HomePage.Home._utils.asequal(True, vertical_scrollbar, "Step 12.06 : Verify vertical bar visible")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Drag the current report container from the lower right corner > Expand container as displayed in the 'Expected' screenshot
        """
        panel = self.driver.find_element_by_css_selector("div[data-ibxp-title='@STR_CONT_TITLE_2']")
        page = self.driver.find_element_by_css_selector("div.pd-page-tab-content-wrapper")
        panel_loc = HomePage.Home._core_utils.get_web_element_coordinate(panel, "bottom_right")
        page_loc = HomePage.Home._core_utils.get_web_element_coordinate(page, "bottom_right", yoffset=-30)
        HomePage.Home._core_utils.drag_and_drop(panel_loc['x'], panel_loc['y'], page_loc['x'], page_loc['y'])
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the entire report is visible when expanded
        """
        actual_grid_col = [grid.text.strip() for grid in self.driver.find_elements_by_css_selector(grid_col_css) if grid.is_displayed()]
        actual_grid_heading = [grid.text.strip() for grid in self.driver.find_elements_by_css_selector(grid_head_css) if grid.is_displayed()]
        HomePage.Home._utils.asequal(grid_columns[:-2], actual_grid_col[:-2], "Step 13.01 : Verify grid columns")
        HomePage.Home._utils.asequal(grid_heading, actual_grid_heading, "Step 13.02 : Verify grid heading")
        HomePage.Home._utils.verify_table_data_using_start_end_rowcolumn(data_file_name, preview_table_css, "Step 13.03 : Verify data grid")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on the Save button
        """
        save_btn = self.driver.find_element_by_css_selector("div.btn-save")
        HomePage.Home._core_utils.left_click(save_btn)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Logout
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.api_logout
        HomePage.Home._utils.capture_screenshot("15", STEP_15)