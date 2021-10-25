"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 17 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9927961_TestClass(BaseTestCase):
    
    def test_C9927961(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """Created local function to reduce the repeated action for closing submenu 
        because requirement is need to verify submenu for all the items and folders under domain"""
        
        def close_submenu(File_name, click_location='middle'):
            NAVIGATION_TOOLBAR = utils.validate_and_get_webdriver_object(HomePage.Workspaces.NavigationBar.locators.navigation_bar_css, "Navigation_bar")
            HomePage.ContextMenu.close(NAVIGATION_TOOLBAR, location=click_location)
            HomePage.Workspaces.ContentArea.right_click_on_file(File_name)
        
        """
        TESTCASE VARIABLES
        """
        IA_Report_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 
                          'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        
        COLLABORATIVE_PORTAL_MENU = ['Run', 'Edit', 'Customizations', 'Manage Alias', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL',
                                     'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        
        HTML_CONTEXT_MENU = ['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut',
                             'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        
        SHORTCUT_CONTEXT_MENU = ['Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        
        FOLDER_CONTEXT_MENU = ['Open', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh',
                               'Security', 'Share', 'Share with...', 'Properties']
        
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
         
        Step_03 = """Expand "P406_S31920" workspace from the resource tree > Click on "My Content" folder
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->My Content')
        utils.capture_screenshot('03.00', Step_03) 
        
        Step_03_01 = """ Step 03.01 Verify the folder'Collaborative Portal Resources and items 
        Report, Portal, Shortcut & HTML page items are available under My Content folder.
        """
        HomePage.Workspaces.ContentArea.verify_files(['Collaborative Portal', 'HTML_Content', 'IA_Report', 'IA_Report - Shortcut'], '03.01')
        HomePage.Workspaces.ContentArea.verify_folders(['Collaborative Portal Resources'], '03.02')
        utils.capture_screenshot('03.01', Step_03_01, expected_image_verify=True)
        
        Step_04 = """ Right click on report "IA_Report" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('IA_Report')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """"Verify the following context menu:
        Run.
        Run... (Run in new window/Run deferred/Run with SQL trace).
        Schedule Email
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Security (Rules on this resource.../Effective Policy...).
        Share.
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(IA_Report_MENU, "04.01")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred', 'Run with SQL trace'], "04.02", menu_path="Run...")
        close_submenu('IA_Report', click_location='bottom_right')
        HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'], '04.03', menu_path='Schedule')
        close_submenu('IA_Report', click_location='bottom_right')
        HomePage.ContextMenu.verify(['Rules on this resource...', 'Effective policy...'], '04.04', menu_path='Security')
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify=True)
        
        Step_05 = """Right click on portal "Collaborative Portal" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Collaborative Portal')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
        Verify the following context menu:
        Run.
        Edit.
        Customizations (Remove my customizations/Remove customizations for all users).
        Manage alias.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Delete DEL.
        Add to Favorites.
        Security (Rules on this resource.../Effective Policy...).
        Share.
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(COLLABORATIVE_PORTAL_MENU, "05.01")
        HomePage.ContextMenu.verify(['Remove my customizations', 'Remove customizations for all users'], "05.02", menu_path="Customizations")
        close_submenu('Collaborative Portal', click_location='bottom_right')
        HomePage.ContextMenu.verify(['Rules on this resource...', 'Effective policy...'], '05.03', menu_path='Security')
        HomePage.ContextMenu.close()
        #HomePage.ContextMenu.close()
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify=True)
        
        Step_06 = """Right click on HTML item "HTML_Content" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('HTML_Content')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """Verify the context menu:
        View.
        View in new window.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Security (Rules on this resource.../Effective Policy...).
        Share.
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(HTML_CONTEXT_MENU, "06.01")
        HomePage.ContextMenu.verify(['Rules on this resource...', 'Effective policy...'], "06.02", menu_path="Security")
        utils.capture_screenshot('06.01', Step_06_01, expected_image_verify=True)
        
        Step_07 = """Right click on Shortcut "IA_Report - Shortcut" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('IA_Report - Shortcut')
        utils.capture_screenshot('07.00', Step_07)
        
        Step_07_01 = """Verify the following context menu:

        Verify the following context menu:
        Delete DEL
        Add to Favorites
        Security (Rules on this resource.../Effective Policy...)
        Share
        Share with...
        Properties
        """
        HomePage.ContextMenu.verify(SHORTCUT_CONTEXT_MENU, "07.01")
        HomePage.ContextMenu.verify(['Rules on this resource...', 'Effective policy...'], '07.02', menu_path='Security')
        utils.capture_screenshot('07.01', Step_07_01, expected_image_verify=True)       
        
        Step_08 = """Right click on 'Collaborative Portal Resources' folder in the content area
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder('Collaborative Portal Resources')
        utils.capture_screenshot('08.00', Step_08)
        
        Step_08_01 = """
        Verify the following context menu:
        Open
        Duplicate
        Cut Ctrl+X
        Copy Ctrl+C
        Paste Ctrl+V (greyed out)
        Delete DEK
        Refresh
        Security (Rules on this resource.../Effective Policy...)
        Share
        Share with...
        Properties
        """
        HomePage.ContextMenu.verify(FOLDER_CONTEXT_MENU, "08.01")
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], '08.02')
        HomePage.ContextMenu.verify(['Rules on this resource...', 'Effective policy...'], '08.03', menu_path='Security')
        utils.capture_screenshot('08.01', Step_08_01, expected_image_verify=True)
        
        Step_09 = """
            Step 9 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('09.00', Step_09)
        
    if __name__ == "__main__":
        unittest.main()
