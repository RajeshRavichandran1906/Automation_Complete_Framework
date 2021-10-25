"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 24 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927963_TestClass(BaseTestCase):
    
    def test_C9927963(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """
            Step 03 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Designer_Framework"
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('Designer_Framework')
        utils.capture_screenshot('03.00', Step_03)
              
        Step_04 = """
            Step 04 : Right click on chart "DF_Chart" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Chart')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
            Step 04 : Verification - Verify the following context menu:
            Run.
            Run... (Run in new window/Run deferred/Run with SQL trace).
            Schedule Email
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Edit with text editor.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create Shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '04.01')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Chart')
        expected_menus = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        HomePage.ContextMenu.verify(expected_menus, '04.02', menu_path='Run...')
                
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Chart')
        expected_menus = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(expected_menus, '04.03', menu_path='Schedule')
                
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Chart')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '04.04', menu_path='Security')
        
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify= True)
        
        Step_05 = """
            Step 05 : Right click on page "DF_Page" in the content area.
        """
        HomePage.Home._core_utils.python_click_with_offset(900, 200)
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Page')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
            Step 05 : Verification - Verify the following context menu:
            Run.
            Run in new window.
            Edit.
            Download translations.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create Shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '05.01')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Page')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '05.02', menu_path='Security')
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify= True)
        
        Step_06 = """
            Step 06 : Right click on page "DF_Report" in the content area.
        """
        HomePage.Home._core_utils.python_click_with_offset(900, 200)
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Report')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """
            Step 06 : Verification - Verify the following context menu:
            Run.
            Run... (Run in new window/Run deferred/Run with SQL trace).
            Schedule Email
            Schedule (Email/FTP/Printer/Report Library/Repository).
            Edit.
            Edit with text editor.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create Shortcut.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '06.01')
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Report')
        expected_menus = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        HomePage.ContextMenu.verify(expected_menus, '06.02', menu_path='Schedule')
        HomePage.ContextMenu.close(location = 'top_middle')
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Report')
        expected_menus = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        HomePage.ContextMenu.verify(expected_menus, '06.03', menu_path='Run...')
        HomePage.Workspaces.ContentArea.right_click_on_file('DF_Report')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '06.04', menu_path='Security')
        
        utils.capture_screenshot('06.01', Step_06_01, expected_image_verify= True)
         
        Step_07 = """
            Step 7 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00', Step_07)
        
    if __name__ == "__main__":
        unittest.main()