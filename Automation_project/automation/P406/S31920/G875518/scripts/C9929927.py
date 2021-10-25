"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 22 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929927_TestClass(BaseTestCase):
    
    def test_C9929927(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        CONTEXT_MENU_ITEMS=['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Share', 'Share with...', 'Properties']
        
        STEP_01 = """
            STEP 01 : Sign in as gs_dev1@ibi.com.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click Workspaces button
        """
        HomePage.Banner.click_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand Workspaces>My Workspace > My Content from the tree
                    Right click on My Content from the tree
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.expand("Workspaces->My Workspace->My Content")
        
        HomePage.Workspaces.ResourcesTree.right_click("My Content")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        STEP_03_01 = """
            STEP 03.01 : Verify My Content right-click menu from the tree
        """
        HomePage.ContextMenu.verify(CONTEXT_MENU_ITEMS, 02.01)
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        
