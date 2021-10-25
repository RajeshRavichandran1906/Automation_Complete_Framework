"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 23 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9927931_TestClass(BaseTestCase):
    
    def test_C9927931(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            TESTCASE CSS
        """
        banner_css = ".pvd-portal-banner"
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : From WebFOCUS Home tab, Under 'PORTALS' section carousel >Click 'VIEW ALL' button
        """
        HomePage.Home.Portals.click_view_all()
        utils.capture_screenshot("02.00", STEP_02)
            
        STEP_03 = """
            Step 03.00 : Right-click on 'V5 Context Menu Testing' > Run
        """
        HomePage.Home.ViewAll.right_click_on_item("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Run")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify that 'V5 Context Menu Testing' runs in a new tab
        """
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(banner_css, "V5 Context", 120)
        utils.verify_current_tab_name("V5 Context Menu Testing", "Step 03.01 : Verify that 'V5 Context Menu Testing' runs in a new tab")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Close the 'V5 Context Menu Testing' run window.
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Click on 'Left arrow' to go back to 'Home tab'
        """
        HomePage.Home.ViewAll.click_left_arrow()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            Step 06.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == "__main__":
    unittest.main() 