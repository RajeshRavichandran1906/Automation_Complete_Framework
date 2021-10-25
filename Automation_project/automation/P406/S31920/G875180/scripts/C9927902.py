"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 06 January 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927902_TestClass(BaseTestCase):
    
    def test_C9927902(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : Click on Workspaces tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03.00 : Expand 'P406_S31920' workspace and Click on 'G875179' folder from the resource tree.
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920")
        HomePage.Workspaces.ResourcesTree.select("G875179")
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04.00 : Right-click on 'V5 Context Menu Testing' from the content area > Select 'Open'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("V5 Context Menu Testing")
        HomePage.ContextMenu.select('Open')
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            Step 04.01 : Verification - 'V5 Context Menu Testing' folder gets opened.              
        """
        HomePage.Workspaces.ResourcesTree.verify_selected_item(["V5 Context Menu Testing"], '04.01')
        utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_04_02 = """
            Step 04.02 : Breadcrumbs displayed as 'Workspaces > P406_S31920 > G875179> V5 Context Menu Testing'
        """
        expected_breadcrumbs = 'Workspaces>P406_S31920>G875179>V5 Context Menu Testing'
        HomePage.Workspaces.NavigationBar.verify_breadcrumbs(expected_breadcrumbs, '04.02')
        utils.capture_screenshot("04.02", STEP_04_02, expected_image_verify = True)
        
        STEP_04_03 = """
            Step 04.03 : Action Bar shows two action tiles 'Folder' and 'Shortcut'
        """
        expected_tab_options = ['Folder' , 'Shortcut']
        HomePage.Workspaces.ActionBar.verify_tab_options(expected_tab_options, '04.03')
        utils.capture_screenshot("04.03", STEP_04_03, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)

if __name__ == "__main__":
    unittest.main() 