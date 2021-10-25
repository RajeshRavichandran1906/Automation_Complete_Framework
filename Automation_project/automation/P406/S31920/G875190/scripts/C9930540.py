"""----------------------------------------------------
Author Name : Robert
Automated on : 22 Jul 2020
----------------------------------------------------"""
import unittest

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930540_TestClass(BaseTestCase):
    
    def test_C9930540(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        
        """TESTCASE VARIABLES"""
        CHOOSE_COLUMNS_CSS = "div.select-data-source div[title='Select columns displayed']"
        DIALOG_TITLE_ALL_CSS= "div.dgrid-header-col-bar-group div.ibx-label-text"
        DIALOG_TITLE_HIDDEN_CSS = "div.dgrid-header-col-bar-group div.dgrid-col-hidden div.ibx-label-text"
        DIALOG_CANCEL_CSS = "div.select-data-source div[title='Cancel']"
        
        
        STEP_01 = """
        Step 01.Sign in to WebFOCUS as Developer
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
        Step 02.00 Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar > Expand the 'Workspaces' from the tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.expand("Workspaces")
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Step 03.00 Click on 'Retail Samples' Workspace > Click on 'Visualize Data' > Click on 'Add Data' 
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_visualize_data()
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
        Step 04.00 Click on 'Choose Columns' > Uncheck 'Type', 'Title' and 'Folder' 
                    > Click on the empty space to close the column lists
        """
        HomePage.Home._core_utils.switch_to_new_window()
        
        HomePage.Home._utils.wait_for_page_loads(40,pause_time=3)
        HomePage.Home._utils.synchronize_until_element_is_visible(CHOOSE_COLUMNS_CSS, 1)
        choose_col_elem=HomePage.Home._utils.validate_and_get_webdriver_object(CHOOSE_COLUMNS_CSS, "CHOOSE_COLUMNS_CSS")
        
        REMOVE_LIST=['Type', 'Name', 'Title', 'Folder']
        
        for item in REMOVE_LIST:
            choose_col_elem.click()
            HomePage.Home._utils.wait_for_page_loads(10)
            HomePage.ContextMenu.select(item)
            HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04, expected_image_verify = True)
        
        STEP_04_01 = """
            Step 04.01 : Verify that there are no more columns available in the 'Select Data Source' dialog
        """
        title_all_elems= HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_ALL_CSS,"DIALOG_TITLE_ALL_CSS")
        title_hidden_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_HIDDEN_CSS,"DIALOG_TITLE_HIDDEN_CSS")
        HomePage.Home._utils.asequal(len(title_all_elems), len(title_hidden_elems), "Step 04.01 Verify no more columns available")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 Click on 'Choose Columns' > Check off 'Name' > Click on the empty space to close the column lists
        """
        choose_col_elem.click()
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.ContextMenu.select("Name")
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Step 05.01 : Verify data resource has no title/description, populate it with the name
        """
        title_all_elems= HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_ALL_CSS,"DIALOG_TITLE_ALL_CSS")
        title_hidden_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_HIDDEN_CSS,"DIALOG_TITLE_HIDDEN_CSS")
        title_visible_elems=list(set(title_all_elems) - set(title_hidden_elems))
        
        title_visible_text = [i.text for i in title_visible_elems]
        HomePage.Home._utils.asequal(len(title_visible_elems), 1, "Step 05.01 Verify one column available")
        HomePage.Home._utils.as_List_equal(['Name'], title_visible_text, "Step 05.02 Verify Name is the only title displayed")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
        Step 06.00 Click 'Cancel' to close the 'Select Data Source' dialog
        """
        cancel_elem=HomePage.Home._utils.validate_and_get_webdriver_object(DIALOG_CANCEL_CSS, "DIALOG_CANCEL_CSS")
        cancel_elem.click()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
        Step 07.00 Close the 'Designer Framework' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """Click on Application menu > Close
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
if __name__ == '__main__':
    unittest.main()