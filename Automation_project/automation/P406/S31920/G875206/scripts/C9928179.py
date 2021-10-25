"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 02-November-2020
-------------------------------------------------------------------------------------------"""

import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928179_TestClass(BaseTestCase):
    
    def test_C9928179(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = "ImageObject"
        file_path = os.path.join(os.getcwd(), "data", "ImageObject.ely")
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Developer User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on 'P406_S31920' > 'G875206' folder in resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875206")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click 'OTHER' category button and Click on 'Upload File' action bar.
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ContentArea.delete_file_if_exists(file_name)
        HomePage.Workspaces.ActionBar.select_tab_option("Upload File")
        HomePage.Home._utils.wait_for_page_loads(10, pause_time=5)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Select 'ImageObject.ely' file from the attachment and Click on 'Open' button.
        """
        FileDialog().open_file(file_path)
        HomePage.ModalDailogs.UploadCompleted.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 'Upload completed' message displays as below.
        """
        HomePage.ModalDailogs.UploadCompleted.verify_messages(['ImageObject.ely Upload completed'], "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click 'X' in the message displayed
        """
        HomePage.ModalDailogs.UploadCompleted.close()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify 'ImageObject.ely' file appears in content area
        """
        HomePage.Workspaces.ContentArea.verify_files([file_name], "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)