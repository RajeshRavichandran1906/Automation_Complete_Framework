"""-------------------------------------------------------------------------------------------
Author Name  : PY15029
Automated On : 24-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as _Designer

class C9928023_TestClass(BaseTestCase):
    
    def test_C9928023(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = _Designer()
        
        """
        TEST CASE VAIABLES
        """
        page_name = 'DF_Custom_Page_1'
        Custom_Folder = 'Custom_Folder'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mridadm", "mrpassadm")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Workspaces' tab > Click on 'Workspaces' from the navigation bar.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Collapse the 'Workspaces' from the tree if expanded.
        """
        HomePage.Workspaces.ResourcesTree.collapse_workspaces()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Expand Global Resources node > 'Page Templates' folder > Click on 'Custom' sub-folder.
        """
        HomePage.Workspaces.ResourcesTree.select("Global Resources->Page Templates->Custom")
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify that it displays 'Folder' action bars.
        """
        HomePage.Workspaces.ActionBar.verify_tab_options(['Folder'], '04.01')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists(Custom_Folder)
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click on Folder action bar.
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Folder")
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that it displays 'New Folder' dialog box with Title text box, Name text box, OK button by default disabled and Cancel button.
        """
        HomePage.ModalDailogs.Folder.wait_for_appear()
        HomePage.ModalDailogs.Folder.verify_title('New Folder', '05.01')
        HomePage.ModalDailogs.Folder.Title.verify_text('', '05.02')
        HomePage.ModalDailogs.Folder.Name.verify_text('', '05.03')
        HomePage.ModalDailogs.Folder.CancelButton.verify_enabled('05.04')
        HomePage.ModalDailogs.Folder.OKButton.verify_disabled('05.05')
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Enter Title 'Custom_Folder' > Click OK.
        """
        HomePage.ModalDailogs.Folder.Title.enter_text(Custom_Folder, False)
        HomePage.ModalDailogs.Folder.OKButton.click()
        HomePage.ModalDailogs.Folder.wait_for_diappear()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify folder is created.
        """
        HomePage.Workspaces.ContentArea.verify_folders([Custom_Folder], '06.01')
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Double click on 'Custom_Folder' from the content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder(Custom_Folder)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click the '+' menu button on the top toolbar and Select 'Assemble Visualizations'> Choose the 'Blank' template
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.wait_for_text('Blank', 80)
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on Application menu > Click 'Save' under
        """
        self.driver.find_element(*Designer.ToolBar._locators.application_menu).click()
        HomePage.ContextMenu.select("Save")
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the breadcrumb trail as 'Global Resources > PGXPageTemplates > Custom > Custom_Folder'
        """
        HomePage.ModalDailogs.Resources.wait_for_appear()
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.verify('Global Resources>PGXPageTemplates>Custom>Custom_Folder', '09.01')
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Enter 'DF_Custom_Page_1' in title and Click on Save.
        """
        HomePage.ModalDailogs.Resources.Title.enter_text(page_name)
        HomePage.ModalDailogs.Resources.SaveButton.click()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify 'DF_Custom_Page_1' is created.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files([page_name], '10.01')
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Right-click on 'DF_Custom_Page_1' from the content area > Select 'Delete' > Click 'OK'
        """
        HomePage.Workspaces.ContentArea.delete_file(page_name)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 'DF_Custom_Page_1' gets deleted.
        """
        HomePage.Workspaces.ContentArea.verify_files([page_name], '10.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Revert back the 'Workspaces' view default by clicking on 'Workspaces' from the navigation tree
        """
        HomePage.Workspaces.ResourcesTree.collapse('Global Resources')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : In the banner link, click on the 'Username' > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)