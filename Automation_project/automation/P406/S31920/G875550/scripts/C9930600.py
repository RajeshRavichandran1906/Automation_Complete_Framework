"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 18-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.chart import Chart

class C9930600_TestClass(BaseTestCase):
    
    def test_C9930600(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        chart_obj = Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        BUCKET_LABEL_LIST = ['Vertical Axis', 'Horizontal Axis', 'Size', 'Color', 'Options']
        FILTER_LABEL_LIST = ['Store Region', 'Store Name', 'Product Category', 'Sale Date Year']
        GSTARTED_CONTEXT_MENU = ['Expand', 'Refresh', 'Properties']
        LEARN_CONTEXT_MENU = ['View in new window', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        EXPLORE_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        VISUALIZATION_CONTEXT_MENU = ['Run', 'Run in new window', 'Edit', 'Copy Ctrl+C', 'Add to Favorites', 'Properties']
        
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
            STEP 03 : Expand Workspaces>Getting Started from the tree
            Right click on Getting Started from the tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        HomePage.Workspaces.ResourcesTree.right_click("Getting Started")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify Getting Started right-click menu from the tree
        """
        HomePage.ContextMenu.verify(GSTARTED_CONTEXT_MENU, "03.01")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right click on Learn WebFOCUS from the content area.
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Getting Started")
        HomePage.Workspaces.ContentArea.right_click_on_file("Learn WebFOCUS")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Learn WebFOCUS right-click menu from the work area(under Items)
        """
        HomePage.ContextMenu.verify(LEARN_CONTEXT_MENU, "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click View in New Window(Launch).
        """
        HomePage.ContextMenu.select("View in new window")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Learn WebFOCUS displays correctly
        """
        HomePage.Home._core_utils.switch_to_new_window()
        kb_title = self.driver.title
        HomePage.Home._utils.asequal(kb_title, "WebFOCUS KnowledgeBase", "Step 05.01 : Verify Learn WebFOCUS displays correctly")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right click on Explore Sales Data from the content area.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file("Explore Sales Data")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Explore Sales Data right-click menu from the work area(under Items)
        """
        HomePage.ContextMenu.verify(EXPLORE_CONTEXT_MENU, "07.01")
        HomePage.ContextMenu.select("Run...")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], "07.02")
        HomePage.Workspaces.ResourcesTree.select("Getting Started")
        HomePage.Workspaces.ContentArea.right_click_on_file("Explore Sales Data")
        HomePage.ContextMenu.select("Schedule")
        HomePage.ContextMenu.verify(['Email','Printer', 'Report Library', 'Repository'], "07.03")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click Run.
        """
        HomePage.Workspaces.ResourcesTree.select("Getting Started")
        HomePage.Workspaces.ContentArea.right_click_on_file("Explore Sales Data")
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Explore Sales Data displays correctly
        """
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_number_of_element(".chartPanel [class^='riser']", 85, 60)
        chart_obj.verify_number_of_risers(parent_css_with_tagname=".chartPanel ", risers_per_segment=1, expected_number=85, msg="Step 08.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], parent_css="", msg="Step 08.02")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], parent_css="", msg="Step 08.03")
        chart_obj.verify_x_axis_title_in_run_window(['Sale Date Month'], parent_css="", msg="Step 08.04")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css="", msg="Step 08.05")
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css="", msg="Step 08.06")
        web_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(".bucket-label", "bucket_labels")
        label_list_elem = [i.text.strip() for i in web_elems]
        HomePage.Home._utils.as_List_equal(BUCKET_LABEL_LIST, label_list_elem, "Step 08.07 : Verify bucket list items")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Right click on Visualization Example from the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Visualization Example")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Visualization Example right-click menu from the work area(under Items)
        """
        HomePage.ContextMenu.verify(VISUALIZATION_CONTEXT_MENU, "10.01")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Run Visualization Example
        """
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify Visualization Example displays correctly
        """
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_number_of_element("div[data-ibxp-component-name='TableChart_2'] svg > g text[class^='xaxis'][class*='labels']", 424, 45)
        '''Outlier Analysis'''
        parent_css = "div[data-ibxp-component-name='TableChart_1']"
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=21, msg="Step 11.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(['0', '100K', '200K', '300K', '400K', '500K', '600K'], parent_css=parent_css, msg="Step 11.02")
        chart_obj.verify_y_axis_label_in_run_window(['0', '40M', '80M', '120M', '160M', '200M', '240M'], parent_css=parent_css, msg="Step 11.03")
        chart_obj.verify_x_axis_title_in_run_window(['Quantity Sold'], parent_css=parent_css, msg="Step 11.04")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css=parent_css, msg="Step 11.05")
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css=parent_css, msg="Step 11.06")
        
        '''Store Rankings'''
        parent_css = "div[data-ibxp-component-name='TableChart_2']"
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=425, msg="Step 11.07 : Verify number of risers")
        elem_list_present_from_actual_list(exp_list=['London Mall', 'London Central', 'London', 'Amsterdam', 'London Airport'], elem_css=parent_css+" svg > g text[class^='xaxis'][class*='labels']", assert_type="asin", msg="Step 11.08 : Verify X-axis label.")
#         chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], parent_css="", msg="Step 11.08")
        chart_obj.verify_y_axis_label_in_run_window(['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M'], parent_css=parent_css, msg="Step 11.09")
        chart_obj.verify_x_axis_title_in_run_window(['Store Name'], parent_css=parent_css, msg="Step 11.10")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css=parent_css, msg="Step 11.11")

        
        '''Revenue by Category'''
        parent_css = "div[data-ibxp-component-name='TableChart_3']"
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=7, msg="Step 11.13 : Verify number of risers")
        elem_list_present_from_actual_list(['Revenue'], parent_css+" text[class^='pieLabel!g']", 'asequal', 'Step 11.14 : Verify Pie label')
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css=parent_css, msg="Step 11.18")
       
        '''Profitability Analysis'''
        parent_css ="div[data-ibxp-component-name='TableChart_4']"
        chart_obj.verify_number_of_risers(parent_css_with_tagname=parent_css+" ", risers_per_segment=1, expected_number=8, msg="Step 11.19 : Verify number of risers")
        chart_obj.verify_legends_in_run_window(['Revenue Percentage Increase', '-0.7', '-0.3', '0.2', '0.7', '1.2', '1.7'], parent_css=parent_css, msg="Step 11.24")
        elem_list_present_from_actual_list(FILTER_LABEL_LIST, ".filter-field-box", "asequal", "Step 11.25 : Verify bucket list items")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

