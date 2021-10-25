"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 11-August-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930310_TestClass(BaseTestCase):
    
    def test_C9930310(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        WORKSPACE_CONTEXT_MENU = ['Collapse', 'Refresh']
        MYWORKSPACE_CONTEXT_MENU = ['Expand', 'Refresh', 'Properties']
        GSTARTED_CONTEXT_MENU = ['Expand', 'Refresh', 'Properties']
        MYWORKSPACE_CONTENT_CONTEXT_MENU = ['Open', 'Refresh', 'Properties']
        GSTARTED_CONTENT_CONTEXT_MENU = ['Open', 'Refresh', 'Properties']
        
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
            STEP 03 : Click on Workspaces from the tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify only My Workspace & Getting Started folders are available from the tree
                        Verify No Action bar is available and that My Workspaces & Getting Started display under Folder
        """
        HomePage.Workspaces.ResourcesTree.verify_items(['Workspaces', 'My Workspace', 'Getting Started'], "03.01", "asequal")
        HomePage.Workspaces.ActionBar.verify_not_displayed("03.02")
        HomePage.Workspaces.ContentArea.verify_folders(['My Workspace', 'Getting Started'], "03.03", "asequal")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Right-click on Workspaces from the tree.
        """
        HomePage.Workspaces.ResourcesTree.right_click("Workspaces")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Workspaces right-click menu from the tree
        """
        HomePage.ContextMenu.verify(WORKSPACE_CONTEXT_MENU, "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Right-click on My Workspace from the tree.
        """
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.right_click("My Workspace")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify My Workspace folder's right-click menu from the tree
        """
        HomePage.ContextMenu.verify(MYWORKSPACE_CONTEXT_MENU, "05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right-click on Getting Started from the tree.
        """
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.right_click("Getting Started")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Getting Started folder's right-click menu from the tree
        """
        HomePage.ContextMenu.verify(GSTARTED_CONTEXT_MENU, "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right-click on My Workspace from the content area.
        """
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        HomePage.Workspaces.ContentArea.right_click_on_folder("My Workspace")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify My Workspaces folder's right-click menu from work area(under Folders)
        """
        HomePage.ContextMenu.verify(MYWORKSPACE_CONTENT_CONTEXT_MENU, "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right-click on Getting Started from the content area.
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        HomePage.Workspaces.ContentArea.right_click_on_folder("Getting Started")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Getting Started folder's right-click menu from work area(under Folders)
        """
        HomePage.ContextMenu.verify(GSTARTED_CONTENT_CONTEXT_MENU, "08.01")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

