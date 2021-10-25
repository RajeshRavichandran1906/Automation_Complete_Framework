"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 21-August-2019
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925815_TestClass(BaseTestCase):
    
    def test_C9925815(self):
        
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
        utils.synchronize_with_visble_text('.files-box', 'Image_Context', homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Right click on uploaded image Image_Context
            Verify context menu
        """
        expected_context_menu = ['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(image_context, expected_context_menu, msg="Step 03.01")
        homepage.verify_repository_folder_item_context_submenu(image_context, "Security", expected_security_submenu, msg="Step 03.02")
        
        """
            STEP 04 : Right click on URL_Context.
            Verify context menu
        """
        expected_context_menu = ['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(url_context, expected_context_menu, msg="Step 04.01")
        homepage.verify_repository_folder_item_context_submenu(url_context, "Security", expected_security_submenu, msg="Step 04.02")
        
        """
            STEP 05 : Right click on Blog_Context
            Verify context menu
        """
        expected_context_menu = ['Edit', 'Comments', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(blog_context, expected_context_menu, msg="Step 05.01")
        homepage.verify_repository_folder_item_context_submenu(blog_context, "Security", expected_security_submenu, msg="Step 05.02")
        
        """
            STEP 06 : Right click on TextEditor_Context.
            Verify context menu
        """
        expected_context_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        expected_run_submenu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        expected_schedule_submenu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        expected_security_submenu = ['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        homepage.verify_repository_folder_item_context_menu(texteditor_context, expected_context_menu, msg="Step 06.01")
        homepage.verify_repository_folder_item_context_submenu(texteditor_context, "Run...", expected_run_submenu, msg="Step 06.02")
        homepage.verify_repository_folder_item_context_submenu(texteditor_context, "Schedule", expected_schedule_submenu, msg="Step 06.03")
        homepage.verify_repository_folder_item_context_submenu(texteditor_context, "Security", expected_security_submenu, msg="Step 06.04")
         
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()