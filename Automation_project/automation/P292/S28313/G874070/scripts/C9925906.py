"""---------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 30-August-2019
Testcase title: Context Menu:Verify Homepage Context menu for Portal & Pages as Basic User.
---------------------------------------------------------------"""

from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.login import Login

class C9925906_TestClass(BaseTestCase):
    
    def test_C9925906(self):
        
        """ CLASS  OBJECTS """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        
        folder_path = "P292_S10660->G671733"
        workspaces = 'Workspaces'
        
        """V4-Collaborative portal """
        
        portal_expected_menu = ['Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        
        """ Page_contex_menu"""
        
        page_expected_menu = ['Properties']
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', workspaces, homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Navigate to 'P292_S10660' domain >> G671733 >> Click on folder Portal/Pages.
        """
        homepage.expand_repository_folder(folder_path+'->Portal/Pages')
        utils.synchronize_with_visble_text('.content-box', 'Items', homepage.home_page_short_timesleep)
        
        """
        Step 03: Right click on V4-Collaborative portal V4PortalContext.
        """
        """
        Step 03:01 Verify context menu,
        Run.
        Remove my customizations.
        Copy.
        Add to Favorites.
        Properties.
        """
        homepage.verify_repository_folder_item_context_menu('V4_Portal_Context',portal_expected_menu, msg="Step:04:01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
        Step 4:Right click on portal page Page_Context.
        Verify context menu,
        Verify context menu,
        Copy.
        Properties
        """
        homepage.verify_repository_folder_item_context_menu('Page_Context',page_expected_menu, msg="Step:06:01")
        left_panel_elem = utils.validate_and_get_webdriver_object(".left-main-panel","left_area_panel")
        core_utils.python_left_click(left_panel_elem)
        
        """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()