"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 01-October-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928022_TestClass(BaseTestCase):
    
    def test_C9928022(self):
        
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
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Collapse the 'Workspaces' from the tree if expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right click on Global Resources node.
        """
        HomePage.Workspaces.ResourcesTree.collapse(global_resources) # Collapse if already expanded - To avoid false verification failure
        HomePage.Workspaces.ResourcesTree.right_click(global_resources)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that following options are displayed:
            1.Expand.
            2.Refresh.
        """
        HomePage.ContextMenu.verify(['Expand', 'Refresh'], "04.01")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Expand Global Resources node.
        """
        HomePage.Workspaces.ResourcesTree.expand(global_resources)
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that following options are displayed:
            1.Page Templates.
            2.Page Templates (Legacy).
            3.Themes.
        """
        tree_items = ['Workspaces', 'Global Resources', 'Page Templates (Legacy)', 'Page Templates', 'Themes']
        HomePage.Workspaces.ResourcesTree.verify_items(tree_items, "05.01", "asequal")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Right click on Global Resources node > click Collapse.
        """
        HomePage.Workspaces.ResourcesTree.right_click(global_resources)
        HomePage.ContextMenu.select("Collapse")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that Global Resources node is collapsed.
        """
        HomePage.Workspaces.ResourcesTree.verify_collapsed(global_resources, "06.01")
        HomePage.Workspaces.ResourcesTree.verify_items(['Workspaces', 'Global Resources'], "06.02", "asequal")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on Global Resources node > click Refresh.
        """
        HomePage.Workspaces.ResourcesTree.right_click(global_resources)
        HomePage.ContextMenu.select("Refresh")
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Themes", 80)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify content area gets refreshed and it shows
            1.Page Templates.
            2.Page Templates (Legacy).
            3.Themes.
        """
        global_resources_folders = ['Page Templates (Legacy)', 'Page Templates', 'Themes']
        HomePage.Workspaces.ContentArea.verify_folders(global_resources_folders, "07.01", "asequal")
        HomePage.Workspaces.ContentArea.verify_files([], "07.02", "asequal")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Expand Global Resources node and right click on Page Templates folder.
        """
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Page Templates")
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that following options are displayed:
            1.Expand.
            2.Refresh.
            3.Security 
            --> Rules...
            --> Rules on this resource...
            --> Effective policy...
            4.Properties.
        """
        page_template_menu = ['Expand', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(page_template_menu, "08.01")
        HomePage.ContextMenu.verify(security_options, "08.02", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Expand Page Templates folder and right click on Standard sub-folder.
        """
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Page Templates->Standard")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that the following options are displayed:
            1.Expand.
            2.Refresh.
            3.Security 
            --> Rules...
            --> Rules on this resource...
            --> Effective policy...
            4.Properties.
        """
        standard_menu = ['Expand', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(standard_menu, "09.01")
        HomePage.ContextMenu.verify(security_options, "09.02", menu_path="Security")
        HomePage.Workspaces.ResourcesTree.select(global_resources)
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click Standard sub-folder under resource tree and right click on Blank from the content area.
        """
        HomePage.Workspaces.ResourcesTree.select(global_resources + "->Page Templates->Standard")
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Blank", 80)
        HomePage.Workspaces.ContentArea.right_click_on_file("Blank")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that the following options are displayed:
            1.Edit
            2.Copy Ctrl+C
            3.Security 
            --> Rules...
            --> Rules on this resource...
            --> Effective policy...
            4.Properties.
        """
        blank_file_menu = ['Edit', 'Copy Ctrl+C', 'Security', 'Properties']
        HomePage.ContextMenu.verify(blank_file_menu, "10.01")
        HomePage.ContextMenu.verify(security_options, "10.02", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right click on Custom sub-folder.
        """
        HomePage.Workspaces.ResourcesTree.right_click(global_resources + "->Page Templates->Custom")
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that the following options are displayed:
            1.Expand.
            2.Paste Ctrl+v (By default greyed out).
            3.Refresh.
            4.Security 
            --> Rules...
            --> Rules on this resource...
            --> Effective policy...
            5.Properties.
        """
        custome_folder_menu = ['Expand', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(custome_folder_menu, "11.01")
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], "11.02")
        HomePage.ContextMenu.verify(security_options, "11.03", menu_path="Security")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)