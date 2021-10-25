"""----------------------------------------------------
Author Name  : Robert
Automated on : 07 August 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927131_TestClass(BaseTestCase):
    
    def test_C9927131(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        ADMIN_CONSOLE_BI_PORTAL = "//div[contains(@id,'Configuration_Settings')]//*[contains(text(),'BI Portal')]"
        ADMIN_CONSOLE_CLIENT_SETTINGS = "//div[contains(@id,'Configuration_Settings')]//*[contains(text(),'Client Settings')]"
        ADMIN_CONSOLE_APPLICATION_SETTINGS = "//div[contains(@id,'Configuration_Settings')]//*[contains(text(),'Application Settings')]"
        ADMIN_CONSOLE_V3PORTAL_CHECKBOX = "//div[contains(@id,'checkboxIBI_V3_PORTAL')]//input"
        ADMIN_CONSOLE_V4PORTAL_CHECKBOX = "//div[contains(@id,'checkboxIBI_V4_PORTAL')]//input"
        ADMIN_CONSOLE_SAVE_BUTTON = "//div[contains(@id,'ClientSaveButton')]"
        WRKBENCH_TEMPLATE = "//div[contains(text(),'Workbench')]"
        V4_CREATE_BUTTON = "//div[contains(text(),'Create')]"
        V4_WORKSPACES = "//*[contains(text(),'Workspaces')]"
        V4_REPORT_OUTPUT = "//*[contains(text(),'Report Output')]"
        V4_SAVE_DIALOG_OK = "//div[@id='dlgPortalSaveDialog']//div[contains(text(),'OK')]"
       
        def verify_window_title(expected_window_title, step):
            #HomePage.Home._core_utils.switch_to_new_window()
            current_window_title = self.driver.title
            HomePage.Home._utils.asequal(current_window_title, expected_window_title, step)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on Workspaces
        """
        HomePage.Banner.close_page_message()
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Home._utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
            STEP 03 : Expand My Workspace -> MY Content folder from the resource tree you have access to
        """
        HomePage.Workspaces.ResourcesTree.expand("My Workspace")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Home._utils.capture_screenshot('03.00',STEP_03)

        
        STEP_04 = """
            STEP 04 : Click on 'Application' category button > click on 'Portal'
        """
        HomePage.Workspaces.ContentArea.delete_folder_if_exists("Portal for MyContent")
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.Home._utils.capture_screenshot('04.00',STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verification - Verify it brings up Portal dialog
        """
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal","04.01")
        HomePage.Home._utils.capture_screenshot('04.01',STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Enter Title as "Portal for MyContent" > Click 'Create'
        """
        HomePage.ModalDailogs.V5Portal.Title.enter_text("Portal for MyContent")
        HomePage.ModalDailogs.V5Portal.CreateButton.click()
        
        HomePage.Home._utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify 'Portal for MyContent' appear as a folder
        """
        HomePage.Workspaces.ContentArea.verify_folders(['Portal for MyContent'], "05.01")
        HomePage.Home._utils.capture_screenshot('05.01',STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click on My Workspace link
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify the portal appears there.
        """
        #HomePage.Workspaces.switch_to_frame()
        HomePage.MyWorkspace.verify_items(['Portal for MyContent'], "05.01")
        HomePage.Home._utils.capture_screenshot('06.01',STEP_06_01, True)
        
        
        STEP_07 = """
            STEP 07 : Right click on that portal
        """
        HomePage.MyWorkspace.right_click_on_item('Portal for MyContent')
        HomePage.Home._utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify there is NO share and share with menu
        """
        HomePage.ContextMenu.verify(['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties'],"07.01")
        HomePage.Home._utils.capture_screenshot('07.01',STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Click on Workspaces
        """
        #HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_breadcrumb("Workspaces")
        HomePage.Home._utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09 = """
            STEP 09 : Expand My Workspace -> MY Content folder from the resource tree you have access to
        """
        HomePage.Workspaces.ResourcesTree.expand("My Workspace->My Content")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Home._utils.capture_screenshot('09.00',STEP_09)
        
        STEP_10 = """
            STEP 10 : Click on Others
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")

        HomePage.Home._utils.capture_screenshot('10.00',STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify no Portal Page and Collaborative Portal
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor'],"10.01")
        
        HomePage.Home._utils.capture_screenshot('10.01',STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : As an Admin user go to the Admin console;
                    Select BI Portal.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('Administration Console')
        HomePage.Home._core_utils.switch_to_new_window()
        expected_window_title = 'Administration Console'
        verify_window_title(expected_window_title, 'Step 11.01 : Verify "Administration Console" new window opens')
        HomePage.Home._utils.wait_for_page_loads(30)
        
        ''' more steps '''
        
        try:
            webelem= self.driver.find_element_by_xpath(ADMIN_CONSOLE_BI_PORTAL)
            if webelem.is_displayed()==False:
                elem=self.driver.find_element_by_xpath(ADMIN_CONSOLE_APPLICATION_SETTINGS)
                elem.click()
            webelem.click()
        except:
            pass
        
        
        HomePage.Home._utils.capture_screenshot('11.00',STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verify Collaborative portal and basic portal is not checked
        """
        v3_elem= self.driver.find_element_by_xpath(ADMIN_CONSOLE_V3PORTAL_CHECKBOX)
        v3_checked = v3_elem.is_selected()
        
        v4_elem= self.driver.find_element_by_xpath(ADMIN_CONSOLE_V4PORTAL_CHECKBOX)
        v4_checked = v4_elem.is_selected()
        
        HomePage.Home._utils.asequal(v3_checked,False, "Step 11.01 : Verify V3 Portal Checkbox is not checked")
        HomePage.Home._utils.asequal(v4_checked,False, "Step 11.01 : Verify V4 Portal Checkbox is not checked")
        HomePage.Home._utils.capture_screenshot('11.01',STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Check Collaborative Portal and Save;
            Close the admin console.
        """
        v4_elem.click()
        save_btn_elem = self.driver.find_element_by_xpath(ADMIN_CONSOLE_SAVE_BUTTON)
        save_btn_elem.click()
        obj=self.driver.switch_to.alert
        obj.accept()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('12.00',STEP_12)
        
        STEP_13 = """
            STEP 13 : Click on Others --> Collaborative Portal
        """
        self.driver.refresh()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.expand("My Workspace->My Content")
        HomePage.Workspaces.ResourcesTree.select("My Content")
        HomePage.Workspaces.ContentArea.delete_file_if_exists("V4 Portal for MyContent")
        HomePage.Workspaces.ContentArea.delete_folder_if_exists("V4 Portal for MyContent Resources")
        
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Collaborative Portal")
        HomePage.Home._utils.capture_screenshot('13.00',STEP_13)
        
        STEP_14 = """
            STEP 14 : Enter Title as "V4 Portal for MyContent" > Click 'Create'
        """
        HomePage.ModalDailogs.CollaborativePortal.Title.enter_text("V4 Portal for MyContent")
        HomePage.ModalDailogs.CollaborativePortal.CreateButton.click()
        HomePage.Home._utils.capture_screenshot('14.00',STEP_14)
        
        STEP_15 = """
            STEP 15 : Choose Workbench template
                    Click Create
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text("#dlgTitleExplorer .window-caption", "Add Page",30)
        webelem = self.driver.find_element_by_xpath(WRKBENCH_TEMPLATE)
        webelem.click()
        webelem =self.driver.find_element_by_xpath(V4_CREATE_BUTTON)
        webelem.click()
        HomePage.Home._utils.capture_screenshot('15.00',STEP_15)
        
        STEP_15_01 = """
            STEP 15.01 : Verify the portal and the resources folder appear
        """
        webelem = self.driver.find_element_by_xpath(V4_WORKSPACES)
        HomePage.Home._utils.verify_element_visiblty(element=webelem, visible=True, msg="Step 15.01 : Veify Resource Folder appear")
        webelem = self.driver.find_element_by_xpath(V4_REPORT_OUTPUT)
        HomePage.Home._utils.verify_element_visiblty(element=webelem, visible=True, msg="Step 15.01 : Veify Report Output appear")
        HomePage.Home._utils.capture_screenshot('15.01',STEP_15_01, True)
        
        STEP_16 = """
            STEP 16 : Save and close the portal.
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object("#saveButton", "Save_Button")
        webelem.click()
        HomePage.Home._utils.synchronize_with_number_of_element("#dlgPortalSaveDialog",1,20)
        webelem = self.driver.find_element_by_xpath(V4_SAVE_DIALOG_OK)
        webelem.click()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('16.00',STEP_16)

        STEP_17 = """
            STEP 17 : Click on My Workspace link
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_my_workspace()

        HomePage.Home._utils.capture_screenshot('17.00',STEP_17)
        
        STEP_17_01 = """
            STEP 17.01 : Verify the portal appears there. It should be the first one listed as this is sorted by Modified
        """
        HomePage.MyWorkspace.verify_items(['V4 Portal for MyContent'], "17.01")
        HomePage.Home._utils.capture_screenshot('17.01',STEP_17_01, True)
        
        STEP_18 = """
            STEP 18 : Right click on the Portal
        """
        HomePage.MyWorkspace.right_click_on_item('V4 Portal for MyContent')
        #HomePage.Workspace.ContentArea.right_click_on_folder('V4 Portal for MyContent')
        HomePage.Home._utils.capture_screenshot('18.00',STEP_18)
        
        STEP_18_01 = """
            STEP 18.01 : Verify there is NO share and share with menu
        """
        HomePage.ContextMenu.verify(['Run', 'Edit', 'Delete DEL', 'Add to Favorites', 'Properties'],"18.01")
        HomePage.Home._utils.capture_screenshot('18.01',STEP_18_01, True)

        STEP_19 = """
            STEP 18 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Banner.close_page_message()
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('Administration Console')
        HomePage.Home._core_utils.switch_to_new_window()
        self.driver.refresh()
        
        HomePage.Home._utils.wait_for_page_loads(30)
        try:
            webelem= self.driver.find_element_by_xpath(ADMIN_CONSOLE_BI_PORTAL)
            if webelem.is_displayed()==False:
                elem=self.driver.find_element_by_xpath(ADMIN_CONSOLE_APPLICATION_SETTINGS)
                elem.click()
                HomePage.Home._utils.wait_for_page_loads(20)
            elem=self.driver.find_element_by_xpath(ADMIN_CONSOLE_CLIENT_SETTINGS)
            elem.click()
            HomePage.Home._utils.wait_for_page_loads(20)
            webelem.click()
            HomePage.Home._utils.wait_for_page_loads(20)
        except:
            pass
        self.driver.find_element_by_xpath(ADMIN_CONSOLE_V4PORTAL_CHECKBOX).click()
        save_btn_elem = self.driver.find_element_by_xpath(ADMIN_CONSOLE_SAVE_BUTTON)
        save_btn_elem.click()
        obj=self.driver.switch_to.alert
        obj.accept()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()

        HomePage.Home._utils.capture_screenshot('19.00',STEP_19)