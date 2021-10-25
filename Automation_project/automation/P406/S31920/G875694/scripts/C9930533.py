"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 14-August-2020
-------------------------------------------------------------------------------------------"""

import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930533_TestClass(BaseTestCase):
    
    def test_C9930533(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_path = os.path.join(os.getcwd(), "data", "car.xlsx")
        file_name = "car"
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'Workspaces' > My Workspace > Click on 'My Content' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace->My Content")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Other' category button > Click on 'Upload File' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ContentArea.delete_file_if_exists(file_name)
        HomePage.Workspaces.ActionBar.select_tab_option("Upload File")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Select an Excel file > CAR
        """
        FileDialog().open_file(file_path)
        HomePage.ModalDailogs.UploadCompleted.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Uploaded Excel File displays under Items folder displays a dialogue showing completion
        """
        HomePage.ModalDailogs.UploadCompleted.verify_messages(['car.xlsx Upload completed'], "05.01")
        HomePage.Workspaces.ContentArea.verify_files([file_name], "05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click X to close the 'Upload Completed' dialog
        """
        HomePage.ModalDailogs.UploadCompleted.close()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right-click on the uploaded file
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify right-click menu
        """
        context_menu = ['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(context_menu, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)