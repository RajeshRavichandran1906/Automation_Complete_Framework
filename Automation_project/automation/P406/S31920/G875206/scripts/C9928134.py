"""----------------------------------------------------
Author Name : Robert
Automated on : 10 Jan 2020
----------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928134_TestClass(BaseTestCase):
    
    def test_C9928134(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        FOLDER_NAME1='C9928134'
        FOLDER_NAME2='C9928134_1'
        ACTION_BAR_TAB_LIST = ['Workspace', 'Folder']
        
        STEP_01 = """
            STEP 01.Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
            STEP 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00',STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 Verification - Verify 2 action bar (Workspaces, Folder) is displayed
        """
        workspace_option = HomePage.Workspaces.ActionBar.locators.action_bar_css
        HomePage.Home._utils.synchronize_with_visble_text(workspace_option, "Workspace", 30)
        HomePage.Workspaces.ActionBar.verify_tab_options(ACTION_BAR_TAB_LIST, '02.01', 'asequal')
        HomePage.Home._utils.capture_screenshot('02.01',STEP_02_01,expected_image_verify=True)
        
        
        STEP_03 = """
            STEP 03.Click on 'Workspaces' action bar
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(FOLDER_NAME1)
        HomePage.Workspaces.ActionBar.select_tab_option("Workspace")
        HomePage.ModalDailogs.NewWorkspace.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 Verification - Verify 'New Workspaces' prompt is displayed
        """
        HomePage.ModalDailogs.NewWorkspace.verify_title('New Workspace', '03.01')
        HomePage.Home._utils.capture_screenshot('03.01',STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """
            STEP 04:Enter Title 'C9928134'
        """
        HomePage.ModalDailogs.NewWorkspace.Title.enter_text(FOLDER_NAME1)
        HomePage.Home._utils.capture_screenshot('04.00',STEP_04)

        STEP_04_01 = """
            STEP 04.01 Verification - Verify the Name will be inherited from the title
            STEP 04.02 Verification - Also, verify that 'Create Reporting Server Application' is checked by default
        """
        HomePage.ModalDailogs.NewWorkspace.Name.verify_text(FOLDER_NAME1,'04.01')
        HomePage.ModalDailogs.NewWorkspace.CreateReportingServerApplication.verify_checked("04.02")
        HomePage.Home._utils.capture_screenshot('04.01',STEP_04_01,expected_image_verify=True)

        STEP_05 = """
            STEP 05 Click on 'Ok' button in new Workspaces prompt
        """
        HomePage.ModalDailogs.NewWorkspace.OKButton.click()
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Workspaces.locators.page_load_completed_css, 50)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME1, 120)
        HomePage.Home._utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
            STEP 05:01 Verification - Verify that the 'C9928134' is created and displayed in the Resource tree/Content area
        """
        HomePage.Workspaces.ContentArea.verify_published_folders([FOLDER_NAME1], '05.01', 'asin')
        HomePage.Home._utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)

        STEP_06 = """
        STEP 06 Right Click on the 'C9928134' > Delete > 'Ok' in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_folder(FOLDER_NAME1)
        HomePage.Home._utils.wait_for_page_loads(80, pause_time=10)
        HomePage.Home._utils.capture_screenshot('STEP 06.00',STEP_06)
        
        STEP_07 = """
        STEP 07 : Again, Click on 'Workspaces' action bar > Enter Title 'C9928134_1' > Uncheck
        'Create Reporting Server Application' > Click Ok
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(FOLDER_NAME2)
        HomePage.Workspaces.ActionBar.select_tab_option("Workspace")
        HomePage.ModalDailogs.NewWorkspace.Title.enter_text(FOLDER_NAME2)
        HomePage.ModalDailogs.NewWorkspace.CreateReportingServerApplication.uncheck()
        HomePage.ModalDailogs.NewWorkspace.OKButton.click()
        HomePage.Home._utils.wait_for_page_loads(100, pause_time=20)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME2, 120)
        HomePage.Home._utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 Verification - Verify that the 'C9928134_1' is created and displayed in the Resource tree/Content area
        """
        HomePage.Workspaces.ContentArea.verify_published_folders([FOLDER_NAME2], '07.01', 'asin')
        HomePage.Home._utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)

        STEP_08 = """
            STEP 08 Right Click on the 'C9928134_1' > Delete > 'Ok' in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_folder(FOLDER_NAME2)
        HomePage.Home._utils.wait_for_page_loads(80, pause_time=10)
        HomePage.Home._utils.capture_screenshot('STEP 08.00',STEP_08)
        
        STEP_09 = """
            STEP 09 In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00',STEP_09)