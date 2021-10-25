"""-------------------------------------------------------------------------------------------
Author Name : Niranjan
Automated On : 28 January 2020
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.webfocus.modal_dialog import ShareWithOthers

class C9928218_TestClass(BaseTestCase):
    
    def test_C9928218(self):
        
        """
            TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        utils     =  UtillityMethods(self.driver)
        ShareWithOther = ShareWithOthers(self.driver)
                
        """
            TESTCASE VARIABLES
        """
        project_id    =  utils.parseinitfile('project_id')
        suite_id      =  utils.parseinitfile('suite_id')
        folder_path   =  project_id + "_" + suite_id

        
        STEP_01 = """  
            STEP 01 : Sign in to WebFOCUS as Developer user
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)    
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and click on 'P406_S31920'
        """
        HomePage.Workspaces.ResourcesTree.expand(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on My Content folder from the resource tree> Right click on report1 > Select Share with...
        """
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Workspaces.ContentArea.right_click_on_file("report1")
        HomePage.ContextMenu.select("Share with...")
        ShareWithOther.wait_for_appear()
        utils.wait_for_page_loads(10)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 ="""
        Verification - Verify 'Share with Others' dialog opens with the following options:
            1.X button is displays at the top right corner of the dialog box
            2.Enter users and groups' search box with the dropdown control is empty
            3.Under shared with it shows 'autobasuser63' and 'autoadvuser59' user
            4.Share with everyone checkbox gets unchecked
            5.Cancel button is enabled
            6.OK button is disabled
        """
        ShareWithOther.SharedWith.verify_remove_icon('04.01')
        ShareWithOther.SearchTextBox.verify_text('', '04.02')
        ShareWithOther.SharedWith.verify_users(['autoadvuser59 autoadvuser59(auto@devmail.com)', 'autobasuser63 autobasuser63'], '04.03')
        ShareWithOther.ShareWithEveryone.verify_unchecked('04.04')
        ShareWithOther.CancelButton.verify_enabled('04.05')
        ShareWithOther.OKButton.verify_disabled('04.06')
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click X button under Shared with 'autobasuser63' textbox to unshare the already shared 'autobasuser63' user > Click OK.
        """
        ShareWithOther.SharedWith.remove('autobasuser63')
        ShareWithOther.OKButton.click()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 ="""
        Verification - Verify 'Share with Others' window gets closed
        """
        ShareWithOther.wait_for_diappear()
        utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == '__main__':
    unittest.main()