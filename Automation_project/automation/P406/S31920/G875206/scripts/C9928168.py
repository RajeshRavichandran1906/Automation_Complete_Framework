"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 13 Dec 2019
----------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9928168_TestClass(BaseTestCase):
    
    def test_C9928168(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        Coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
    
        
        def verify_library_access_window_title(expected_title,msg):
            access_list_elem = utils.validate_and_get_webdriver_object("#AccessListEditor_ribbonTabPane",'Access_list_ribbon_tab')
            access_list_title = access_list_elem.text
            utils.asin(expected_title,access_list_title,msg)

        Step_01 = """
        Step 01.Sign into WebFOCUS Home Page as dev User.
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_03 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00', Step_03)
        
        Step_04 = """
        Step 04 Click on 'SCHEDULE' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('SCHEDULE')
        utils.capture_screenshot('04.00', Step_04)
        
        Step_05 = """
        Step 05 Click on 'Access List' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Access List")
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
        Step 05.01 Verification -Verify 'Library Access List' window is displayed
        """
        Coreutils.switch_to_new_window()
        verify_library_access_window_title("Library Access List","Step 05.01 : Verify Library Access List window")
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify=True)
        
        Step_06 = """
        Step 06 Close 'Library Access List' window
        """
        Coreutils.switch_to_previous_window()
        utils.capture_screenshot('06.00', Step_06)
        
        Step_07 = """
        Step 07  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00', Step_07)
        
    if __name__ == "__main__":
        unittest.main()