"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 30 July 2020
-----------------------------------------------------------------------------------------------"""
from common.wftools.page_designer import Run
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_portal import Banner
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9946064_TestClass(BaseTestCase):
    
    def test_C9946064(self):
        
        """
        TESTCASE OBJECTS
        """
        OldHomePage = Wf_Mainpage(self.driver)
        HomePage = ParisHomePage(self.driver)
        PortalBanner = Banner(self.driver)
        PageDesigner = Run(self.driver)
        
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
            STEP 01 : Sign in as gs_bas1@ibi.com
        """
        HomePage.invoke_with_login('mridbas','mridbaspass')
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
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that 'Portal_admin2' run without any error
        """
        PortalBanner.verify_portal_top_banner_title(portal_file, 'Step 03.01 : Verify that "Portal_admin2" run without any error')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Close 'Portal_admin2' run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05 : Double click to run 'car2'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(car_file)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify that 'car2' run without any error
        """
        HomePage.RunWindow.verify_title(car_file, '05.01')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click 'X' to close 'car2' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : Double click to run 'Summit1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_file)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that 'Summit1' run without any error
        """
        HomePage.RunWindow.verify_title(summit_file, '07.01')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Click 'X' to close 'Summit1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_09 = """
            STEP 09 : Double click to run 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that 'Summit_URL1' run without any error
        """
        btn_css = "a[title^='Register']"
        HomePage.RunWindow.verify_title(summit_url_file, '09.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(btn_css, 'Register', 60)
        btn_text = self.driver.find_element_by_css_selector(btn_css).text.strip()
        HomePage.Home._utils.asequal('Register Now', btn_text, 'Step 09.02 : Verify that "Summit_URL1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Click 'X' to close 'Summit_URL1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_11 = """
            STEP 11 : Double click to run 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify that 'Vis_after_Upload1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_upload_file, '11.01')
        HomePage.Home._utils.capture_screenshot('11.01', STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Click 'X' to close 'Vis_after_Upload1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_13 = """
            STEP 13 : Double click to run 'Visualization Example - Shortcut1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Verify that 'Visualization Example - Shortcut11' run without any error
        """
        pd_css = ".pd-page-content-wrapper"
        containers = ['Outlier Analysis', 'Store Rankings', 'Revenue by Category', 'Profitability Analysis']
        HomePage.RunWindow.verify_title(visual_exp_file, '13.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 13.02 : Verify that "Visualization Example - Shortcut1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('13.01', STEP_13_01, True)
        
        STEP_14 = """
            STEP 14 : Click 'X' to close 'Visualization Example - Shortcut1' run window
        """
        HomePage.RunWindow.close() 
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_15 = """
            STEP 15 : Right-click on 'Portal_admin2' > Select 'Properties'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_file)
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)
        
        STEP_15_01 = """
            STEP 15.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 15.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('15.01', STEP_15_01, True)
        
        STEP_16 = """
            STEP 16 : Click on 'car2'
        """
        HomePage.Workspaces.ContentArea.select_file(car_file)
        HomePage.Home._utils.capture_screenshot('16.00', STEP_16)
        
        STEP_16_01 = """
            STEP 21.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 16.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot('16.01', STEP_16_01, True)
        
        STEP_17 = """
            STEP 17 : Click on 'Summit1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_file)
        HomePage.Home._utils.capture_screenshot('17.00', STEP_17)
        
        STEP_17_01 = """
            STEP 17.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 17.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('17.01', STEP_17_01, True)
        
        STEP_18 = """
            STEP 18 : Click on 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot('18.00', STEP_18)
        
        STEP_18_01 = """
            STEP 18.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 18.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'")
        HomePage.Home._utils.capture_screenshot('18.01', STEP_18_01, True)
        
        STEP_19 = """
            STEP 19 : Click on 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot('19.00', STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 19.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot('19.01', STEP_19_01, True)
        
        STEP_20 = """
            STEP 20 : Click on 'Visualization Example - Shortcut1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('20.00', STEP_20)
        
        STEP_20_01 = """
            STEP 21.01 : Verify Properties dialog opens for ''Visualization Example - Shortcut1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 20.01 : Verify Properties dialog opens for ''Visualization Example - Shortcut1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('20.01', STEP_20_01, True)
        
        STEP_21 = """
            STEP 21 : Click 'Cancel' to close the properties dialog
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('21.00', STEP_21)
        
        STEP_22 = """
            STEP 22 : Click on 'Utilities'
        """
        HomePage.Banner.click_utilities()
        HomePage.Home._utils.capture_screenshot('22.00', STEP_22)
        
        STEP_22_01 = """
            STEP 22.01 : Verify the following options : Deferred Status, Stop Requests
        """
        utilities_context = ['Deferred Status', 'Stop Requests', 'Magnify Search Page']
        HomePage.ContextMenu.verify(utilities_context, "22.01")
        HomePage.Home._utils.capture_screenshot('22.01', STEP_22_01, True)
        
        STEP_23 = """
            STEP 23 : Click on 'Help' (?)
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot('23.00', STEP_23)
        
        STEP_23_01 = """
            STEP 23.01 : Verify the following options:
            1.WebFOCUS Online Help
            2.Technical Resources
            3.Community
            4.About WebFOCUS
            5.License
            6.Information Builders Home
        """
        help_context = ['WebFOCUS Online Help', 'Technical Resources', 'Community', 'About WebFOCUS', 'License', 'TIBCO Software Inc.']
        HomePage.ContextMenu.verify(help_context, "23.01")
        HomePage.Home._utils.capture_screenshot('23.01', STEP_23_01, True)
        
        STEP_24 = """
            STEP 24 : Click on the 'User name' (Getting Started Basic user1) > Select 'Change Password''
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('24.00', STEP_24)
        
        STEP_25 = """
            STEP 35 : Enter new Password twice: Password1, click Change Password button
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot('25.00', STEP_25)
        
        STEP_25_01 = """
            STEP 25.01 : Verify 'Your password has been changed'prompt gets displayed with a transparent green color background
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '25.01')
        HomePage.NotifyPopup.verify_background_color('25.02')
        HomePage.NotifyPopup.verify_transparent('25.03')
        HomePage.Home._utils.capture_screenshot('25.01', STEP_25_01, True)
        
        STEP_26 = """
            STEP 26 : Click on 'Invite User'
        """
        HomePage.Banner.click_invite_user()
        HomePage.ModalDailogs.InviteUser.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('26.00', STEP_26)
        
        STEP_27 = """
            STEP 27 : Enter any name and a valid email > Click Invite
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text("WebFOCUS")
        HomePage.ModalDailogs.InviteUser.LastName.enter_text("IBI")
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text("c9946064autotest@ibi.com")
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot('27.00', STEP_27)
        
        STEP_27_01 = """
            STEP 27.01 : Verify that 'Invite successfully sent' message displayed
        """
        HomePage.ModalDailogs.InviteUser.ErrorMessage.verify_text('Invite successfully sent.', '27.01')
        HomePage.Home._utils.capture_screenshot('27.01', STEP_27_01, True)
        
        STEP_28 = """
            STEP 28 : Click 'Cancel' to close the 'Invite User' dialog
        """
        HomePage.ModalDailogs.InviteUser.CancelButton.click()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('28.00', STEP_28)
        
        STEP_29 = """
            STEP 29 : Multi-select and right-click on 'Portal_admin2', 'car2' and 'Visualization Example - Shortcut1' > Select 'Add to Favorites'
        """
        HomePage.Workspaces.ContentArea.select_multiple_file([portal_file, car_file]) #Already Visualization Example - Shortcut1 selected
        HomePage.Workspaces.ContentArea.right_click_on_file(visual_exp_file)
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('29.00', STEP_29)
        
        STEP_30 = """
            STEP 30 : Click on 'WebFOCUS Home' view
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot('30.00', STEP_30)
        
        STEP_30_01 = """
            STEP 30.01 : Verify that 'Portal_admin2', 'car2' and 'Visualization Example - Shortcut1' gets displayed under 'Favorites' section
        """
        HomePage.Home.Favorites.verify_items([portal_file, car_file, visual_exp_file], '30.01')
        HomePage.Home._utils.capture_screenshot('30.01', STEP_30_01, True)
        
        STEP_31 = """
            STEP 31 : Double click to run 'Visualization Example - Shortcut1' under Favorites section
        """
        HomePage.Home.Favorites.double_click_on_item(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('31.00', STEP_31)
        
        STEP_31_01 = """
            STEP 31.01 : Verify that 'Visualization Example - Shortcut1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_exp_file, '31.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 31.02 : Verify that "Visualization Example - Shortcut1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('31.01', STEP_31_01, True)
        
        STEP_32 = """
            STEP 32 : Click 'X' to close the run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('32.00', STEP_32)
        
        STEP_33 = """
            STEP 33 : Double click to run 'Visualization Example - Shortcut1' under Recents section
        """
        HomePage.Home.Recents.double_click_on_item(visual_exp_file)
        HomePage.Home._utils.capture_screenshot('33.00', STEP_33)
        
        STEP_33_01 = """
            STEP 33.01 : Verify that 'Visualization Example - Shortcut1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_exp_file, '33.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 33.02 : Verify that "Visualization Example - Shortcut1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('33.01', STEP_33_01, True)
        
        STEP_34 = """
            STEP 34 : Click 'X' to close the run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('34.00', STEP_34)
        
        STEP_35 = """
            STEP 35 : Run 'Portal_admin2' under Portals section
        """
        HomePage.Home.Portals.double_click_on_item(portal_file)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot('35.00', STEP_35)
        
        STEP_35_01 = """
            STEP 35 : Verify that 'Portal_admin2' run without any error
        """
        PortalBanner.verify_portal_top_banner_title(portal_file, 'Step 35.01 : Verify that "Portal_admin2" run without any error')
        HomePage.Home._utils.capture_screenshot('35.01', STEP_35_01, True)
        
        STEP_36 = """
            STEP 36 : Close the portal.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('36.00', STEP_36)
        
        STEP_37 = """
            STEP 37 : Signout WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('37.00', STEP_37)