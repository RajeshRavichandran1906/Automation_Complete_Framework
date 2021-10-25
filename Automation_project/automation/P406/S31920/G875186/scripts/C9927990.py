"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 18 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927990_TestClass(BaseTestCase):
    
    def test_C9927990(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Right-click on "P406_S31920" workspace from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify the Context Menu:
            Expand/Collapse.
            Paste Ctrl+V(Grayed out).
            Refresh.
            Security (Rules on this resource.../Effective Policy...).
            Properties.
        """
        expected_menus = ['Expand', 'Paste Ctrl+V', 'Refresh', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Click "Expand" option.
        """
        HomePage.ContextMenu.select("Expand")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : From the Resource Tree > Right click on "My Content" folder under "P406_S31920" workspace
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->My Content")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verify the Context Menu:
            Expand/Collapse.
            Paste Ctrl+V (Grayed out).
            Delete DEL.
            Refresh.
            Security (Rules on this resource.../Effective Policy...).
            Share/Unshare.
            Share with.
            Properties.
        """
        expected_menus = ['Expand', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Security', 'Unshare', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Paste Ctrl+V']
        HomePage.ContextMenu.verify_disabled_options(expected_menus, "05.02")
        expected_menus = ['Rules on this resource...', 'Effective policy...']
        HomePage.ContextMenu.verify(expected_menus, "05.03", menu_path = "Security")
        HomePage.ContextMenu.close(location='top_right')
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
       
        STEP_06 = """
            Step 06.00 : From the Resource Tree > Right click on "Hidden Content" folder under "P406_S31920" workspace
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->Hidden Content")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify the Context Menu:
            Expand/Collapse.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Paste Ctrl+V (Grayed out).
            Delete DEL.
            Refresh.
            Unpublish/Publish.
            Show/Hide.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Expand', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Show', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "06.01")
        expected_menus = ['Paste Ctrl+V']
        HomePage.ContextMenu.verify_disabled_options(expected_menus, "06.02")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "06.03", menu_path = "Security")
        HomePage.ContextMenu.close(location='top_right')
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : From the Resource Tree > "P406_S31920" workspace from the resource tree > Right-click on "G784912" folder
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G784912")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify the Context Menu:
            Expand/Collapse.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Paste Ctrl+V(Grayed out).
            Delete DEL.
            Refresh.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Expand', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "07.01")
        expected_menus = ['Paste Ctrl+V']
        HomePage.ContextMenu.verify_disabled_options(expected_menus, "07.02")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "07.03", menu_path = "Security")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)
        
if __name__ == "__main__":
    unittest.main() 