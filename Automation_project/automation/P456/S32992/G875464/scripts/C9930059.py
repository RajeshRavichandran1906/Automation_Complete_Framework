"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 07 July 2020
-----------------------------------------------------------------------------------------------"""

import os
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930059_TestClass(BaseTestCase):
    
    def test_C9930059(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        ExcelPath = os.path.join(os.getcwd(), "data", "EN_centurymaster.xlsx")
        
        STEP_01 = """
            STEP 01 : Go to Workspaces -> Workspace -> My Workspace
        """
        HomePage.invoke_with_login('mriddev4','mrpassdev4')
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.select('My Workspace')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Go to WebFOCUS
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on "+" Sign -> Get Data -> Excel
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Get Data')
        HomePage.GetDataFrame.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.GetDataFrame.locators.content_css, "Excel", 80)
        HomePage.GetDataFrame.GetData.LocalFiles.select('Excel')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04 : Choose "EN_centurymaster.xlsx" and Click Open
        """
        HomePage.Home._utils.wait_for_page_loads(2,pause_time=3)
        FileDialog().open_file(ExcelPath)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.GetDataFrame.locators.content_css, "myhome", 80)
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that "abc_1" folder should displayed under Application Folder
        """
        HomePage.GetDataFrame.UploadingData.Sheets.ApplicationFolder.verify_selected_folder('myhome', '04.01')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Close it
        """
        HomePage.GetDataFrame.close()
        HomePage.GetDataFrame.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        