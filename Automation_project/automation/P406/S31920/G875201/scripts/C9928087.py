"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 27 January 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.webfocus.modal_dialog import ShareWithOthers
from common.wftools.designer_portal import Two_Level_Side
from common.wftools.paris_home_page import ParisHomePage
from common.locators.portal_designer import Vfive_Designer


class C9928087_TestClass(BaseTestCase):
    
    def test_C9928087(self):
        
        """"
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        ShareWithOther = ShareWithOthers(self.driver)
        two_level_portal = Two_Level_Side(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id    =  utils.parseinitfile('project_id')
        suite_id      =  utils.parseinitfile('suite_id')
        group_id    =  utils.parseinitfile('group_id')
        folder_path =  project_id + "_" + suite_id+'->'+group_id
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Navigate to 'P406_S31920' workspace > Double click on 'G875201' folder
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Right click on 'V5_Sharing' from the content area > Select Run
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder('V5_Sharing')
        HomePage.ContextMenu.select('Run')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(Vfive_Designer.page_header_css, 'Page', 120)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Click on 'Share' button from the personal page toolbar
        """
        two_level_portal.click_on_page_header_button('Stop sharing')
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06.00 : Click on the drop-down in the search box > Select 'Users' in the drop-down list
        """
        ShareWithOther.wait_for_appear()
        ShareWithOther.SearchTextBox.click_dropdown_button()
        HomePage.ContextMenu.select('Users')
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
        Step 07.0 : Enter 'auto' in the 'Enter users' search box 
        """
        ShareWithOther.SearchTextBox.enter_text("auto")
        utils.wait_for_page_loads(40)
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
        Step 07.01 : Verify the list of users containing with a word 'auto' are displayed as follows:
        autobasuser63 (previously added 'autobasuser63' user is greyed out)
        """
        ShareWithOther.UserGroupResults.verify_disabled_results(["autobasuser63 autobasuser63"],'07.01')
        ShareWithOther.UserGroupResults.verify_description_contains_searched_text("auto",'07.02')
        utils.capture_screenshot("07.01", STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """Click on 'autobasuser63' user
        Step 08 :
        """
        ShareWithOther.UserGroupResults.select("autobasuser63")
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """Verify that unable to select 'autobasuser63' user
        """
        ShareWithOther.UserGroupResults.verify_disabled_results(["autobasuser63 autobasuser63"],'08.01')
        utils.capture_screenshot("08.01", STEP_08_01,expected_image_verify=True)
        
        STEP_09 = """Click 'Cancel' to close the Share with dialog box
        Step 09 :
        """
        ShareWithOther.CancelButton.click()
        utils.capture_screenshot("09.00", STEP_09)
        
        
        STEP_10 = """
           STEP 10.00 : Close the portal run window
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot("10.00", STEP_10)
        
        STEP_11 = """
            STEP 11.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("11.00", STEP_11)