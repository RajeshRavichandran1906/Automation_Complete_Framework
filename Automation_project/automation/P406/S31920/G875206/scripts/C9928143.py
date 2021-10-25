"""----------------------------------------------------
Author Name : Vishnu_priya
Automated on : 17 Jan 2020
----------------------------------------------------"""
import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.wf_mainpage import Wf_Mainpage


class C9928143_TestClass(BaseTestCase):
    
    def test_C9928143(self):
        
        """TESTCASE OBJECTS"""
        
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        
        Step1 = """
        Step 01.Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00', Step1)
        
        Step2 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00', Step2)
        
        Step3 = """
        Step 03.Expand the 'Workspaces' from the tree and 
        """
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        utils.capture_screenshot('03.00', Step3)
        
        Step4 = """Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('04.00', Step4)
        
        Step5 = """
        Step 05.Click on 'InfoAssist' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("INFOASSIST")
        utils.capture_screenshot('05.00', Step5)
        
        Step6 = """
        Step 06.Click on 'Sample Content' action bar under 'InfoAssist' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Sample Content")
        utils.wait_for_page_loads(20)
        utils.capture_screenshot('06.00', Step6)
        
        Step_06_01 = """
        Verify 'Sample Content' prompt is displayed
        """
        old_homepage.resource_dialog().verify_caption_title("Sample Content",'05.01')
        utils.capture_screenshot('06.01', Step_06_01,expected_image_verify=True)
        
        Step_07 = """Click on 'Cancel' in 'Sample Content' prompt
        """
        old_homepage.resource_dialog().click_button("Cancel")
        utils.wait_for_page_loads(40)
        utils.capture_screenshot('07.00', Step_07)
        
        Step8 = """
        Step 08.In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00', Step8)
        
if __name__ == '__main__':
    unittest.main()