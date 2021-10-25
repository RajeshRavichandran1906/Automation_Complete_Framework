"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 05-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.security_center import Security_Center

class C9929865_TestClass(BaseTestCase):
    
    def test_C9929865(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Security = Security_Center(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        my_workspace = "My Workspace"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Administrator
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify that the first available workspace is 'My Workspace'
        """
        folders_obj = self.driver.find_elements(*HomePage.Workspaces.ResourcesTree.locators.items)[:2]
        actual_folders = [folder.text.strip() for folder in folders_obj]
        HomePage.Home._utils.asequal(['Workspaces', 'My Workspace'], actual_folders, "Step 02.01 : Verify that the first available workspace is 'My Workspace'")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Expand 'My Workspace' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.expand(my_workspace)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that 'My Content' is available under My Workspace
        """
        HomePage.Workspaces.ResourcesTree.verify_items(['My Content'], "03.01", parent_folder=my_workspace)
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on 'My Workspace' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select(my_workspace)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that no action bar is displayed in the content area
        """
        HomePage.Workspaces.ActionBar.verify_not_displayed("04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on 'My Content' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select(my_workspace + "->My Content")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that action bars (DATA, APPLICATION, INFOASSIST, SCHEDULE, and OTHER) are available
        """
        actionbar_tabs = ['DATA', 'APPLICATION', 'INFOASSIST', 'SCHEDULE', 'OTHER']
        HomePage.Workspaces.ActionBar.verify_tabs(actionbar_tabs, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right-click on 'My Workspace_My Content_folder' from the content area > Select 'Copy'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("My Workspace_My Content_folder")
        HomePage.ContextMenu.select("Copy")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right-click on 'My Workspace' from the resuource tree
        """
        HomePage.Workspaces.ResourcesTree.right_click(my_workspace)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following context menu:
            * Collapse
            * Delete DEL
            * Refresh
            * General access > All users/Workspace groups (by default selected)
            * Unpublish
            * Hide
            * Security > Rules.../Rules on this resource.../Effective policy.../Owner...
            * Properties
            (Note: Paste option is not available. Since this is not writable location)
        """
        options = ['Collapse', 'Delete DEL', 'Refresh', 'General access', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(options, "07.01")
        HomePage.ContextMenu.verify(['All users', 'Workspace groups'], "07.02", menu_path="General access")
        HomePage.ContextMenu.close(location='bottom_middle', y=4)
        HomePage.Workspaces.ResourcesTree.right_click(my_workspace)
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], "07.03", menu_path="Security")
        HomePage.ContextMenu.close(location='bottom_middle', y=4)
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right-click on My Workspace > Hover over mouse to the 'General access'
        """
        HomePage.Workspaces.ResourcesTree.right_click(my_workspace)
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that by default Workspace groups is selected
        """
        HomePage.ContextMenu.verify_selected_options(['Workspace groups'], "08.01", menu_path="General access")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click on 'Settings' > 'Security Center'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select("Security Center")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Under Groups section > Expand My_Workspace group
        """
        Security.expand_group_section_("My_Workspace")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that 'Authors' and 'BasicUsers' subgroups are available by default
        """
        user_row_css = "#SecurityManagerDialog_treeGroups tr.selected ~ tr>td:nth-child(1)"
        users = [user.text.strip() for user in self.driver.find_elements_by_css_selector(user_row_css)[:3]]
        HomePage.Home._utils.verify_list_values(['Authors', 'BasicUsers'], users, "Step 10.01 : Verify that 'Authors' and 'BasicUsers' subgroups are available by default", assert_type="asin")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
        
        STEP_11 = """
            STEP 11 : Close security center window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)
        
        STEP_12 = """
            STEP 12 : Click on 'User' banner link > Select 'SignOut'
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)