"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 2 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9927946_TestClass(BaseTestCase):
    
    def test_C9927946(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : From the 'WebFOCUS Home' tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing'
        """
        HomePage.Home.Favorites.right_click_on_item('V5 Context Menu Testing')
        utils.capture_screenshot('02.00', Step_02) 
        
        Step_02_01 = """
        Verify that 'Run', 'Edit', 'Remove from Favorites', and 'Properties' context menus are displayed
        """
        HomePage.ContextMenu.verify(['Run', 'Edit', 'Remove from Favorites', 'Properties'],'02.01')
        utils.capture_screenshot('02.01', Step_02_01,expected_image_verify=True)
        
        Step_03 = """
            Step 3 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('03.00', Step_03)
        
    if __name__ == "__main__":
        unittest.main()