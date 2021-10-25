"""------------------------------------------------------------------------
Author : Prabhakaran
Automated On : 13-August-2019
------------------------------------------------------------------------"""

from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.pages.wf_legacymainpage import Wf_Legacymainpage
import unittest

class C3023969_TestClass(BaseTestCase):
    
    def test_C3023969(self):
        
        """ CLASS OBJECTS """
        homepage = Wf_Mainpage(self.driver)
        loginpage = Login(self.driver)
        utils = UtillityMethods(self.driver)
        legacyhome = Wf_Legacymainpage(self.driver)
    
        """
            STEP 01 : Open a new browser session
            STEP 02 : Enter URL, http://{machine_name}:{port}/context-root/home
            Verify that this brings up the Sign In page.
            STEP 03 : Enter valid WF_Administrator credentials.
            Verify that you are now logged into the new Home page.
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(".left-main-panel", "Content", homepage.home_page_long_timesleep)
        
        """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        
        """
            STEP 05 : Enter URL, http://{machine_name}:{port}/context-root/legacyhome
            Verify that this brings up the Sign In page.
            STEP 06 : Enter valid WF_Administrator credentials
            Verify that you are now logged into the Legacy page,
        """
        utils.invoke_legacyhomepage('mrid', 'mrpass')
        utils.synchronize_with_visble_text("#treeView", "Workspaces", homepage.home_page_long_timesleep)
        
        """
            STEP 07 : From the top right banner link >> Click Sign Out.
        """
        legacyhome.select_or_verify_top_banner_links("sign_out")
        
if __name__ == '__main__':
    unittest.main() 