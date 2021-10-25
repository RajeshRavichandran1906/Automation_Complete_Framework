"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 18-August-2020
-------------------------------------------------------------------------------------------"""

from common.wftools.page_designer import Run
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_portal import Banner
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.paris_home_page import ParisHomePage

class C9946033_TestClass(BaseTestCase):
    
    def test_C9946033(self):
        
        """
        TEST CASE OBJECTS
        """
        OldHomePage = Wf_Mainpage(self.driver)
        HomePage = ParisHomePage(self.driver)
        PortalBanner = Banner(self.driver)
        PageDesigner = Run(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        portal_file = "Portal_admin2"
        car_file = "car2"
        summit_file = "Summit1"
        summit_url_file = "Summit_URL1"
        visual_upload_file = "Vis_after_Upload1"
        visual_exp_file = "Visualization Example - Shortcut1"
        alert_msg = 'No writable folder found'
        
        STEP_01 = """
            STEP 01 : Sign in as gs_aut1@ibi.com
        """
        HomePage.invoke_with_login('mridauth1','mrpassauth1')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_01_EXPECTED = """
            STEP 01 - Expected : Verify Welcome page features:
            Getting Started, Favorites and Portals sections
        """
        HomePage.Home.verify_sections(['GETTING STARTED', 'FAVORITES', 'PORTALS'], '01.01', assert_type='asin')
        HomePage.Home._utils.capture_screenshot("01 - Expected", STEP_01_EXPECTED, True)

        STEP_02 = """
            STEP 02 : Expand [+] area
        """
        HomePage.Banner.click_plus()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that 'VISUALIZE DATA' having two functions:
            1. Create New Visualization
            Start a brand new visualization from scratch
            2. Assemble Visualizations
            Leverage existing content you created or shared by others to assemble new visualization.
            Verify that 'MANAGE DATA'having two functions:
            3. Get Data
            4.Prepare and ManageData
        """
        expected_tools = ['Create New Visualization Start a brand new visualization from scratch', 'Assemble Visualizations Leverage existing content you created or shared by others to assemble new visualization.', 'Get Data', 'Prepare and Manage Data']
        tool_obj = self.driver.find_elements(*HomePage.Banner.locators.ToolListMenu.tools)
        actual_tools = [tool.text.strip().replace("\n", " ") for tool in tool_obj if tool.is_displayed()]
        HomePage.Home._utils.asequal(expected_tools, actual_tools, "Step 02.01 : Verify the VISUALIZE DATA functions")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click Get Data
        """
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that 'No writable folder found' message gets displayed
        """
        HomePage.ModalDailogs.Alert.verify_message(alert_msg, '03.01')
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click OK to close the message prompt
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Expand [+] area and select Create New Visualization
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Create New Visualization')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that 'No writable folder found' message gets displayed
        """
        HomePage.ModalDailogs.Alert.verify_message(alert_msg, '05.01')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click OK to close the message prompt
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Expand [+] area and select Assemble Visualizations.
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that 'No writable folder found' message gets displayed
        """
        HomePage.ModalDailogs.Alert.verify_message(alert_msg, '07.01')
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click OK to close the message prompt
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Expand [+] area and select Prepare and Manage Data.
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Prepare and Manage Data')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that 'No writable folder found' message gets displayed
        """
        HomePage.ModalDailogs.Alert.verify_message(alert_msg, '09.01')
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click OK to close the message prompt
        """
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on Workspaces view > Click on 'Getting Started' workspace from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select('Getting Started')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, 'Admin2', 30)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that no category buttons are available (Application and Other)
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed('11.01')
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Expand Getting Started > Click on 'Admin2' from the resource tree > Double click to run 'Portal_admin1'
        """
        HomePage.Workspaces.ResourcesTree.select('Getting Started->Admin2')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_file, 30)
        HomePage.Workspaces.ContentArea.double_click_on_file(portal_file)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that 'Portal_admin2' run without any error
        """
        PortalBanner.verify_portal_top_banner_title(portal_file, 'Step 12.01 : Verify that "Portal_admin2" run without any error')
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Close 'Portal_admin2' run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Double click to run 'car2'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(car_file)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify that 'car2' run without any error
        """
        HomePage.RunWindow.verify_title(car_file, '14.01')
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click 'X' to close 'car2' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Double click to run 'Summit1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_file)
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify that 'Summit1' run without any error
        """
        HomePage.RunWindow.verify_title(summit_file, '16.01')
        HomePage.Home._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Double click to run 'Summit_URL1'
        """
        HomePage.RunWindow.close()
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_url_file)
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify that 'Summit_URL1' run without any error
        """
        btn_css = "a[title^='Register']"
        HomePage.RunWindow.verify_title(summit_url_file, '17.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(btn_css, 'Register', 60)
        btn_text = self.driver.find_element_by_css_selector(btn_css).text.strip()
        HomePage.Home._utils.asequal('Register Now', btn_text, 'Step 17.02 : Verify that "Summit_URL1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Click 'X' to close 'Summit_URL1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Double click to run 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify that 'Vis_after_Upload1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_upload_file, '19.01')
        HomePage.Home._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click 'X' to close 'Vis_after_Upload1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Double click to run 'Visualization Example- Shortcut1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify that 'Visualization Example- Shortcut1' run without any error
        """
        pd_css = ".pd-page-content-wrapper"
        containers = ['Outlier Analysis', 'Store Rankings', 'Revenue by Category', 'Profitability Analysis']
        HomePage.RunWindow.verify_title(visual_exp_file, '21.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 21.02 : Verify that "Visualization Example- Shortcut" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Click 'X' to close 'Visualization Example- Shortcut1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("22", STEP_22)

        STEP_23 = """
            STEP 23 : Right-click on 'Portal_admin2' > Select 'Properties'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(portal_file)
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.capture_screenshot("23", STEP_23)

        STEP_23_EXPECTED = """
            STEP 23 - Expected : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 23.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot("23 - Expected", STEP_23_EXPECTED, True)

        STEP_24 = """
            STEP 24 : Click on 'car2'
        """
        HomePage.Workspaces.ContentArea.select_file(car_file)
        HomePage.Home._utils.capture_screenshot("24", STEP_24)

        STEP_24_EXPECTED = """
            STEP 24 - Expected : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 24.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot("24 - Expected", STEP_24_EXPECTED, True)

        STEP_25 = """
            STEP 25 : Click on 'Summit1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_file)
        HomePage.Home._utils.capture_screenshot("25", STEP_25)

        STEP_25_EXPECTED = """
            STEP 25 - Expected : Verify Properties dialog opens for 'Summit1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 25.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot("25 - Expected", STEP_25_EXPECTED, True)

        STEP_26 = """
            STEP 26 : Click on 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot("26", STEP_26)

        STEP_26_EXPECTED = """
            STEP 26 - Expected : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 26.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'")
        HomePage.Home._utils.capture_screenshot("26 - Expected", STEP_26_EXPECTED, True)

        STEP_27 = """
            STEP 27 : Click on 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot("27", STEP_27)

        STEP_27_EXPECTED = """
            STEP 27 - Expected : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Query Detail'], "Step 27.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot("27 - Expected", STEP_27_EXPECTED, True)

        STEP_28 = """
            STEP 28 : Click on 'Visualization Example- Shortcut1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("28", STEP_28)

        STEP_28_EXPECTED = """
            STEP 28 - Expected : Verify Properties dialog opens for ''Visualization Example- Shortcut1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General'], "Step 28.01 : Verify Properties dialog opens for ''Visualization Example- Shortcut' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot("28 - Expected", STEP_28_EXPECTED, True)

        STEP_29 = """
            STEP 29 : Click 'Cancel' to close the properties dialog
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("29", STEP_29)

        STEP_30 = """
            STEP 30 : Click on 'Utilities'
        """
        HomePage.Banner.click_utilities()
        HomePage.Home._utils.capture_screenshot("30", STEP_30)

        STEP_30_EXPECTED = """
            STEP 30 - Expected : Verify the following options:
            1. Deferred Status
            2. Stop Requests
        """
        utilities_context = ['Deferred Status', 'Stop Requests', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page']
        HomePage.ContextMenu.verify(utilities_context, "30.01")
        HomePage.Home._utils.capture_screenshot("30 - Expected", STEP_30_EXPECTED, True)

        STEP_31 = """
            STEP 31 : Click on 'Help' (?)
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("31", STEP_31)

        STEP_31_EXPECTED = """
            STEP 31 - Expected : Verify the following options:
            1. WebFOCUS Online Help
            2. Technical Resources
            3. Community
            4. About WebFOCUS
            5. License
            6. Information Builders Home
        """
        help_context = ['WebFOCUS Online Help', 'Technical Resources', 'Community', 'About WebFOCUS', 'License', 'TIBCO Software Inc.']
        HomePage.ContextMenu.verify(help_context, "31.01")
        HomePage.Home._utils.capture_screenshot("31 - Expected", STEP_31_EXPECTED, True)

        STEP_32 = """
            STEP 32 : Click on the 'User name' (Getting Started Author user1) > Select 'Change Password'
        """
        HomePage.Banner.click_user()
        HomePage.ContextMenu.select('Change Password')
        HomePage.ModalDailogs.ChangePassword.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("32", STEP_32)

        STEP_32_EXPECTED = """
            STEP 32 - Expected : Change password window is displayed
        """
        HomePage.ModalDailogs.ChangePassword.verify_title("Change Password", "32.01")
        HomePage.Home._utils.capture_screenshot("32 - Expected", STEP_32_EXPECTED, True)

        STEP_33 = """
            STEP 33 : Enter new Password twice: Password1, click Change Password button
        """
        HomePage.ModalDailogs.ChangePassword.NewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ConfirmNewPassword.enter_text("Password1")
        HomePage.ModalDailogs.ChangePassword.ChangePasswordButton.click()
        HomePage.Home._utils.capture_screenshot("33", STEP_33)

        STEP_33_EXPECTED = """
            STEP 33 - Expected : Verify 'Your password has been changed'prompt gets displayed with a transparent green color background
        """
        HomePage.NotifyPopup.verify_text('Your password has been changed', '33.01')
        HomePage.NotifyPopup.verify_background_color('33.02')
#         HomePage.NotifyPopup.verify_transparent('33.03') scenario verified in the test case 'C9946063'
        HomePage.Home._utils.capture_screenshot("33 - Expected", STEP_33_EXPECTED, True)

        STEP_34 = """
            STEP 34 : Click on Invite User
        """
        HomePage.Banner.click_invite_user()
        HomePage.ModalDailogs.InviteUser.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("34", STEP_34)

        STEP_35 = """
            STEP 35 : Enter any name and a valid email > Click Invite
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text("WebFOCUS")
        HomePage.ModalDailogs.InviteUser.LastName.enter_text("IBI")
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text("c9946033autotest@ibi.com")
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        HomePage.Home._utils.capture_screenshot("35", STEP_35)

        STEP_35_EXPECTED = """
            STEP 35 - Expected : Verify that 'Invite successfully sent' message displayed
        """
        HomePage.ModalDailogs.InviteUser.ErrorMessage.verify_text('Invite successfully sent.', '35.01')
        HomePage.Home._utils.capture_screenshot("35 - Expected", STEP_35_EXPECTED, True)

        STEP_36 = """
            STEP 36 : Click 'Cancel' to close the 'Invite User' dialog
        """
        HomePage.ModalDailogs.InviteUser.CancelButton.click()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("36", STEP_36)

        STEP_37 = """
            STEP 37 : Multi-select and right-click on 'Portal_admin2', 'car2' and 'Visualization Example- Shortcut1' > Select 'Add to Favorites'
        """
        HomePage.Workspaces.ContentArea.select_multiple_file([portal_file, car_file]) #Already Visualization Example- Shortcut selected
        HomePage.Workspaces.ContentArea.right_click_on_file(visual_exp_file)
        HomePage.ContextMenu.select('Add to Favorites')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("37", STEP_37)

        STEP_38 = """
            STEP 38 : Click on 'WebFOCUS Home' view
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot("38", STEP_38)

        STEP_38_EXPECTED = """
            STEP 38 - Expected : Verify that 'Portal_admin1', 'car1' and 'Visualization Example- Shortcut' gets displayed under 'Favorites' section
        """
        HomePage.Home.Favorites.verify_items([portal_file, car_file, visual_exp_file], '38.01')
        HomePage.Home._utils.capture_screenshot("38 - Expected", STEP_38_EXPECTED, True)

        STEP_39 = """
            STEP 39 : Double click to run 'Visualization Example- Shortcut1' under Favorites section
        """
        HomePage.Home.Favorites.double_click_on_item(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("39", STEP_39)

        STEP_39_EXPECTED = """
            STEP 39 - Expected : Verify that 'Visualization Example- Shortcut1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_exp_file, '39.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 39.02 : Verify that "Visualization Example- Shortcut" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("39 - Expected", STEP_39_EXPECTED, True)

        STEP_40 = """
            STEP 40 : Click 'X' to close the run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("40", STEP_40)

        STEP_41 = """
            STEP 41 : Double click to run 'Visualization Example- Shortcut1' under Recents section
        """
        HomePage.Home.Recents.double_click_on_item(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("41", STEP_41)

        STEP_41_EXPECTED = """
            STEP 41 - Expected : Verify that 'Visualization Example- Shortcut1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_exp_file, '41.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 41.02 : Verify that "Visualization Example- Shortcut" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("41 - Expected", STEP_41_EXPECTED, True)

        STEP_42 = """
            STEP 42 : Click 'X' to close the run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("42", STEP_42)

        STEP_43 = """
            STEP 43 : Run 'Portal_admin2' under Portals section
        """
        HomePage.Home.Portals.double_click_on_item(portal_file)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("43", STEP_43)

        STEP_43_EXPECTED = """
            STEP 43 - Expected : Verify that 'Portal_admin2' run without any error
        """
        PortalBanner.verify_portal_top_banner_title(portal_file, 'Step 43.01 : Verify that "Portal_admin2" run without any error')
        HomePage.Home._utils.capture_screenshot("43 - Expected", STEP_43_EXPECTED, True)

        STEP_44 = """
            STEP 44 : Close the portal.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("44", STEP_44)

        STEP_45 = """
            STEP 45 : Signout WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("45", STEP_45)