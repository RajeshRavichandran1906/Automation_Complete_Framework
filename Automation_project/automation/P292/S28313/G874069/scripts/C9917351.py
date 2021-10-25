"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 22-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9917351_TestClass(BaseTestCase):
    
    def test_C9917351(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->Designer"
        designer_chart_context = "DesignerChart_Context"
        workbook_context = "Workbook_Context"
        designer_page_context = "DesignerPage_Context"
        v5_portal_Context = "V5Portal_Context"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Designer.
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', 'DesignerChart_Context', homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on chart DesignerChart_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(designer_chart_context, expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(designer_chart_context, "Run...", expected_run_submenu, msg="Step 03.02", close_context_menu_css="#search-field-desktop")
        homepage.verify_repository_folder_item_context_submenu(designer_chart_context, "Schedule", expected_schedule_submenu, msg="Step 03.03")
        homepage.verify_repository_folder_item_context_submenu(designer_chart_context, "Security", expected_security_submenu, msg="Step 03.04")
        
        """
            STEP 04 : Right click on workbook Workbook_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(workbook_context, expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(workbook_context, "Security", expected_security_submenu, msg="Step 04.02")
        
        """
            STEP 05 : Right click on page DesignerPage_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(designer_page_context, expected_context_menu, msg="Step 05.01")
        homepage.verify_repository_folder_item_context_submenu(designer_page_context, "Security", expected_security_submenu, msg="Step 05.02", close_context_menu_css="#search-field-desktop")
        
        """
            STEP 06 : Right click on Designer portal V5Portal_Context
            Verify context menu
        """
        expected_context_menu = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_customizations_submenu = ['Remove my customizations', 'Remove customizations for all users']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(v5_portal_Context, expected_context_menu, msg="Step 06.01")
        homepage.verify_repository_folder_item_context_submenu(v5_portal_Context, "Customizations", expected_customizations_submenu, msg="Step 06.02")
        homepage.verify_repository_folder_item_context_submenu(v5_portal_Context, "Security", expected_security_submenu, msg="Step 06.03")
        
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()