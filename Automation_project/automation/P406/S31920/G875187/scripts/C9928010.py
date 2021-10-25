"""-------------------------------------------------------------------------------------------
Author Name : Vpriya
Automated On : 12 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928010_TestClass(BaseTestCase):
    
    def test_C9928010(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Basic User.
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_03 = """
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces")
        utils.capture_screenshot('03.00', Step_03)
        
         
        Step_04 = """
            Step 04 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "ReportingObject".
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('ReportingObject')
        utils.capture_screenshot('04.00', Step_04)
         
        Step_04_01 = """
            Step 04 : Verification - Verify 'ReportingObject_Context' is not available in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files(["ReportingObject_Context"],"04.01",assert_type='asnotin')
        utils.capture_screenshot('04.01', Step_04_01, expected_image_verify= True)
        
        Step_05 = """
            Step 5 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('05.00', Step_05)
        
    if __name__ == "__main__":
        unittest.main()