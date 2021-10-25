"""-------------------------------------------------------------------------------------------
Author Name : Prasanth
Automated On : 29 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930332_TestClass(BaseTestCase):
    
    def test_C9930332(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        PORTAL_CONTEXT_MENU=['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties'] 
        PAGE_CONTEXT_MENU=['Edit', 'Duplicate', 'Delete DEL', 'Share', 'Share with...', 'Properties']
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_03 = """Right click on V4-Collaborative portal V4PortalContext.
        """
        HomePage.MyWorkspace.right_click_on_item('V4_Portal_Context')
        utils.capture_screenshot('03.00', Step_03)
        
        Step_03_01 = """ Verify the following Context Menu:
        Run.
        Edit.
        Delete DEL.
        Add to Favorites.
        Properties.
        """
        HomePage.ContextMenu.verify(PORTAL_CONTEXT_MENU,'03.01')
        utils.capture_screenshot('03.01',Step_03_01,expected_image_verify=True)
        
        Step_04 = """Right click on V5 Portal V5Portal_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('V5Portal_Context')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
        Verify context menu,
        Run.
        Edit.
        Delete DEL.
        Add to Favorites.
        Properties.
        """
        HomePage.ContextMenu.verify(PORTAL_CONTEXT_MENU,'04.01')
        utils.capture_screenshot('04.01',Step_04_01,expected_image_verify=True)
        
        Step_05 = """Right click on portal page Page_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('Page_Context')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """ Verify the following Context Menu:
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(PAGE_CONTEXT_MENU,'05.01')
        utils.capture_screenshot('05.01',Step_05_01,expected_image_verify=True)
        
        Step_05 = """
            Step 5 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('05.00', Step_05)
        
    if __name__ == "__main__":
        unittest.main()