"""---------------------------------------------------------------
Author Name : vishnu_priya
Automated On : 30-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925905_TestClass(BaseTestCase):
    
    def test_C9925905(self):
        
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
        workspaces = 'Workspaces'
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as basic User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspaces, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Designer.
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', 'DesignerChart_Context', homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on chart DesignerChart_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...','Add to Favorites','Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred']
        homepage.verify_repository_folder_item_context_menu(designer_chart_context, expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(designer_chart_context, "Run...", expected_run_submenu, msg="Step 03.02", close_context_menu_css="#search-field-desktop")
        
        """
            STEP 04 : Right click on workbook Workbook_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run in new window','Add to Favorites','Properties']
        homepage.verify_repository_folder_item_context_menu(workbook_context, expected_context_menu, msg="Step 04.01")
        
        """
            STEP 05 : Right click on page DesignerPage_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run in new window','Add to Favorites','Properties']
        homepage.verify_repository_folder_item_context_menu(designer_page_context, expected_context_menu, msg="Step 05.01")
        
        """
            STEP 06 : Right click on Designer portal V5Portal_Context
            Verify context menu
        """
        expected_context_menu = ['Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        homepage.verify_repository_folder_item_context_menu(v5_portal_Context, expected_context_menu, msg="Step 06.01")
        
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()