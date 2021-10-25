"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 24 July 2020
-----------------------------------------------------------------------------------------------"""
import os, keyboard
from common.wftools.page_designer import Run
from common.lib.uiauto import FileDialog
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer_portal import Banner
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.text_editor import Wf_Mainpage as Wf_texteditor
from common.wftools.wf_mainpage import Wf_Mainpage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class C9946025_TestClass(BaseTestCase):
    
    def test_C9946025(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        TextEditor = Wf_texteditor(self.driver)
        OldHomePage = Wf_Mainpage(self.driver)
        PortalBanner = Banner(self.driver)
        PageDesigner = Run(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        portal_file = "Portal_admin2"
        car_file = "car2"
        summit_file = "Summit1"
        summit_url_file = "Summit_URL1"
        visual_upload_file = "Vis_after_Upload1"
        visual_exp_file = "Visualization Example - Shortcut1"
        IMGPATH = os.path.join(os.getcwd(), "data", "Summit.png")
        FEX_FILE_NAME = "C9946022.txt"
        EXCELPATH = os.path.join(os.getcwd(), "data", "Upload_data.xlsx")
        DF_DEFAULT_MESSAGE_BOX = ".base-canvas .messageLabel .ibx-label-text"
        DF_LOGO_CSS = "div[class*='ds-logo-designer']"
        WF_SERVER_LOGO_CSS ="div img[class*='wcx-webfocus-logo']"
        DF_SAVE_DIALOG_TITLE_CSS = ".open-dialog-resources .sd-form-field-text-title input"
        WF_SERVER_SAVE_DIALOG_TITLE_CSS = ".ibx-dialog-content .wcx-fp-filename input"
        DF_SAVE_DIALOG_SAVE_CSS = ".open-dialog-resources .ibx-dialog-ok-button"
        WF_SERVER_SAVE_DIALOG_OKBTN =".ibx-dialog-ok-button"
        DF_FILE_NAME = "Vis_after_Upload_dev1"
        DF_FILE_NAME2 = "Vis_assembleddev1"
        DF_FILE_LIST = [DF_FILE_NAME]
        ITEMS_PUBLISHED_CSS = "div.files-box div[class*='published']"

        
        STEP_01 = """
            STEP 01 : Sign in as gs_dev1@ibi.com
        """
        
        HomePage.invoke_with_login('mriddev', 'mriddevpass')
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify WebFOCUS Homepage opens with Getting Started, Favorites and Portals sections.
        """
        HomePage.Home.verify_sections(['GETTING STARTED', 'FAVORITES', 'PORTALS'], '01.01', assert_type='asin')
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select("Deferred Status")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(20)
        web_elem = self.driver.find_element_by_css_selector("#DeleteMenuItem_top")
        web_elem.click()
        try:
            alert = Alert(self.driver)
            alert.accept()
        except:
            print("No alert noticed")
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02 : Expand [+] area
        """
        HomePage.Banner.click_plus()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify that 'VISUALIZE DATA' having two functions:
                        1. Create New Visualization
                        Start a brand new visualization from scratch
                        2. Assemble Visualizations
                        Leverage existing content you created or shared by others to assemble new visualization.
                        
                        Verify that 'MANAGE DATA'having two functions:
                        3. Get Data
                        4.Prepare and ManageData
        """
        expected_tools = ['Create New Visualization Start a brand new visualization from scratch', 'Assemble Visualizations Leverage existing content you created or shared by others to assemble new visualization.', 'Get Data', 'Prepare and Manage Data']
        tool_obj = self.driver.find_elements(*HomePage.Banner.locators.ToolListMenu.tools)
        actual_tools = [tool.text.strip().replace("\n", " ") for tool in tool_obj if tool.is_displayed()]
        HomePage.Home._utils.asequal(expected_tools, actual_tools, "Step 02.01 : Verify the VISUALIZE DATA functions")

        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01)
        
        
        
        STEP_03 = """
            STEP 03 : Expand Getting Started > Click on 'Admin2' from the resource tree > Double click to run 'Portal_admin1'
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Workspaces.ResourcesTree.select('Getting Started->Admin2')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, portal_file, 30)
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_file)
        HomePage.ContextMenu.select("Run")
        
        #HomePage.Workspaces.ContentArea.double_click_on_folder(portal_file)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that 'Portal_admin2' run without any error
        """
        PortalBanner.verify_portal_top_banner_title(portal_file, 'Step 03.01 : Verify that "Portal_admin2" run without any error')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Close 'Portal_admin2' run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            STEP 05 : Double click to run 'car2'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(car_file)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify that 'car2' run without any error
        """
        HomePage.RunWindow.verify_title(car_file, '05.01')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01)
        
        STEP_06 = """
            STEP 06 : Click 'X' to close 'car2' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Double click to run 'Summit1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_file)
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that 'Summit1' run without any error
        """
        HomePage.RunWindow.verify_title(summit_file, '12.01')
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01)
        
        STEP_08 = """
            STEP 08 : Click 'X' to close 'Summit1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_09 = """
            STEP 09 : Double click to run 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(summit_url_file)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that 'Summit_URL1' run without any error
        """
        btn_css = "a[title^='Register']"
        HomePage.RunWindow.verify_title(summit_url_file, '09.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(btn_css, 'Register', 60)
        btn_text = self.driver.find_element_by_css_selector(btn_css).text.strip()
        HomePage.Home._utils.asequal('Register Now', btn_text, 'Step 09.02 : Verify that "Summit_URL1" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("09.01", STEP_09_01)
        
        STEP_10 = """
            STEP 10 : Click 'X' to close 'Summit_URL1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_11 = """
            STEP 11 : Double click to run 'Vis_after_Upload1
            
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify that 'Vis_after_Upload1' run without any error
        """
        HomePage.RunWindow.verify_title(visual_upload_file, '11.01')
        HomePage.Home._utils.capture_screenshot("11.01", STEP_11_01)
        
        STEP_12 = """
            STEP 12 : Click 'X' to close 'Vis_after_Upload1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_13 = """
            STEP 13 : Double click to run 'Visualization Example- Shortcut1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Verify that 'Visualization Example- Shortcut1' run without any error
        """
        pd_css = ".pd-page-content-wrapper"
        containers = ['Outlier Analysis', 'Store Rankings', 'Revenue by Category', 'Profitability Analysis']
        HomePage.RunWindow.verify_title(visual_exp_file, '13.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(pd_css, 'Analysis', 120)
        PageDesigner.verify_containers_title(containers, 'Step 13.02 : Verify that "Visualization Example- Shortcut" run without any error')
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("13.01", STEP_13_01)
        
        STEP_14 = """
            STEP 14 : Click 'X' to close 'Visualization Example- Shortcut1' run window
        """
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("14.00", STEP_14)
        
        STEP_15 = """
            STEP 15 : Right-click on 'Portal_admin2' > Select 'Properties'
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder(portal_file)
        HomePage.ContextMenu.select('Properties')
        HomePage.Home._utils.capture_screenshot("15.00", STEP_15)
        
        STEP_15_01 = """
            STEP 15.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced'], "Step 15.01 : Verify Properties dialog opens for 'Portal_admin2' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot('15.01', STEP_15_01, True)
        
        STEP_16 = """
            STEP 16 : Click on 'car2'
        """
        HomePage.Workspaces.ContentArea.select_file(car_file)
        HomePage.Home._utils.capture_screenshot("16.00", STEP_16)
        
        STEP_16_01 = """
            STEP 16.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced', 'Query Detail'], "Step 16.01 : Verify Properties dialog opens for 'car2' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot("16.01", STEP_16_01)
        
        
        STEP_17 = """
            STEP 17 : Click on 'Summit1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_file)
        HomePage.Home._utils.capture_screenshot("17.00", STEP_17)
        
        STEP_17_01 ="""
            STEP 17.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced'], "Step 17.01 : Verify Properties dialog opens for 'Summit1' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot("17.01", STEP_17_01)
        
        
        STEP_18 = """
            STEP 18 : Click on 'Summit_URL1'
        """
        HomePage.Workspaces.ContentArea.select_file(summit_url_file)
        HomePage.Home._utils.capture_screenshot("18.00", STEP_18)
        
        STEP_18_01 ="""
            STEP 18.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced'], "Step 18.01 : Verify Properties dialog opens for 'Summit_URL1' and 'General tab' only available'")
        HomePage.Home._utils.capture_screenshot("18.01", STEP_18_01)
        
        STEP_19 = """
            STEP 19 : Click on 'Vis_after_Upload1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_upload_file)
        HomePage.Home._utils.capture_screenshot("19.00", STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced', 'Query Detail'], "Step 19.01 : Verify Properties dialog opens for 'Vis_after_Upload1' and it have 'General and Query tabs'")
        HomePage.Home._utils.capture_screenshot('19.01', STEP_19_01, True)
        
        STEP_20 = """
            STEP 20 : Click on 'Visualization Example- Shortcut1'
        """
        HomePage.Workspaces.ContentArea.select_file(visual_exp_file)
        HomePage.Home._utils.capture_screenshot("20.00", STEP_20)
        
        STEP_20_01 = """
        STEP 20.01 : Verify Properties dialog opens for ''Visualization Example- Shortcut1' and 'General tab' only available
        """
        OldHomePage.verify_property_dialog_tab_list(['General', 'Advanced'], "Step 20.01 : Verify Properties dialog opens for ''Visualization Example- Shortcut' and 'General tab' only available")
        HomePage.Home._utils.capture_screenshot("20.01", STEP_20_01)
        
        STEP_21 = """
            STEP 21 : Click 'Cancel' to close the properties dialog
        """
        OldHomePage.select_property_dialog_save_cancel_button('Cancel')
        #HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("21.00", STEP_21)
        
        STEP_22 = """
            STEP 22 : In BIP tree create Dev1 private folder under Getting Started workspace.
            Right-click on Dev1 folder
        """
        HomePage.Workspaces.ResourcesTree.select("Getting Started")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists("Dev1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        HomePage.ModalDailogs.Folder.Title.enter_text("Dev1")
        HomePage.ModalDailogs.Folder.OKButton.click()
        HomePage.Home._utils.capture_screenshot("22.00", STEP_22)
        
        STEP_22_01 = """
            STEP 22_01 : Verify context menu:
        """
        FOLDER_CONTEXT_MENU =['Open', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Publish', 'Hide', 'Security', 'Properties']
        HomePage.Workspaces.ContentArea.right_click_on_folder("Dev1")
        HomePage.ContextMenu.verify(FOLDER_CONTEXT_MENU, "22.01")
        HomePage.Home._utils.capture_screenshot("22.01", STEP_22_01, True)
        
        STEP_23 = """
            STEP 23 : Under Getting Started/Dev1 create private Portal_dev1
                    Right-click on Portal_dev1
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.Title.enter_text("Portal_dev1")
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.capture_screenshot("23.00", STEP_23)
        
        STEP_23_01 = """
            STEP 23_01 : Verify context menu:
        """
        PORTAL_CONTEXT_MENU =['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        HomePage.Workspaces.ContentArea.right_click_on_folder("Portal_dev1")
        HomePage.ContextMenu.verify(PORTAL_CONTEXT_MENU, "23.01")
        HomePage.Home._utils.capture_screenshot("23.01", STEP_23_01, True)
        
        STEP_24 = """
            STEP 24 : Under Getting Started/Dev1 > Click on OTHER and upload attached Summit.png
                    Right-click on Summit.png
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Upload File")
        HomePage.Home._utils.wait_for_page_loads(30)
        FileDialog().open_file(IMGPATH)
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Summit")
        HomePage.Home._utils.capture_screenshot("24.00", STEP_24)
        
        STEP_24_01 = """
            STEP 24_01 : Verify context menu:
        """
        IMAGE_CONTEXT_MENU =['View', 'View in new window', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(IMAGE_CONTEXT_MENU, '24.01')
        HomePage.Home._utils.capture_screenshot("24.01", STEP_24_01, True)
        
        STEP_25 = """
            STEP 25 : Click on URL tile, enter URL
                https://www.informationbuilders.com/summit
                Enter title URL_dev1
                Save URL.
        """
        upload_close_btn_elem = HomePage.Home._utils.validate_and_get_webdriver_object(".ibx-popup .ibx-title-bar-close-button" , 'UPLOAD_CLOSE_BTN_CSS')
        upload_close_btn_elem.click()
        IBI_URL = "https://www.informationbuilders.com/summit"
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ActionBar.select_tab_option("URL")
        HomePage.ModalDailogs.URL.URL.enter_text(IBI_URL)
        HomePage.ModalDailogs.URL.Title.enter_text("URL_dev1")
        HomePage.ModalDailogs.URL.OKButton.click()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("25.00", STEP_25)
        
        STEP_26 = """
            STEP 26 : Right-click on URL
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file("URL_dev1")
        
        HomePage.Home._utils.capture_screenshot("26.00", STEP_26)
        
        STEP_26_01 = """
            STEP 26_01 : Verify context menu:
        """
        URL_CONTEXT_MENU=['View', 'View in new window', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(URL_CONTEXT_MENU, '26.01')
        HomePage.Home._utils.capture_screenshot("26.01", STEP_26_01, True)
        
        STEP_27 = """
            STEP 27 : Click on Shortcut tile > Click Master file radio button > Click on Browse
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.ModalDailogs.Shortcut.wait_for_appear(20)
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.click()
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.capture_screenshot("27.00", STEP_27)
        
        STEP_28 = """
            STEP 28 : Select retail_sales.mas > Click Select > Change Title to retail_sales_dev1 > click OK
        """
        HomePage.ModalDailogs.Resources.GridView.Files.click('retail_sales.mas')
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        #HomePage.ModalDailogs.Shortcut.wait_for_diappear(10)
        HomePage.Home._utils.capture_screenshot("28.00", STEP_28)
        
        STEP_28_01 = """
            STEP 28_01 : Shortcut is created with temporary displayed msg:
        """
        HomePage.Home._utils.verify_element_visiblty(element_css=".notify-popup.success", visible=True, msg="Step 28.01 : Verify temporary displayed message")
        HomePage.Workspaces.ContentArea.verify_files(['retail_sales'], '28.01')
        HomePage.Home._utils.capture_screenshot("28.01", STEP_28_01, True)
        
        STEP_29 = """
            STEP 29 : Click on Shortcut tile > Click Browse > Select Visualization Example under Getting Started top level > 
                        Change Title to Visualization Example - dev1 > Click Select
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select("Getting Started")
        HomePage.ModalDailogs.Resources.GridView.Files.click('Visualization Example')
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.ModalDailogs.Shortcut.Title.enter_text("Visualization Example - dev1")
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.wait_for_page_loads(20)
        #HomePage.ModalDailogs.Shortcut.wait_for_diappear(20)
        HomePage.Home._utils.capture_screenshot("29.00", STEP_29) 

        STEP_29_01 = """
            STEP 29_01 : Visualization Example - dev1 is created under
                Getting_Started/Dev1
        """
        HomePage.Workspaces.ContentArea.verify_files(['Visualization Example - dev1'], '29.01')
        HomePage.Home._utils.capture_screenshot("29.01", STEP_29_01, True)
        
        STEP_30 = """
            STEP 30 : Right click on Visualization Example - dev1 and select Run in new window
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file("Visualization Example - dev1")
        HomePage.ContextMenu.select('Run in new window')
        HomePage.Home._utils.capture_screenshot("30.00", STEP_30)
        
        STEP_30_01 = """
            STEP_30.01 : Visualization Example output is displayed in the next tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        container_elems=HomePage.Home._utils.validate_and_get_webdriver_objects("[data-ibx-type='pdContainer']", 'CONTAINER_CSS')
        HomePage.Home._utils.asequal(len(container_elems), 4, 'STEP_30.01 : Verify Visualization with 4 containers')
        HomePage.Home._utils.capture_screenshot("30.01", STEP_30_01)
        
        STEP_31 = """
            STEP 31 : Close the run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("31.00", STEP_31)
        
        STEP_32 = """
            STEP 32 : Click on Text Editor action tile under other category button > Select FOCEXEC > Enter the following:
                TABLE FILE retail_sales
                PRINT CITY
                END

                Save it as city_dev1.fex.
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
        HomePage.ModalDailogs.Resources.Title.enter_text("city_dev1")
        HomePage.ModalDailogs.Resources.SaveButton.click()
        HomePage.Home._utils.capture_screenshot("32.00", STEP_32)
        
        STEP_33 = """
            STEP 33 : Right click on city_dev1.fex
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file("city_dev1")
        HomePage.Home._utils.capture_screenshot("33.00", STEP_33)
        
        STEP_33_01 = """
            STEP 33_01 : Verify context menu:
        """
        FEX_CONTEXT_MENU=['Run', 'Run...', 'Schedule', 'Edit', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(FEX_CONTEXT_MENU, '33.01')
        HomePage.Home._utils.capture_screenshot("33.01", STEP_33_01, True)
        
        STEP_34 = """
            STEP 34 : Save attached UploadTree.xlsx on your machine.
            Click Get Data > Click on Excel > browse to the saved on your machine UploadTree.xlsx > Load it > Visualize it > save as Vis_after_Upload _dev1 in Dev1 folder
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Banner.click_get_data()
        HomePage.GetDataFrame.switch_to_frame()
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.GetDataFrame.locators.content_css, "Excel", 80)
        HomePage.GetDataFrame.GetData.LocalFiles.select('Excel')
        HomePage.Home._utils.wait_for_page_loads(30)
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
        #HomePage.Home._utils.wait_for_page_loads(30)
        visualize_data="div.wcxcomponent div[title='Visualize Data']"
        HomePage.Home._utils.synchronize_with_visble_text(visualize_data, 'Visualize Data',30)
        visualize_elem = HomePage.Home._utils.validate_and_get_webdriver_object(visualize_data, "VISUALIZE_BTN_CSS")
        visualize_elem.click()
        HomePage.Home._utils.capture_screenshot("34.00", STEP_34)
        
        STEP_34_01 = """
            STEP 34.01 : Verify Designer loaded
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.synchronize_with_visble_text(DF_DEFAULT_MESSAGE_BOX, "Drop measures & dimensions here",30)
        HomePage.Home._utils.verify_element_text(DF_DEFAULT_MESSAGE_BOX, "Drop measures & dimensions here", "Step 34.01 : Verify Designer is loaded")
        
        search_box_elem = HomePage.Home._utils.validate_and_get_webdriver_object(".resource-box .wfc-mdfp-search", "SEARCH_BOX")
        search_box_elem.click()
        keyboard.write("Re", delay=1)
        
        region_elem = self.driver.find_element(By.XPATH, '//*[contains(text(), "Region")]')
        revenue_elem = self.driver.find_element(By.XPATH, '//*[contains(text(), "Revenue")]')
        HomePage.Home._core_utils.python_doubble_click(region_elem)
        HomePage.Home._core_utils.python_doubble_click(revenue_elem)
        HomePage.Home._utils.wait_for_page_loads(40)
        
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
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
        #HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        
        HomePage.Workspaces.ContentArea.verify_files(DF_FILE_LIST, "34.01", 'asin')
        HomePage.Home._utils.capture_screenshot("34.01", STEP_34_01, True)
     
        STEP_35 = """
            STEP 35 : Right click on Vis_after_Upload
                and select Run in new window
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file(DF_FILE_NAME)
        HomePage.ContextMenu.select("Run...->Run in new window")
        HomePage.Home._utils.capture_screenshot("35.00", STEP_35)
        
        STEP_35_01 = """
            STEP 35_01 : Output is displayed in the next tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        no_of_risers = HomePage.Home._utils.validate_and_get_webdriver_objects("#jschart_HOLD_0 rect[class^='riser!s0!g']", "RISER_CSS")
        HomePage.Home._utils.asequal(len(no_of_risers), 7, 'Step 35.01 : Verify Visualization output')

        HomePage.Home._utils.capture_screenshot("35.01", STEP_35_01, True)
        
        STEP_36 = """
            STEP 36 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("36.00", STEP_36)
        
        STEP_37 = """
            STEP 37 : Expand [+] area > select Assemble Visualizations > Select Grid 2-1 template
        """
        HomePage.Workspaces.switch_to_default_content()
        grid_2_1 = "div[title='Grid 2-1']"
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualizations")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_number_of_element("div.df-tp-item",6,30)
        web_elem= HomePage.Home._utils.validate_and_get_webdriver_object(grid_2_1,'grid_2_1')
        web_elem.click()
        HomePage.Home._utils.synchronize_with_number_of_element("[data-ibx-type='pdContainer']",3,40)
        
        HomePage.Home._utils.capture_screenshot("37.00", STEP_37)
        
        STEP_38 = """
            STEP 38 : Add Vis_after_Upload dev1 and Summit.png under Getting Started/Dev1 to containers 1 and 2. Save it as Vis _assembleddev1
        """
        xpath1 = "//div[contains(text(),'Vis_after_Upload_dev1')]"
        source_elem=self.driver.find_element_by_xpath(xpath1)
        xpath2 = "//div[contains(text(),'Panel 1')]"
        target_elem = self.driver.find_element_by_xpath(xpath2)
        HomePage.Home._utils.drag_drop_using_uisoup(source_elem, target_elem)
        HomePage.Home._utils.wait_for_page_loads(30)
        
        xpath1 = "//div[contains(text(),'Summit')]"
        source_elem=self.driver.find_element_by_xpath(xpath1)
        xpath2 = "//div[contains(text(),'Panel 2')]"
        target_elem = self.driver.find_element_by_xpath(xpath2)
        HomePage.Home._utils.drag_drop_using_uisoup(source_elem, target_elem)
        HomePage.Home._utils.wait_for_page_loads(30)
        
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write(DF_FILE_NAME2,delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._core_utils.switch_to_previous_window()
        
        HomePage.Home._utils.capture_screenshot("38.00", STEP_38)
        
        STEP_39 = """
            STEP 39 : Right click on Vis assembleddev1
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file(DF_FILE_NAME2)
        HomePage.Home._utils.capture_screenshot("39.00", STEP_39)
        
        STEP_39_01 = """
            STEP 39_01 : Verify context menu:
        """
        VISUAL_CONTEXT_MENU=['Run', 'Run in new window', 'Edit', 'Download translations...', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Create shortcut', 'Delete DEL', 'Add to Favorites', 'Hide', 'Security', 'Properties']
        HomePage.ContextMenu.verify(VISUAL_CONTEXT_MENU, '39.01')
        HomePage.Home._utils.capture_screenshot("39.01", STEP_39_01, True)
        
        STEP_40 = """
            STEP 40 : Right click on Vis assembleddev1 and select Run in new window
        """
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file(DF_FILE_NAME2)
        HomePage.ContextMenu.select("Run in new window")

        HomePage.Home._utils.capture_screenshot("40.00", STEP_40)
        
        STEP_40_01 = """
            STEP 40_01 : Output is displayed in the next tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        page_title = self.driver.title
        HomePage.Home._utils.asin(DF_FILE_NAME2, page_title, "Step 40.01 : Verify Output is displayed in the next tab")
        HomePage.Home._utils.capture_screenshot("40.01", STEP_40_01, True)
        
        STEP_41 = """
            STEP 41 : Close the run window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("41.00", STEP_41)
        
        STEP_42 = """
            STEP 42 : Right click on Vis_after_Upload_dev1 and select Run/Run Deferred.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("Dev1")
        HomePage.Workspaces.ContentArea.right_click_on_file(DF_FILE_NAME)
        HomePage.ContextMenu.select("Run...->Run deferred")
        HomePage.Home._utils.capture_screenshot("42.00", STEP_42)
        
        STEP_43 = """
            STEP 43 : In Deferred Report Description enter 'def_Vis_after_Upload_dev1' and click OK
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.synchronize_with_number_of_element('input#new_description',1,20)
        web_elem=HomePage.Home._utils.validate_and_get_webdriver_object('input#new_description','INPUT_BOX')
        web_elem.clear()
        web_elem.click()
        web_elem.send_keys("def_Vis_after_Upload_dev1")
        web_elem=HomePage.Home._utils.validate_and_get_webdriver_object('input#okButton', 'OK_BUTTON')
        web_elem.click()
        HomePage.Home._utils.wait_for_page_loads(30)

        HomePage.Home._utils.capture_screenshot("43.00", STEP_43)
        
        
        STEP_44 = """
            STEP 44 : Click Deferred Report Status interface link
        """
        HomePage.Home._utils.synchronize_with_number_of_element('#deferMsg a',1,20)
        web_elem=HomePage.Home._utils.validate_and_get_webdriver_object('#deferMsg a', 'LINK')
        web_elem.click()
                                                                    
        HomePage.Home._utils.capture_screenshot("44.00", STEP_44)
        
        STEP_44_01 = """
            STEP 44_01 : Verify that def_Vis_after_Upload is in Queued or Completed status.
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        deferred_report_queued ="//span[contains(text(),'def_Vis_after_Upload_dev1')]"
        web_elem = self.driver.find_element_by_xpath(deferred_report_queued)
        HomePage.Home._utils.verify_element_visiblty(element=web_elem, visible=True, msg="Step 44.01 : Verify def_Vis_after_Upload is in Queued or Completed status")
        HomePage.Home._utils.capture_screenshot("44.01", STEP_44_01, True)
        
        STEP_45 = """
            STEP 45 : Click View from Deferred Report Status
        """
        view_btn_xpath="//tr//a[contains(@href, 'vis_after_upload_dev1')]//img[contains(@src,'ENdeview')]"
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH, view_btn_xpath)))
        web_elem = self.driver.find_element_by_xpath(view_btn_xpath)
        web_elem.click()
        HomePage.Home._utils.capture_screenshot("45.00", STEP_45)
        
        STEP_45_01 = """
            STEP 45_01 : output is displayed
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        
        '''need checkpoint for output window'''
        page_title = self.driver.title
        HomePage.Home._utils.asin("Chart1", page_title, "Step 45.01 : Verify Output is displayed in the next tab")

        HomePage.Home._core_utils.switch_to_previous_window()

        HomePage.Home._utils.capture_screenshot("45.01", STEP_45_01, True)
        
        STEP_46 = """
            STEP 46 : Click delete
            
        """
        del_btn_xpath="//tr//a[contains(@href, 'def_Vis_after_Upload_dev1')]//img[contains(@src,'ENdedelete')]"
        web_elem = self.driver.find_element_by_xpath(del_btn_xpath)
        web_elem.click()
        obj = self.driver.switch_to.alert
        obj.accept()

        HomePage.Home._utils.capture_screenshot("46.00", STEP_46)
        
        STEP_46_01 = """
            STEP 46_01 : Verify no report submited message
        """
        verify_msg_css= "//html/body/div[1]"
        web_elem = self.driver.find_element_by_xpath(verify_msg_css)
        actual_msg = web_elem.text
        expected_text = 'There are no deferred requests submitted for your ID.'
        HomePage.Home._utils.asequal(expected_text,actual_msg, "Step 46.01 : Verify no report submitted message")
        HomePage.Home._utils.capture_screenshot("46.01", STEP_46_01, True)
        
        STEP_47 = """
            STEP 47 : Close Deferred Report Status
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("47.00", STEP_47)
        
        STEP_48 = """
            STEP 48 : Expand [+] area and select Prepare and Manage Data.
        """
        grid_2_1 = "div[title='Grid 2-1']"
        HomePage.Banner.click_plus()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Banner.ToolListMenu.select_tool("Prepare and Manage Data")
        
        HomePage.Home._utils.capture_screenshot("48.00", STEP_48)
        
        STEP_48_01 = """
            STEP 48_01 : Verify Webconsole window opens in a new tab
        """
        HomePage.Home._core_utils.switch_to_new_window()
        page_title = self.driver.title
        HomePage.Home._utils.asin('WebConsole', page_title, "Step 48.01 : Verify webconsole is opened in new tab")
        
        HomePage.Home._utils.capture_screenshot("48.01", STEP_48_01, True)
        
        STEP_49 = """
            STEP 49 : Double click on getting_started folder in content area;
            Double click on retail_sales
        """
        gs_css = "//div[@qa='MFLeftContent']//div[contains(text(), 'getting_started')]"
        rsales= "//div[@qa='MFRightContent']//div[contains(text(), 'retail_sales')]"
        web_elem = self.driver.find_element_by_xpath(gs_css)
        HomePage.Home._utils.click_type_using_pyautogui(web_elem, doubleClick=True)
        HomePage.Home._utils.wait_for_page_loads(20)
        web_elem = self.driver.find_element_by_xpath(rsales)
        HomePage.Home._utils.click_type_using_pyautogui(web_elem, doubleClick=True)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("49.00", STEP_49)
        
        STEP_50 = """
            STEP 50 : Use Save As option to save it as retail_sales_dev1.
            Close the retail_samples window.
        """
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(WF_SERVER_LOGO_CSS, "WF_SERVER_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save As")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(WF_SERVER_SAVE_DIALOG_TITLE_CSS, "WF_SERVER_SAVE_DIALOG_TITLE_CSS")
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write("retail_sales_dev1",delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(WF_SERVER_SAVE_DIALOG_OKBTN, "WF_SERVER_SAVE_DIALOG_OKBTN")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._core_utils.switch_to_previous_window()

        HomePage.Home._utils.capture_screenshot("50.00", STEP_50)
        
        STEP_51 = """
            STEP 51 : Refresh the WebConsole;
                Double click on getting_started folder in content area.
        """
        self.driver.refresh
        HomePage.Home._utils.wait_for_page_loads(40)
        
        web_elem = self.driver.find_element_by_xpath(gs_css)
        HomePage.Home._utils.click_type_using_pyautogui(web_elem, doubleClick=True)
        HomePage.Home._utils.wait_for_page_loads(40)
        
        HomePage.Home._utils.capture_screenshot("51.00", STEP_51)
        
        STEP_51_01 = """
            STEP 51_01 : retail_sales_dev1.mas is saved under getting_started app folder
        """
        rsales_test= "//div[@qa='MFRightContent']//div[contains(text(), 'retail_sales_dev1')]"
        web_elem = self.driver.find_element_by_xpath(rsales_test)
        HomePage.Home._utils.verify_element_visiblty(element=web_elem, visible=True, msg="Step 51.01 : Verify retail_sales_dev1.mas is saved under getting_started app folder")

        HomePage.Home._utils.capture_screenshot("51.01", STEP_51_01, True)
        
        STEP_52 = """
            STEP 52 : Close the WebConsole windows.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("52.00", STEP_52)
        
 
        STEP_53 = """
        STEP 53 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("53.00", STEP_53)
