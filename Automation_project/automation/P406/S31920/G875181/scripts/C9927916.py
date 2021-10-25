"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 03 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927916_TestClass(BaseTestCase):
    
    def test_C9927916(self):
        
        """
            TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
                
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder in the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
                
        STEP_04 = """
            Step 04.00 : Right-click on 'V5 Context Menu Testing' from the content area > Select 'Expand'
        """
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G875179->V5 Context Menu Testing")
        HomePage.ContextMenu.select('Expand')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - Verify that 'V5 Context Menu Testing' portal gets expanded from the Resource tree
        """
        HomePage.Workspaces.ResourcesTree.verify_expanded('V5 Context Menu Testing', '04.01')
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_04_02 = """
            Step 04.02 : Verification - Verify based on the breadcrumb user inside the 'V5 Context Menu Testing' folder and breadcrumb as 'Workspaces > P406_S31920 > G875179'
        """
        expected_breadcrumbs = "Workspaces>P406_S31920>G875179"
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, '04.02')
        utils.capture_screenshot("04.02", STEP_04_02, True)
        
        STEP_05 = """
            Step 05.00 : Click on 'V5 Context Menu Testing' from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("V5 Context Menu Testing")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            Step 05.01 : Verification - Verify that 'Action Bar' shows two action tiles 'Folder' and 'Shortcut'
        """
        expected_options = ['Folder', 'Shortcut']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_options, '05.01')
        utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            Step 06.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("06.00", STEP_06)

if __name__ == "__main__":
    unittest.main() 