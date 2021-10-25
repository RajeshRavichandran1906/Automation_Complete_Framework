"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 10 January 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.webfocus.modal_dialog import ShareWithOthers

class C9928209_TestClass(BaseTestCase):
    
    def test_C9928209(self):
        
        """
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        ShareWithOther = ShareWithOthers(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id  =  utils.parseinitfile('project_id')
        suite_id    =  utils.parseinitfile('suite_id')
        folder_path =  project_id + "_" + suite_id
        file_name   =  "report1"
        
        STEP_01 = """
            Step 01 : Sign in to WebFOCUS as Developer user
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Expand the 'Workspaces' from the tree and Click on 'P406_S31920'
        """
        HomePage.Workspaces.ResourcesTree.expand(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Click on My Content from the tree
        """
        HomePage.Workspaces.ResourcesTree.select("My Content")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify report1 appears in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files([file_name], "04.01")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on report1 and select Share with...
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Share with...')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Verify 'Share with Others' window appears with the following options:
            1.'Enter users and groups' search box is empty with the dropdown control,
            2.Cancel button is enabled by default and OK button is disabled,
            3.Share with everyone checkbox gets uncheck
        """
        ShareWithOther.wait_for_appear()
        ShareWithOther.verify_title("Share with Others", "05.01")
        ShareWithOther.SearchTextBox.verify_text('', "05.02")
        ShareWithOther.SearchTextBox.verify_dropdown_dsiplayed("05.03")
        ShareWithOther.CancelButton.verify_enabled("05.04")
        ShareWithOther.OKButton.verify_disabled("05.05")
        ShareWithOther.ShareWithEveryone.verify_unchecked("05.06")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Click Cancel button to close the Share with Others window
        """
        ShareWithOther.CancelButton.click()
        ShareWithOther.wait_for_diappear()
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)