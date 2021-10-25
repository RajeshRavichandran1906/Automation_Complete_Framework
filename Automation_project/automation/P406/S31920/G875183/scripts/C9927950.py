"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 02 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9927950_TestClass(BaseTestCase):
    
    def test_C9927950(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : From WebFOCUS Home tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing' > Run
        """
        HomePage.Home.Favorites.right_click_on_item('V5 Context Menu Testing')
        HomePage.ContextMenu.select('Run')
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """ 
            Step 02.00 : Verification - Verify that 'V5 Context Menu Testing' runs in a new tab with the URL:
            http://machine_name:port/alias/portal/P406_S31920/G875179/V5_Context_Menu_Testing
        """
        core_utils.switch_to_new_window()
        utils.verify_current_tab_name('V5 Context Menu Testing', 'Step 02.01 : Verify tab name')
        utils.verify_current_url('portal/P406_S31920/G875179/V5_Context_Menu_Testing', 'Step 02.02 : Verify url')
        utils.capture_screenshot("02.01", STEP_02_01, True)
        
        STEP_03 = """
            Step 03.00 : Close the 'V5 Context Menu Testing' run window.
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : In the banner link, click on the top right username > Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("04.00", STEP_04)

if __name__ == "__main__":
    unittest.main() 