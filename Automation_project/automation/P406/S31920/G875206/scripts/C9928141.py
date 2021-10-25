"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 26 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928141_TestClass(BaseTestCase):
    
    def test_C9928141(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        document = Document(self.driver)
        core_utils = CoreUtillityMethods(self.driver)

        """
            TESTCASE VARIABLES
        """
        cancel_button_css = "#IbfsOpenFileDialog7_btnCancel"
        master_dialog_css = "#dlgIbfsOpenFile7"
        document_css = "#iaCanvasContainer"
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Click on 'INFOASSIST' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Click on 'Document' action bar under 'INFOASSIST' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Document")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify the Master File Dialog is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        document.switch_to_new_window()
        document.wait_for_visible_text(cancel_button_css, "Cancel", time_out = 150)
        utils.verify_object_visible(master_dialog_css, True, "Step 05.01 : Verify the Master File Dialog is displayed")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Select 'wf_retail_lite.mas' > open
        """
        utils.select_masterfile_in_open_dialog("baseapp", "wf_retail_lite")
        utils.synchronize_with_visble_text(document_css, "Document", 120)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify IA Document is open
        """
        utils.verify_object_visible("#iaCanvasCaptionLabel", True, "Step 06.01 : Verify IA Document is open")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Click on IA Globe > Exit
        """
        document.select_ia_application_menu("exit")
        core_utils.switch_to_previous_window(window_close = False)
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)
        
if __name__ == "__main__":
    unittest.main() 