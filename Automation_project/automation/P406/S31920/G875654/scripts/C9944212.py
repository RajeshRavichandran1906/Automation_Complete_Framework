"""-----------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 20 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944212_TestClass(BaseTestCase):
    
    def test_C9944212(self):
        
        """
        TESTCASE VARIABLES
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on V4-Collaborative portal V4_Portal_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('V4_Portal_Context')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify context menu,
            Run
            Edit
            Delete DEL
            Add to Favorites
            Properties
        """
        v4_context_menu = ['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(v4_context_menu,'03.01')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        HomePage.ContextMenu.close()
       
        STEP_04 = """
            STEP 04 : Right click on V5 Portal V5Portal_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('V5Portal_Context')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify context menu,
            Run
            Edit
            Delete DEL
            Add to Favorites
            Properties
        """
        v5_context_menu = ['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(v5_context_menu,'04.01')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Right click on portal page Page_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('Page_Context')
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Edit
            Duplicate
            Delete DEL
            Share
            Share with...
            Properties
        """
        page_context_menu = ['Edit', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(page_context_menu,'05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)