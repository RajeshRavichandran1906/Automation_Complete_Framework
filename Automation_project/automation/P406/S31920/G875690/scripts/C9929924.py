"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 29 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929924_TestClass(BaseTestCase):
    
    def test_C9929924(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        UTIL_MENU_LIST =['Deferred Status', 'Stop Requests', 'ReportCaster Explorer', 'ReportCaster Status', 'Magnify Search Page']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Utilities ribbon
        """
        HomePage.Banner.click_utilities()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.1 : Verify Utilities drop down
        """
        HomePage.ContextMenu.verify(UTIL_MENU_LIST, '02.01')
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01, True)
        
        STEP_03 = """
            STEP 03.00 : Sign out WF.
        """
        HomePage.Banner.sign_out()
                
