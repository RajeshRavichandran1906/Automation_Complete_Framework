"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 21 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930331_TestClass(BaseTestCase):
    
    def test_C9930331(self):
        
        """
        TESTCASE VARIABLES
        """
        HomePage = ParisHomePage(self.driver)
        DF_Chart=['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        DF_Chart_SUBMENU=['Run in new window']
        Schedule_SUBMENU =['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        DF_Report=['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        DF_Report_SUBMENU=['Run in new window']
        DPAGE_CONTEXT_MENU=['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        
            
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        HomePage.Home._utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """Right click on chart DF_Chart
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Chart')
        HomePage.Home._utils.capture_screenshot('03.00', Step_03) 
        
        Step_03_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Schedule Email
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(DF_Chart,'03.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'],'03.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('DF_Chart')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'03.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot('03.01',Step_03_01,expected_image_verify=True) 

        Step_04 = """Right click on report DF_Report...
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Report')
        HomePage.Home._utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """ Verify the following Context Menu:
        Run.
        Run... (Run in new window)
        Edit.
        Schedule Email
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(DF_Report,'04.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'],'04.02', menu_path='Run...')
        HomePage.MyWorkspace.right_click_on_item('DF_Report')
        HomePage.ContextMenu.verify(Schedule_SUBMENU,'04.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot('04.01',Step_04_01,expected_image_verify=True)
        
        Step_05 = """Right click on page DF_Page.
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Page')
        HomePage.Home._utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """ Verify the following Context Menu:
        Run.
        Run in new window.
        Edit.
        Download translations...
        Duplicate.
        Delete DEL.
        Add to Favorites.
        Share
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(DPAGE_CONTEXT_MENU,'05.01')
        HomePage.Home._utils.capture_screenshot('05.01',Step_05_01,expected_image_verify=True)

        Step_06 = """
            Step 6 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('06.00', Step_06)
        
    if __name__ == "__main__":
        unittest.main()