"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 17-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930467_TestClass(BaseTestCase):
    
    def test_C9930467(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        author_user = HomePage.Home._core_utils.parseinitfile("mridauth")
        file_name = "Discount by Category"
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Author User
        """
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Shared with Me' view
        """
        HomePage.Banner.click_shared_with_me()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify Shared with Me is empty
        """
        HomePage.SharedWithMe.verify_items([], "02.01", "asequal")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Sign out and sign in as Administrator.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Workspaces' view
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Exapnd 'Getting Started' workspace > Right-Click on 'Visualization' folder folder from the resource tree > Select 'Copy'
        """
        HomePage.Workspaces.ResourcesTree.select("Getting Started->Visualizations")
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select("Copy")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Expand'My Workspace' > Right-click on 'My Content' folder from the resource tree > Select 'Paste'
        """
        tree_path = "My Workspace->My Content"
        HomePage.Workspaces.ResourcesTree.select(tree_path)
        HomePage.Workspaces.ContentArea.delete_file_if_exists(file_name)
        HomePage.Workspaces.ResourcesTree.right_click(tree_path)
        HomePage.ContextMenu.select("Paste")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Right-click on 'Discount by Category' > Select 'Share with...'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select("Share with...")
        HomePage.ModalDailogs.ShareWithOthers.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Enter 'autocloudauth12@ibi.com' in the 'Enter users and groups' textbox
        """
        HomePage.ModalDailogs.ShareWithOthers.SearchTextBox.enter_text(author_user)
        HomePage.ModalDailogs.ShareWithOthers.UserGroupResults.wait_for_visible()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click 'autocloudauth12@ibi.com' in the lists
        """
        HomePage.ModalDailogs.ShareWithOthers.UserGroupResults.select("HP Cloud Author user 13")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click OK
        """
        HomePage.ModalDailogs.ShareWithOthers.OKButton.click()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Sign out and sign in as Author user
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.invoke_with_login("mridauth", "mrpassauth")
        HomePage.Banner.close_page_message()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on 'Shared with Me' view
        """
        HomePage.Banner.click_shared_with_me()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Right click on 'Discount by Category'
        """
        HomePage.SearchResuls.right_click_on_item(file_name)
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Visualization report's right-click menu
        """
        context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(context_menu, "13.01")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click Run
        """
        HomePage.ContextMenu.select("Run")
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify Shared Visualization report displays correctly
        """
        labels = ['Video Production', 'Televisions', 'Computers', 'Accessories', 'Camcorder', 'Media Player', 'Stereo Systems']
        actaul_labels = [label.text.strip() for label in self.driver.find_elements_by_css_selector("#jschart_HOLD_0 .group-label text")]
        HomePage.Home._utils.asequal(labels, actaul_labels, "Step 14.01 : Verify Shared Visualization report displays correctly")
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Sign out WF.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)