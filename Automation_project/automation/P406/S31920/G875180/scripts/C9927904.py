"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 16 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927904_TestClass(BaseTestCase):
    
    def test_C9927904(self):
        
        """
        TESTCASE OBJECTS
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)

        """
        TESTCASE VARIABLES
        """
        portal_banner_css = ".pvd-portal-banner"
        
        STEP_01 = """
            Step 01 :  Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Right-click on 'V5 Context Menu Testing' from the content area > Select 'Run'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        HomePage.ContextMenu.select("Run")
        HomePage.Workspaces.switch_to_default_content()
        chart.switch_to_new_window()
        chart.wait_for_visible_text(portal_banner_css, "V5 Context", time_out = 120)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - Verify that 'V5 Context Menu Testing' runs in a new tab
        """
        actual_title = self.driver.title
        msg = "Step 04.01 : Verify that 'V5 Context Menu Testing' runs in a new tab"
        utils.asequal("V5 Context Menu Testing", actual_title, msg)
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05 : Close the 'V5 Context Menu Testing' run window.
        """
        chart.switch_to_previous_window()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            Step 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)
        
if __name__ == "__main__":
    unittest.main() 