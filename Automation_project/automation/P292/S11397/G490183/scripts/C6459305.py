"""-------------------------------------------------------------------------------------------
Created on June 27, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459305
Test Case Title =  Verify Upload Data functionality
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.pages import wf_mainpage as main_pages
from common.wftools import report
from common.wftools import chart
import time


class C6459305_TestClass(BaseTestCase):

    def test_C6459305(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_run = Run(self.driver)
        mainpage_obj = main_pages.Wf_Mainpage(self.driver)
        report_obj=report.Report(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
            TESTCASE CSS
        """
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        explorer_css = "div[class^='file-item file-item-published']"
        excel_css=".wcx-grid-body>div :nth-child(3)"
        Load_css=".wcx-highlighted.wcx-ribbon-vbox div[title='Load and go to the next step to Report']"
        load_options_css=".ibx-popup .wcx-popup-window-container"
        Date_rec_css='div[data-ibx-type="ibxPopup"] [data-ibx-type="ibxSelectItemList"] div[qa="DATREC - fast binary"]'
        ibisamp_css='.wcx-fp-tree div[wcnode="ibisamp"]'
        preview_item_css="#singleReportLayout #TableChart_1 [class*='ibi-preview-title-n1']"
        preview_item_css2="#singleReportLayout #TableChart_1 [class*='ibi-preview-title-n2']"
        
        def select_load_options_value(self, select_options, text_string_to_enter=None, change_opt=None):
            grid_elem=self.driver.find_elements_by_css_selector(".pop-top [class*='wcx-form-item']")
            k=[(i,obj_ ) for i,obj_ in enumerate(grid_elem,0) if obj_.is_displayed() and obj_.text!='' and obj_.text.strip() == select_options][0]
            if change_opt != None:
                options_to_click=grid_elem[k[0]+1].find_element_by_css_selector('.fa-ellipsis-h')
                core_utils.python_left_click(options_to_click)
            else:
                options_to_click=grid_elem[k[0]+1].find_element_by_css_selector('input')
                core_utils.python_left_click(options_to_click)
            if text_string_to_enter != None:
                utils.set_text_to_textbox_using_keybord(text_string=text_string_to_enter,text_box_elem=options_to_click)
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G490183' folder;
            Double click on 'Explorer Widget page'
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        pd_design.run_page_designer_by_double_click("Explorer Widget page")
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        
        """
        Step 4:Click on Upload Data action tile
        Verify the Web Console window opens in a new tab
        """
        main_page.select_action_bar_tab('Data')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Metadata', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Upload Data')
        
        
        """
        Step 5:Right click on Excel and select Upload Data;
        Choose "uploadtree_xls. xls" file from \ibirisc2\bipgqashare\Images_and_Things
        Verify upload completed
        """
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(excel_css,'Excel',main_page.home_page_medium_timesleep)
        excel_elem=utils.validate_and_get_webdriver_object(excel_css, 'excel_elem')
        core_utils.python_right_click(excel_elem)
        time.sleep(2)
        mainpage_obj.select_context_menu_item('Upload Data')
        time.sleep(2)
        main_page.upload_file_using_action_bar(['UploadTree'])

        """
        Step 6:Click 'Load and Report' button on the Ribbon.
        Verify Target Load Options dialog appears as below
        """
        utils.synchronize_with_visble_text(Load_css,'goto_next_right',main_page.home_page_long_timesleep)
        Load_button_elem=utils.validate_and_get_webdriver_object(Load_css,'Load_button_Css')
        core_utils.python_left_click(Load_button_elem)

        """
        Step 7:Click Adapter dropdown-> Choose DATREC- fast binary;
        Click on 'Proceed to Load' button
        Verify 'uploadtree_xls.mas' has been created under 'G490183' folder in content area as below
        """
        utils.synchronize_until_element_is_visible(load_options_css,main_page.home_page_long_timesleep)
        select_load_options_value(self,'Adapter')
        utils.synchronize_with_visble_text(Date_rec_css,'DATREC - fast binary',main_page.home_page_long_timesleep)
        Date_rec_elem=utils.validate_and_get_webdriver_object(Date_rec_css,'apdater_options_pop_up_css')
        core_utils.python_left_click(Date_rec_elem)
        time.sleep(9)
        select_load_options_value(self,'Synonym Application',change_opt='True')
        utils.synchronize_with_visble_text(ibisamp_css, 'ibisamp', main_page.home_page_long_timesleep)
        ibisamp_elem=utils.validate_and_get_webdriver_object(ibisamp_css,'ibisamp_file_css')
        core_utils.python_left_click(ibisamp_elem)
        time.sleep(9)
        main_page.click_button_on_popup_dialog("OK")
        time.sleep(9)
        main_page.click_button_on_popup_dialog("Proceed to Load")
        time.sleep(5)
        Load_button_elem=utils.validate_and_get_webdriver_object(Load_css,'Load_button_Css')
        core_utils.python_left_click(Load_button_elem)
        time.sleep(2)
        core_utils.switch_to_previous_window(window_close=False)

        """
        Step 8:Click on Report action tile from under InfoAssist category;
        Choose 'uploadtree_xls.mas' from under 'myhome' app directory
        """
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.select_action_bar_tab('InfoAssist')
        utils.synchronize_with_visble_text(locator_obj.content_area_css, 'Report', main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option('Report')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text("#dlgIbfsOpenFile7 #paneIbfsExplorer_exTree table>tbody :nth-child(7)",'ibisamp',main_page.home_page_medium_timesleep)
        utils.select_masterfile_in_open_dialog("ibisamp","uploadtree_xls_")
        utils.synchronize_until_element_is_visible(".bi-tree-view-body-content>table>tbody>tr", main_page.home_page_medium_timesleep)

        """
        step 9:Double click add Name and DomID fields
        Verify report in live preview
        """
        report_obj.double_click_on_datetree_item("Name",1)
        utils.synchronize_with_visble_text(preview_item_css, "Name", main_page.home_page_medium_timesleep)
        report_obj.double_click_on_datetree_item("DomID",1)
        utils.synchronize_with_visble_text(preview_item_css2, "DomID", main_page.home_page_medium_timesleep)
        report_obj.create_report_data_set_in_preview("TableChart_1" ,20, 2,"C6459305.xlsx")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 20, 2, "C6459305.xlsx","Step 9.1")

        """
        Step 10:Click Run
        Verify report runs without any error as below
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.create_table_data_set(None,"C6459305_run.xlsx")
        report_obj.verify_table_data_set(None,"C6459305_run.xlsx","Step 10.1")

        """
        Step 11:Click save;
        Enter title as 'Report' and Click Save
        """
        report_obj.switch_to_default_content()
        report_obj.select_ia_toolbar_item("toolbar_save")
        chart_obj.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        report_obj.save_file_in_save_dialog("Report")

 
        """
        Step 12:Close IA
        Verify 'Report' is available under 'G490183' folder in content area as below
        """
        chart_obj.select_ia_exit_from_application_btn()
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page.verify_items_in_grid_view(["Report"],"asin","Step 12.1 Verify 'Report' is available under 'G490183' folder in content area as below")

        """
        Step 13:Double click on 'Report' from content area
        Verify report runs from explorer widget page without any error as below
        """
        pd_design.run_page_designer_by_double_click("Report")

        """
        Step 14:Close report
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()

 
        """
        Step 15:Right click on 'Report' and select Edit
        Verify report opens in a new tab with the live preview canvas as below
        """
        main_page.right_click_folder_item_and_select_menu("Report","Edit")
        core_utils.switch_to_new_window()
        utils.synchronize_until_element_is_visible(".bi-tree-view-body-content>table>tbody>tr", main_page.home_page_medium_timesleep)
        report_obj.create_report_data_set_in_preview("TableChart_1" ,20, 2,"C6459305.xlsx")
        report_obj.verify_report_data_set_in_preview("TableChart_1", 20, 2, "C6459305.xlsx","Step 9.1")


        """
        Step 16:Click IA application main menu and click on Exit
        """
        
        chart_obj.select_ia_exit_from_application_btn()
 
        """
        Step 17:Close the 'Explorer widget' page run window.
        Verify 'Report' and 'uploadtree_xls.mas' are displayed under 'P292_S11397' domain -> 'G490183' folder in Home page
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(["Report"],"asin","Step 12.1 Verify 'Report' is available under 'G490183' folder in content area as below")
        main_page.verify_items_in_grid_view(["uploadtree_xls_"],"asin","Step 12.2 Verify 'Report' is available under 'G490183' folder in content area as below")
        
        """
        Step 18:Sign Out WF
        """
        main_page.signout_from_username_dropdown_menu()
 

 

 
if __name__ == '__main__':
    unittest.main() 