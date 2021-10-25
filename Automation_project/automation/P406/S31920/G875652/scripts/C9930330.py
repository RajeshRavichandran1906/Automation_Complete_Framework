"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 21 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930330_TestClass(BaseTestCase):
    
    def test_C9930330(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        STANDARD_CONTEXT_MENU=['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        Schedule_SUBMENU =['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        VISUAL_CONTEXT_MENU=['Run', 'Run...', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        STANDARD_RUN_SUBMENU=['Run in new window', 'Run deferred']
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
         
        Step_03 = """Right-click on report Report_Context
        """
        HomePage.MyWorkspace.right_click_on_item('Report_Context')
        utils.capture_screenshot('03.00', Step_03) 
        
        Step_03_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(STANDARD_CONTEXT_MENU,'03.01')
        HomePage.ContextMenu.verify(STANDARD_RUN_SUBMENU,'03.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('Report_Context')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'03.03', menu_path='Schedule')
        utils.capture_screenshot('03.01',Step_03_01,expected_image_verify=True) 

        Step_04 = """Right-click on chart Chart_Context..
        """
        HomePage.MyWorkspace.right_click_on_item('Chart_Context')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(STANDARD_CONTEXT_MENU,'04.01')
        HomePage.ContextMenu.verify(STANDARD_RUN_SUBMENU,'04.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('Chart_Context')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'04.03', menu_path='Schedule')
        utils.capture_screenshot('04.01',Step_04_01,expected_image_verify=True)
        
        Step_05 = """Right-click on chart Visual_Context..
        """
        HomePage.MyWorkspace.right_click_on_item('Visual_Context')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(VISUAL_CONTEXT_MENU,'05.01')
        HomePage.ContextMenu.verify(['Run in new window'],'05.02', menu_path='Run...')
        
        utils.capture_screenshot('05.01',Step_05_01,expected_image_verify=True)
        
        Step_06 = """Right-click on chart Document_Context..
        """
        HomePage.MyWorkspace.right_click_on_item('Document_Context')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(STANDARD_CONTEXT_MENU,'06.01')
        HomePage.ContextMenu.verify(STANDARD_RUN_SUBMENU,'06.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('Document_Context')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'06.03', menu_path='Schedule')

        utils.capture_screenshot('06.01',Step_06_01,expected_image_verify=True)

        Step_07 = """Right-click on chart Alert_Context..
        """
        HomePage.MyWorkspace.right_click_on_item('Alert_Context')
        utils.capture_screenshot('07.00', Step_07)
        
        Step_07_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(STANDARD_CONTEXT_MENU,'07.01')
        HomePage.ContextMenu.verify(STANDARD_RUN_SUBMENU,'07.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('Alert_Context')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'07.03', menu_path='Schedule')
        
        utils.capture_screenshot('07.01',Step_07_01,expected_image_verify=True)
        
        Step_08 = """
            Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00', Step_08)
        
    if __name__ == "__main__":
        unittest.main()