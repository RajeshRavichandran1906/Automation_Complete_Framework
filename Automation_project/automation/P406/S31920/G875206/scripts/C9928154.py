"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 27 Dec 2019
----------------------------------------------------"""
import time

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage

    
class C9928154_TestClass(BaseTestCase):
    
    def test_C9928154(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
    
        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00',STEP_01)

        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists('C9928154_0')
        "Delete if create folder already exixts,added to remove rerun confilicts issue"
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04 Click on 'OTHER' category button and Click on 'Folder' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_04_01 = """ Verification
        Verify that the 'New Folder' prompt is displayed
        """
        HomePage.ModalDailogs.Folder.verify_title('New Folder','04.01')
        utils.capture_screenshot('04.01',STEP_04_01)
        
        STEP_05 = """
        Step 05 Enter Title 'C9928154_0'
        """
        
        HomePage.ModalDailogs.Folder.Title.enter_text('C9928154_0')
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verification -Verify the Name will be inherited from the title
        """
        HomePage.ModalDailogs.Folder.Name.verify_text("C9928154_0",'05.01')
        utils.capture_screenshot('05.01',STEP_05_01)
        
        STEP_05_02 = """Verification -Also, Verify 'OK' button got enable after title is being entered
        """
        HomePage.ModalDailogs.Folder.OKButton.verify_enabled('05.02')
        utils.capture_screenshot('05.02',STEP_05_02)
        
        STEP_06 = """
        Step 06 Click on 'Ok' button in new folder prompt
        """
        HomePage.ModalDailogs.Folder.OKButton.click()
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        Verify that the 'C9928154_0' is displayed in Content area
        """
        HomePage.Workspaces.ContentArea.verify_folders(["C9928154_0"],'06.01')
        utils.capture_screenshot('06.01',STEP_06_01)
        
        STEP_07 = """
        Right Click on the 'C9928154_0' > Delete > yes in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_folder('C9928154_0')
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
        Verify that the 'C9928154_0' is not displayed in Content area
        """
        HomePage.Workspaces.ContentArea.verify_folders(["C9928154_0"], '07.01', assert_type='asnotin')
        utils.capture_screenshot('07.01',STEP_07_01)
        
        
        STEP_08 = """
        Step 08  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00',STEP_08)