"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 31 Mach 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927932_TestClass(BaseTestCase):
    
    def test_C9927932(self):
        
        """
            TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
            TESTCASE CSS
        """
        setup_url = HomePage.Home._utils.get_setup_url()
        actual_setup_url = setup_url.replace("home8206", '')
        expected_url = actual_setup_url + 'portal/P406_S31920/G875179/V5_Context_Menu_Testing'
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : From WebFOCUS Home tab, Under 'PORTALS' section carousel >Click 'VIEW ALL' button
        """
        HomePage.Home.Portals.click_view_all()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
            
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5 Context Menu Testing' > Edit
        """
        HomePage.Home.ViewAll.right_click_on_item("V5 Context Menu Testing", index=2)
        HomePage.ContextMenu.select("Edit")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify the 'Edit Portal' dialog box opened with the following options:
            1.Title as 'V5 Context Menu Testing'
            2.Name as 'V5_Context_Menu_Testing'
            3.Alias as empty
            4.Banner toggle button is on
            5.Show portal title in banner checkbox is checked
            6.Logo is disabled with the text Not Selected and Browse button is on the right of the logo
            7.Two level side navigation is selected
            8.Show top navigation in banner with a checkbox is disabled
            9.Maximum width text box is available and 100% is set by default
            10.Theme is "Designer 2018"
            11.URL as 'http://machinename:port/alias/portal/P406_S31920/G8751...' and it is disabled
            12.Save button is disabled and the Cancel button is enabled
        """
        HomePage.ModalDailogs.V5Portal.verify_title("Edit Portal", "03.01")
        HomePage.ModalDailogs.V5Portal.Title.verify_text("V5 Context Menu Testing", "03.02")
        HomePage.ModalDailogs.V5Portal.Name.verify_text("V5_Context_Menu_Testing", "03.03")
        HomePage.ModalDailogs.V5Portal.Alias.verify_text("", "03.04")
        HomePage.ModalDailogs.V5Portal.Banner.verify_on("03.05")
        HomePage.ModalDailogs.V5Portal.ShowPortalTitle.verify_checked("03.06")
        HomePage.ModalDailogs.V5Portal.Logo.verify_enabled("03.07")
        HomePage.ModalDailogs.V5Portal.Logo.verify_placeholder("Not Selected", "03.08")
        HomePage.ModalDailogs.V5Portal.Logo.verify_browse_button_displayed("03.09")
        HomePage.ModalDailogs.V5Portal.Navigation.verify_selected_navigation(['Two-level side'], "03.10")
        HomePage.ModalDailogs.V5Portal.ShowTopNavigation.verify_disabled("03.11")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "03.12")
        HomePage.ModalDailogs.V5Portal.Theme.verify_text("Designer 2018", "03.13")
        HomePage.ModalDailogs.V5Portal.URL.verify_read_only("03.14")
        HomePage.ModalDailogs.V5Portal.URL.verify_text(expected_url, "03.15")
        HomePage.ModalDailogs.V5Portal.CancelButton.verify_enabled("03.16")
        HomePage.ModalDailogs.V5Portal.SaveButton.verify_disabled("03.17")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            STEP 04.00 : Click the 'Cancel' button.
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        
        STEP_05 = """
            STEP 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_05)