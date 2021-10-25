"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 13 February 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928155_TestClass(BaseTestCase):
    
    def test_C9928155(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage  =  ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        cancel_button = "div[qa='Cancel']"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on 'Retail Samples' workspaces
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on '+' icon > Click on 'Get Data' button
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify the 'Get Data' window opens
        """
        HomePage.GetDataFrame.verify_title("Get Data", "04.01")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Close Get Data Window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on the 'Get Data' button
        """
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify the 'Get Data' window opens
        """
        HomePage.GetDataFrame.verify_title("Get Data", "06.01")
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Close Get Data Window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_08 = """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)