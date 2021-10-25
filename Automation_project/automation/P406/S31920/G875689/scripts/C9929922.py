"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 22 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929922_TestClass(BaseTestCase):
    
    def test_C9929922(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        HELP_MENU_ITEMS=['WebFOCUS Online Help', 'Technical Resources', 'Community', 'About WebFOCUS', 'License', 'TIBCO Software Inc.']
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click the Help ribbon
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify help drop down
        """
        HomePage.ContextMenu.verify(HELP_MENU_ITEMS, 02.01)
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01)
        HomePage.Banner.sign_out()
        
