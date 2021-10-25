"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 03 March 2020
-----------------------------------------------------------------------------------------------"""
import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928178_TestClass(BaseTestCase):
    
    def test_C9928178(self):
        
        """
        TESTCASE OBJECTS
        """
        OpenDialog  =  FileDialog()
        HomePage    =  ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        zip_file = 'Home_Thumbnail'
        zip_file_path = os.path.join(os.getcwd(), 'data', zip_file + '.zip')
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Developer User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view.
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on 'P406_S31920' > 'G875206' folder in resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G875206')
        HomePage.Workspaces.ContentArea.delete_file_if_exists(zip_file)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click 'OTHER' category button and Click on 'Upload File' action bar.
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        HomePage.Workspaces.ActionBar.select_tab_option('Upload File')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Select the "Home_Thumbnail.zip" file from the attachment and click on the 'Open' button.
        """
        OpenDialog.open_file(zip_file_path)
        HomePage.Home._utils.wait_for_page_loads(60, pause_time=2)
        HomePage.ModalDailogs.UploadCompleted.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify "Upload completed" message displays as below.
        """
        HomePage.ModalDailogs.UploadCompleted.verify_messages(['Home_Thumbnail.zip Upload completed'], '05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click "X" in the message displayed.
        """
        HomePage.ModalDailogs.UploadCompleted.close()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify "Home_Thumbnail.zip" file appears in content area.
        """
        HomePage.Workspaces.ContentArea.verify_files([zip_file], '06.01')
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)