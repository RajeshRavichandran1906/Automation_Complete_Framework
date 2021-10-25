"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 11 May 2020
-----------------------------------------------------------------------------------------------"""
import time
from common.wftools.report import Report
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.global_variables import Global_variables

class C9945171_TestClass(BaseTestCase):
    
    def test_C9945171(self):
        
        """
            TEST CASE OBJECTS
        """
        report = Report(self.driver)
        HomePage = ParisHomePage(self.driver)
        global_var_obj = Global_variables()
    
        """
            TEST CASE VARIABLES
        """
        case_id = global_var_obj.current_test_case
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        LIVE_PREVIEW_COL_TITLE = ['COUNTRY']
        REPORT_SHORTCUT_TITLE='Report_Context - Shortcut'
        report_css="#TableChart_1 div[class^='x']"
        
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
        HomePage.Workspaces.ContentArea.delete_file_if_exists(REPORT_SHORTCUT_TITLE)
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
            STEP 06 : Click on > (carot symbol) next to 'P406_S31920' > Click on 'G784912' folder > Double click on 'IA/Visualization' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.click_arrow('P406_S31920')
        time.sleep(5)
        HomePage.ContextMenu.select('G784912')
        time.sleep(5)
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('IA/Visualization')
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on 'Report_Context'
        """
        HomePage.ModalDailogs.Resources.GridView.Files.click('Report_Context')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify the 'Title' = 'Chart_Context' and 'Name' = 'Chart_Context.fex'
        """
        HomePage.ModalDailogs.Resources.Title.verify_text('Report_Context','07.01')
        HomePage.ModalDailogs.Resources.Name.verify_text('Report_Context.fex', '07.02')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01)
        
        STEP_08 = """
            STEP 08 : Click on the 'Select' button
        """
        HomePage.ModalDailogs.Resources.SelectButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify the following:
            Target path = 'IBFS:/WFC/Repository/P406_S31920/G784912/IA_Visualization/Report_Context.fex'
            Title = Report_Context - Shortcut
            Summary should be empty
            Both 'Cancel' and 'OK' buttons get enabled
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_text('IBFS:/WFC/Repository/P406_S31920/G784912/IA_Visualization/Report_Context.fex','08.01')
        HomePage.ModalDailogs.Shortcut.Title.verify_text(REPORT_SHORTCUT_TITLE,'08.02')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text('','08.03')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled('08.04')
        HomePage.ModalDailogs.Shortcut.OKButton.verify_enabled('08.05')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, expected_image_verify=True)
        
        STEP_09 = """
            STEP 09 : Click OK button
        """
        HomePage.ModalDailogs.Shortcut.OKButton.click()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that shortcut for an item (Report_Context - Shortcut) is being created properly
            and showing in the content area and the correct shortcut icon is showing as expected
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files([REPORT_SHORTCUT_TITLE],'09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01)
        
        STEP_10 = """
            STEP 10 : Right-click on 'Report_Context - Shortcut' item > Click on 'Run'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(REPORT_SHORTCUT_TITLE)
        time.sleep(10)
        HomePage.ContextMenu.select('Run')
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify that 'Report_Context - Shortcut' run without any error
        """
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.RunWindow.verify_title(REPORT_SHORTCUT_TITLE, '10.01')
        HomePage.RunWindow.switch_to_frame()
        HomePage.Home._utils.wait_for_page_loads(30)
        #report.create_html_report_dataset(DATA_SET_NAME1, table_css="table[summary='Summary']")
        report.verify_html_report_dataset(DATA_SET_NAME1, "STEP 10.01 : Verify that 'Report_Context - Shortcut' run without any error", table_css="table[summary='Summary']")
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01,expected_image_verify=True)
        
        STEP_11 = """
            STEP 11 : Close the run window
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_12 = """
            STEP 12 : Edit 'Report_Context - Shortcut'
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(REPORT_SHORTCUT_TITLE)
        time.sleep(10)
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Verify it restored successfully without any error
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.synchronize_with_number_of_element(report_css, 55, 150)
        
        msg = "Step 12.01 : Verify 'IA' window is displayed"
        report.verify_report_column_titles_on_preview(1, 1, LIVE_PREVIEW_COL_TITLE, msg=msg)
        HomePage.Home._utils.capture_screenshot('12.01', STEP_12_01,expected_image_verify=True)
        
        STEP_13 = """
            STEP 13 : Close IA tool
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        
        STEP_14 = """
            STEP 14 : Right-click on 'Report_Context - Shortcut' item > Click on 'Delete'
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.delete_file(REPORT_SHORTCUT_TITLE)
        HomePage.Home._utils.capture_screenshot('14.00', STEP_14)
        
        STEP_14_01 = """
            STEP 14.01 : Verify that 'Report_Context - Shortcut' item get deleted
        """
        HomePage.Workspaces.ContentArea.verify_shortcut_files(REPORT_SHORTCUT_TITLE, '14.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot('14.01', STEP_14_01 ,expected_image_verify=True)
        
        STEP_15 = """ 
            STEP 15 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('15.00', STEP_15)