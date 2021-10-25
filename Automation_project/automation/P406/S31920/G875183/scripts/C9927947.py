"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 2 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927947_TestClass(BaseTestCase):
    
    def test_C9927947(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        Core_utils = CoreUtillityMethods(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : From the 'WebFOCUS Home' tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing' > Click Run
        """
        HomePage.Home.Favorites.right_click_on_item('V5 Context Menu Testing')
        HomePage.ContextMenu.select("Run")
        utils.capture_screenshot('02.00', Step_02) 
        
        Step_02_01 = """
        Verify that 'V5 Context Menu Testing' portal run in a new tab with URL as: 'http://machinename:port/alias/portal/portal/P406_S31920/G875179/V5_Context_Menu_Testing'
        """
        Core_utils.switch_to_new_window()
        utils.verify_current_url("portal/P406_S31920/G875179/V5_Context_Menu_Testing",'Step 02.01 Current URl')
        utils.verify_current_tab_name("V5 Context Menu Testing","Step 02.02 Current tab title")
        utils.capture_screenshot('02.01', Step_02_01,expected_image_verify=True)
        
        Step_03 = """
        Close the 'V5 Context Menu Testing' portal run window
        """
        Core_utils.switch_to_previous_window()
        utils.capture_screenshot('03.00', Step_03) 
        
        Step_04 = """
            Step 4 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('04.00', Step_04)
        
    if __name__ == "__main__":
        unittest.main()