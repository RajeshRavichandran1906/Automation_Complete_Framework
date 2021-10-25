"""----------------------------------------------------
Author Name : Robert
Automated on : 22 Jul 2020
----------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930537_TestClass(BaseTestCase):
    
    def test_C9930537(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        
        """TESTCASE VARIABLES"""
        CHOOSE_COLUMNS_CSS = "div.select-data-source div[title='Select columns displayed']"
        DIALOG_TITLE_ALL_CSS= "div.dgrid-header-col-bar-group div.ibx-label-text"
        DIALOG_TITLE_HIDDEN_CSS = "div.dgrid-header-col-bar-group div.dgrid-col-hidden div.ibx-label-text"
        DIALOG_CANCEL_CSS = "div.select-data-source div[title='Cancel']"
        wf_retail_lite_title = "div.home-grid-row[data-ibfs-path*='wf_retail_lite'] div.dgrid-cell:nth-of-type(3)"
        wf_retail_lite_name = "div.home-grid-row[data-ibfs-path*='wf_retail_lite'] div.dgrid-cell:nth-of-type(2)"
        wf_retail_lite_filesize = "div.home-grid-row[data-ibfs-path*='wf_retail_lite'] div.dgrid-cell:nth-of-type(10)"
        
        
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
        
        STEP_03_01 = """
            Step 03.01 :  Verify that Type, Title and Folder gets visible by default & Other columns 
            (Name, Summary, Tags, Owner, Last Modified, Created On, File Size and Path) get hidden by default
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(40,pause_time=3)
        HomePage.Home._utils.synchronize_until_element_is_visible("div[class='dgrid-cell'][title]", 30)
        element_obj = self.driver.find_elements_by_css_selector("div[class='dgrid-cell'][title]")
        elem = HomePage.Home._core_utils.get_element_object_by_text(element_obj, 'retail_samples')
#         elem=self.driver.find_element_by_css_selector("div[class='dgrid-cell'][title='retail_samples']")
#         jsobj.scrollIntoView(elem)
        HomePage.Home._core_utils.double_click(elem)
        title_all_elems= HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_ALL_CSS,"DIALOG_TITLE_ALL_CSS")
        title_hidden_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(DIALOG_TITLE_HIDDEN_CSS,"DIALOG_TITLE_HIDDEN_CSS")
        title_visible_elems=list(set(title_all_elems) - set(title_hidden_elems))
        title_visible_text = [i.text for i in title_visible_elems]
        HomePage.Home._utils.asequal(len(title_visible_elems), 4, "Step 03.01 : Verify 3 columns available")
        title_visible_text.sort()
        HomePage.Home._utils.as_List_equal(['Folder', 'Name', 'Title', 'Type'], title_visible_text, "Step 03.01 : Verify that Type, Title, Name and Folder gets visible by default & Other columns")
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)

        
        
        STEP_04 = """
        Step 04.00 Click on 'Choose Columns' > Check off 'Name' > Click on the empty space to close the column lists 
                    
        """
        HomePage.Home._utils.wait_for_page_loads(40)
        choose_col_elem=HomePage.Home._utils.validate_and_get_webdriver_object(CHOOSE_COLUMNS_CSS, "CHOOSE_COLUMNS_CSS")
        
#         ADD_LIST=['Name']
#         
#         for item in ADD_LIST:
#             choose_col_elem.click()
#             HomePage.Home._utils.wait_for_page_loads(10)
#             HomePage.ContextMenu.select(item)
#             HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04, expected_image_verify = True)
        
        STEP_04_01 = """
            Step 04.01 : Verify that 'Title' column displayed only tile/description for all the data resource type (Master files, Reporting objects, and Business views) and 
            file extensions (.mas, .fex.,) are not included in the title, it is included in the name column
        """
        titles = ['wf_retail_lite' , 'WFR Lite Fact/Dim Cluster'] #writing this to work on all environment
        title = HomePage.Home._utils.validate_and_get_webdriver_object(wf_retail_lite_title, 'title name')   
        display_title = [title.text]
        HomePage.Home._utils.verify_list_values(display_title,titles, "Step 04.01 : Verify Title column displays only title", assert_type='asin')
#         HomePage.Home._utils.verify_element_text(wf_retail_lite_title, "wf_retail_lite", "Step 04.01 : Verify Title column displays only title")
        HomePage.Home._utils.verify_element_text(wf_retail_lite_name, "wf_retail_lite.mas", "Step 04.01 : Verify Name column displays file extensions")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)
        
        STEP_05 = """
            Step 05.00 Click on 'Choose Columns' > Check off 'File Size' > Click on the empty space to close the column lists
        """
        choose_col_elem.click()
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.ContextMenu.select("File Size")
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
        Step 05.01 : Verify that column size should display units such as KB, MB, and GB
        """
        filesize = self.driver.find_element_by_css_selector(wf_retail_lite_filesize).text.strip()
        HomePage.Home._utils.asin("KB", filesize, "Step 05.01 : Verify column size should display units such as KB, MB and GB")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """
        Step 06.00 Click 'Cancel' to close the 'Select Data Source' dialog
        """
        cancel_elem=HomePage.Home._utils.validate_and_get_webdriver_object(DIALOG_CANCEL_CSS, "DIALOG_CANCEL_CSS")
        cancel_elem.click()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
                
        STEP_07 = """In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Home._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
if __name__ == '__main__':
    unittest.main()