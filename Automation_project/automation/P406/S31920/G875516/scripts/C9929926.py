"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 18 August 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9929926_TestClass(BaseTestCase):
    
    def test_C9929926(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        
        STEP_01 = """
            STEP 01 : Sign in as Author user
        """
        
        HomePage.invoke_with_login('mridauth', 'mrpassauth')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click Workspaces>My Workspace>Content
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.expand("My Workspace")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify ACTION BAR
        """
        HomePage.Workspaces.ActionBar.verify_tabs(['APPLICATION', 'SCHEDULE', 'OTHER'], "02.01")
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.verify_tab_options(['Portal'],"02.01")
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01, True)
        
        STEP_03 = """
            STEP 03.00 : Click on Schedule
        """
        HomePage.Workspaces.ActionBar.select_tab("SCHEDULE")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify tab options for Schedule
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(['Access List','Distribution List'],"03.01")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)

        STEP_04 = """
            STEP 04.00 : Click on Other
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify tab options for OTHER
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder','Upload File','URL','Shortcut'],"04.01")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        
