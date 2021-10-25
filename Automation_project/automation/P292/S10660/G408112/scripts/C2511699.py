"""------------------------------------------------------------------------------------
Author Name : Prabhakaran.
Automated Date : 08-August-2019
------------------------------------------------------------------------------------"""

from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage

class C2511699_TestClass(BaseTestCase):

    def test_C2511699(self):
        
        """CLASS OBJECTS"""
        homepage = Wf_Mainpage(self.driver)
        login = Login(self.driver)
        utils = UtillityMethods(self.driver)
        
        """COMMON VARIABLES"""
        side_bar_css = ".left-main-panel"
    
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        login.invoke_home_page('mridadm', 'mrpassadm')
        utils.synchronize_with_visble_text(side_bar_css, "Content", homepage.home_page_long_timesleep)
        
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text(".toolbar", "Workspaces", homepage.home_page_short_timesleep)
        
        """
            STEP 02 : Under Repository tree >> Select 'Retail_Samples' Domain.
        """
        homepage.expand_repository_folder("Retail Samples")
        utils.synchronize_with_visble_text(".files-box", "Portal", homepage.home_page_short_timesleep)
        
        """
            STEP 03 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        
        """
            STEP 04 : Sign into WebFOCUS Home Page as Admin User.
            Verify the state of the Home Page Repository Tree >> 'Retail_Samples' is the Domain that is selected by default.
        """
        login.invoke_home_page('mridadm', 'mrpassadm')
        utils.synchronize_with_visble_text(side_bar_css, "Content", homepage.home_page_long_timesleep)
        homepage.verify_crumb_box("Workspaces->Retail Samples", "Step 04.01 :  Verify the state of the Home Page Repository Tree >> 'Retail_Samples' is the Domain that is selected by default")
        
        """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()