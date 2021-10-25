"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 03 February 2020
-----------------------------------------------------------------------------------------------"""
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928175_TestClass(BaseTestCase):
    
    def test_C9928175(self):
        
        """
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        case_id = "C9928175"
        portal_url = Login(self.driver).create_setup_url().replace("home8206", "") + "portal/Retail_Samples"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on 'APPLICATION' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Click on 'Portal' action bar
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(case_id)
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify New Portal dialog box is displayed
        """
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal", "05.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text('', "05.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text('', "05.03")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text('', "05.04")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("05.05")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("05.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_placeholder("Not Selected", "05.07")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(["Two-level side"], "05.08")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("05.09")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_unchecked("05.10")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "05.11")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "05.12")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(portal_url, "05.13")
        HomePage.ModalDailogs.V5Portal.CreateMyPagesMenu.verify_unchecked("05.14")
        utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Enter title 'C9928175' > Create
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(case_id)
        utils.capture_screenshot("06.00", STEP_06)
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.ModalDailogs.V5Portal.wait_for_diappear()
        utils.wait_for_page_loads(40, pause_time=2)
        
        STEP_06_01 = """
            STEP 06.01 : Verify 'C9928175' is displayed in content area
        """
        HomePage.Workspaces.ContentArea.verify_folders([case_id], "06.01")
        utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Right click on 'C9928175' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_folder(case_id)
        utils.wait_for_page_loads(20, pause_time=2)
        utils.capture_screenshot("07.00", STEP_07)
        
        TEP_07_01 = """
            STEP 07.01 : Verify 'C9928175' is not displayed in content area
        """
        HomePage.Workspaces.ContentArea.verify_folders([case_id], "06.01",  assert_type='asnotin')
        utils.capture_screenshot("07.01", TEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)