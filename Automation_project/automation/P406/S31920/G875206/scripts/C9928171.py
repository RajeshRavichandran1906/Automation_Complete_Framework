"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 07 February 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import text_editor as TextEditor
from common.wftools.paris_home_page import ParisHomePage

class C9928171_TestClass(BaseTestCase):
    
    def test_C9928171(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage  =  ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        case_id = "C9928171"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on 'Other' category button and Click on 'Text Editor' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ContentArea.delete_file_if_exists(case_id)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Click on 'Text Editor' action bar > Select 'FOCEXEC(fex)'
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Text Editor")
        HomePage.ModalDailogs.NewTextResource.wait_for_appear()
        HomePage.ModalDailogs.NewTextResource.select_file_type('FOCEXEC (fex)')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify Texteditor window opens with the New FOCEXEC file tab
        """
        TextEditor.wf_texteditor(self.driver).verify_tabs(['New FOCEXEC File'], '05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click on Application menu > Save > Enter title as 'C9928171' > Click Save
        """
        TextEditor.editor_toolbar(self.driver).save_page_from_application_menu(page_title=case_id)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on Application menu > Exit
        """
        TextEditor.editor_toolbar(self.driver).select_application_menu_option('Exit')
        HomePage.Home._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that 'C9928171' is displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files([case_id], '07.01')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Right click on 'C9928171' > Delete > Click Yes in the 'Delete' dialog box
        """
        HomePage.Workspaces.ContentArea.delete_file(case_id)
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that 'C9928171' is not displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files([case_id], '08.01','asnotin')
        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)