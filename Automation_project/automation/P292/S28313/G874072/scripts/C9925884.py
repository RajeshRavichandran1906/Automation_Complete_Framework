"""---------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 29-August-2019
Test case title: Context Menu:Verify Homepage Context menu for Portal & Pages as Developer.
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login

class C9925884_TestClass(BaseTestCase):
   
    def test_C9925884(self):
       
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
       
        """V4-Collaborative portal """
       
        portal_expected_menu = ['Run', 'Edit', 'Customizations', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        portal_customization_sub_menu = ['Remove my customizations', 'Remove customizations for all users']
        portal_security_sub_menu  = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        workspace = "Workspaces"
        
        """ Page_contex_menu"""
        page_expected_menu = ['Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Unlink Page', 'Unpublish', 'Hide', 'Security', 'Properties']
       
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspace, homepage.home_page_long_timesleep)
       
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Portal/Pages.
        """
        homepage.expand_repository_folder('P292_S10660->G671733->Portal/Pages')
        utils.synchronize_with_visble_text('.content-box', 'Items', homepage.home_page_short_timesleep)
       
        """
        Step 03: Right click on V4-Collaborative portal V4PortalContext.
        """
        """
        Step 03:01 Verify context menu,
        Run.
        Edit.
        Customizations (Remove my customizations/Remove customizations for all users).
        Cut.
        Copy.
        Delete.
        Add to Favorites.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('V4_Portal_Context',portal_expected_menu, msg="Step:03:01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        homepage.verify_repository_folder_item_context_submenu('V4_Portal_Context','Security',portal_security_sub_menu,msg= "Step:03:02")
        homepage.verify_repository_folder_item_context_submenu('V4_Portal_Context','Customizations',portal_customization_sub_menu,msg= "Step:03:03")
       
        """
        Step 4:Right click on portal page Page_Context.
        Verify context menu,
        Edit.
        Duplicate.
        Cut.
        Copy.
        Delete.
        Unlink page.
        Unpublish/Publish.
        Hide/Show.
        Security (Rules on this resource/Effective Policy/Owner).
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('Page_Context',page_expected_menu, msg="Step:04:01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        homepage.verify_repository_folder_item_context_submenu('Page_Context','Security',portal_security_sub_menu,msg= "Step:04:02")
       
        """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()