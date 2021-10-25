"""-------------------------------------------------------------------------------------------
Author Name : Niranjan/Joyal
Automated On : 24 January 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928215_TestClass(BaseTestCase):
    
    def test_C9928215(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage  =  ParisHomePage(self.driver)
        utils     =  UtillityMethods(self.driver)
                
        """
        TESTCASE VARIABLES
        """
        project_id    =  utils.parseinitfile('project_id')
        suite_id      =  utils.parseinitfile('suite_id')
        folder_path   =  project_id + "_" + suite_id
        file_name     =  "report1"
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Developer user
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on 'P406_S31920'
        """
        HomePage.Workspaces.ResourcesTree.expand(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on My Content folder from the resource tree > click on report1 
        """
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Workspaces.ContentArea.select_file(file_name)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verification - Verify share icon appear for report1 in content area. 
        """
        HomePage.Workspaces.ContentArea.verify_shared_files(['report1'], '04.01')
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("05.00", STEP_05)