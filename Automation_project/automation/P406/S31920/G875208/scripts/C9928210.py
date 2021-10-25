"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 16 January 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.webfocus.modal_dialog import ShareWithOthers

class C9928210_TestClass(BaseTestCase):
    
    def test_C9928210(self):
        
        """
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        ShareWithOther = ShareWithOthers(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        expected_menu =  ['Users', 'Groups', 'Users/Groups']
        project_id    =  utils.parseinitfile('project_id')
        suite_id      =  utils.parseinitfile('suite_id')
        folder_path   =  project_id + "_" + suite_id
        file_name     =  "report1"
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Developer user
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on 'P406_S31920'
        """
        HomePage.Workspaces.ResourcesTree.expand(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on My Content folder > Right-click on report1 > Select Share with...
        """
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Share with...')
        ShareWithOther.wait_for_appear()
        utils.wait_for_page_loads(10)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05.00 : Click on drop-down in the search box
        """
        ShareWithOther.SearchTextBox.click_dropdown_button()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify Users, Groups and Users/groups (By default checked) are appears
        """
        HomePage.ContextMenu.verify(expected_menu, "05.01")
        HomePage.ContextMenu.verify_selected_options([expected_menu[2]], "05.02")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            STEP 06.00 : Click on Users in the drop-down list.
        """
        HomePage.ContextMenu.select(expected_menu[0])
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify Users is checked, 'Enter users' appears in the search box and the drop-down lists still appear
        """
        HomePage.ContextMenu.verify(expected_menu, "06.01")
        HomePage.ContextMenu.verify_selected_options([expected_menu[0]], "06.02")
        ShareWithOther.SearchTextBox.verify_placeholder("Enter users", "06.03")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            STEP 07.00 : Click on Groups in the drop-down list
        """
        HomePage.ContextMenu.select(expected_menu[1])
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify Groups is checked, 'Enter groups' appears in the search box and the drop-down lists still appear
        """
        HomePage.ContextMenu.verify(expected_menu, "07.01")
        HomePage.ContextMenu.verify_selected_options([expected_menu[1]], "07.02")
        ShareWithOther.SearchTextBox.verify_placeholder("Enter groups", "07.03")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            STEP 08.00 : Click on Groups in the drop-down list
        """
        HomePage.ContextMenu.select(expected_menu[2])
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify Users/Groups is checked, 'Enter users/groups' appears in the search box and the drop-down lists still appear
        """
        HomePage.ContextMenu.verify(expected_menu, "08.01")
        HomePage.ContextMenu.verify_selected_options([expected_menu[2]], "08.02")
        ShareWithOther.SearchTextBox.verify_placeholder("Enter users and groups", "08.03")
        utils.capture_screenshot("08.01", STEP_08_01, expected_image_verify = True)
        
        STEP_09 = """
            STEP 09.00 : Click Cancel button to close the Share with Others window.
        """
        ShareWithOther.CancelButton.click()
        ShareWithOther.wait_for_diappear()
        utils.capture_screenshot("09.00", STEP_09)
        
        STEP_10 = """
            STEP 10.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("10.00", STEP_10)