"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 27 January 2020
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.webfocus.modal_dialog import ShareWithOthers

class C9928217_TestClass(BaseTestCase):
    
    def test_C9928217(self):
        
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
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
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
        
        STEP_05 = """
            STEP 05 : Click on the drop-down in the search box > Choose Users in the drop-down list.
        """
        ShareWithOther.SearchTextBox.click_dropdown_button()
        HomePage.ContextMenu.select('Users')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Enter 'autobasuser63' in the 'Enter user' search box > Click on 'autobasuser63' user > Click OK
        """
        ShareWithOther.SearchTextBox.enter_text("autobasuser63")
        ShareWithOther.UserGroupResults.wait_for_visible()
        ShareWithOther.UserGroupResults.select("autobasuser63")
        ShareWithOther.OKButton.click()
        utils.wait_for_page_loads(10)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on My Content folder from the resource tree> Right click on report1 > Select Share with... > Click on the drop-down in the search box > Choose Users in the drop-down list
        """
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Workspaces.ContentArea.right_click_on_file("report1")
        HomePage.ContextMenu.select("Share with...")
        ShareWithOther.wait_for_appear()
        utils.wait_for_page_loads(10)
        ShareWithOther.SearchTextBox.click_dropdown_button()
        HomePage.ContextMenu.select('Users')
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_8 = """
            STEP 08 : Enter 'autobasuser6' in the 'Enter user' search box
        """
        ShareWithOther.SearchTextBox.enter_text("autobasuser6")
        ShareWithOther.UserGroupResults.wait_for_visible()
        utils.capture_screenshot("08.00", STEP_8)
        
        STEP_08_01 = """
            STEP 08.01 : Verify the list of users containing with the word 'autobasuser6' are displayed and
            autobasuser63 (previously added 'autobasuser63' user is greyed out)
        """
        ShareWithOther.UserGroupResults.verify_description_contains_searched_text("autobasuser6", "08.01")
        ShareWithOther.UserGroupResults.verify_name_contains_searched_text("autobasuser6", "08.02")
        ShareWithOther.UserGroupResults.verify_disabled_results(['autobasuser63 autobasuser63'], "08.03")
        utils.capture_screenshot("08.01", STEP_08_01)
        
        STEP_09 = """
            STEP 09 : Click on 'autobasuser63' user
        """
        ShareWithOther.UserGroupResults.select("autobasuser63")
        utils.capture_screenshot("09.00", STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that unable to select 'autobasuser63' user
        """
        ShareWithOther.UserGroupResults.verify_disabled_results(['autobasuser63 autobasuser63'], "09.01")
        utils.capture_screenshot("09.01", STEP_09_01)
        
        STEP_10 = """
            STEP 10 : Click Cancel to close the Share with dialog box.
        """
        ShareWithOther.CancelButton.click()
        utils.wait_for_page_loads(10)
        utils.capture_screenshot("10.00", STEP_10)
        
        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("11.00", STEP_11)

if __name__ == '__main__':
    unittest.main()