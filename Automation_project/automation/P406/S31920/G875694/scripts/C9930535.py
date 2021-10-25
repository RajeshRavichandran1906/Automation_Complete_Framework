"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 10-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930535_TestClass(BaseTestCase):
    
    def test_C9930535(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        SHORTCUT_CONTEXT_MENU = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand Workspaces>My Workspace>My Content from the Tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.expand("My Workspace->My Content")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : From the Action Bar, click on Other tab>Shortcut
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ContentArea.delete_file_if_exists("retail_sales")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify New Shortcut dialogue comes up
        """
        HomePage.ModalDailogs.Shortcut.wait_for_appear(20)
        HomePage.ModalDailogs.Shortcut.verify_title("New Shortcut", "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on the Master file radio button and Browse
        """
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.click()
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Select EDASERVE> retail_samples folder
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select("EDASERVE")
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click("getting_started")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click wf_retail_lite.mas and press the 'Select' button>click 'OK'
        """
        HomePage.ModalDailogs.Resources.GridView.Files.click('retail_sales.mas')
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify uploaded shortcut as well as pop up message display
        """
        HomePage.Home._utils.verify_element_visiblty(element_css=".notify-popup.success", visible=True, msg="Step 07.01 : Verify temporary displayed message")
        HomePage.Workspaces.ContentArea.verify_files(['retail_sales'], '07.02')
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right-click on the shortcut
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("retail_sales")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify right-click menu
        """
        HomePage.ContextMenu.verify(SHORTCUT_CONTEXT_MENU, '08.01')
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

