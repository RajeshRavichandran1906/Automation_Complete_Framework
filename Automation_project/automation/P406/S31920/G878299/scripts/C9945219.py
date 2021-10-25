"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 11 May 2020
-----------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage


class C9945219_TestClass(BaseTestCase):
    
    def test_C9945219(self):
        
        """
            TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
            TEST CASE VARIABLES
        """
        PORTAL_SHORTCUT_TITLE='Portal_Page_Context - Shortcut'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree > Click on 'Shortcut Testing'
        """
        HomePage.Workspaces.ResourcesTree.select('P406_S31920->G878309->Shortcut Testing')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        HomePage.Workspaces.ContentArea.delete_file_if_exists(PORTAL_SHORTCUT_TITLE)
        HomePage.Workspaces.ActionBar.select_tab_option('Shortcut')
        HomePage.ModalDailogs.Shortcut.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
            STEP 05 : Click the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click on > (carot symbol) next to 'P406_S31920' > Click on 'G784912' folder > Double click on 'Portal/Pages' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.click_arrow('P406_S31920')
        time.sleep(5)
        HomePage.ContextMenu.select('G784912')
        time.sleep(5)
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Portal/Pages')
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on 'Portal_Page_Context'
        """
        HomePage.ModalDailogs.Resources.GridView.Files.click('Portal_Page_Context')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify the 'Title' = 'Portal_Page_Context' and 'Name' = 'Portal_Page_Context'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text('Portal_Page_Context','07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text('Portal_Page_Context.page', '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01)
        
        STEP_08 = """
            STEP 08 : Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify the following:
            Target path = 'IBFS:/WFC/Repository/P406_S31920/G784912/IA_Visualization/Portal_Page_Context.fex'
            Title = Portal_Page_Context - Shortcut
            Summary should be empty
            Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/P406_S31920/G784912/Portal_Pages/Portal_Page_Context.page','08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text(PORTAL_SHORTCUT_TITLE,'08.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('','08.03')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('08.04')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('08.05')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, expected_image_verify=True)
        
        STEP_09 = """
            STEP 09 : Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that shortcut for an item (Portal_Page_Context - Shortcut) is being created properly
            and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([PORTAL_SHORTCUT_TITLE],'09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01)
        
        STEP_10 = """
            STEP 10 : Right-click on 'Portal_Page_Context - Shortcut' item > Click on 'Delete'
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file(PORTAL_SHORTCUT_TITLE)
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify that 'Portal_Page_Context - Shortcut' item get deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files(PORTAL_SHORTCUT_TITLE, '10.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01 ,expected_image_verify=True)
        
        STEP_11 = """ 
            STEP 11 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)