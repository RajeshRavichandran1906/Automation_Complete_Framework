"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 10 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944220_TestClass(BaseTestCase):
    
    def test_C9944220(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Basic User
        """
        HomePage.invoke_with_login('mridbas','mrpassbas')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify 'My Workspaces' view is not available for Basic User
        """
        HomePage.Banner.verify_top_bar_menus_title(['My Workspaces'], "01.01", "asnotin")
        HomePage.Home._utils.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02 : In the banner link, click on the top right username > Sign Out
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)