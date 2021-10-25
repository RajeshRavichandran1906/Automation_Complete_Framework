"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 18 Aug 2020
-----------------------------------------------------------------------------------------------"""
import os, keyboard
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.text_editor import Wf_Mainpage as Wf_texteditor
from common.wftools.wf_mainpage import Wf_Mainpage
from selenium.webdriver.common.by import By
from common.locators.designer.components.toolbar import Toolbar

class C9946022_TestClass(BaseTestCase):
    
    def test_C9946022(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        TextEditor = Wf_texteditor(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        FOLDER_CONTEXT_MENU=['Open', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Publish', 'Hide', 'Security', 'Properties']
        PORTAL_CONTEXT_MENU=['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        IMAGE_CONTEXT_MENU=['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Hide', 'Security', 'Properties']
        URL_CONTEXT_MENU=['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        FEX_CONTEXT_MENU=['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        SC_GROUP_PARENT = "#SecurityManagerDialog_treeGroups tr td:nth-of-type(1)"
        EXPAND_ICON_CSS =" img.bi-tree-view-expand-icon"
        GROUP_NAME ="Getting_Started"
        EXPECTED_GROUP_LIST =['Getting Started', 'Getting Started Basic Users', 'Getting Started Advanced Users', 'Getting Started Authors', 'Getting Started Developers', 'Getting Started Group Administrators']
        IMGPATH = os.path.join(os.getcwd(), "data", "Summit.png")
        EXCELPATH = os.path.join(os.getcwd(), "data", "Upload_data.xlsx")
        IBI_URL = "https://www.informationbuilders.com/summit"
        FEX_FILE_NAME = "C9946022.txt"
        DF_DEFAULT_MESSAGE_BOX = ".base-canvas .messageLabel .ibx-label-text"
        DF_LOGO_CSS = Toolbar().application_menu
        DF_SAVE_DIALOG_TITLE_CSS = ".open-dialog-resources .sd-form-field-text-title input"
        DF_SAVE_DIALOG_SAVE_CSS = ".open-dialog-resources .ibx-dialog-ok-button"
        DF_FILE_NAME = "Vis_after_Upload"
        DF_FILE_LIST = [DF_FILE_NAME]
        ITEMS_PUBLISHED_CSS = "div.files-box div[class*='published']"

        
        STEP_01 = """
            STEP 01 : Sign in as Administrator
        """
        
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Open Security Center and expand Getting Started group
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select("Security Center")
        HomePage.Home._core_utils.switch_to_new_window()
        GROUP_NAME_ELEMS=HomePage.Home._utils.validate_and_get_webdriver_objects(SC_GROUP_PARENT,'SC_GROUP_PARENT')
        GROUP_NAME_EXPAND_ICON_ELEMS=HomePage.Home._utils.validate_and_get_webdriver_objects(SC_GROUP_PARENT+EXPAND_ICON_CSS,'SC_GROUP_EXPAND_ICON')
        ACTUAL_GROUP_LIST=[el.text.strip() for el in GROUP_NAME_ELEMS]
        GROUP_NAME_EXPAND_ICON_ELEMS[ACTUAL_GROUP_LIST.index(GROUP_NAME)].click()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify 5 subgroups and above users in the corresponding
        """
        ACTUAL_GROUPS = HomePage.Home._utils.validate_and_get_webdriver_objects("#SecurityManagerDialog_treeGroups tr td:nth-of-type(2)", 'GROUP_NAME_DESCRIPTION_CSS')
        ACTUAL_GROUP_LIST=[el.text.strip() for el in ACTUAL_GROUPS]
        print(ACTUAL_GROUP_LIST)
        SET1 = set(EXPECTED_GROUP_LIST)
        SET2 = set(ACTUAL_GROUP_LIST)
        if SET1.intersection(SET2):
            boolval=True
        else:
            boolval=False
        HomePage.Home._utils.asequal(True,boolval,"Step 02.01 : Verify 5 groups present in the group list.")
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01)
        
        STEP_03 = """
            STEP 03 : Close the Securit.y Center
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : In BIP tree create Admin1 private folder under Getting Started workspace.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.expand("Getting Started")
        HomePage.Workspaces.ResourcesTree.select("Getting Started")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists("Admin1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        HomePage.ModalDailogs.Folder.Title.enter_text("Admin1")
        HomePage.ModalDailogs.Folder.OKButton.click()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Right-click on Admin1 folder
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder("Admin1")
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify context menu:
        """
        HomePage.ContextMenu.verify(FOLDER_CONTEXT_MENU, '05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01)
        
        STEP_06 = """
            STEP 06 : Under Getting Started/Admin1 create private Portal_admin1
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.Title.enter_text("Portal_admin1")
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Right-click on Portal_admin1
        """
        #HomePage.Home._core_utils.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_folder("Portal_admin1")
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify context menu:
        """
        HomePage.ContextMenu.verify(PORTAL_CONTEXT_MENU, '07.01')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01)
        
        STEP_08 = """
            STEP 08 : Click on OTHER and upload attached Summit.png
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Upload File")
        HomePage.Home._utils.wait_for_page_loads(30,pause_time=3)
        FileDialog().open_file(IMGPATH)
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_09 = """
            STEP 09 : Right-click on Summit.png
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Summit")
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify context menu:
        """
        HomePage.ContextMenu.verify(IMAGE_CONTEXT_MENU, '09.01')
        HomePage.Home._utils.capture_screenshot("09.01", STEP_09_01)
        
        STEP_10 = """
            STEP 10 : Click on URL tile, enter URL
            https://www.informationbuilders.com/summit
            Enter title Summit_URL
            Save URL
        """
        upload_close_btn_elem = HomePage.Home._utils.validate_and_get_webdriver_object(".ibx-popup .ibx-title-bar-close-button" , 'UPLOAD_CLOSE_BTN_CSS')
        upload_close_btn_elem.click()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.ModalDailogs.URL.URL.enter_text(IBI_URL)
        HomePage.ModalDailogs.URL.Title.enter_text("Summit_URL")
        HomePage.ModalDailogs.URL.OKButton.click()
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_11 = """
            STEP 11 : Right-click on URL
            
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Summit_URL")
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify context menu:
        """
        HomePage.ContextMenu.verify(URL_CONTEXT_MENU, '11.01')
        HomePage.Home._utils.capture_screenshot("11.01", STEP_11_01)
        
        STEP_12 = """
            STEP 12 : Click on Shortcut tile.
            For Repository shortcut Browse to Getting Started top level and 
            select Visualization Example.
            Click Select
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select("Getting Started")
        HomePage.ModalDailogs.Resources.GridView.Files.click('Visualization Example')
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.ModalDailogs.Shortcut.OKButton.click() 
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Visualization Example - Shortcut is created under
            Getting_Started/Admin1
        """
        HomePage.Workspaces.ContentArea.verify_files(['Visualization Example - Shortcut'], '12.01')
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01)
        
        
        STEP_13 = """
            STEP 13 : Right click on Visualization Example - Shortcut
            and select Run in new window
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Visualization Example - Shortcut")
        HomePage.ContextMenu.select('Run in new window')
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Visualization Example output is displayed in the next tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        container_elems=HomePage.Home._utils.validate_and_get_webdriver_objects("[data-ibx-type='pdContainer']", 'CONTAINER_CSS')
        HomePage.Home._utils.asequal(len(container_elems), 4, 'Step 13.01 : Verify Visualization with 4 containers')
        HomePage.Home._utils.capture_screenshot("13.01", STEP_13_01)
        
        STEP_14 = """
            STEP 14 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("14.00", STEP_14)
        
        STEP_15 = """
            STEP 15 : Click on Text Editor tile.
                Enter
                TABLE FILE retail_sales
                PRINT CITY
                END
                Save it as car1.fex.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Text Editor")
        HomePage.ModalDailogs.NewTextResource.select_tab('CONTENT')
        HomePage.ModalDailogs.NewTextResource.select_file_type("FOCEXEC (fex)")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        TextEditor.enter_data_to_texteditor_from_file(FEX_FILE_NAME)
        TextEditor.click_menu_bar_button('Save')
        HomePage.ModalDailogs.Resources.Title.enter_text("car1")
        HomePage.ModalDailogs.Resources.SaveButton.click()
        
        HomePage.Home._utils.capture_screenshot("15.00", STEP_15)
        
        STEP_16 = """
            STEP 16 : Close the TE and right click on car1.fex
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("car1")
        HomePage.Home._utils.capture_screenshot("16.00", STEP_16)
        STEP_16_01 = """
            STEP 16.01 : Verify context menu:
        """
        HomePage.ContextMenu.verify(FEX_CONTEXT_MENU, '16.01')
        HomePage.ContextMenu.select("Run...")
        HomePage.ContextMenu.verify(['Run in new window', 'Run deferred', 'Run with SQL trace'], "16.02")
        HomePage.Workspaces.ResourcesTree.select("Admin1")
#         HomePage.Workspaces.ContentArea.right_click_on_file("car1")
#         HomePage.ContextMenu.select("Schedule")
#         HomePage.ContextMenu.verify(['Email', 'FTP', 'Printer', 'Report Library', 'Repository'], "16.03")
        HomePage.Home._utils.capture_screenshot("16.01", STEP_16_01)
        
        
        STEP_17 = """
            STEP 17 : Save attached Upload_data.xlsx on your machine.
            Click Get Data, then Excel and browse to saved on your machine Upload_data.xlsx. 
            Load it and Visualize it and save as Vis_after_Upload in Admin1 folder
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.GetDataFrame.locators.content_css, "Excel", 80)
        HomePage.GetDataFrame.GetData.LocalFiles.select('Excel')
        HomePage.Home._utils.wait_for_page_loads(30,pause_time=3)
        FileDialog().open_file(EXCELPATH)
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.GetDataFrame.locators.content_css, "myhome", 80)
        load_elem = HomePage.Home._utils.validate_and_get_webdriver_object("div[qa='Load']", "LOAD_BTN_CSS")
        load_elem.click()
        HomePage.Home._utils.wait_for_page_loads(30)
        try:
            confirm_dialog_okbtn = HomePage.Home._utils.validate_and_get_webdriver_object(".common-confirm-dlg .ibx-dialog-ok-button", 'Confirm_dialog_Ok')
            confirm_dialog_okbtn.click()
        except:
            pass
        HomePage.Home._utils.wait_for_page_loads(60)
        visualize_elem = HomePage.Home._utils.validate_and_get_webdriver_object("div.wcx-buttonpane-buttons div[qa='Visualize Data']", "VISUALIZE_BTN_CSS")
        visualize_elem.click()
        HomePage.Home._utils.capture_screenshot("17.00", STEP_17)
        STEP_17_01 ="""
            STEP 17.01 : Verify Designer loaded
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.synchronize_with_visble_text(DF_DEFAULT_MESSAGE_BOX, "Drop measures & dimensions here",30)
        HomePage.Home._utils.verify_element_text(DF_DEFAULT_MESSAGE_BOX, "Drop measures & dimensions here", "Step 17.01 : Verify Designer is loaded")
        
        search_box_elem = HomePage.Home._utils.validate_and_get_webdriver_object(".resource-box .wfc-mdfp-search", "SEARCH_BOX")
        search_box_elem.click()
        keyboard.write("Re", delay=1)
        
        region_elem = self.driver.find_element(By.XPATH, '//*[contains(text(), "Region")]')
        revenue_elem = self.driver.find_element(By.XPATH, '//*[contains(text(), "Revenue")]')
        HomePage.Home._core_utils.python_doubble_click(region_elem)
        HomePage.Home._core_utils.python_doubble_click(revenue_elem)
        HomePage.Home._utils.wait_for_page_loads(40)
        
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects_using_locator(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write(DF_FILE_NAME,delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._core_utils.switch_to_previous_window()
        #HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.switch_to_frame()
        
        HomePage.Workspaces.ContentArea.verify_files(DF_FILE_LIST, "17.01", 'asin')

        HomePage.Home._utils.capture_screenshot("17.01", STEP_17_01)
        STEP_18 = """
            STEP 18 : Right click on Vis_after_Upload
            and select Run in new window
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file(DF_FILE_NAME)
        HomePage.ContextMenu.select("Run...->Run in new window")
        HomePage.Home._utils.capture_screenshot("18.00", STEP_18)
        
        STEP_18_01 ="""
            STEP 18.01 : output is displayed in the next tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        no_of_risers = HomePage.Home._utils.validate_and_get_webdriver_objects("#jschart_HOLD_0 rect[class^='riser!s0!g']", "RISER_CSS")
        HomePage.Home._utils.asequal(len(no_of_risers), 7, 'Step 18.01 : Verify Visualization output')
        HomePage.Home._utils.capture_screenshot("18.01", STEP_18_01)
        STEP_19 = """
            STEP 19 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("19.00", STEP_19)
        
        STEP_20 = """
            STEP 20 : Publish Admin1 folder.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ResourcesTree.right_click("Admin1")
        HomePage.ContextMenu.select("Publish")
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("20.00", STEP_20)
        
        STEP_20_01 = """
        STEP 20.01 : Verified all items in Admin1 folder are published
        """
        published_elems = HomePage.Home._utils.validate_and_get_webdriver_objects(ITEMS_PUBLISHED_CSS, 'ITEMS_PUBLISHED_CSS')
        HomePage.Home._utils.asequal(len(published_elems), 6, 'Step 20.01 : Verify all items are published')
        HomePage.Home._utils.capture_screenshot("20.01", STEP_20_01)
        STEP_21 = """
            STEP 21 : Open Properties for each item in Admin1 folder
        """
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_folder("Portal_admin1")
        HomePage.ContextMenu.select("Properties")
        
        HomePage.Home._utils.capture_screenshot("21.00", STEP_21)
        
        STEP_21_01 = """
        STEP 21.01 : General and Advanced tabs are available (Query Details tab is available for fexes).
        """
        expected_tab = ['General', 'Advanced', 'Server']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.01 : Verify that properties dialog box for Portal_admin1")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("car1")
        HomePage.ContextMenu.select("Properties")
        
        expected_tab = ['General', 'Advanced', 'Query Detail', 'Server']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.02 : Verify that properties dialog box for car1.fex")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Summit")
        HomePage.ContextMenu.select("Properties")
        
        expected_tab = ['General', 'Advanced']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.03 : Verify that properties dialog box for Summit.png")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Summit_URL")
        HomePage.ContextMenu.select("Properties")

        expected_tab = ['General', 'Advanced']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.04 : Verify that properties dialog box for Summit_URL")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
       
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ContentArea.right_click_on_file("Vis_after_Upload")
        HomePage.ContextMenu.select("Properties")
        
        expected_tab = ['General', 'Advanced', 'Query Detail', 'Server']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.05 : Verify that properties dialog box for Vis_after_upload")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")
        
        HomePage.Workspaces.ResourcesTree.select("Admin1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Visualization Example - Shortcut")
        HomePage.ContextMenu.select("Properties")
        
        expected_tab = ['General', 'Advanced']
        old_homepage.verify_property_dialog_tab_list(expected_tab, "STEP 21.06 : Verify that properties dialog box for Visualization Shortcut")
        old_homepage.select_property_dialog_save_cancel_button("Cancel")

        HomePage.Home._utils.capture_screenshot("21.01", STEP_21_01)
        
        
        STEP_22 = """
        STEP 22 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("22.00", STEP_22)
