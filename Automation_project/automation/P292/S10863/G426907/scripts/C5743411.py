'''
Created on July 16, 2019.

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743411
TestCase Name = Check Style menu
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C5743411_TestClass(BaseTestCase):

    def test_C5743411(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        quick_filter_css = "[title='Quick filter']"
        page_selected_css = ".pd-page-tab.tpg-selected>div[class='pd-selection {0}']"
        selected_filter_cell_css = ".pd-regular-filter-wrapper .pd-filter-grid .pd-filter-cell:first-child>div[class='pd-selection {0}']"
        grid_panel_filter_cell_css = ".pd-container .pd-filter-cell:first-child>div[class='pd-selection {0}']"
        selected_filter_control_css = ".pd-regular-filter-wrapper .pd-filter-grid .pd-filter-cell:first-child .pd-filter-panel >div[class='pd-selection {0}']"
        selected_container_css = ".pd-container >div[class='pd-selection {0}']"
        selected_section_css = ".pd-page-acc-section >div[class='pd-selection {0}']"
        grid_box = "div.pd-page-canvas div.pd-page-acc-section div[class='pd-page-section-grid-box']"
        direction = ['north', 'south', 'east', 'west']
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        
        '''
        local method
        '''
        def verify_red_dots(element_css, msg):
            for option in direction:
                acutal = util_obj.validate_and_get_webdriver_object(element_css.format(option), 'red dots').is_displayed()
                if acutal:
                    status_expected = True
                    status_actual = True
                else:
                    status_expected = option
                    status_actual = '{0} not having red dots'.format(option)
                    break
            util_obj.asequal(status_expected, status_actual, msg)
            
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S10863' domain -> 'G426906' folder;
                Click on Page action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 4: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        page_designer_obj.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        page_designer_obj.drag_content_item_to_blank_canvas('Category Sales', 1, content_folder_path='Retail Samples->Portal->Small Widgets')
        util_obj.synchronize_until_element_is_visible(quick_filter_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 6: Click on quick filter icon
        """
        page_designer_obj.click_quick_filter()
        util_obj.synchronize_until_element_disappear(quick_filter_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 7: Click on the Page
                Verify there is a red dotted line surrounding the whole page
        """
        page_designer_obj.select_page_from_bottom_tab('Page 1')
        util_obj.synchronize_until_element_is_visible(page_selected_css.format(direction[0]), main_page_obj.home_page_long_timesleep)
        verify_red_dots(page_selected_css, 'Step 07.00: Verify there is a red dotted line surrounding the whole page.')
        
        """
        Step 8: Click open properties pane
                Verify the style menus appears as below
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab('Style')
        page_designer_obj.verify_setting_tab_properties('Page Style', ['Theme=Designer 2018', 'Margin=off', 'Maximum width=off'], 'Step 08.00: Verify the style menus appears as below.', property_tab_name='style')
        util_obj.verify_picture_using_sikuli('step_08_01.png', 'Step 08.01: Verify the style menus appears as below.')
        
        """
        Step 9: Click on the first Cell of the filter tool bar
                Verify there is a red dotted line surrounding the whole filter cell
        """
        page_designer_obj.select_filter_grid_cell(1)
        verify_red_dots(selected_filter_cell_css, 'Step 09.00: Verify there is a red dotted line surrounding the whole filter cell.')
        
        """
        Step 10: Click on the Cell for the filter tool bar and click open properties panel
                Verify the style menus appears as below
        """
        page_designer_obj.select_filter_grid_cell(4)
        util_obj.verify_picture_using_sikuli('step_10_00.png', 'Step 10.00: Verify the style menus appears as below.')
        
        """
        Step 11: Drag and drop grid container next to first panel;
                Click on the first cell in grid panel and click open properties pane
                Verify the style menus appears as below
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        page_designer_obj.drag_container_item_to_blank_canvas('Grid', 4)
        page_designer_obj.select_filter_grid_cell(1, grid_container_title='Panel 2')
        verify_red_dots(grid_panel_filter_cell_css, 'Step 11.00: Verify there is a red dotted line surrounding the whole filter control.')
        util_obj.verify_picture_using_sikuli('step_11_01.png', 'Step 11.01: Verify the style menus appears as below.')
        
        """
        Step 12: Click on the first filter control of the filter tool bar
                Verify there is a red dotted line surrounding the whole filter control
        """
        page_designer_obj.select_filter_grid_cell(1, click_on_location='middle')
        verify_red_dots(selected_filter_control_css, 'Step 12.00: Verify there is a red dotted line surrounding the whole filter control.')
        
        """
        Step 13: Click open properties pane
                Verify the style menus appears as below
        """
        util_obj.verify_picture_using_sikuli('step_13_00.png', 'Step 13.00: Verify the style menus appears as below.')
        
        """
        Step 14: Click on first container
                Verify there is a red dotted line surrounding the whole container
        """
        page_designer_obj.select_container('Category Sales')
        verify_red_dots(selected_container_css, 'Step 12.00: Verify there is a red dotted line surrounding the whole filter control.')
        
        """
        Step 15: Click open properties pane
                Verify the style menus appears as below
        """
        util_obj.verify_picture_using_sikuli('step_15_00.png', 'Step 15.00: Verify the style menus appears as below.')
        
        """
        Step 16: Click on the section
                Verify there is a red dotted line surrounding the whole section
        """
        core_util_obj.python_left_click(util_obj.validate_and_get_webdriver_objects(grid_box, 'section grid box')[6])
        verify_red_dots(selected_section_css, 'Step 16.00: Verify there is a red dotted line surrounding the whole filter control.')
        
        """
        Step 17: Click open properties pane
                Verify the style menus appears as below
        """
        util_obj.verify_picture_using_sikuli('step_17_00.png', 'Step 17.00: Verify the style menus appears as below.')
        
        """
        Step 18: Close page without saving
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 19: Sign out WF
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        