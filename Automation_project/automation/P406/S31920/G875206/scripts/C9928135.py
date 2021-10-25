"""----------------------------------------------------
Author Name : Robert
Automated on : 09 Jan 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage

class C9928135_TestClass(BaseTestCase):
    
    def test_C9928135(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        main_page=Wf_Mainpage(self.driver)
        
        """TESTCASE VARIABLES"""
        FOLDER_LIST=['C9928135']
        FOLDER_NAME='C9928135'
        
        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Click on 'Folder' action bar
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(FOLDER_NAME)
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """
        Step 03.01 Verification - Verify that the 'New Folder' prompt is displayed 
        """
        HomePage.ModalDailogs.Folder.verify_title('New Folder', '03.01')
        utils.capture_screenshot('03.01',STEP_03_01,expected_image_verify=True)
        
        STEP_04 = """
        Step 04:Enter Title 'C9928135'
        """
        HomePage.ModalDailogs.Folder.Title.enter_text(FOLDER_NAME)
        utils.capture_screenshot('04.00',STEP_04)

        STEP_04_01 = """
        Step 04.01 Verification - Verify the Name will be inherited from the title
        Step 04.02 Verification - Also, Verify 'OK' button got enable after the title is being entered
        """
        HomePage.ModalDailogs.Folder.Name.verify_text(FOLDER_NAME,'04.01')
        HomePage.ModalDailogs.Folder.OKButton.verify_enabled('04.02')
        utils.capture_screenshot('04.01',STEP_04_01,expected_image_verify=True)

        STEP_05 = """
        Step 05 Click on the 'Ok' button in new folder prompt
        """
        HomePage.ModalDailogs.Folder.OKButton.click()
        utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME, 60)
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05:01 Verification - Verify that the 'C9928135' is displayed in the Content area as unpublished by default
        Step 05:02 Verification - Verify that the 'C9928135' is displayed in the resource tree as italic by default
        """
        HomePage.Workspaces.ContentArea.verify_unpublished_folders(FOLDER_LIST, '05.01', 'asin')
        main_page.verify_repository_folder_font_style(FOLDER_NAME, 'italic', '05.02')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)

        STEP_06 = """
        Step 06 Right click on 'C9928135' > Publish
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(FOLDER_NAME)
        HomePage.ContextMenu.select('Publish')
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Workspaces.locators.page_load_completed_css, 60, 5)
        utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME, 60)
        utils.capture_screenshot('Step 06.00',STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verification - Verify that the 'C9928135' is displayed in the Content area as published
        Step 06.02 Verification - Verify that the 'C9928135' is displayed in the resource tree as published
        """
        HomePage.Workspaces.ContentArea.verify_published_folders(FOLDER_LIST, '06.01', 'asin')
        main_page.verify_repository_folder_font_style(FOLDER_NAME, 'normal', '06.02')
        utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)

        STEP_07 = """
        Step 07 Right Click on the 'C9928135' > Delete > 'OK' in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_folder(FOLDER_NAME)
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
        Step 07.01 Verification - Verify that the 'C9928135' is not displayed in the Content area
        """
        HomePage.Workspaces.ContentArea.verify_folders(FOLDER_LIST, '07.01', 'asnotin')
        utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Step 08 Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09 = """
        Step 09 Click on 'OTHER' Category button.
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_10 = """   
        Step 10 Click on 'Folder' action bar
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(FOLDER_NAME)
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        utils.capture_screenshot('10.00',STEP_10)
        
        STEP_10_01 = """ 
        Step 10.01 Verify that the 'New Folder' prompt is displayed
        """
        HomePage.ModalDailogs.Folder.verify_title('New Folder', '10.01')
        utils.capture_screenshot('10.01',STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """   
        Step 11 Click on 'Folder' action bar
        """
        HomePage.ModalDailogs.Folder.Title.enter_text(FOLDER_NAME)
        utils.capture_screenshot('11.00',STEP_11)
        
        STEP_11_01 = """ 
        Step 11.01 Verify the Name will be inherited from the title
        Step 11.02 Also, Verify 'OK' button got enable after the title is being entered
        """
        HomePage.ModalDailogs.Folder.Name.verify_text(FOLDER_NAME,'11.01')
        HomePage.ModalDailogs.Folder.OKButton.verify_enabled('11.02')
        utils.capture_screenshot('11.01',STEP_11_01,expected_image_verify=True)
        
        STEP_12 = """
        Step 12 Click on the 'Ok' button in new folder prompt
        """
        HomePage.ModalDailogs.Folder.OKButton.click()
        utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME, 60)
        utils.capture_screenshot('12.00',STEP_12)
        
        STEP_12_01 = """
        Step 12:01 Verification - Verify that the 'C9928135' is displayed in the Content area as unpublished by default
        """
        HomePage.Workspaces.ContentArea.verify_unpublished_folders(FOLDER_LIST, '12.01', 'asin')
        utils.capture_screenshot('12.01',STEP_12_01,expected_image_verify=True)
        
        STEP_13 = """
        Step 13 Right click on 'C9928135' > Publish
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(FOLDER_NAME)
        HomePage.ContextMenu.select('Publish')
        HomePage.Home._utils.synchronize_until_element_is_visible(HomePage.Workspaces.locators.page_load_completed_css, 60, 5)
        utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, FOLDER_NAME, 60)
        utils.capture_screenshot('Step 13.00',STEP_13)
        
        STEP_13_01 = """
        Step 13.01 Verification - Verify that the 'C9928135' is displayed in the Content area as published
        """
        HomePage.Workspaces.ContentArea.verify_published_folders(FOLDER_LIST, '13.01', 'asin')
        utils.capture_screenshot('13.01',STEP_13_01,expected_image_verify=True)
        
        STEP_14 = """
        Step 14 Right Click on the 'C9928135' > Delete > 'OK' in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_folder(FOLDER_NAME)
        utils.capture_screenshot('14.00',STEP_14)
        
        STEP_14_01 = """
        Step 14.01 Verification - Verify that the 'C9928135' is not displayed in the Content area
        """
        HomePage.Workspaces.ContentArea.verify_folders(FOLDER_LIST, '14.01', 'asnotin')
        utils.capture_screenshot('14.01',STEP_14_01,expected_image_verify=True)
        

        STEP_15 = """
        Step 15 In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('15.00',STEP_15)