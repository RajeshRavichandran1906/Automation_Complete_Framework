"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 04-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
import keyboard
from common.wftools.designer_portal import Portal

class C9928118_TestClass(BaseTestCase):
    
    def test_C9928118(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        portal_name = "v5-Twotop"
        DF_LOGO_CSS = "div[title='WebFOCUS Designer Menu']"
        DF_SAVE_DIALOG_TITLE_CSS = ".open-dialog-resources .sd-form-field-text-title input"
        DF_SAVE_DIALOG_SAVE_CSS = ".open-dialog-resources .ibx-dialog-ok-button"
        PG_FILE_NAME1 = "Base Page1"
        PG_FILE_NAME2 = "FPage1"
        PG_FILE_NAME3 = "FPage2"

        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view and Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G875202' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.expand("P406_S31920->G875202")
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on Application category button > Click on Portal action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(portal_name) #Delete portal if already exits.
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Enter title as 'v5-Twotop' in create portal dialog;
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text(portal_name)        
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Choose 'Two-level top' navigation
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Two-level top")
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click Create
        """
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on 'v5-Twotop' in tree and select Folder tile in action bar;
            Enter title as 'Folder1' and click ok
        """
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Workspaces.ResourcesTree.select(portal_name)
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        HomePage.ModalDailogs.Folder.wait_for_appear(10)
        HomePage.ModalDailogs.Folder.Title.enter_text('Folder1')
        HomePage.ModalDailogs.Folder.OKButton.click()
        
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on 'v5-Twotop' in tree and select Page tile in action bar
        """
        HomePage.Workspaces.ResourcesTree.select(portal_name)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Choose Grid 2-1 template and save page as 'Base Page1'
        """
        HomePage.Home._utils.wait_for_page_loads(40)
        self.driver.find_element_by_css_selector("div[title='Grid 2-1']").click()
        HomePage.Home._utils.synchronize_with_visble_text(".pd-page-title .ibx-label-text", "Page Heading", 40)
        
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write(PG_FILE_NAME1,delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        

        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on main menu -> Save as;
            Enter title as 'FPage1' and save it under P292_S19901-> G520448-> v5-Twotop-> Folder1
        """
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save As...")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        
        folder_elem = self.driver.find_element_by_xpath("//div[contains(text(),'Folder1')]")
        HomePage.Home._core_utils.double_click(folder_elem)
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write(PG_FILE_NAME2,delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)


        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on main menu -> Save as;
            Enter title as 'FPage2' and click save as button
        """
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_LOGO_CSS, "DF_LOGO_CSS")
        logo_elem[0].click()
        HomePage.ContextMenu.select("Save As...")
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem= HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_TITLE_CSS, "DF_SAVE_DIALOG_TITLE_CSS")
        
#         folder_elem = self.driver.find_element_by_xpath("//div[contains(text(),'Folder1')]")
#         HomePage.Home._core_utils.double_click(folder_elem)
        input_elem[0].clear()
        HomePage.Home._utils.wait_for_page_loads(20)
        input_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(10)
        keyboard.write(PG_FILE_NAME3,delay=1)
        
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Close designer
        """
        HomePage.Home._core_utils.switch_to_previous_window()

        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Right click on 'v5-Twotop' in tree and select Run
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select(portal_name)
        HomePage.Workspaces.ResourcesTree.right_click(portal_name)
        HomePage.ContextMenu.select("Run")

        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify portal appears as below
        """
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(".pvd-portal-title .ibx-label-text", 'v5-Twotop', 30)
        
        HomePage.Home._utils.verify_element_text(".pvd-portal-title .ibx-label-text", 'v5-Twotop', "Step 14.1 Verify Portal title")
        HomePage.Home._utils.verify_element_text(".ibx-csl-items-box .pvd-close-run-left-panel:nth-of-type(1)", "Base Page1", "Step 14.2a Verify First Tab name")
        HomePage.Home._utils.verify_element_text(".ibx-csl-items-box .pvd-close-run-left-panel:nth-of-type(2)", "Folder1", "Step 14.2b Verify Second Tab name")
        
        container_obj = self.driver.find_elements_by_css_selector(".ibx-selection-manager .pd-container")
        HomePage.Home._utils.verify_visible_elements(container_obj, 3, "Step 14.3 Verify 3 containers")
        
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on 'Folder1'
        """
        self.driver.find_element_by_css_selector(".ibx-csl-items-box .pvd-close-run-left-panel:nth-of-type(2)").click()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify FPage1 and FPage2 are available and appears as below
        """
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.verify_element_text(".pvd-second-level-carousel .ibx-csl-items-box .pvd-close-run-left-panel:nth-of-type(1)", "FPage1", "Step 15.1a Verify First Tab name")
        HomePage.Home._utils.verify_element_text(".pvd-second-level-carousel .ibx-csl-items-box .pvd-close-run-left-panel:nth-of-type(2)", "FPage2", "Step 15.1b Verify Second Tab name")
        container_obj = self.driver.find_elements_by_css_selector(".ibx-selection-manager .pd-container")
        HomePage.Home._utils.verify_visible_elements(container_obj, 3, "Step 15.2 Verify the containers present")

        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Close portal
        """
        HomePage.Home._core_utils.switch_to_previous_window()

        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()


        HomePage.Home._utils.capture_screenshot("17", STEP_17)

