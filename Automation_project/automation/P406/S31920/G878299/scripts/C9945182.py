"""-------------------------------------------------------------------------------------------
Author Name : Vishnu priya 
Automated On : 16 April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
import time

class C9945182_TestClass(BaseTestCase):
    
    def test_C9945182(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VARIABLES
        """
        shortcut_report = 'TextEditor_Context - Shortcut'
        
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
        HomePage.Workspaces.ContentArea.delete_file_if_exists(shortcut_report)
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
            STEP 06 : Click on > (carot symbol) next to 'P406_S31920' > Click on 'G784912' folder > 
            Double click on 'Images/URL/Blog/TextEditor' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.click_arrow('P406_S31920')
        HomePage.ContextMenu.select('G784912')
        time.sleep(2)
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('Images/URL/Blog/TextEditor')
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : 'Click on 'TextEditor_Context'''
        """
        HomePage.ModalDailogs.Resources.GridView.Files.click('TextEditor_Context')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
        Verify the 'Title' = 'TextEditor_Context' and 'Name' = 'TextEditor_Context.fex'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text('TextEditor_Context','07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text('texteditor_context.fex', '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
        Target path = 'IBFS:/WFC/Repository/P406_S31920/G784912/Images_URL_Blog_TextEditor/texteditor_context.fex'
        Title = TextEditor_Context - Shortcut
        Summary should be empty
        Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/P406_S31920/G784912/Images_URL_Blog_TextEditor/texteditor_context.fex','08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text('TextEditor_Context - Shortcut','08.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('','08.03')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('08.04')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('08.05')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01,expected_image_verify=True)
        
        STEP_09 ="""
        Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
        Verify that shortcut for an item (TextEditor_Context - Shortcut) is being created properly
        and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files(['TextEditor_Context - Shortcut'],'09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01,expected_image_verify=True)
        
        STEP_10 = """
        Right-click on 'TextEditor_Context - Shortcut' item > Click on 'Run'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('TextEditor_Context - Shortcut')
        HomePage.ContextMenu.select('Run')
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
        Verify that 'TextEditor_Context - Shortcut' run without any error
        """
        output_text = HomePage.Home._utils.validate_and_get_webdriver_object(".output-area-label .ibx-label-text","output_label_text").text
        HomePage.Home._utils.asequal('TextEditor_Context - Shortcut',output_text,"Step:10.01 verify the title ")
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """
        Close the run window
        """
        close_button = HomePage.Home._utils.validate_and_get_webdriver_object(".output-area-close-button","close_button")
        HomePage.Home._core_utils.python_left_click(close_button)
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_12 = """
        Edit 'TextEditor_Context - Shortcut'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('TextEditor_Context - Shortcut')
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_12_01 = """
        Verify it restored successfully without any error
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name('Editor',"Step 12.01 verify the TED tool")
        HomePage.Home._utils.capture_screenshot('12.01', STEP_12_01,expected_image_verify=True)
        
        STEP_13 = """
        Close TED tool
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_14 = """
        Right-click on 'TextEditor_Context' item > Click on 'Delete'
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file('TextEditor_Context - Shortcut')
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_14_01 = """
        Verify that 'TextEditor_Context - Shortcut' item get deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files('TextEditor_Context - Shortcut','14.01','asnotin')
        HomePage.Home._utils.capture_screenshot('14.01', STEP_14_01 ,expected_image_verify=True)
        
        STEP_15 = """
            STEP 15 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)