"""----------------------------------------------------
Author Name : Aftab/Joyal
Automated on : 13 Dec 2019
----------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928176_TestClass(BaseTestCase):
    
    def test_C9928176(self):
        
        """TESTCASE OBJECTS"""
        
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step1 = """
        Step 01.Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00', Step1)
        
        Step2 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step2)
        
        Step3 = """
        Step 03.Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00', Step3)
        
        Step4 = """
        Step 04.Click on 'APPLICATION' category button
        Verify that 'Portal' Action bar is displayed under 'Data' category
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.verify_tab_options(['Portal'],'04.00')
        utils.capture_screenshot('04.00', Step4,expected_image_verify= True)
        
        Step5 = """
        Step 05.Click on 'P292_S19901' from the resource tree
        Verify that still 'APPLICATION' category is chosen
        Also, Verify that 'Portal' Action bars is displayed
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920')
        HomePage.Workspaces.ActionBar.verify_selected_tab(['APPLICATION'], '05.00')
        HomePage.Workspaces.ActionBar.verify_tab_options(['Portal'], '05.01')
        utils.capture_screenshot('05.00', Step5, expected_image_verify= True)
        
        Step6 = """
        Step 06.In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('06.00', Step6)
        
if __name__ == '__main__':
    unittest.main()