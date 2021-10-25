"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 12 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C9928150_TestClass(BaseTestCase):
    
    def test_C9928150(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        Coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
    
        
        def verify_Distribution_List_window_title(expected_title,msg):
            access_list_elem = utils.validate_and_get_webdriver_object("#AddrbookEditor_ribbonTabPane",'Access_list_ribbon_tab')
            access_list_title = access_list_elem.text
            utils.asin(expected_title,access_list_title,msg)

        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)

        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04 Click on 'SCHEDULE' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('SCHEDULE')
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Step 05 Click on 'Distribution List' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Distribution List")
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verification -Verify 'Distribution List' window is displayed
        """
        Coreutils.switch_to_new_window()
        verify_Distribution_List_window_title("Distribution List","Step 05:01 Verify 'Distribution List' window is displayed")
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Step 06 Close 'Distribution List' window
        """
        Coreutils.switch_to_previous_window()
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_07 = """
        Step 07  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00',STEP_07)