"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 18 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927962_TestClass(BaseTestCase):
    
    def test_C9927962(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """created local function to reduce the repeated action for closing submenu 
        because requirement is need to verify submenu for all the items and folders under domain"""
        
        def close_submenu(File_name,click_location ='middle'):
            NAVIGATION_TOOLBAR = utils.validate_and_get_webdriver_object(HomePage.Workspaces.NavigationBar.locators.navigation_bar_css,"Navigation_bar")
            HomePage.ContextMenu.close(NAVIGATION_TOOLBAR, location = click_location)
            HomePage.Workspaces.ContentArea.right_click_on_file(File_name)
        
        """
        TESTCASE VARIABLES
        """
        REPORT_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 
                               'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        CHART_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 
                              'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']

        
        VISUAL_CONTEXT_MENU = ['Run', 'Run...', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 
                            'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        DOC_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 
                            'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        ALERT_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 
                              'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        CENTURY_SALES_CONTEXT_MENU = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 
                                      'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        
        
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
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "IA/Visualization".
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G784912->IA/Visualization')
        utils.capture_screenshot('03.00', Step_03) 
        
        Step_04 = """Right click on report "Report_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Report_Context')
        utils.capture_screenshot('04.00', Step_04)
 
        Step_04_01 = """Verification -Verify the context menu:
        Run.
        Run... (Run in new window/Run deferred/Run with SQL trace).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(REPORT_CONTEXT_MENU,'04.01')
        HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'],'04.02',menu_path='Schedule')
        close_submenu('Report_Context')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred', 'Run with SQL trace'],'04.03',menu_path='Run...')
        close_submenu('Report_Context')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'04.04',menu_path='Security')
        utils.capture_screenshot('04.01', Step_04_01,expected_image_verify=True)
         
        Step_05 = """Step 05:Right click on chart "Chart_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Chart_Context')
        utils.capture_screenshot('05.00', Step_05)
         
        Step_05_01 = """Verification- Step 05.01 Verify the context menu:
        Run.
        Run... (Run in new window/Run deferred/Run with SQL trace).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(CHART_CONTEXT_MENU,'05.01')
        HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'],'05.02',menu_path='Schedule')
        close_submenu('Chart_Context',click_location='bottom_right')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred', 'Run with SQL trace'],'05.03',menu_path='Run...')
        close_submenu('Chart_Context',click_location='bottom_right')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'05.04',menu_path='Security')
        utils.capture_screenshot('05.01',Step_05_01,expected_image_verify=True)
 
 
        Step_06 = """Step 06 Right click on item "Visual_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Visual_Context')
        utils.capture_screenshot('06.00', Step_06)
         
        Step_06_01 = """ Verification -Verify the context menu:
        Run.
        Run... (Run in new window).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(VISUAL_CONTEXT_MENU,'06.01')
        HomePage.ContextMenu.verify(['Run in new window'],'06.02',menu_path='Run...')
        close_submenu('Visual_Context')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'06.03',menu_path='Security')
        utils.capture_screenshot('06.01', Step_06_01,expected_image_verify=True)
        
        Step_07 = """Step 07 Right click on document "Document_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Document_Context')
        utils.capture_screenshot('07.00', Step_07)

        Step_07_01 = """ Verification- Step 07.01 Verify the context menu:
        Run.
        Run... (Run in new window/Run deferred/Run with SQL trace).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(DOC_CONTEXT_MENU,'07.01')
        HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'],'07.02',menu_path='Schedule')
        '''Document_context is middle item if click_location is middle it clicks the first option in context menu so bottom_right'''
        close_submenu('Document_Context',click_location='bottom_right')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred', 'Run with SQL trace'],'07.03',menu_path='Run...')
        close_submenu('Document_Context',click_location='bottom_right')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'07.04',menu_path='Security')
        utils.capture_screenshot('07.01', Step_07_01,expected_image_verify=True)
        
        Step_08 = """Step 08 Right click on alert "Alert_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Alert_Context')
        utils.capture_screenshot('08.00',Step_08)
    
        Step_08_01 = """
        Step 08.01 Verify the context menu:
        Run.
        Run... (Run in new window/Run deferred).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Create shortcut.
        Delete DEL.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(ALERT_CONTEXT_MENU,'08.01')
        HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'],'08.02',menu_path='Schedule')
        close_submenu('Alert_Context')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'],'08.03',menu_path='Run...')
        close_submenu('Alert_Context')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'08.04',menu_path='Security')
        utils.capture_screenshot('08.01',Step_08_01,expected_image_verify=True)
        
        
        Step_09 = """ Step 09 Right click on sample content "centurysales" in the content area.
        """
        close_submenu('Alert_Context')
        HomePage.Workspaces.ContentArea.right_click_on_folder('centurysales')
        utils.capture_screenshot('09.00',Step_09)

        Step_09_01 = """ Step 09.01 Verify the context menu:
        Open.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Paste Ctrl+V.
        Delete.
        Refresh.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(CENTURY_SALES_CONTEXT_MENU,'09.01')
        HomePage.ContextMenu.verify(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'],'09.02',menu_path='Security')
        utils.capture_screenshot('09.01',Step_09_01,expected_image_verify=True)
        
        Step_10 = """
            Step 10 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('10.00', Step_10)
        
    if __name__ == "__main__":
        unittest.main()