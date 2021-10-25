"""-----------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 07 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944210_TestClass(BaseTestCase):
    
    def test_C9944210(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        schedule = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on My Workspace tab.
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Right-click on report Report_Context.
        """
        HomePage.MyWorkspace.right_click_on_item('Report_Context')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify context menu
            Run.
            Run... (Run in new window)
            Schedule Email
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        report_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(report_context_menu,'03.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '03.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Report_Context')
        HomePage.ContextMenu.verify(schedule, '03.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
       
        STEP_04 = """
            STEP 04 : Right-click on chart Chart_Context
        """
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Chart_Context')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify context menu,
            Run.
            Run... (Run in new window)
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Schedule Email
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        chart_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(chart_context_menu,'04.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '04.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Chart_Context')
        HomePage.ContextMenu.verify(schedule, '04.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Right-click on item Visual_Context.
        """
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Visual_Context')
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Run
            Run... (Run in new window)
            Edit
            Duplicate
            Delete DEL
            Add to Favorites
            Share
            Share with...
            Properties
        """
        visual_context_menu = ['Run', 'Run...', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(visual_context_menu,'05.01')
        HomePage.ContextMenu.verify(['Run in new window'], '05.02', menu_path='Run...')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Right-click on document Document_Context
        """
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Document_Context')
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify context menu,
            Run.
            Run... (Run in new window)
            Schedule Email
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        document_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(document_context_menu,'06.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '06.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', x=-5,y=-5)
        HomePage.MyWorkspace.right_click_on_item('Document_Context')
        HomePage.ContextMenu.verify(schedule, '06.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, True)
       
        STEP_07 = """
            STEP 07 : Right-click on alert Alert_Context.
        """
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Alert_Context')
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify context menu,
            Run.
            Run... (Run in new window)
            Schedule Email
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        alert_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(alert_context_menu,'07.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '07.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('Alert_Context')
        HomePage.ContextMenu.verify(schedule, '07.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)