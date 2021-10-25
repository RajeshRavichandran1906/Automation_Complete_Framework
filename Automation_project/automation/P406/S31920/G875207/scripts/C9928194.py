"""----------------------------------------------------
Author Name : Vishnu Priya
Automated on : 30 Dec 2019
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928194_TestClass(BaseTestCase):
    
    def test_C9928194(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        
        """TESTCASE VARIABLES"""
        
        Expected_action_bar = ['Workspace', 'Folder']
        Expected_title = 'New Workspace'
        
        
        STEP_01 = """
        Step 01.Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces'from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        bread_crumb = HomePage.Workspaces.NavigationBar.locators.breadcrumbs[1]
        bread_crumb_ele = HomePage.Home._utils.validate_and_get_webdriver_objects(bread_crumb, 'bread crumb')
        bread_crumb_list= [x.text for x in bread_crumb_ele]
        if 'Workspaces' not in bread_crumb_list: 
            HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00',STEP_02)
        
        STEP_02_01 = """Verify two action tiles (Workspaces, Folder) are displayed
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(Expected_action_bar,'02.01')
        HomePage.Home._utils.capture_screenshot('02.01',STEP_02_01,expected_image_verify=True)
        
        STEP_03 = """Click on 'Workspaces' action tile in Action Bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option('Workspace')
        HomePage.ModalDailogs.NewWorkspace.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """Verify that only significant words are capitalized in the title case as 'New Workspaces'
        """
        HomePage.ModalDailogs.NewWorkspace.verify_title(Expected_title, '03.01')
        HomePage.Home._utils.capture_screenshot('03.01',STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """Click Cancel to close the dialog box
        """
        HomePage.ModalDailogs.NewWorkspace.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Step 5 In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('05.00',STEP_05)