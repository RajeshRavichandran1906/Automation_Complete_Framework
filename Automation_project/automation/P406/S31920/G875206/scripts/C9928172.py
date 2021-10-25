"""----------------------------------------------------
Author Name : Prabhakaran/Joyal
Automated on : 13 Jan 2020
----------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928172_TestClass(BaseTestCase):
    
    def test_C9928172(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)

        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as Admin User.
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
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9928172')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists('C9928172 Resources')
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04 Click on 'OTHER' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """Click on 'URL' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verification -Verify New URL dialog box opens
        Also, Verify Ok button is disabled
        """
        HomePage.ModalDailogs.URL.verify_title("New URL",'05.01')
        HomePage.ModalDailogs.URL.OKButton.verify_disabled('05.02')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Step 06 Enter title 'C9928172' and enter "www.ibi.com" in URL
        """
        HomePage.ModalDailogs.URL.Title.enter_text('C9928172')
        HomePage.ModalDailogs.URL.URL.enter_text("www.ibi.com")
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """Verify Ok button is Enabled
        """
        HomePage.ModalDailogs.URL.OKButton.verify_enabled('06.01')
        utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
        Click Ok button in New URL dialog box
        """
        HomePage.ModalDailogs.URL.OKButton.click()
        utils.capture_screenshot('07.00',STEP_07)
        
        
        STEP_07_01 = """ Verification - 
        Verify 'IBI URL' is displayed in content area
        """
        HomePage.Workspaces.ContentArea.verify_files(["C9928172"],'07.01')
        utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Right click on 'C9928172' > Edit
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928172')
        HomePage.ContextMenu.select('Edit')
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_08_01 = """
        Verify Edit URL dialog box opens
        Also, Verify Update button is disabled
        """
        HomePage.ModalDailogs.URL.verify_title("Edit URL",'08.01')
        HomePage.ModalDailogs.URL.UpdateButton.verify_disabled('08.02')
        utils.capture_screenshot('08.01',STEP_08_01,expected_image_verify=True)
        
        STEP_09 = """Change the title as 'C9928172_1'
        """
        HomePage.ModalDailogs.URL.Title.enter_text('C9928172_1')
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_09_01 = """
        Verify Update button is enabled
        """
        HomePage.ModalDailogs.URL.UpdateButton.verify_enabled('09.01')
        utils.capture_screenshot('09.01',STEP_09_01,expected_image_verify=True)
        
        STEP_10 = """Click 'Update' in Edit URL dialog box
        """
        HomePage.ModalDailogs.URL.UpdateButton.click()
        utils.capture_screenshot('10.00',STEP_10)
        
        STEP_10_01 ="""
        Verify that the title edited 'C9928172_1' is displayed in the Content area
        """
        HomePage.Workspaces.ContentArea.verify_files(["C9928172_1"],'10.01')
        utils.capture_screenshot('10.01',STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """Right click on 'C9928172_1' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file('C9928172_1')
        utils.capture_screenshot('11.00',STEP_11)
        
        STEP_12 = """
        Step 12  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('12.00',STEP_12)
        
if __name__ == "__main__":
    unittest.main()