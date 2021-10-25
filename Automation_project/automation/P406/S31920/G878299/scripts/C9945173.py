"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 03 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9945173_TestClass(BaseTestCase):
    
    def test_C9945173(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        report = 'Reports'
        shortcut_report = 'Reports - Shortcut'
        
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
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(shortcut_report)
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
            STEP 06 : Click on 'Workspaces' from the breadcrumb trail > Double click on 
            'Retail Samples' workspace > Click on 'Reports' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select_workspaces()
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Retail Samples')
        HomePage.ModalDailogs.Resources.GridView.Folders.click(report)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify that Title and Name should be 'Reports' in the entry box and 'Select' button get enabled
        """
        HomePage.ModalDailogs.Resources.Title.verify_text(report, '06.01')
        HomePage.ModalDailogs.Resources.Name.verify_text(report, '06.02')
        HomePage.ModalDailogs.Resources.SelectButton.verify_enabled('06.03')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify the following:
            1.Target path = 'IBFS:WFC/Repository/Retail_Samples/Rep...'
            2.Title = Reports - Shortcut
            3.Summary should be empty
            4.Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/Retail_Samples/Reports', '07.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text('Reports  - Shortcut', '07.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('', '07.03')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('07.04')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('07.05')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, shortcut_report, 60)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that shortcut for an item (Reports - Shortcut folder) is being created properly
            and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_folders([shortcut_report], '08.01')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Right-click on 'Reports - Shortcut' folder > Click on 'Delete'
        """
        HomePage.Workspaces.ContentArea.delete_folder(shortcut_report)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that 'Reports - Shortcut' folder get deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_folders([shortcut_report], '09.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)