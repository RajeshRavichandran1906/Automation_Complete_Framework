"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 29-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925889_TestClass(BaseTestCase):
    
    def test_C9925889(self):
        
        """
            Class Objects
        """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            Common Variables
        """
        folder_path = "P292_S10660->G671733->My Content"
        contents = ["Margin by Product Category", "Retail Samples", "Retail Sales Filter Panel", "Margin by Product Category - Shortcut"]
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain Tree >> Click on 'My Content' folder underneath 'P292_S10660' domain
            Verify items Report, Portal, Shortcut & HTML page items are available under My Content folder
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', contents[1], homepage.home_page_short_timesleep)
        homepage.verify_items_in_grid_view(contents, 'asin', "Step 02.01 : Verify items Report, Portal, Shortcut & HTML page items are available under My Content folder")
        
        """
            STEP 03 : Right click on report Margin by Product Category
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred']
        expected_schedule_submenu = ['Email', 'Printer', 'Report Library', 'Repository']
        homepage.verify_repository_folder_item_context_menu(contents[0], expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(contents[0], "Run...", expected_run_submenu, msg="Step 03.02")
        homepage.verify_repository_folder_item_context_submenu(contents[0], "Schedule", expected_schedule_submenu, msg="Step 03.03")
        
        """
            STEP 04 : Right click on portal Retail Samples
            Verify context menu
        """
        expected_context_menu = ['Run', 'Customizations', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        customizations_submenu = ['Remove my customizations']
        homepage.verify_repository_folder_item_context_menu(contents[1], expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(contents[1], "Customizations", customizations_submenu, msg="Step 04.02")
        
        """
            STEP 05 : Right click on HTML page Retail Sales Filter Panel
            Verify context menu
        """
        expected_context_menu = ['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        homepage.verify_repository_folder_item_context_menu(contents[2], expected_context_menu, msg="Step 05.01")
        
        """
            STEP 06 : Right click on Shortcut Margin by Product Category - Shortcut
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Share', 'Share with...', 'Properties']
        run_submenu = ['Run in new window', 'Run deferred']
        schedule_sub_menu = ['Email', 'Printer', 'Report Library', 'Repository']
        homepage.verify_repository_folder_item_context_menu(contents[3], expected_context_menu, msg="Step 06.01")
        homepage.verify_repository_folder_item_context_submenu(contents[3], "Run...", run_submenu, msg="Step 06.02")
        homepage.verify_repository_folder_item_context_submenu(contents[3], "Schedule", schedule_sub_menu, msg="Step 06.03")
        
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()