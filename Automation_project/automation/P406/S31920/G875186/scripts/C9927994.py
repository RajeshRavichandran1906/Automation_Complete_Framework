"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 31 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.locators.paris_home_page import Workspaces

class C9927994_TestClass(BaseTestCase):
    
    def test_C9927994(self):
        
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
            Step 03.00 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Portal/Pages".
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G784912")
        HomePage.Workspaces.ContentArea.double_click_on_folder("Portal/Pages")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right click on chart "V4_Portal_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("V4_Portal_Context")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
           Step 04.00 : Verify the context menu: 
            Run.
            Edit.
            Customizations (Remove my customizations/Remove customizations for all users).
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Edit', 'Customizations', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "04.01")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "04.02", menu_path = "Security")
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5Portal_Context")
        expected_menus = ['Remove my customizations','Remove customizations for all users']
        HomePage.ContextMenu.verify(expected_menus, "04.03", menu_path = "Customizations")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Right click on chart "Page_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Page_Context")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
           Step 05.00 : Verify the context menu: 
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Unlink page.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties..
        """
        expected_menus = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Unlink Page', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, "05.02", menu_path = "Security")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        
        STEP_06 = """
        Right click on V5 portal "V5Portal_Context" in the content area.
        """
        Nav_bar_elem = utils.validate_and_get_webdriver_object("div.toolbar ","nav_bar_css")
        HomePage.ContextMenu.close(Nav_bar_elem,location="middle")
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5Portal_Context")
        utils.capture_screenshot("06.00", STEP_06, expected_image_verify = True)
        
        STEP_06_01 = """
        Verify the context menu:
        Open
        Run
        Edit
        Customizations (Remove my customizations/Remove customizations for all users)
        Paste Ctrl+V (greyed out by default)
        Delete DEL
        Add to Favorites
        Unpublish/Publish
        Hide/Show
        Security (Rules on this resource.../Effective policy.../Owner...)
        Properties
        """
        expected_menus = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, step_num='06.01')
        expected_menus = ['Remove my customizations','Remove customizations for all users']
        HomePage.ContextMenu.verify(expected_menus, "06.02", menu_path = "Customizations")
        HomePage.ContextMenu.close(Nav_bar_elem,location="middle")
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5Portal_Context")
        HomePage.ContextMenu.verify(expected_menus, "06.04", menu_path = "Security")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)

if __name__ == "__main__":
    unittest.main() 