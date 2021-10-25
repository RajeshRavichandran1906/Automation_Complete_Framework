"""-------------------------------------------------------------------------------------------
Created on July 03, 2019
@author: vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6459316
Test Case Title =  Create,Run and Restore Alert Assist
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.wftools import report
from common.wftools import chart
import time


class C6459316_TestClass(BaseTestCase):

    def test_C6459316(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        pd_design = Design(self.driver)
        main_page_run = Run(self.driver)
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
        
        expected_title='Alert - WebFOCUS Alert Assist'
        querypane_css = "#queryBoxColumn"
        expected_alert_text='Alert'
        
        def click_on_alert_tree_test_component(item_to_click):
            alert_content_view=utils.validate_and_get_webdriver_objects(".bi-tree-view-body-content table>tbody>tr>td span","content_tree_css")
            for x in alert_content_view:
                if x.text==item_to_click:
                    core_utils.python_right_click(x)
        
        def click_on_multiple_bipopup():
            utils.select_or_verify_bipop_menu("New")
            utils.select_or_verify_bipop_menu("WebFOCUS Test")
            
        def multiple_bipopup_for_report():
            utils.select_or_verify_bipop_menu("New")
            utils.select_or_verify_bipop_menu("New Report")
            utils.select_or_verify_bipop_menu("Report")
            
        def preview_heading(parent_css,expected_list,msg):
            actual_heading_elem=utils.validate_and_get_webdriver_objects(parent_css,"Alert_report_heading")
            actual_heading_text=[x.text.strip() for x in actual_heading_elem]
            utils.asequal(actual_heading_text,expected_list,msg)
            
        
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
        Step 4:Click on Alert action tile from under InfoAssist category
        Verify Alert Assists opens in a new tab
        """
        main_page.select_action_bar_tab("InfoAssist")
        utils.synchronize_with_visble_text(".ia-group-tab", "Alert",main_page.chart_long_timesleep)
        main_page.select_action_bar_tabs_option("Alert")
        core_utils.switch_to_new_window()
        time.sleep(2)
        Actual_title=self.driver.title
        utils.asequal(Actual_title,expected_title,"Step 04.01: Verify Alert Assists opens in a new tab")
        
        """
        Step 5:Right-click Test component > New > WebFOCUS Test;
        Choose Car.mas under ibisamp folder > Click open.
        """
        click_on_alert_tree_test_component('Test')
        click_on_multiple_bipopup()
        core_utils.switch_to_new_window()
        utils.select_masterfile_in_open_dialog('ibisamp', 'car')

        """
        Step 6:Double click COUNTRY, CAR and SALES fields
        Verify Live Preview appears as below
        """
        chart_obj.double_click_on_datetree_item('COUNTRY',1)
        chart_obj.wait_for_visible_text(querypane_css,'COUNTRY')
        chart_obj.double_click_on_datetree_item('CAR', 1)
        chart_obj.wait_for_visible_text(querypane_css,'CAR')
        chart_obj.double_click_on_datetree_item('SALES', 1)
        chart_obj.wait_for_visible_text(querypane_css,'SALES')
        preview_heading("#TableChart_1 div .foc-meta-title",['COUNTRY', 'CAR', 'SALES'],"Step 06.01: verify chart preview heaing")
        

        """
        Step 7:Click IA > Exit > Click Yes to save
        """
        chart_obj.select_visualization_application_menu_item('exit')
        self.driver.find_element_by_css_selector("#saveAllDlg #btnYes").click()

        """
        Step 8:Right-click Result component > New > New Report > Report ;
        Choose Car.mas under ibisamp folder > Click open
        """
        core_utils.switch_to_previous_window(window_close=False)
        click_on_alert_tree_test_component('Result')
        multiple_bipopup_for_report()
        core_utils.switch_to_new_window()
        utils.select_masterfile_in_open_dialog('ibisamp', 'car')
        
        """
        step 9:Double-click MODEL and SEATS fields
        Verify Live preview appears as below
        """
        chart_obj.double_click_on_datetree_item('MODEL',1)
        chart_obj.wait_for_visible_text(querypane_css,'MODEL')
        chart_obj.double_click_on_datetree_item('SEATS', 1)
        chart_obj.wait_for_visible_text(querypane_css,'SEATS')
        preview_heading("#TableChart_1 div .foc-meta-title",['MODEL', 'SEATS'],"Step 09.01: verify chart preview heaing")
        

        """
        Step 10:Click IA > Exit > Click Yes to save
        """
        chart_obj.select_visualization_application_menu_item('exit')
        self.driver.find_element_by_css_selector("#saveAllDlg #btnYes").click()
        
        """
        Step 11:Click AA menu > Save;
        Enter title as 'Alert' > Click Save.
        Verify that the 'Alert' is created and listed under G490183 folder
        """
        time.sleep(5)
        core_utils.switch_to_previous_window(window_close=False)
        chart_obj.select_visualization_application_menu_item('exit')
        self.driver.find_element_by_css_selector(".button-focus").click()
        utils.ibfs_save("Alert")
        
        """
        Step 12:Double click on 'Alert'
        Verify the following report is displayed as below
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        pd_design.run_page_designer_by_double_click("Alert")
        time.sleep(2)
        main_page_run.switch_to_frame()
        report_obj.verify_table_data_set('table[Summary="Summary"]', 'C6459316.xlsx',"Step 12.00: Verify the following report is displayed as below")
        
        """
        Step 13:Close the 'Alert' run window.
        """
        main_page_run.switch_to_default_content()
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        main_page_run.close()
        
        """
        Step 14:Right click on 'Alert' > Edit
        """
        utils.synchronize_with_visble_text(explorer_css, "Explorer", 30)
        main_page.right_click_folder_item_and_select_menu("Alert", 'Edit')
        core_utils.switch_to_new_window()
        alert_elem=utils.validate_and_get_webdriver_object(".bi-tree-view table>tbody>tr>td","Alert_text").text.strip()
        utils.asequal(alert_elem,expected_alert_text,"Step 14.2 verify the alert page")
        
        """
        Step 15:Click AA > Exit.
        """
        chart_obj.select_visualization_application_menu_item('exit')
        core_utils.switch_to_previous_window(window_close=False)
        
 
        """
        Step 16:Close the 'Explorer widget' page run window
        Verify Home page is displayed and 'Alert' is listed under G490183 folder
        """
        main_page_run.switch_to_frame()
        pd_design.switch_to_container_frame("Panel 1")
        pd_design.switch_to_default_page()
        main_page_run.close()
        main_page_run.switch_to_default_content()
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        self.driver.refresh()
        utils.synchronize_with_visble_text(explorer_css, "Explorer",main_page.home_page_medium_timesleep)
        main_page.verify_items_in_grid_view(["Alert"],"asin","Step 16.01: Verify 'Alert' is available under 'G490183' folder in content area as below")

        
        """
        Step 17:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
 

 

 
if __name__ == '__main__':
    unittest.main() 