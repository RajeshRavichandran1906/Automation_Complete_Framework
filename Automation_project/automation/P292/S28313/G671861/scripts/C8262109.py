'''
Created on May 31, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262109
TestCase Name = check unpublished state
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage, report
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262109_TestClass(BaseTestCase):

    def test_C8262109(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        report_obj = report.Report(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        dialog_css = "[id*='dlgIbfsOpenFile'] [class*='active'][class*='window']"
        preview_css = "#TableChart_1"
        workspaces ="Workspaces"
        
        """
        TESTCASE VARIABLES
        """
        report_fex = 'Un publish Report1'
        domain = 'Thumbnail Testing'
        repository_folder = 'Domains->Thumbnail Testing'
        action_tile = 'Designer'
        action_bar = 'Page'
        blank_template = 'Blank'
        ia_action_tile = 'InfoAssist'
        report_action_bar = 'Report'
        small_widgets_fex_list = ['Category Sales', 'Regional Sales Trend', 'Discount by Region', 'Regional Profit by Category', 'Average Cost v Sales', 'Average Cost vs Revenue Scatter', 'Product Profit Line By Month', 'Revenue Product Bar', 'Revenue Region Bar']
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Click on 'Thumbnail Testing' domain and Click on Page action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 04.00: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, blank_template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(blank_template)
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.00: Click on Domains node to go up a level
        """
        page_designer_obj.collapse_content_folder(domain)
        
        """
        Step 05.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below
        """
        page_preview_obj.verify_page_domain_tree_node([workspaces, 'Public', 'Thumbnail Testing', 'Retail Samples'], "Step 05.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below")
        
        """
        Step 06.00: Minimize page designer and bring up HOME page
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)
        
        """
        Step 07.00: Expand Retail samples --> Portal --> Small widgets folder
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder("Retail Samples->Portal->Small Widgets")
        sleep(5)
        
        """
        Step 08.00: Right click on 'Category Sales' and choose Unpublish
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Category Sales', context_menu_item_path='Duplicate')
        util_obj.wait_for_page_loads(30, pause_time=5)
        
        """
        Step 08.01: Verify thumbnail for unpublished 'Category Sales' widget appears as below
        """
        main_page_obj.verify_content_area_item_publish_or_unpublish('Category Sales_1', item_status='unpublish', msg="Step 08.01: Verify thumbnail for unpublished 'Category Sales' widget appears as below")
        
        """
        Step 09.00: Click on 'Thumbnail Testing' domain -> Choose 'Report' action tile from under Info assist category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ia_action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(ia_action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(report_action_bar)
        sleep(8)
      
        """
        Step 10.00: Choose car.mas;
        Add COUNTRY and CAR fields;
        Save report as 'Un publish Report1' and close IA
        """
        core_util_obj.switch_to_new_window()
        if self.driver.title == 'Page':
            core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(dialog_css,1, main_page_obj.home_page_medium_timesleep)
        report_obj.select_masterfile_in_open_dialog('ibisamp', 'car')
        util_obj.wait_for_page_loads(time_out=20, pause_time=5)
        util_obj.synchronize_with_visble_text(preview_css,'Drag and drop fields onto the', main_page_obj.home_page_medium_timesleep)
        report_obj.double_click_on_datetree_item("COUNTRY")
        util_obj.synchronize_with_visble_text("#TableChart_1", 'COUNTRY', 40)
        report_obj.double_click_on_datetree_item("CAR")
        util_obj.synchronize_with_visble_text("#TableChart_1", 'CAR', 40)
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog(report_fex)
        report_obj.select_visualization_application_menu_item('close')
        
        """
        Step 10.01: Verify thumbnail for unpublished report appears as below
        """
        core_util_obj.switch_to_previous_window(window_close=True)
        sleep(2)
        if self.driver.title == 'Page':
            core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish(report_fex, item_status='unpublish', msg="Step 10.01: Verify thumbnail for unpublished report appears as below")
        sleep(5)
        
        """
        Step 11.00: Minimize HOME page and get back to page designer
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 12.00: Expand Retail samples --> Portal --> Small widgets folder
        """
        page_designer_obj.expand_content_folder("Retail Samples->Portal->Small Widgets")
        
        """
        Step 12.01: Verify thumbnail for unpublished 'Category Sales' widget appears as below
        """
        page_designer_obj.verify_unpublished_content_items(['Category Sales_1'], '12.01:')
        page_preview_obj.verify_page_domain_tree_node(small_widgets_fex_list, "Step 12.02: Verify thumbnail for unpublished 'Category Sales' widget appears as below")
        
        """
        Step 13.00: Close designer without saving the page
        """ 
        page_designer_obj.close_page_designer_without_save_page()
        
        """
        Step 14: Right click on 'Category Sales' and choose Publish.
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder("Retail Samples->Portal->Small Widgets")
        main_page_obj.right_click_folder_item_and_select_menu('Category Sales_1', context_menu_item_path='Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.wait_for_page_loads(10)
        
        """
        Step 15.00: Signout WF
        """ 
        
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()