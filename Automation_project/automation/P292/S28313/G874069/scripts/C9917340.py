"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 21-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9917340_TestClass(BaseTestCase):
    
    def test_C9917340(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->IA/Visualization"
        report_context = "Report_Context"
        chart_context = "Chart_Context"
        visual_context = "Visual_Context"
        document_context = "Document_Context"
        alert_context = "Alert_Context"
        centurysales = "centurysales"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder IA/Visualization.
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', 'Alert_Context', homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right-click on report Report_Context
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(report_context, expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(report_context, "Run...", expected_run_submenu, msg="Step 03.02")
        homepage.verify_repository_folder_item_context_submenu(report_context, "Schedule", expected_schedule_submenu, msg="Step 03.03")
        homepage.verify_repository_folder_item_context_submenu(report_context, "Security", expected_security_submenu, msg="Step 03.04")
        
        """
            STEP 04 : Right-click on chart Chart_Context
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(chart_context, expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(chart_context, "Run...", expected_run_submenu, msg="Step 04.02", close_context_menu_css = 'div.left-main-panel')
        homepage.verify_repository_folder_item_context_submenu(chart_context, "Schedule", expected_schedule_submenu, msg="Step 04.03", close_context_menu_css = 'div.left-main-panel')
        homepage.verify_repository_folder_item_context_submenu(chart_context, "Security", expected_security_submenu, msg="Step 04.04", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 05 : Right-click on item Visual_Context
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(visual_context, expected_context_menu, msg="Step 05.01")
        homepage.verify_repository_folder_item_context_submenu(visual_context, "Run...", expected_run_submenu, msg="Step 05.02", close_context_menu_css = 'div.left-main-panel')
        homepage.verify_repository_folder_item_context_submenu(visual_context, "Security", expected_security_submenu, msg="Step 05.03", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 06 : Right-click on document Document_Context
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(document_context, expected_context_menu, msg="Step 06.01")
        homepage.verify_repository_folder_item_context_submenu(document_context, "Run...", expected_run_submenu, msg="Step 06.02")
        homepage.verify_repository_folder_item_context_submenu(document_context, "Schedule", expected_schedule_submenu, msg="Step 06.03", close_context_menu_css = 'div.left-main-panel')
        homepage.verify_repository_folder_item_context_submenu(document_context, "Security", expected_security_submenu, msg="Step 06.04", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 07 : Right-click on alert Alert_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(alert_context, expected_context_menu, msg="Step 07.01")
        homepage.verify_repository_folder_item_context_submenu(alert_context, "Run...", expected_run_submenu, msg="Step 07.02", close_context_menu_css="#search-field-desktop")
        homepage.verify_repository_folder_item_context_submenu(alert_context, "Schedule", expected_schedule_submenu, msg="Step 07.03", close_context_menu_css = 'div.left-main-panel')
        homepage.verify_repository_folder_item_context_submenu(alert_context, "Security", expected_security_submenu, msg="Step 07.04", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 08 : Right-click on sample content centurysales
            Verify context menu
        """
        expected_context_menu = ['Open', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(centurysales, expected_context_menu, msg="Step 08.01")
        homepage.verify_repository_folder_item_context_submenu(centurysales, "Security", expected_security_submenu, msg="Step 08.02", close_context_menu_css = 'div.left-main-panel')
        
        """
            STEP 09 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()