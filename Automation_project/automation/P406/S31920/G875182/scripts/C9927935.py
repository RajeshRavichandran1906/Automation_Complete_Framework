"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 23 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9927935_TestClass(BaseTestCase):
    
    def test_C9927935(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        Core_utils = CoreUtillityMethods(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developers User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : From WebFOCUS Home tab, Under 'PORTALS' section carousel >Click 'VIEW ALL' button
        """
        HomePage.Home.Portals.click_view_all()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Right-click on 'V5 Context Menu Testing' > Run'
        """
        HomePage.Home.ViewAll.right_click_on_item("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Run")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verification - Verify that 'V5 Context Menu Testing' runs in a new tab with the URL:
            http://machine_name:port/alias/portal/P406_S31920/G875179/V5_Context_Menu_Testing
        """
        Core_utils.switch_to_new_window()
        portal_title = self.driver.find_element_by_css_selector(".pvd-portal-title")
        Portal_Text= portal_title.text
        utils.asequal(Portal_Text,'V5 Context Menu Testing',"Step 03.01 verify portal_title")
        Actual_set_up_url =utils.get_setup_url().replace('home8206','')
        Portal_URL = "portal/P406_S31920/G875179/V5_Context_Menu_Testing"
        Expected_URL = Actual_set_up_url+Portal_URL
        Actual_URL = self.driver.current_url
        utils.asequal(Expected_URL,Actual_URL,"Step 03.02 verify the portal url")
        utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Click on 'Left arrow' to go back to 'Home tab'
        """
        Core_utils.switch_to_previous_window()
        HomePage.Home.ViewAll.click_left_arrow()
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)
        

if __name__ == "__main__":
    unittest.main() 