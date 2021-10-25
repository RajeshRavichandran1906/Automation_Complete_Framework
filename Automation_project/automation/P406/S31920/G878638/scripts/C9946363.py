"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 28-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946363_TestClass(BaseTestCase):
    
    def test_C9946363(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        folder_path = "P406_S31920->G878638"
        file_name = "C9946363_V5_Portal"
        user_btn_css = "div.pvd-menu-admin"
        admin_user_options = ['Administration', 'Tools', 'Preferences', 'Help', 'Remove my customizations', 'Change Password', 'Sign Out']
        user_options = ['Tools', 'Preferences', 'Help', 'Remove my customizations', 'Change Password', 'Sign Out']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(switch_to_frame=True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : From the resource tree, Expand 'P406_S31920' workspace > Click on 'G878638' folder > Right-click on 'C9946363_V5_Portal' from the content area > Click Run
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        HomePage.Workspaces.ContentArea.right_click_on_folder(file_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_btn_css, 60)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on the 'User name'
        """
        user_btn = HomePage.Home._utils.validate_and_get_webdriver_object(user_btn_css, "V5 portal user button")
        HomePage.Home._core_utils.left_click(user_btn)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the following options are displayed.
        """
        HomePage.ContextMenu.verify(admin_user_options, "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Close the portal run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out and Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mriddev", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on the 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(switch_to_frame=True)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : From the resource tree, Expand 'P406_S31920' workspace > Click on 'G878638' folder > Right-click on 'C9946363_V5_Portal' from the content area > Click Run
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        HomePage.Workspaces.ContentArea.right_click_on_folder(file_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_btn_css, 60)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on the 'User name'
        """
        user_btn = HomePage.Home._utils.validate_and_get_webdriver_object(user_btn_css, "V5 portal user button")
        HomePage.Home._core_utils.left_click(user_btn)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the portal run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Click Sign Out and Sign into WebFOCUS Home Page as Advanced User.
        """
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on the 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(switch_to_frame=True)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : From the resource tree, Expand 'P406_S31920' workspace > Click on 'G878638' folder > Right-click on 'C9946363_V5_Portal' from the content area > Click Run
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_btn_css, 60)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Click on the 'Username'.
        """
        user_btn = HomePage.Home._utils.validate_and_get_webdriver_object(user_btn_css, "V5 portal user button")
        HomePage.Home._core_utils.left_click(user_btn)
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "14.01")
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the portal run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : In the banner link, click on the top right username > Click Sign Out and Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Click on the 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(switch_to_frame=True)
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : From the resource tree, Expand 'P406_S31920' workspace > Click on 'G878638' folder > Right-click on 'C9946363_V5_Portal' from the content area > Click Run
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select("Run")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(user_btn_css, 60)
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on the 'Username'.
        """
        user_btn = HomePage.Home._utils.validate_and_get_webdriver_object(user_btn_css, "V5 portal user button")
        HomePage.Home._core_utils.left_click(user_btn)
        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following options are displayed.
        """
        HomePage.ContextMenu.verify(user_options, "19.01")
        HomePage.Home._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Close the portal run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("21", STEP_21)