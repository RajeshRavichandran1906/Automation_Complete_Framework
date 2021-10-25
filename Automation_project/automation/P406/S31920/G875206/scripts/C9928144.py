"""----------------------------------------------------
Author Name : Robert
Automated on : 17 Jul 2020
----------------------------------------------------"""
import unittest

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods

class C9928144_TestClass(BaseTestCase):
    
    def test_C9928144(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """TESTCASE VARIABLES"""
        DF_BLANK_TEMPLATE_CSS=".df-template-picker div[title='Blank']"
        DF_ASSEMBLE_CSS = ".tlm-assemble"
        DF_CONTAINER_CSS = "[data-ibx-type='pdContainer']"
        DF_LOGO_CSS = "div[title='WebFOCUS Designer Menu']"
        DF_SAVE_DIALOG_TITLE_CSS = ".open-dialog-resources .sd-form-field-text-title input"
        DF_SAVE_DIALOG_SAVE_CSS = ".open-dialog-resources .ibx-dialog-ok-button"
        DF_FILE_NAME = "C9928144"
        DF_FILE_LIST = [DF_FILE_NAME]
        
        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
        Step 02.00 Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Step 03.00 Click on Retail Samples from the resource tree 
        """
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
        Step 04.00 Click '+' menu button on the top toolbar
        """
        HomePage.Workspaces.ContentArea.delete_file_if_exists(DF_FILE_NAME)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
        Step 05.00 Click 'Assemble Visualization' from Tool list menu
        """
        assemble_elem=HomePage.Home._utils.validate_and_get_webdriver_object(DF_ASSEMBLE_CSS,"DF_ASSEMBLE_CSS")
        assemble_elem.click()

        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verify 'Choose template' dialog is displayed
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_object_visible(DF_BLANK_TEMPLATE_CSS, True, "Step 05.01 Verify Template dialog is open")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
        Step 06.00 Select 'Blank' template
        """
        blank_elem=HomePage.Home._utils.validate_and_get_webdriver_object(DF_BLANK_TEMPLATE_CSS, "DF_BLANK_TEMPLATE_CSS")
        blank_elem.click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
        Step 06.01 Verify the canvas shows Blank template
        """
        #HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.verify_object_visible(DF_CONTAINER_CSS, False, "Step 06.01 Verify blank template loaded")
#         HomePage.Home._utils.synchronize_with_number_of_element(DF_CONTAINER_CSS, 1, 60)
#         container_obj = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_CONTAINER_CSS, "DF_CONTAINER_CSS")
#         number_of_containers = len(container_obj)
#         container_obj = HomePage.Home._utils.asequal(1,number_of_containers,"Step 06.01 Verify blank template loaded")
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """
        Step 07.00 Click on Application menu > Save > enter title 'C9928144' > Save
        """
        #HomePage.Workspaces.switch_to_default_content()
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save")
        utils.synchronize_with_visble_text(DF_SAVE_DIALOG_SAVE_CSS, 'Save', 60)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        input_elem[0].click()
        input_elem[0].clear()
        input_elem[0].send_keys(DF_FILE_NAME)
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """Click on Application menu > Close
        """
        logo_elem[0].click()
        HomePage.ContextMenu.select("Close")
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """Verify the created 'C9928144' is displayed in the content area
                        Also, Verify the correct thumbnail appears
        """
        HomePage.Home._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(DF_FILE_LIST, "08.01", 'asin')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, expected_image_verify = True)
        
        STEP_09 = """
                Right Click on 'C9928144' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file(DF_FILE_NAME)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
                Verify the created 'C9928144' is not displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files(DF_FILE_LIST, "09.01", 'asnotin')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, expected_image_verify = True)
        
        STEP_10 = """
        Step 10. In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
if __name__ == '__main__':
    unittest.main()