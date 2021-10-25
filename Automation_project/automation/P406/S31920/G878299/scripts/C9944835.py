"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 06-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944835_TestClass(BaseTestCase):
    
    def test_C9944835(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        workspace = "Retail Samples"
        workspace_name = "Retail_Samples"
        workspace_shortcut = "Retail Samples - Shortcut"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree > Click on 'Shortcut Testing'
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G878309->Shortcut Testing')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(workspace_shortcut)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.ModalDailogs.Shortcut.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on 'Workspaces' from the breadcrumb trail > Click on 'Retail_Samples' workspace
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select_workspaces()
        HomePage.ModalDailogs.Resources.GridView.Folders.click(workspace)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that Title and Name should be 'Retail_Samples' in the entry box and the 'Select' button get enabled
        """
        HomePage.ModalDailogs.Resources.Title.verify_text(workspace, "06.01")
        HomePage.ModalDailogs.Resources.Name.verify_text(workspace_name, "06.02")
        HomePage.ModalDailogs.Resources.SelectButton.verify_enabled("06.03")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following:
    
            1. Target path = 'IBFS:WFC/Repository/Retail_Samples'
            2. Title = Retail_Samples - Shortcut
            3. Summary should be empty
            4. Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/Retail_Samples', "07.01")
        HomePage.ModalDailogs.Shortcut.Title.verify_text(workspace_shortcut, "07.02")
        HomePage.ModalDailogs.Shortcut.Summary.verify_text("", "07.03")
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled("07.04")
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled("07.05")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that shortcut for an item (Retail_Samples - Shortcut workspace) is being created properly
            and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Home._utils.wait_for_page_loads(50)
        HomePage.Workspaces.ContentArea.verify_shortcut_folders([workspace_shortcut], '08.01')
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Double click on 'Retail_Samples - Shortcut'
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder(workspace_shortcut)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Right-click on 'Retail_Samples - Shortcut' workspace > Click on 'Delete'
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G878309->Shortcut Testing')
        HomePage.Workspaces.ContentArea.delete_folder(workspace_shortcut)
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that 'Retail_Samples - Shortcut' workspace get deleted
        """
        HomePage.Workspaces.ContentArea.verify_folders([workspace_shortcut], "10.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

