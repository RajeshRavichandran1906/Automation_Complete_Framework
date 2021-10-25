"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 03-September-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.locators import wf_mainpage_locators

class C9925903_TestClass(BaseTestCase):
    
    def test_C9925903(self):
        
        """
            Class Objects
        """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            Common Variables
        """
        folder_path = "P292_S10660->G671733->My Content"
        contents = ["Margin by Product Category - Shortcut", "Retail Samples - Shortcut", "Retail Sales Filter Panel - Shortcut"]
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Basic User
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, homepage.home_page_medium_timesleep)
        
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
        expected_context_menu = ['Run', 'Run...', 'Delete DEL', 'Add to Favorites', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred']
        homepage.verify_repository_folder_item_context_menu(contents[0], expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(contents[0], "Run...", expected_run_submenu, msg="Step 03.02")
        
        """
            STEP 04 : Right click on portal Retail Samples - Shortcut.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Customizations', 'Delete DEL', 'Add to Favorites', 'Properties']
        customizations_submenu = ['Remove my customizations']
        homepage.verify_repository_folder_item_context_menu(contents[1], expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(contents[1], "Customizations", customizations_submenu, msg="Step 04.02")
        
        """
            STEP 05 : Right click on HTML page Retail Sales Filter Panel - Shortcut
            Verify context menu
        """
        expected_context_menu = ['View', 'View in new window', 'Delete DEL', 'Add to Favorites', 'Properties']
        homepage.verify_repository_folder_item_context_menu(contents[2], expected_context_menu, msg="Step 05.01")
        
        """
            STEP 06 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()