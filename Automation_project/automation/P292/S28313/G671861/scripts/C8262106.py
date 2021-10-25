'''
Created on May 29, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262106
TestCase Name = check thumbnail for fex
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262106_TestClass(BaseTestCase):

    def test_C8262106(self):
        
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
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        Case_ID = 'C8262106'
        repository_folder = 'Domains->Thumbnail Testing'
        action_tile = 'Designer'
        action_bar = 'Page'
        small_widgets_fex_list = ['Category Sales', 'Regional Sales Trend', 'Discount by Region', 'Regional Profit by Category', 'Average Cost v Sales', 'Average Cost vs Revenue Scatter', 'Product Profit Line By Month', 'Revenue Product Bar', 'Revenue Region Bar']
        responsive_tables_fex_list = ['Accordion DataTable', 'Enhanced Accordion', 'Enhanced Accordion with Inline Styling', 'Freeze DataTable', 'Standard Autofit Off', 'Standard Autofit On']
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 03.00: Click on 'Thumbnail Testing' domain and Click on Page action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 04.00: Choose Grid 2-1 template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.00: Expand Retail samples --> portal --> small widgets folder from the tree
        """
        page_designer_obj.collapse_content_folder("Thumbnail Testing")
        page_designer_obj.expand_content_folder("Retail Samples->Portal->Small Widgets")
        util_obj.synchronize_with_visble_text(".pd-content-tab-page", small_widgets_fex_list[0], main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.01: Verify thumbnails for all fexes appears as below
        """
        page_preview_obj.verify_page_domain_tree_node(small_widgets_fex_list, "Step 05.01: Verify thumbnails for all fexes appears as below")
        
        """
        Step 06.00: Minimize page designer and invoke HOME page
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 07.00: Expand Retail samples --> portal --> small widgets folder from the tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder("Retail Samples->Portal->Small Widgets")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, small_widgets_fex_list[0], main_page_obj.home_page_medium_timesleep)
        
        """
        Step 07.01: Verify thumbnails for all fexes appears as below in content area
        """
        main_page_obj.verify_items_in_grid_view(small_widgets_fex_list, comparision_type='asListEqual', msg="Step 07.01: Verify thumbnails for all fexes appears as below in content area")
        
        """
        Step 08.00: Minimize HOME page and get back to page designer
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 09.00: Expand Retail samples --> portal --> Responsive Tables folder
        """
        page_designer_obj.collapse_content_folder("Small Widgets->Portal->Retail Samples")
        page_designer_obj.expand_content_folder("Retail Samples->Portal->Responsive Tables")
        util_obj.synchronize_with_visble_text(".pd-content-tab-page", responsive_tables_fex_list[0], main_page_obj.home_page_medium_timesleep)
        
        """
        Step 09.01: Verify thumbnails for all fexes appears as below
        """
        page_preview_obj.verify_page_domain_tree_node(responsive_tables_fex_list, "Step 09.01: Verify thumbnails for all fexes appears as below")
        
        """
        Step 10.00: Minimize page designer and invoke HOME page
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 11.00: Expand Retail samples --> portal --> Responsive Tables folder
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder("Retail Samples->Portal->Responsive Tables")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, responsive_tables_fex_list[0], main_page_obj.home_page_medium_timesleep)
        
        """
        Step 11.01: Verify thumbnails for all fexes appears as below in content area
        """
        main_page_obj.verify_items_in_grid_view(responsive_tables_fex_list, comparision_type='asListEqual', msg="Step 11.01: Verify thumbnails for all fexes appears as below in content area")
        
        """
        Step 12.00: Minimize HOME page and get back to page designer
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 13.00: Save page as 'C8262106' and close designer
        """ 
        page_designer_obj.save_page_from_toolbar(Case_ID)
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 14.00: Signout WF
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()