'''
Created on May 30, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262108
TestCase Name = check published state
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage, report
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262108_TestClass(BaseTestCase):

    def test_C8262108(self):
        
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
        
        """
        TESTCASE VARIABLES
        """
        report_fex = 'Published Report1'
        domain = 'Thumbnail Testing'
        workspaces ="Workspaces"
        repository_folder = workspaces+'->Thumbnail Testing'
        action_tile = 'Designer'
        action_bar = 'Page'
        blank_template = 'Blank'
        ia_action_tile = 'InfoAssist'
        report_action_bar = 'Report'
        small_widgets_fex_list = ['Category Sales', 'Regional Sales Trend', 'Discount by Region', 'Regional Profit by Category', 'Average Cost v Sales', 'Average Cost vs Revenue Scatter', 'Product Profit Line By Month', 'Revenue Product Bar', 'Revenue Region Bar']
        responsive_tables_fex_list = ['Accordion DataTable', 'Enhanced Accordion', 'Enhanced Accordion with Inline Styling', 'Freeze DataTable', 'Standard Autofit Off', 'Standard Autofit On']
           
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
        Step 03.00: Click on 'Thumbnail Testing' domain 
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 05.00: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, blank_template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(blank_template)
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 06.00: Click on Domains node to go up a level
        """
        page_designer_obj.collapse_content_folder(domain)
        
        """
        Step 06.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below
        """
        page_preview_obj.verify_page_domain_tree_node([workspaces, 'Public', 'Thumbnail Testing', 'Retail Samples'], "Step 06.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below")
        
        """
        Step 07.00: Click the arrow next to 'Thumbnail Testing' domain
        """
        page_designer_obj.expand_content_folder(domain)
        
        """
        Step 07.01: Verify thumbnail for 'My Content' folder appears as below
        """
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing', 'My Content'], "Step 07.01: Verify thumbnail for 'My Content' folder appears as below")
        
        """
        Step 08.00: Expand Retail samples --> Portal --> Small widgets folder
        """
        page_designer_obj.collapse_content_folder(domain)
        page_designer_obj.expand_content_folder("Retail Samples->Portal->Small Widgets")
        util_obj.wait_for_page_loads(time_out=15, pause_time=5)
        
        """
        Step 08.01: Verify all fexes have thumbnails as below
        """
        page_preview_obj.verify_page_domain_tree_node(small_widgets_fex_list, "Step 08.01: Verify all fexes have thumbnails as below")
        
        """
        Step 09.00: Expand Retail samples --> Portal --> Responsive Tables folder
        """
        page_designer_obj.collapse_content_folder("Small Widgets->Portal->Retail Samples")
        page_designer_obj.expand_content_folder("Retail Samples->Portal->Responsive Tables")
        util_obj.wait_for_page_loads(time_out=15, pause_time=5)
        
        """
        Step 09.01: Verify all fexes have thumbnails as below
        """
        page_preview_obj.verify_page_domain_tree_node(responsive_tables_fex_list, "Step 09.01: Verify all fexes have thumbnails as below")
        
        """
        Step 10.00: Minimize page designer and bring up HOME page
        """
        util_obj.switch_to_window(0)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)
        
        """
        Step 11.00: Click on 'Thumbnail Testing' domain -> Choose 'Report' action tile from under Infoassist category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ia_action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(ia_action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(report_action_bar)
        util_obj.wait_for_page_loads(20, pause_time=8)
        
        """
        Step 12.00: Choose car.mas;
        Add COUNTRY and CAR fields;
        Save report as 'Published Report1' and close IA
        """
        self.driver.switch_to_window(self.driver.window_handles[2])
        util_obj.synchronize_with_number_of_element(dialog_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(20, pause_time=5)
        
        report_obj.select_masterfile_in_open_dialog('ibisamp', 'car')
        util_obj.wait_for_page_loads(time_out=20, pause_time=5)
        util_obj.synchronize_with_visble_text(preview_css,'Drag and drop fields onto the', main_page_obj.home_page_medium_timesleep)
#         util_obj.synchronize_with_number_of_element(preview_css,1, main_page_obj.home_page_medium_timesleep)
        
        report_obj.double_click_on_datetree_item("COUNTRY")
        util_obj.synchronize_with_visble_text("#TableChart_1", 'COUNTRY', 40)
        
        report_obj.double_click_on_datetree_item("CAR")
        util_obj.synchronize_with_visble_text("#TableChart_1", 'CAR', 40)
        
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog(report_fex)
        report_obj.select_visualization_application_menu_item('close')
        self.driver.close()
        
        """
        Step 13.00: Right click on that 'Published Report1' and Select Publish
        """
        util_obj.switch_to_window(0)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(report_fex, context_menu_item_path='Publish')
        util_obj.wait_for_page_loads(time_out=15, pause_time=5)
        
        """
        Step 13.01: Verify thumbnail for 'Published Report1'
        """
        main_page_obj.verify_content_area_item_publish_or_unpublish(report_fex, item_status='publish', msg="Step 13.01: Verify thumbnail for 'Published Report1'")
        
        """
        Step 14.00: Minimize HOME page and get back to page designer
        """
        util_obj.switch_to_window(1)
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.collapse_content_folder("Responsive Tables->Portal->Retail Samples")
        page_designer_obj.expand_content_folder(domain)
        
        """
        Step 14.01: Verify that the report is published and not greyed;
                    Verify thumbnail for 'Published Report1'
        """
        page_designer_obj.verify_published_content_items([report_fex], 'Step 14.01:')
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing', 'My Content', report_fex], "Step 14.02: Verify thumbnail for 'Published Report1'")
        
        """
        Step 15.00: Close designer without saving the page
        """ 
        page_designer_obj.close_page_designer_without_save_page()
        
        """
        Step 16.00: Signout WF
        """ 
        util_obj.switch_to_window(0)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ia_action_tile, main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()