"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 21-September-2020
-------------------------------------------------------------------------------------------"""
import pyautogui, time
from common.wftools.page_designer import Design
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.color import Color
from common.wftools.paris_home_page import ParisHomePage
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous

class C9927396_TestClass(BaseTestCase):
    
    def test_C9927396(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Page = Design(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        choose_template_css = ".df-template-picker.pop-top .ibx-dialog-title-box"
        grid_2_1_css = ".pop-top div[title='Grid 2-1']"
        node_xpath = "//div[normalize-space()='{0}'][contains(@class, 'tnode-label')]"
        
        STEP_01 = """
            STEP 01 : Login WebFOCUS as developer user.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces.
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P452_S31923' domain and Click on 'G784935' folder.
        """
        HomePage.Workspaces.ResourcesTree.select("P452_S31923->G784935")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on '+' button and Select 'Assemble Visualizations'.
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualizations")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(choose_template_css, "Template", 40)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Try to move the 'Choose Template' dialog.
        """
        template_diaglog = self.driver.find_element_by_css_selector(choose_template_css)
        template_dialog_location = template_diaglog.location
        dialog_loc = HomePage.Home._core_utils.get_web_element_coordinate(template_diaglog)
        HomePage.Home._core_utils.drag_and_drop(dialog_loc['x'], dialog_loc['y'], dialog_loc['x'] + 150, dialog_loc['y'])
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=2)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that you can't move the dialog.
        """
        HomePage.Home._utils.asequal(template_dialog_location,  template_diaglog.location, "Step 05.01 : Verify that you can't move the dialog.")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Choose the 'Grid 2-1' template.
        """
        grid_2_1_object = self.driver.find_element_by_css_selector(grid_2_1_css)
        HomePage.Home._core_utils.left_click(grid_2_1_object)
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=4)
        HomePage.Home._utils.synchronize_with_visble_text("div.pd-page-canvas", "Panel 1", 30)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the page canvas.
        """
        panels = ['Panel 1', 'Panel 2', 'Panel 3']
        Page.verify_containers_title(panels, "Step 06.01 : Verify the page canvas")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        selected_node_css = "div.tnode-label.ibx-sm-selected"
        for _ in range(2):
            selected_node = self.driver.find_element_by_css_selector(selected_node_css)
            HomePage.Home._core_utils.left_click(selected_node)
            HomePage.Home._utils.wait_for_page_loads(30, pause_time=2)
        for node in ["Retail Samples", "Portal", "Test Widgets"]:
            node = self.driver.find_element_by_xpath(node_xpath.format(node))
            HomePage.Home._core_utils.left_click(node)
            HomePage.Home._utils.wait_for_page_loads(30, pause_time=2)
            
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Drag and drop 'Blue' to Panel 1.
        """
        self.drag_content_item_to_container_and_verify_drop_color("Blue", "Panel 1", "08.01")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Drag and drop 'Gray' to Panel 2.
        """
        self.drag_content_item_to_container_and_verify_drop_color("Gray", "Panel 2", "09.01")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Drag and drop 'Green' to Panel 3.
        """
        self.drag_content_item_to_container_and_verify_drop_color("Green", "Panel 3", "10.01")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify As you drag you should see a blue rectangle and it shows where you can drop the item.
            Verify content added into the Grid 2-1 template.
        """
        panels = ['Blue', 'Gray', 'Green']
        Page.verify_containers_title(panels, "Step 06.01 : Verify the page canvas")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click the 'Webfocus Designer' dropdown in Toolbar and Click 'Close'.
        """
        application_btn = self.driver.find_element_by_css_selector("div.ds-logo")
        HomePage.Home._core_utils.left_click(application_btn)
        HomePage.ContextMenu.select("Close Designer")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click 'No' button.
        """
        no_btn_css = "div.pd-warning-dirty-no"
        HomePage.Home._utils.synchronize_with_visble_text(no_btn_css, "No", 20)
        no_btn = self.driver.find_element_by_css_selector(no_btn_css)
        HomePage.Home._core_utils.left_click(no_btn)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Home._core_utils.switch_to_previous_window(False)
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

    
    def drag_content_item_to_container_and_verify_drop_color(self, content_item, container_title, step_num):
        """
        Description : Drag content item and drop to canvas container and verify drop background color
        :Usage - drag_content_item_to_container_and_verify_drop_color("report", "Panel1", "02.02")
        """
        HomePage = ParisHomePage(self.driver)
        node_xpath = "//div[normalize-space()='{0}'][contains(@class, 'tnode-label')]"
        content_obj = self.driver.find_element_by_xpath(node_xpath.format(content_item))
        container_obj = PageDesignerMiscelaneous(self.driver).get_pd_container_object(container_title)
        source_location = HomePage.Home._core_utils.get_web_element_coordinate(content_obj)
        target_location = HomePage.Home._core_utils.get_web_element_coordinate(container_obj)
        HomePage.Home._core_utils.left_click(content_obj)
        time.sleep(1)
        pyautogui.mouseDown(source_location['x'], source_location['y'], duration=1)
        pyautogui.moveTo(target_location['x'], target_location['y'], duration=1)
        time.sleep(1)
        drop_target_highlighted_obj = HomePage.Home._utils.validate_and_get_webdriver_object(".pd-container-drop", "Drop background", container_obj)
        actual_color = Color.from_string(drop_target_highlighted_obj.value_of_css_property('background-color')).rgba if drop_target_highlighted_obj.is_displayed() else ""
        expected_color = "rgba(41, 182, 246, 1)"
        msg = "Step {0} : Verify '{1}' color shows while drop content in {2} container".format(step_num, expected_color, container_title)
        HomePage.Home._utils.asequal(expected_color, actual_color, msg)
        pyautogui.mouseUp(target_location['x'], target_location['y'])