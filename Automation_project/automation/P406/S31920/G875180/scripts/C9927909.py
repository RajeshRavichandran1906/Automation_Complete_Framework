"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 17 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9927909_TestClass(BaseTestCase):
    
    def test_C9927909(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        portal_banner_css = ".pvd-portal-banner"
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        HomePage.Home._utils.synchronize_with_number_of_element(HomePage.Workspaces.locators.iframe_css, 1, 60)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right-click on 'V5 Context Menu Testing' from the content area > Click Run
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Run")
        HomePage.Workspaces.switch_to_default_content()
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - Verify that 'V5 Context Menu Testing' run in a new tab and URL displayed as below: http://machinename:port/alias/portal/P406_S31920/G875179/V5_Context_Menu_Testing
        """
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(portal_banner_css, "V5 Context", 120)
        utils.verify_current_tab_name("V5 Context Menu Testing", "Step 04.01 : Verify that 'V5 Context Menu Testing' run in a new tab")
        utils.verify_current_url("portal/P406_S31920/G875179/V5_Context_Menu_Testing", "Step 04.02 : Verification - Verify URL displayed as below: http://machinename:port/alias/portal/P406_S31920/G875179/V5_Context_Menu_Testing")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Close the 'V5 Context Menu Testing' run window
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            Step 06.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == "__main__":
    unittest.main() 