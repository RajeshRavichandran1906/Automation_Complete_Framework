"""---------------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 30-August-2019
---------------------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C9925888_TestClass(BaseTestCase):
    
    def test_C9925888(self):
        
        """
            Class Objects
        """
        loginpage = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            Common Variables
        """
        banner_css = ".home-banner .banner-group-spacer"
        folder_path1 = "P292_S10660"
        folder_path2 = folder_path1 + "->My Content"
        folder_path3 = folder_path2 + "->G671733"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Advanced User
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Workspaces', homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain Tree >> Right-click on P292_S10660 domain
            Verify context menu - ['Collapse', 'Refresh', 'Properties']
        """
        expectd_contextmenu = ['Collapse', 'Refresh', 'Properties']
        homepage.verify_repository_folder_context_menu(folder_path1, expectd_contextmenu, msg="Step 02.01")
        banner = self.driver.find_element_by_css_selector(banner_css)
        core_utils.left_click(banner)
        
        """
            STEP 03 : Under Domain Tree >> Right-click on My Content folder underneath 'P292_S10660' domain.
            Verify context menu - ['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Share', 'Share with...', 'Properties']
        """
        expectd_contextmenu = ['Collapse', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Share', 'Share with...', 'Properties']
        homepage.verify_repository_folder_context_menu(folder_path2, expectd_contextmenu, msg="Step 03.01")
        banner = self.driver.find_element_by_css_selector(banner_css)
        core_utils.left_click(banner)
        
        """
            STEP 04 : Under Domain Tree >> Right-click on G671733 folder underneath 'P292_S10660' domain.
            Verify context menu - ['Collapse', 'Copy Ctrl+C', 'Refresh', 'Properties']
        """
        expectd_contextmenu = ['Collapse', 'Copy Ctrl+C', 'Refresh', 'Properties']
        homepage.verify_repository_folder_context_menu(folder_path3, expectd_contextmenu, msg="Step 03.01")
        
        """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()