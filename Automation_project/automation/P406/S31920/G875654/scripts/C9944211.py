"""-----------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 10 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944211_TestClass(BaseTestCase):
    
    def test_C9944211(self):
        
        """
        TESTCASE VARIABLES
        """
        HomePage = ParisHomePage(self.driver)
        schudle_menu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        
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
            STEP 03 : Right click on chart DF_Chart
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Chart')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify context menu,
            Run.
            Run... (Run in new window).
            Schedule (Email, FTP, Printer, Report Library, Repository)
            Edit.
            Duplicate.
            Delete DEL.
            Add to Favorites.
            Share
            Share with...
            Properties.
        """
        chart_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(chart_context_menu,'03.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '03.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('DF_Chart')
        HomePage.ContextMenu.verify(schudle_menu, '03.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
       
        STEP_04 = """
            STEP 04 : Right click on workbook DF_Report
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Report')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify context menu,
            Run.
            Run... (Run in new window).
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
        HomePage.ContextMenu.verify(report_context_menu,'04.01')
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred'], '04.02', menu_path='Run...')
        HomePage.ContextMenu.close(location='top_middle', y=-5)
        HomePage.MyWorkspace.right_click_on_item('DF_Report')
        HomePage.ContextMenu.verify(schudle_menu, '04.03', menu_path='Schedule')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Right click on page DF_Page
        """
        HomePage.MyWorkspace.right_click_on_item('DF_Page')
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu,
            Run
            Run in new window.
            Edit
            Download translations...
            Duplicate
            Delete DEL
            Add to Favorites
            Share
            Share with...
            Properties
        """
        page_context_menu = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        HomePage.ContextMenu.verify(page_context_menu,'05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)