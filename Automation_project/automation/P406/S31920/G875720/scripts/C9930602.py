"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 14-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.chart import Chart

class C9930602_TestClass(BaseTestCase):
    
    def test_C9930602(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        chart_obj = Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        VISUALIZATIONS_CONTEXT_MENU = ['Expand', 'Copy Ctrl+C', 'Refresh', 'Properties']
        VISUALIZATIONS_ITEMS = ['Discount by Category', 'Outlier Analysis', 'Profitability Analysis', 'Revenue by Category', 'Revenue Flow', 'Revenue over Time', 'Store Rankings']
        VISUALIZATIONS_ITEMS_CONTEXT_MENU = ['Run', 'Run...', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        FILTER_LABEL_LIST = ['Store Region', 'Store Name', 'Product Category', 'Sale Date Year']
        
        def elem_list_present_from_actual_list(exp_list, elem_css, assert_type, msg):
            web_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(elem_css, "web_element")
            actual_list = [i.text.strip() for i in web_elems]
            HomePage.Home._utils.verify_list_values(exp_list, actual_list, msg, assert_type)

        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand Workspaces>Getting Started>Visualizations from the tree
            Right click on Visualizations from the tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.expand("Workspaces->Getting Started")
        HomePage.Workspaces.ResourcesTree.right_click("Visualizations")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify Visualizations right-click menu from the tree
        """
        HomePage.ContextMenu.verify(VISUALIZATIONS_CONTEXT_MENU, "03.01")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right click on items under Visualizations content area.
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Visualizations")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify right-click menu of Items from the work area(under Items)
    
            Note: All the same
        """
        for item in VISUALIZATIONS_ITEMS:
            HomePage.Workspaces.ContentArea.right_click_on_file(item)
            HomePage.ContextMenu.verify(VISUALIZATIONS_ITEMS_CONTEXT_MENU, "04.01")
            HomePage.Workspaces.ResourcesTree.select("Visualizations")
        Rev_flow_2_xpath="(//following-sibling::div[normalize-space() = 'Revenue Flow'][contains(@class, 'file-item-hbox')]/parent::div)[2]"
        web_elem = self.driver.find_element_by_xpath(Rev_flow_2_xpath)
        HomePage.Home._core_utils.right_click(web_elem)
        HomePage.ContextMenu.verify(VISUALIZATIONS_ITEMS_CONTEXT_MENU, "04.01")
        HomePage.Workspaces.ResourcesTree.select("Visualizations")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Run Discount by Category
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[0])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify it displays correctly
        """
        PIE_LABEL_LIST1 =['0.00', '1,000,000.00', '2,000,000.00', '3,000,000.00', '4,000,000.00', '5,000,000.00', '6,000,000.00', '7,000,000.00', '8,000,000.00', '9,000,000.00', '10,000,000.00', '11,000,000.00']
        PIE_LABEL_LIST2 =['Video Production', 'Televisions', 'Computers', 'Accessories', 'Camcorder', 'Media Player', 'Stereo Systems']
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_number_of_element("#jschart_HOLD_0 [class^='riser']", 7, 60)
        chart_obj.verify_number_of_risers(parent_css_with_tagname="#jschart_HOLD_0 ", risers_per_segment=1, expected_number=7, msg="Step 05.01 : Verify number of risers")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list=PIE_LABEL_LIST1, parent_css="#jschart_HOLD_0", label_css="text[class*='label']", msg="Step 05.02 ")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_label_list=PIE_LABEL_LIST2, parent_css="#jschart_HOLD_0", label_css=".group-label text", msg="Step 05.03 ")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Run Outlier Analysis
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[1])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify it displays correctly
        """
        parent_css = "#jschart_HOLD_0"
        HomePage.RunWindow.switch_to_frame()
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=21, msg="Step 07.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(['0', '100K', '200K', '300K', '400K', '500K', '600K'], parent_css=parent_css, msg="Step 07.02")
        chart_obj.verify_y_axis_label_in_run_window(['0', '40M', '80M', '120M', '160M', '200M', '240M'], parent_css=parent_css, msg="Step 07.03")
        chart_obj.verify_x_axis_title_in_run_window(['Quantity Sold'], parent_css=parent_css, msg="Step 07.04")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css=parent_css, msg="Step 07.05")
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css=parent_css, msg="Step 07.06")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Run Profitability Analysis
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[2])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify it displays correctly
        """
        parent_css ="#jschart_HOLD_0"
        HomePage.RunWindow.switch_to_frame()
        LEGEND_LABELS = ['Revenue Percentage Increase', '-1', '9.1', '19.2', '29.3', '39.4', '49.5']
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=22, msg="Step 09.01 : Verify number of risers")
        chart_obj.verify_legends_in_run_window(LEGEND_LABELS, parent_css=parent_css, msg="Step 09.02")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Run Revenue by Category
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[3])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify it displays correctly
        """
        parent_css = "#jschart_HOLD_0"
        HomePage.RunWindow.switch_to_frame()
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=7, msg="Step 11.01 : Verify number of risers")
        elem_list_present_from_actual_list(['Revenue'], parent_css+" text[class^='pieLabel!g']", 'asequal', 'Step 11.02 : Verify Pie label')
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css=parent_css, msg="Step 11.03")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Run Revenue Flow
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[4])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify it displays correctly
        """
        
        HomePage.RunWindow.switch_to_frame()
        elem_list_present_from_actual_list(FILTER_LABEL_LIST, ".pd-amper-label .ibx-label-text", "asequal", "Step 13.03 : Verify bucket list items")
        self.driver.switch_to_frame(self.driver.find_element_by_css_selector("[class*='iframe-frame']"))
        parent_css = "#jschart_HOLD_0"
        path_elems=self.driver.find_elements_by_css_selector(parent_css+" path.link")
        HomePage.Home._utils.asequal(28,len(path_elems),"Step 13.02 : Verify path elements")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Run Revenue Flow
        """
        Rev_flow_2_xpath="(//following-sibling::div[normalize-space() = 'Revenue Flow'][contains(@class, 'file-item-hbox')]/parent::div)[2]"
        web_elem = self.driver.find_element_by_xpath(Rev_flow_2_xpath)
        HomePage.Home._core_utils.right_click(web_elem)
        HomePage.Home._utils.wait_for_page_loads(30)
        #HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[5],file_type='fex')
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify it displays correctly
        """
        HomePage.RunWindow.switch_to_frame()
        parent_css = "#jschart_HOLD_0"
        path_elems=self.driver.find_elements_by_css_selector(parent_css+" path.link")
        HomePage.Home._utils.asequal(28,len(path_elems),"Step 15.02 : Verify path elements")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Run Revenue over Time
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[5])
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify it displays correctly
        """
        parent_css = "#jschart_HOLD_0"
        X_AXIS_LABELS =['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        Y_AXIS_LABELS =['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
        VERTICAL_LABEL = ['Sale Date Year : Sale Date Month']
        HomePage.RunWindow.switch_to_frame()
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=48, msg="Step 17.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(X_AXIS_LABELS, parent_css=parent_css, msg="Step 17.02")
        chart_obj.verify_y_axis_label_in_run_window(Y_AXIS_LABELS, parent_css=parent_css, msg="Step 17.03")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css="", msg="Step 17.04")
        elem_list_present_from_actual_list(VERTICAL_LABEL, parent_css+" .gVertTitle", 'asequal', 'Step 17.05 : Verify X-Axis Labels')
        HomePage.Home._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Run Store Rankings
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(VISUALIZATIONS_ITEMS[6])
        HomePage.ContextMenu.select("Run")

        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify it displays correctly
        """
        parent_css = "#jschart_HOLD_0"
        X_AXIS_LABELS =['London Mall', 'London Central', 'London', 'Amsterdam']
        Y_AXIS_LABELS =['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        HomePage.RunWindow.switch_to_frame()
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=425, msg="Step 19.01 : Verify number of risers")
        chart_obj.verify_y_axis_label_in_run_window(Y_AXIS_LABELS, parent_css=parent_css, msg="Step 19.02")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css="", msg="Step 19.03")
        chart_obj.verify_x_axis_title_in_run_window(['Store Name'], parent_css="", msg="Step 19.04")
        elem_list_present_from_actual_list(X_AXIS_LABELS, parent_css+" svg > g text[class^='xaxis'][class*='labels']", 'asin', 'Step 19.05 : Verify X-Axis Labels')
        HomePage.Home._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("21", STEP_21)

