"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Rajesh
Automated On : 24 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928467_TestClass(BaseTestCase):
    
    def test_C9928467(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign in to WebFOCUS as Developer User.
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand Workspaces > P406_S31920> G875163 >Click "Breadcrumb Trail and Search" in tree
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Click on Retail Samples in tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples"
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "04.01")
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : Revert back the Home Page by its default state (Click Workspaces and click on Workspaces from navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            Step 06.00 : Expand Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples in tree
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            Step 07.00 : Click on Charts in the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Charts")
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            Step 07.01 : Verify breadcrumb trail is "Workspaces > P406_S31920> G875163 > Breadcrumb Trail and Search > Retail Samples > Charts"
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Charts"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "07.01")
        utils.capture_screenshot("07.01", STEP_07_01, expected_image_verify = True)
        
        STEP_08 = """
            Step 08.00 : Revert back the Home Page by its default state (Click content from side bar and click on Workspaces from navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_09 = """
            Step 09.00 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("09.00", STEP_09)

if __name__ == "__main__":
    unittest.main()