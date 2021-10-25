"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 14 February 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928136_TestClass(BaseTestCase):
    
    def test_C9928136(self):
        
        """
        TESTCASE OBJECTS
        """
        utils = UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        cancel_button = "div[qa='Cancel']"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : From 'WebFOCUS Home' tab > Click on the 'Get Data' button
        """
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 75)
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "02.01")
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on the '+' icon > Choose 'Get Data' button
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "04.01")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on 'My Workspace' tab > Click on the 'Get Data' button
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "06.01")
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_08 = """
            STEP 08 : Click on the '+' icon > Choose 'Get Data' button
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "08.01")
        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)
        
        STEP_10 = """
            STEP 10 : Click on 'Shared with Me' tab > Click on the 'Get Data' button
        """
        HomePage.Banner.click_shared_with_me()
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "10.01")
        HomePage.Home._utils.capture_screenshot("10.01", STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_12 = """
            STEP 12 : Click on the '+' icon > Choose 'Get Data' button
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "12.01")
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)
        
        STEP_14 = """
            STEP 14 : Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14.00", STEP_14)
        
        STEP_15 = """
            STEP 15 : Click on the 'Get Data' button
        """
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("15.00", STEP_15)
        
        STEP_15_01 = """
            STEP 15.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "15.01")
        HomePage.Home._utils.capture_screenshot("15.01", STEP_15_01, True)
        
        STEP_16 = """
            STEP 16 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("16.00", STEP_16)
        
        STEP_17 = """
            STEP 17 : Click on the '+' icon > Choose 'Get Data' button
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        utils.synchronize_with_visble_text(cancel_button, 'Cancel', 60)
        HomePage.Home._utils.capture_screenshot("17.00", STEP_17)
        
        STEP_17_01 = """
            STEP 17.01 : Verify Get Data window opened properly
        """
        HomePage.GetDataFrame.verify_title('Get Data', "17.01")
        HomePage.Home._utils.capture_screenshot("17.01", STEP_17_01, True)
        
        STEP_18 = """
            STEP 18 : Close Get Data window
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("18.00", STEP_18)
        
        STEP_19 = """
            STEP 19 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("19.00", STEP_19)