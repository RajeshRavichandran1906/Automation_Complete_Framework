"""---------------------------------------------------------------
Author Name : Niranjan
Automated On : 27-August-2019
Testcase title: Context Menu:Verify Homepage Context menu for items underneath My_Content Folder as Developer
Testrail link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9925881
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login

class C9925881_TestClass(BaseTestCase):
    
    def test_C9925881(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        folder_path = project_id+'_'+suite_id
        expected_items = ['Retail Samples', 'Margin by Product Category', 'Margin by Product Category - Shortcut', 'Retail Sales Filter Panel']
        Workspaces = "Workspaces"
        
        report_expected_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        report_run_sub_menu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        report_schedule_sub_menu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        report_security_sub_menu = ['Rules on this resource...', 'Effective policy...']
        
        
        portal_expected_menu = ['Run', 'Edit', 'Customizations', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        portal_customization_sub_menu=['Remove my customizations', 'Remove customizations for all users']
        portal_security_sub_menu = ['Rules on this resource...', 'Effective policy...']
        
        
        HTML_expected_menu =['View', 'View in new window', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        HTML_security_sub_menu = ['Rules on this resource...', 'Effective policy...']
        
        
        shortcut_expected_menu = ['Run', 'Run...', 'Schedule', 'Edit', 'Edit with text editor', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Security', 'Share', 'Share with...', 'Properties']
        shortcut_security_sub_menu =['Rules on this resource...', 'Effective policy...']
        shortcut_run_sub_menu = ['Run in new window', 'Run deferred', 'Run with SQL trace']
        shortcut_schedule_sub_menu = ['Email', 'FTP', 'Printer', 'Report Library', 'Repository']
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', Workspaces, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain Tree >> Click on 'My Content' folder underneath 'P292_S10660' domain.
        """
        homepage.expand_repository_folder(folder_path+'->My Content')
        utils.synchronize_with_visble_text('.content-box', 'Items', homepage.home_page_short_timesleep)
        
        """
        Step 02:01:Verify items Report, Portal, Shortcut & HTML page items are available under My Content folder.
        """
        homepage.verify_items_in_grid_view(expected_items, comparision_type='asin',msg="Step 02:01 Verify items Report, Portal, Shortcut & HTML page items are available under My Content folder")
        
        """
        Step 03: Right click on report Margin by Product Category.
        """
        """
        Step 03:01 Verify context menu,
        Run.
        Run (Run in new window/Run deferred/Run with SQL trace).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut.
        Copy.
        Create Shortcut.
        Delete.
        Add to Favorites.
        Security (Rules on this resource/Effective Policy).
        Share.
        Share with.
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('Margin by Product Category',report_expected_menu, msg="Step:03:01")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category','Run...',report_run_sub_menu,msg= "Step:03:02")
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category','Schedule',report_schedule_sub_menu,msg= "Step:03:03")
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category','Security',report_security_sub_menu,msg= "Step:03:04")
        
        """
        Step 04:Right click on portal Retail Samples.
        Verify context menu,
        Run.
        Edit.
        Customizations (Remove my customizations/Remove customizations for all users).
        Cut.
        Copy.
        Delete.
        Add to Favorites.
        Security (Rules on this resource/Effective Policy).
        Share.
        Share with.
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('Retail Samples',portal_expected_menu, msg="Step:04:01")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_item_context_submenu('Retail Samples','Security',portal_security_sub_menu,msg= "Step:04:02")
        homepage.verify_repository_folder_item_context_submenu('Retail Samples','Customizations',portal_customization_sub_menu,msg= "Step:04:03")
        
        """
        Step 5:Right click on HTML page Retail Sales Filter Panel.
        Verify context menu,
        View.
        View in new window.
        Edit with text editor.
        Duplicate.
        Cut.
        Copy.
        Create Shortcut.
        Delete.
        Add to Favorites.
        Security (Rules on this resource/Effective Policy).
        Share.
        Share with.
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('Retail Sales Filter Panel',HTML_expected_menu, msg="Step:05:01")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_item_context_submenu('Retail Sales Filter Panel','Security',HTML_security_sub_menu,msg="step05:02")
        
        """
        Step 6:Right click on Shortcut Margin by Product Category - Shortcut.
        Verify context menu,
        Run.
        Run (Run in new window/Run deferred/Run with SQL trace).
        Schedule (Email/FTP/Printer/Report Library/Repository).
        Edit.
        Edit with text editor.
        Duplicate.
        Cut.
        Copy.
        Delete.
        Add to Favorites.
        Security (Rules on this resource/Effective Policy).
        Share.
        Share with.
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('Margin by Product Category - Shortcut',shortcut_expected_menu, msg="Step:06:01")
        banner_elem = utils.validate_and_get_webdriver_object(".banner-group-spacer","banner_area")
        core_utils.python_left_click(banner_elem)
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category - Shortcut','Security',shortcut_security_sub_menu,msg="step06:02")
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category - Shortcut','Run...',shortcut_run_sub_menu,msg="step06:03")
        homepage.verify_repository_folder_item_context_submenu('Margin by Product Category - Shortcut','Schedule',shortcut_schedule_sub_menu,msg="step06:04")
        
        """
            STEP 07 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()