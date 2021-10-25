"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 19-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928024_TestClass(BaseTestCase):
    
    def test_C9928024(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        global_resources = "Global Resources"
        security_options = ['Rules...', 'Rules on this resource...', 'Effective policy...']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Workspaces' tab > Click on 'Workspaces' from the navigation bar.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Collapse the 'Workspaces' from the tree if expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Expand Global Resources node and Right click on Page Templates Legacy folder.
        """
        HomePage.Workspaces.ResourcesTree.expand(global_resources)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that following options are displayed:
            1.Expand.
            2.Refresh.
            3.Security 
            --> Rules
            --> Rules on this resources..
            --> Effective policy...
            4.Properties.
        """
        pt_context_menu = ['Expand', 'Refresh', 'Security', 'Properties']
        HomePage.Workspaces.ResourcesTree.collapse("Page Templates (Legacy)")
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Page Templates (Legacy)")
        HomePage.ContextMenu.verify(pt_context_menu, "04.01")
        HomePage.ContextMenu.verify(security_options, "04.02", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Expand Page Templates Legacy folder > Select Standard sub-folder > right click on '1 Column' page.
        """
        HomePage.Workspaces.ResourcesTree.expand(global_resources + "->Page Templates (Legacy)")
        HomePage.Workspaces.ResourcesTree.select(global_resources + "->Standard")
        HomePage.Workspaces.ContentArea.right_click_on_file("1 Column")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that following options are displayed:
            1.Copy (Ctrl+C)
            2.Security 
            --> Rules
            --> Rules on this resources..
            --> Effective policy...
            3.Properties.
        """
        page_context_menu = ['Copy Ctrl+C', 'Security', 'Properties']
        HomePage.ContextMenu.verify(page_context_menu, "05.01")
        HomePage.ContextMenu.verify(security_options, "05.02", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Expand Standard sub-folder and right click on Resources.
        """
        HomePage.Workspaces.ResourcesTree.expand(global_resources + "->Standard")
        HomePage.Workspaces.ResourcesTree.collapse("Resources")
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Resources")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that following options are displayed:
            1.Expand.
            2.Refresh.
            3.Security 
            --> Rules
            --> Rules on this resources..
            --> Effective policy...
            4.Properties.
        """
        resources_context_menu = ['Expand', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(resources_context_menu, "06.01")
        HomePage.ContextMenu.verify(security_options, "06.02", menu_path="Security")
        HomePage.ContextMenu.close(location="bottom_middle", y=5)
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on Resources folder and right click on '1 Column' from the content area.
        """
        HomePage.Workspaces.ResourcesTree.select(global_resources + "->Resources")
        HomePage.Workspaces.ContentArea.right_click_on_file("1 Column")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify that the following options are displayed:
            1.View.
            2.View in new window.
            3.Copy (Ctrl+C)
            4.Security 
            --> Rules
            --> Rules on this resources..
            --> Effective policy...
            5.Properties.
        """
        page_context_menu = ['View', 'View in new window', 'Copy Ctrl+C', 'Security', 'Properties']
        HomePage.ContextMenu.verify(page_context_menu, "07.01")
        HomePage.ContextMenu.verify(security_options, "07.02", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Right click on Custom folder under resource tree.
        """
        HomePage.Workspaces.ResourcesTree.collapse("Custom")
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Custom")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that the following options are displayed:
            1.Expand.
            2.Paste Ctrl+V (By default disabled)
            3.Refresh.
            4.Security 
            --> Rules
            --> Rules on this resources..
            --> Effective policy...
            5.Properties.
        """
        custom_context_menu = ['Expand', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(custom_context_menu, "08.01")
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], "08.02")
        HomePage.ContextMenu.verify(security_options, "08.03", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Revert back the 'Workspaces' view default by clicking on 'Workspaces' from the navigation tree
        """
        HomePage.Workspaces.ResourcesTree.collapse(global_resources)
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : In the banner link, click on the 'Username' > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)