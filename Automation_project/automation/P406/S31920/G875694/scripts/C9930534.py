"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 12-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930534_TestClass(BaseTestCase):
    
    def test_C9930534(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        url_name = "ibi website"
        url = "https://www.informationbuilders.com/"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand Workspaces>My Workspace>My Content from the Tree
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace->My Content")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : From the Action Bar, click on Other tab>URL
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        HomePage.Workspaces.ContentArea.delete_file_if_exists(url_name)
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.ModalDailogs.URL.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify New URL dialogue comes up
        """
        HomePage.ModalDailogs.URL.verify_title("New URL", "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Give it a 'Title' and 'URL'
            Ex: ibi website - https://www.informationbuilders.com/
        """
        HomePage.ModalDailogs.URL.Title.enter_text(url_name)
        HomePage.ModalDailogs.URL.URL.enter_text(url)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click 'OK'
        """
        HomePage.ModalDailogs.URL.OKButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, url_name, 60)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify URL has been created
        """
        HomePage.Workspaces.ContentArea.verify_files([url_name], "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right-click on the 'URL'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(url_name)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify right-click menu
        """
        url_context_menu = ['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(url_context_menu, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Select 'View in new window' option
        """
        HomePage.ContextMenu.select("View in new window")
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify ibi website launched with the below URL,
            https://www.ibi.com/ and Tab title as 'Data and Analytics Company    
        """
        HomePage.Home._utils.asequal("https://www.ibi.com/", self.driver.current_url, "Step 08.01 : Verify ibi website can be launched")
        HomePage.Home._utils.asin("Data and Analytics Company", self.driver.title, "Step 08.02 : Verify ibi website can be launched with tab title as 'Data and Analytics Company")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Close the window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)