"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 17-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.chart import Chart

class C9930007_TestClass(BaseTestCase):
    
    def test_C9930007(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        chart_obj = Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        BUCKET_LABEL_LIST = ['Vertical Axis', 'Horizontal Axis', 'Size', 'Color', 'Options']
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_01_EXPECTED = """
            STEP 01 - Expected : Verify Favorites displays empty
        """
        HomePage.Home.Favorites.verify_items([], 01.01, assert_type='asequal')
        HomePage.Home._utils.capture_screenshot("01 - Expected", STEP_01_EXPECTED, True)

        STEP_02 = """
            STEP 02 : From Getting Started, right-click Explore Sales Data>Add to Favorites
        """
        HomePage.Home.GettingStarted.right_click_on_item('Explore Sales Data')
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify Explore Sales Data report displays correctly under Favorites
        """
        HomePage.Home.Favorites.verify_items(['Explore Sales Data'], 02.01, assert_type='asequal')
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Right-click on Explore Sales Data report under Favorites.
        """
        HomePage.Home.Favorites.right_click_on_item('Explore Sales Data')
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify Explore Sales Data report right-click menu under Favorites
        """
        HomePage.ContextMenu.verify(['Run', 'Run...', 'Edit', 'Remove from Favorites', 'Properties'], "03.01")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], "03.02", menu_path="Run...")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Run Explore Sales Data
        """
        HomePage.Home.Favorites.right_click_on_item('Explore Sales Data')
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Explore Sales Data report runs correctly
        """
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_number_of_element(".chartPanel [class^='riser']", 85, 60)
        chart_obj.verify_number_of_risers(parent_css_with_tagname=".chartPanel ", risers_per_segment=1, expected_number=85, msg="Step 04.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], parent_css="", msg="Step 04.02")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], parent_css="", msg="Step 04.03")
        chart_obj.verify_x_axis_title_in_run_window(['Sale Date Month'], parent_css="", msg="Step 04.04")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css="", msg="Step 04.05")
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css="", msg="Step 04.06")
        web_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(".bucket-label", "bucket_labels")
        label_list_elem = [i.text.strip() for i in web_elems]
        HomePage.Home._utils.as_List_equal(BUCKET_LABEL_LIST, label_list_elem, "Step 04.07 : Verify bucket list items")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Close the Run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Explore Sales Data report displays under Recents
        """
        HomePage.Home.Recents.verify_items(['Explore Sales Data'], 05.01)
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right-click on Explore Sales Data report under Recents.
        """
        HomePage.Home.Recents.right_click_on_item('Explore Sales Data')
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Explore Sales Data report right-click menu under Recents
        """
        HomePage.ContextMenu.verify(['Run', 'Run...','Schedule', 'Edit', 'Remove from Recents', 'Add to Favorites', 'Properties'], "06.01")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], "06.02", menu_path="Run...")
        HomePage.Home.Recents.right_click_on_item('Explore Sales Data')
        HomePage.ContextMenu.verify(['Email', 'Printer', 'Report Library', 'Repository'], "06.03", menu_path="Schedule")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Run Explore Sales Data
        """
        HomePage.Home.Recents.right_click_on_item('Explore Sales Data')
        HomePage.ContextMenu.select("Run")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Explore Sales Data report runs correctly
        """
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_number_of_element(".chartPanel [class^='riser']", 85, 60)
        chart_obj.verify_number_of_risers(parent_css_with_tagname=".chartPanel ", risers_per_segment=1, expected_number=85, msg="Step 07.01 : Verify number of risers")
        chart_obj.verify_x_axis_label_in_run_window(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], parent_css="", msg="Step 07.02")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], parent_css="", msg="Step 07.03")
        chart_obj.verify_x_axis_title_in_run_window(['Sale Date Month'], parent_css="", msg="Step 07.04")
        chart_obj.verify_y_axis_title_in_run_window(['Revenue'], parent_css="", msg="Step 07.05")
        chart_obj.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css="", msg="Step 07.06")
        web_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(".bucket-label", "bucket_labels")
        label_list_elem = [i.text.strip() for i in web_elems]
        HomePage.Home._utils.as_List_equal(BUCKET_LABEL_LIST, label_list_elem, "Step 07.07 : Verify bucket list items")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.RunWindow.close()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

