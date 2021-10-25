"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 31 Jan 2020
----------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930522_TestClass(BaseTestCase):
    
    def test_C9930522(self):
        
        """
            TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        STEP_01 = """
        STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        utils.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
        STEP 01.01 : Verify the 'Settings' icon is not available in the banner link.
        """
        HomePage.Banner.verify_top_bar_menus_title(['Settings'], "01.01", assert_type='asnotin')
        utils.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
        STEP 02 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        STEP 03 : Sign into WebFOCUS Home Page as Basic User
        """
        HomePage.invoke_with_login('mridbas', 'mrpassbas')
        utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
        STEP 03.01 : Verify the 'Settings' icon is not available in the banner link
        """
        HomePage.Banner.verify_top_bar_menus_title(['Settings'], "03.01", assert_type='asnotin')
        utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
        STEP 04 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
        STEP 05 : Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login('mridadv', 'mrpassadv')
        utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
        STEP 05.01 : Verify the 'Settings' icon is not available in the banner link
        """
        HomePage.Banner.verify_top_bar_menus_title(['Settings'], "05.01", assert_type='asnotin')
        utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
        STEP 06 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot('06.00', STEP_06)