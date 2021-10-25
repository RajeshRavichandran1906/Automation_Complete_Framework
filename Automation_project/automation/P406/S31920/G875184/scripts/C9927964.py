"""-------------------------------------------------------------------------------------------
Author Name : Robert/Joyal
Automated On : 16 December 2019
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927964_TestClass(BaseTestCase):
    
    def test_C9927964(self):
        
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
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """
            Step 03 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Designer".
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('Portal/Pages')
        utils.capture_screenshot('03.00', Step_03)
              
        Step_04 = """
            Step 04 : Right click on V4-Collaborative portal "V4_Portal_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('V4_Portal_Context')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
            Step 04 : Verification - Verify the following context menu:
            Run.
            Edit.
            Customizations (Remove my customizations/Remove customizations for all users).
            Manage alias.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Add to Favorites.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Run', 'Edit', 'Customizations', 'Manage Alias', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '04.01')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('V4_Portal_Context')
        expected_menus = ['Remove my customizations', 'Remove customizations for all users']
        HomePage.ContextMenu.verify(expected_menus, '04.02', menu_path='Customizations')
                
        HomePage.Workspaces.ContentArea.right_click_on_file('V4_Portal_Context')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '04.03', menu_path='Security')
        
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify= True)
        
        Step_05 = """
            Step 05 : Right click on portal page "Page_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Page_Context')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
            Step 05 : Verification - Verify the following context menu:
            Edit.
            Duplicate.
            Cut Ctrl+X.
            Copy Ctrl+C.
            Delete DEL.
            Unlink page.
            Unpublish/Publish.
            Hide/Show.
            Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
            Properties.
        """
        expected_menus = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Unlink Page', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '05.01')
        
        HomePage.Workspaces.ContentArea.right_click_on_file('Page_Context')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '05.02', menu_path='Security')
        
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify= True)
        
        Step_06 = """
        Step 06 : Right click on V5 Portal 'V5Portal_Context' in the content area.
        """
        HomePage.ContextMenu.close(location = 'top_middle')
        HomePage.Workspaces.ContentArea.right_click_on_folder('V5Portal_Context')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """
        Verify the following context menu:
        Open
        Run
        Edit
        Customizations (Remove my customizations/Remove customizations for all users)
        Paste Ctrl+V (greyed out by default)
        Delete DEL
        Add to Favorites
        Unpublish/Publish
        Hide/Show
        Security (Rules.../Rules on this resource.../Effective policy.../Owner...)
        Properties
        """
        expected_menus = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '06.01')
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'],'06.02')
        expected_menus = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        HomePage.ContextMenu.verify(expected_menus, '06.03', menu_path='Security')
        HomePage.ContextMenu.close(location = 'top_middle')
        expected_menus = ['Remove my customizations', 'Remove customizations for all users']
        HomePage.Workspaces.ContentArea.right_click_on_folder('V5Portal_Context')
        HomePage.ContextMenu.verify(expected_menus, '06.04', menu_path='Customizations')
        utils.capture_screenshot('06.01', Step_06_01, expected_image_verify= True)
        
        
        Step_07 = """
            Step 7 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00', Step_07)
        
        
    if __name__ == "__main__":
        unittest.main()