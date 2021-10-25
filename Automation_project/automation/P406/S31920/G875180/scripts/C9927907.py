"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 3 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9927907_TestClass(BaseTestCase):
    
    def test_C9927907(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)

        
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
            Step 04 : Right-click on 'V5 Portal Delete' from the content area > Click Delete > Click OK
        """
        HomePage.Workspaces.ContentArea.delete_folder("V5 Portal Delete")
        utils.capture_screenshot("05.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 :Verify 'V5 Portal Delete' portal deleted from the content area.
        """
        HomePage.Workspaces.ContentArea.verify_folders(["V5 Portal Delete"],'05.01',assert_type='asnotin')
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)
        
if __name__ == "__main__":
    unittest.main() 