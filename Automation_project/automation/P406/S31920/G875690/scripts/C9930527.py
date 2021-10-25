"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 07-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930527_TestClass(BaseTestCase):
    
    def test_C9930527(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = "stoprequest"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Double click to run 'stoprequest.fex' under My Workspaces > My Content folder
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace->My Content")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, file_name, 50)
        HomePage.Workspaces.ContentArea.double_click_on_file(file_name)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click the 'Utilities' from the banner link
        """
        HomePage.Banner.click_utilities()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Select 'Stop Requests'
        """
        HomePage.ContextMenu.select('Stop Requests')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Stop Requests dialogue displays '1 requests(s) stopped':
        """
        HomePage.ModalDailogs.Alert.verify_message("1 request(s) stopped.", "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click OK to close the stop requests prompt
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following:
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        expected_server_msg = "Reporting Server Message Reporting server agent has been terminated by user or operator"
        actual_server_msg = self.driver.find_element_by_css_selector("body").text.strip().replace("\n", " ")
        HomePage.Home._utils.asequal(expected_server_msg, actual_server_msg, "Step 06.01 : Verify '{}' displayed".format(expected_server_msg))
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click 'X' to close the 'stoprequest' run window
        """
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)