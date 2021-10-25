"""----------------------------------------------------
Author Name : Vishnu_priya
Automated on : 26 Dec 2019
----------------------------------------------------"""
import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9928173_TestClass(BaseTestCase):
    
    def test_C9928173(self):
        
        """TESTCASE OBJECTS"""
        
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
        Step 01.Sign into WebFOCUS as Admin User.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_02_01 = """
        Verification - Verify that 'Action Bar' title is there with the expanded icon at the end of the action bar.
        """
        HomePage.Workspaces.ActionBar.verify_displayed('02.01')
        utils.capture_screenshot('02.01', Step_02_01,expected_image_verify=True)
        
        Step_03 = """
        Step 03.Click on 'Collapse action bar' icon.
        """
        HomePage.Workspaces.ActionBar.collapse()
        utils.capture_screenshot('03.00', Step_03)
        
        Step_03_01 = """
        Verification - Verify that 'Action Bar' gets collapsed and it still shows 'Action Bar' title
        """
        HomePage.Workspaces.ActionBar.verify_collapsed('03.01')
        utils.capture_screenshot('03.01', Step_03_01,expected_image_verify=True)
        
        Step_04 = """
        Expand the 'Workspaces' from the tree and Click on 'Retail Samples'
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_04_01 = """
        Verification - Verify that still 'Action Bar' title shows but it is in the collapsed state.
        """
        HomePage.Workspaces.ActionBar.verify_collapsed('04.01')
        utils.capture_screenshot('04.01', Step_04_01)
        
        Step_05 = """
        Click on 'Expand action bar' icon.
        """
        HomePage.Workspaces.ActionBar.expand()
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
        Verification - Verify that all the available action bars and category buttons are displayed. Also at the end of the action bar, its icon gets expanded
        """
        HomePage.Workspaces.ActionBar.verify_expanded('05.01')
        utils.capture_screenshot('05.01', Step_05_01)
    
        Step6 = """
        Step 06.In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('06.00', Step6)
        
if __name__ == '__main__':
    unittest.main()