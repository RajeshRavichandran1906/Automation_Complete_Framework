"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 31 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9946063_TestClass(BaseTestCase):
    
    def test_C9946063(self):
        
        """
        TESTCASE OBJECTS
        """
        OldHomePage = Wf_Mainpage(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VAIABLES
        """
        portal_file = "Portal_admin2"
        car_file = "car2"
        summit_file = "Summit1"
        summit_url_file = "Summit_URL1"
        visual_upload_file = "Vis_after_Upload1"
        visual_exp_file = "Visualization Example - Shortcut1"
        
        STEP_01 = """
            STEP 01 : Sign in as gs_gradm1@ibi.com
        """
        HomePage.invoke_with_login('mridgradm','mridgradmpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify the following:
            1.WebFOCUS Homepage opens with Getting Started, Favorites and Portals sections.
            2.[+] area is not available
        """
        HomePage.Home.verify_sections(['GETTING STARTED', 'FAVORITES', 'PORTALS'], '01.01', assert_type='asin')
        plus_icon_visible = self.driver.find_element(*HomePage.Banner.locators.plus_icon).is_displayed()
        HomePage.Home._utils.asequal(False, plus_icon_visible, "Step 01.02 : Verify [+] area is not available")
        HomePage.Home._utils.capture_screenshot('01.01', STEP_01_01, True)
    
        STEP_02 = """
            STEP 02 : Click on Workspaces view > Click on 'Getting Started' workspace from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select('Getting Started')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, 'Admin2', 30)
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify that no category buttons are available (Application and Other)
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed('02.01')
        HomePage.Home._utils.capture_screenshot('02.01', STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Expand Getting Started > Click on 'Admin2' from the resource tree > Double click to run 'Portal_admin2'
        """
        HomePage.Workspaces.ResourcesTree.select('Getting Started->Admin2')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_file, 30)
        HomePage.Workspaces.ContentArea.double_click_on_file(portal_file)
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that 'Portal_admin2' cannot be run/viewed.
        """
        HomePage.Home._utils.verify_number_of_browser_windows(1, '03.01')
        HomePage.RunWindow.verify_not_displayed('03.02')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Double click to run 'car2'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(car_file)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that 'car2' cannot be run/viewed.
        """
        HomePage.RunWindow.verify_not_displayed('04.01')
        HomePage.Home._utils.verify_number_of_browser_windows(1, '04.02')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Double click to run 'Summit1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_file)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify that 'Summit1' cannot be run/viewed.
        """
        HomePage.RunWindow.verify_not_displayed('05.01')
        HomePage.Home._utils.verify_number_of_browser_windows(1, '05.02')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Double click to run 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify that 'Summit_URL1' cannot be run/viewed.
        """
        HomePage.RunWindow.verify_not_displayed('06.01')
        HomePage.Home._utils.verify_number_of_browser_windows(1, '06.02')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
    
        STEP_07 = """
            STEP 07 : Double click to run 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that 'Vis_after_Upload1' cannot be run/viewed.
        """
        HomePage.RunWindow.verify_not_displayed('07.01')
        HomePage.Home._utils.verify_number_of_browser_windows(1, '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Double click to run 'Visualization Example - Shortcut1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that 'Visualization Example- Shortcut1' cannot be run/viewed.
        """
        HomePage.RunWindow.verify_not_displayed('08.01')
        HomePage.Home._utils.verify_number_of_browser_windows(1, '08.02')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Right-click on 'Portal_admin2' > Select 'Properties'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_file)
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 09.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Click on 'car2'
        """
        HomePage.Workspaces.ContentArea.select_file(car_file)
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 10.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : Click on 'Summit1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_file)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 11.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Click on 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 12.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'")
        HomePage.Home._utils.capture_screenshot('12.01', STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : Click on 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 13.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot('13.01', STEP_13_01, True)
        
        STEP_14 = """
            STEP 14 : Click on 'Visualization Example - Shortcut1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_14_01 = """
            STEP 24.01 : Verify Properties dialog opens for ''Visualization Example - Shortcut1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 14.01 : Verify Properties dialog opens for ''Visualization Example - Shortcut1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('14.01', STEP_14_01, True)
        
        STEP_15 = """
            STEP 15 : Click 'Cancel' to close the properties dialog
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)
        
        STEP_16 = """
            STEP 16 : Click on Settings icon (top right options)
        """
        HomePage.Banner.click_settings()
        HomePage.Home._utils.capture_screenshot('16.00', STEP_16)
        
        STEP_16_01 = """
            STEP 26.01 : Verify the following options
            1.Security Center
            2.Manage Private Resources
            3.Normal view (By default checked)
            4.Administration view
        """
        settings_context = ['Security Center', 'Manage Private Resources', 'Normal view', 'Administration view']
        HomePage.ContextMenu.verify(settings_context, "16.01")
        HomePage.ContextMenu.verify_selected_options(['Normal view'], '16.02')
        HomePage.Home._utils.capture_screenshot('16.01', STEP_16_01, True)
        
        STEP_17 = """
            STEP 17 : Click Security Center
        """
        tab_css = "#dlgSecurityManager .bi-tab-button"
        HomePage.ContextMenu.select('Security Center')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(tab_css, 'Users ', 60)
        HomePage.Home._utils.capture_screenshot('17.00', STEP_17)

        STEP_17_01 = """
            STEP 17.01 : Verify Security Center window visible.
        """
        tab_name = self.driver.find_element_by_css_selector(tab_css).text.strip()
        HomePage.Home._utils.asequal('Users & Groups', tab_name, "Step 17.01 : Verify Security Center window visible")
        HomePage.Home._utils.capture_screenshot('17.01', STEP_17_01, True)
        
        STEP_18 = """
            STEP 18 : Close the Security Center window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('18.00', STEP_18)
        
        STEP_19 = """
            STEP 19 : Click on 'Help' (?)
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot('19.00', STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify the following options:
            1.WebFOCUS Online Help
            2.Technical Resources
            3.Community
            4.About WebFOCUS
            5.License
            6.Information Builders Home
        """
        help_context = ['WebFOCUS Online Help', 'Technical Resources', 'Community', 'About WebFOCUS', 'License', 'TIBCO Software Inc.']
        HomePage.ContextMenu.verify(help_context, "19.01")
        HomePage.Home._utils.capture_screenshot('19.01', STEP_19_01, True)
        
        STEP_20 = """
            STEP 20 : Click on the 'User name' (Getting Started Group Admin user1) > Select 'Change Password'
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('20.00', STEP_20)
        
        STEP_21 = """
            STEP 21 : Enter new Password twice: Password1, click Change Password button
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot('21.00', STEP_21)
        
        STEP_21_01 = """
            STEP 21.01 : Verify 'Your password has been changed'prompt gets displayed with a transparent green color background
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '21.01')
#         HomePage.NotifyPopup.verify_background_color('21.02')commenting this function because NotifyPopup disappear soon but this call is tested in the previous test case
        HomePage.NotifyPopup.verify_transparent('21.03')
        HomePage.Home._utils.capture_screenshot('21.01', STEP_21_01, True)
        
        STEP_22 = """
            STEP 22 : Click on 'Invite User'
        """
        HomePage.Banner.click_invite_user()
        HomePage.ModalDailogs.InviteUser.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('22.00', STEP_22)
        
        STEP_23 = """
            STEP 23 : Enter any name and a valid email > Click Invite
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text("WebFOCUS")
        HomePage.ModalDailogs.InviteUser.LastName.enter_text("IBI")
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text("c9946063autotest@ibi.com")
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot('23.00', STEP_23)
        
        STEP_23_01 = """
            STEP 23.01 : Verify that 'Invite successfully sent' message displayed
        """
        HomePage.ModalDailogs.InviteUser.ErrorMessage.verify_text('Invite successfully sent.', '23.01')
        HomePage.Home._utils.capture_screenshot('23.01', STEP_23_01, True)
        
        STEP_24 = """
            STEP 24 : Click 'Cancel' to close the 'Invite User' dialog
        """
        HomePage.ModalDailogs.InviteUser.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('24.00', STEP_24)
        
        STEP_25 = """
            STEP 25 : Signout WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('25.00', STEP_25)