"""-------------------------------------------------------------------------------------------
Author Name : Robert/Rajesh
Automated On : 26 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928469_TestClass(BaseTestCase):
    
    def test_C9928469(self):
        
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
            Step 03.00 : Expand Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875163->Breadcrumb Trail and Search->Retail Samples")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Double click on Charts in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("Charts")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Click on > before Charts in breadcrumb trail
        """
        HomePage.Workspaces.NavigationBar.click_breadcrumb_arrow("Retail Samples")
        utils.capture_screenshot("05.00", STEP_05)
    
        STEP_05_01 = """
            Step 05.01 : Verify drop-down list appears with My Content, Reports, Charts, Documents, Visualizations, Portal, InfoApps, Mobile and Hidden Content
        """
        expected_menus = ['My Content', 'Reports', 'Charts', 'Documents', 'Visualizations', 'Portal', 'InfoApps', 'Mobile', 'Hidden Content']
        HomePage.ContextMenu.verify(expected_menus, "05.01")
        utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
            Step 06.00 : Select Documents from drop down list
        """
        HomePage.ContextMenu.select("Documents")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            Step 06.01 : Verify breadcrumb trail is "Workpsaces > P406_S31920 > G875163 > Breadcrumb Trail and Search > Retail Samples > Documents".
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875163>Breadcrumb Trail and Search>Retail Samples>Documents"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, "06.01")
        utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
            Step 07.00 : Revert back the Home Page by its default state (Click on Workspaces from navigation bar)
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_08 = """
            Step 08.00 : In the banner link, click on the top right username > Sign out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("08.00", STEP_08)
        
if __name__ == "__main__":
    unittest.main()