"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 07 July 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927918_TestClass(BaseTestCase):
    
    def test_C9927918(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        setup_url = utils.get_setup_url()
        actual_setup_url = setup_url.replace("home8206", '')
        expected_url = actual_setup_url + 'portal/P406_S31920/G875179/V5_Context_Menu_Testing'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_04 = """
            STEP 03 : Expand 'P406_S31920' workspace > 'G875179' folder in the resource tree.
            STEP 04 : Right-click on 'V5 Context Menu Testing' from the resource tree > Select 'Edit'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875179->V5 Context Menu Testing")
        HomePage.ContextMenu.select("Edit")
        HomePage.ModalDailogs.V5Portal.wait_for_appear(10)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verification-
            1. Title as 'V5 Context Menu Testing'
            2. Name as 'V5_Context_Menu_Testing'
            3. Alias as empty
            4. Banner toggle button is on
            5. Show portal title in banner checkbox is checked
            6. Logo is enabled with the text Not Selected and Browse button is on the right of the logo
            7. Two level side navigation is selected
            8. Show top navigation in banner with a checkbox is disabled
            9. Maximum width text box is available and 100% is set by default
            10. Theme is "Designer 2018" 
            11. URL as 'http://machinename:port/alias/portal/P406_S31920/G8751...' and it is read-only
            12. Save button is disabled and the Cancel button is enabled
        """
        HomePage.ModalDailogs.V5Portal.Title.verify_text("V5 Context Menu Testing", "04.01")
        HomePage.ModalDailogs.V5Portal.Name.verify_text("V5_Context_Menu_Testing", "04.02")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "04.03")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.04")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("04.05")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("04.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_placeholder("Not Selected", "04.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_browse_button_displayed("04.08")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(['Two-level side'], "04.09")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("04.10")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.11")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "04.12")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("04.13")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(expected_url, "04.14")
        HomePage.ModalDailogs.V5Portal.CancelButton.verify_enabled("04.15")
        HomePage.ModalDailogs.V5Portal.SaveButton.verify_disabled("04.16")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            STEP 05 : Click the 'Cancel' button.
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == "__main__":
    unittest.main() 