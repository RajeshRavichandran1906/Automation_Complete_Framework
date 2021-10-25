"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 30 January 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage


class C9928091_TestClass(BaseTestCase):
    
    def test_C9928091(self):
        
        """"
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id    =  utils.parseinitfile('project_id')
        suite_id      =  utils.parseinitfile('suite_id')
        group_id    =  utils.parseinitfile('group_id')
        folder_path =  project_id + "_" + suite_id+'->'+group_id
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Navigate to 'P406_S31920' workspace > Click on 'G875201' folder
        """
        HomePage.Workspaces.ResourcesTree.select(folder_path)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Double click on 'V5_Sharing' from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("V5_Sharing")
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : Double click on 'My Pages' folder in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("My Pages")
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Verify Sharing icon appears in 'My Content' folder in the content area
        """
        HomePage.Workspaces.ContentArea.verify_shared_folders(["My Content"],"05.01")
        utils.capture_screenshot("05.01", STEP_05_01)
        
        STEP_06 = """
        Double click on 'My Content' folder in the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("My Content")
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
        Verify added 'Page 1' personal page appears with sharing icon in the content area
        """
        HomePage.Workspaces.ContentArea.verify_shared_files(["Page 1"],'06.01',assert_type='asnotin')
        utils.capture_screenshot("06.01", STEP_06_01)
        
        STEP_07 = """
            STEP 07.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("07.00", STEP_07)