'''
Created on Aug 30, 2019

@author: Niranjan
Test rail link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925909
Test case title: Context Menu:Verify Homepage Context menu for Image/URL/Blog/TextEditor items as Basic User.
'''
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925909_TestClass(BaseTestCase):
    
    def test_C9925909(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        folder_path = "P292_S10660->G671733->Images/URL/Blog/TextEditor"
        image_context = "Image_Context"
        url_context = "URL_Context"
        blog_context = "Blog_Context"
        texteditor_context = "TextEditor_Context"
        workspace = "Workspaces"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspace, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Image/URL/Blog/TextEditor.
        """
        homepage.expand_repository_folder(folder_path)
        utils.synchronize_with_visble_text('.files-box', 'Image_Context', homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on uploaded image Image_Context
            Verify context menu
            View.
            View in new window.
            Properties.
        """
        expected_context_menu = ['View', 'View in new window', 'Properties']
        homepage.verify_repository_folder_item_context_menu(image_context, expected_context_menu, msg="Step 03.01")
        
        """
            STEP 04 : Right click on URL_Context.
            Verify context menu
            View.
            View in new window.
            Add to Favorites.
            Properties.
        """
        expected_context_menu = ['View', 'View in new window', 'Add to Favorites', 'Properties']
        homepage.verify_repository_folder_item_context_menu(url_context, expected_context_menu, msg="Step 04.01")
        
        """
            STEP 05 : Right click on Blog_Context
            Verify context menu
            Comments (View comments).
            Properties.
        """
        expected_context_menu = ['Comments', 'Properties']
        homepage.verify_repository_folder_item_context_menu(blog_context, expected_context_menu, msg="Step 05.01")
        
        """
            STEP 06 : Right click on TextEditor_Context.
            Verify context menu
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        expected_context_menu = ['Run', 'Run...', 'Add to Favorites', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred']
        homepage.verify_repository_folder_item_context_menu(texteditor_context, expected_context_menu, msg="Step 06.01")
        homepage.verify_repository_folder_item_context_submenu(texteditor_context, "Run...", expected_run_submenu, msg="Step 06.02")
         
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()