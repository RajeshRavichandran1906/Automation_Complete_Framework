"""----------------------------------------------------
Author Name  : Robert
Automated on : 09-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.chart import Chart

class C9946217_TestClass(BaseTestCase):
    
    def test_C9946217(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context"
        setup_url = HomePage.Home._utils.get_setup_url()
        actual_setup_url = setup_url.replace("home8206", '')
        expected_url = actual_setup_url + 'portal/P406_S31920/~autoadmuser59/'+PORTAL_NAME
        
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5Portal_Context' > Select 'Edit'
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.ContextMenu.select("Edit")
        HomePage.ModalDailogs.V5Portal.wait_for_appear(10)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the 'Edit Portal' dialog box opened with the following options:
                Title as 'V5Portal_Context'
                Name as 'V5Portal_Context'
                Alias as empty
                Banner toggle button is on
                Show portal title in banner checkbox is checked
                Logo is disabled with the text Not Selected and Browse button is on the right of the logo
                Two level side navigation is selected
                Show top navigation in banner with a checkbox is disabled
                Maximum width text box is available and 100% is set by default
                Theme is "Designer 2018"
                URL as 'http://machinename:port/alias/portal/P406_S31920/G8751...' and it is read-only
                Save button is disabled and the Cancel button is enabled
        """
        HomePage.ModalDailogs.V5Portal.verify_title("Edit Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text(PORTAL_NAME, "04.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text(PORTAL_NAME, "04.03")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "04.04")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("04.05")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("04.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("04.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_placeholder("Not Selected", "04.08")
        HomePage.ModalDailogs.V5Portal.Logo.verify_browse_button_displayed("04.09")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(['Two-level side'], "04.10")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("04.11")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.12")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "04.13")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("04.14")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(expected_url, "04.15")
        HomePage.ModalDailogs.V5Portal.CancelButton.verify_enabled("04.16")
        HomePage.ModalDailogs.V5Portal.SaveButton.verify_disabled("04.17")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)

        
        STEP_04 = """
            STEP 04.00 : Click the 'Cancel' button.
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)

        STEP_05 = """
            STEP 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
