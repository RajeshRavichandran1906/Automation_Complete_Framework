"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 18 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927995_TestClass(BaseTestCase):
    
    def test_C9927995(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """
            Step 03 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "ReportingObject".
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('ReportingObject')
        utils.capture_screenshot('03.00', Step_03)
              
        Step_04 = """
            Step 04 : Right click on "ReportingObject_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('ReportingObject_Context')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
            Step 04 : Verification - Verify the following context menu:
            Run.
            Run... (Run in new window/Run deferred).
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Create shortcut.
            Delete DEL.
            New (Designer[Workbook/Chart], InfoAssist[Report/Chart/Document]).
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Run...', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'open_in_new New', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '04.01')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('ReportingObject_Context')
        expected_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_menus, '04.02', menu_path='Run...')
        
        NAVIGATION_TOOLBAR = utils.validate_and_get_webdriver_object(HomePage.Workspaces.NavigationBar.locators.navigation_bar_css,"Navigation_bar")
        HomePage.ContextMenu.close(NAVIGATION_TOOLBAR, location='bottom_right')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('ReportingObject_Context')
        expected_menus = ['Report', 'Chart', 'Document']
        HomePage.ContextMenu.verify(expected_menus, '04.03', menu_path='New->InfoAssist')
        HomePage.ContextMenu.close(NAVIGATION_TOOLBAR, location='bottom_right')
        HomePage.Workspaces.ContentArea.right_click_on_file('ReportingObject_Context')
        expected_menus = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '04.04', menu_path='Security')
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify= True)
        
        
        Step_05 = """
            Step 5 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('05.00', Step_05)
        
    if __name__ == "__main__":
        unittest.main()