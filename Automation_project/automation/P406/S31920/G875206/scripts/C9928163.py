"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 01-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.webfocus.modal_dialog import Common as ModalDialog

class C9928163_TestClass(BaseTestCase):
    
    def test_C9928163(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = "C9928163"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_file_if_exists(file_name)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on '+' menu button on top toolbar > Select 'Assemble Visualizations'
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualizations")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify New Page dialog box opens
        """
        ModalDialog(self.driver, "Template dialog").verify_title("Choose Template", "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Select 'Blank' template
        """
        blank_object = self.driver.find_element_by_css_selector(".pop-top [title='Blank']")
        HomePage.Home._core_utils.left_click(blank_object)
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.synchronize_with_visble_text("div.pd-page-title", "Page", 30)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the canvas shows Blank template
        """
        blank_convas = self.driver.find_element_by_css_selector("div.pd-page-section-grid").is_displayed()
        HomePage.Home._utils.asequal(True, blank_convas, "Step 05.01 : Verify the canvas shows Blank template")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on Application menu > Save > enter title 'C9928163' > Save
        """
        application_menu_css = "div[title='WebFOCUS Designer Menu']"
        application_menu = self.driver.find_element_by_css_selector(application_menu_css)
        HomePage.Home._core_utils.left_click(application_menu)
        HomePage.ContextMenu.select("Save")
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.ModalDailogs.Resources.Title.enter_text(file_name)
        HomePage.ModalDailogs.Resources.SaveButton.click()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on Application menu > Close
        """
        application_menu = self.driver.find_element_by_css_selector(application_menu_css)
        HomePage.Home._core_utils.left_click(application_menu)
        HomePage.ContextMenu.select("Close")
        HomePage.Home._core_utils.switch_to_previous_window(False)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the created 'C9928163' is displayed in content area
            Also, Verify the correct thumbnail appears
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files([file_name], "07.01")
        file = HomePage.Workspaces.ContentArea._get_file_object_(file_name).find_element_by_css_selector("img[src$='pgx.svg ']")
        HomePage.Home._utils.asequal(True, file.is_displayed(), "Step 07.02 : Verify thumbnail appears")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
        
        STEP_08 = """
            STEP 08 : Right Click on 'C9928163' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file(file_name)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify the created 'C9928163' is not displayed in content area
        """
        HomePage.Workspaces.ContentArea.verify_files([file_name], "08.01", "asnotin")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)