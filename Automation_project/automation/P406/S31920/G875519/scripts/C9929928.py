"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 31 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929928_TestClass(BaseTestCase):
    
    def test_C9929928(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign In to WebFOCUS as Author
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Expand Workspaces>My Workspace>Right-click Shared Content in tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Workspaces.ResourcesTree.expand("My Workspace")
        HomePage.Workspaces.ResourcesTree.select("My Workspace")
        HomePage.Workspaces.ResourcesTree.right_click("Shared Content")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify Shared Content right-click menu from the tree
        """
        HomePage.ContextMenu.verify(['Expand', 'Refresh'], "03.01")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04.00 : Right-click on Shared Content in content area.
        """
        HomePage.Workspaces.ResourcesTree.select("My Workspace")
        HomePage.Workspaces.ResourcesTree.select("Shared Content")
        
        HomePage.Workspaces.ContentArea.right_click_on_folder("HP Cloud Author user 1")
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify Shared Content folder's right click menu from work area(under Folder)
        """
        HomePage.ContextMenu.verify(['Open', 'Refresh', 'Properties'], "04.01")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        
