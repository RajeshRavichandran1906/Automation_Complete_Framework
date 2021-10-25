'''
Created on Jul 12, 2019

@author: Aftab

Test rail link: http://172.19.2.180/testrail/index.php?/cases/view/5743393
Test case name: Quick Filter type :Filter Bar

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5743393_TestClass(BaseTestCase):

    def test_C5743393(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
                
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        quick_filter_css = "[title='Quick filter']"
        page_filter_grid = ".pd-filter-grid"
                
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        template = 'Blank'
        
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
        util_obj.synchronize_with_visble_text(pop_top_css, template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(template)
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
                Verify a number with the amount of filters will appear in a red circle on top of the Quick Filter button, on the top right corner as below
        """
        page_designer_obj.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        page_designer_obj.drag_content_item_to_blank_canvas('Category Sales', 1, content_folder_path='Retail Samples->Portal->Small Widgets')
        util_obj.synchronize_until_element_is_visible(quick_filter_css, main_page_obj.home_page_long_timesleep)
        page_designer_obj.verify_quick_filter_value('6', 'Step 05.00')
        
        """
        Step 6: Click on the quick filter button
                Verify by default filter bar opens up with the filters as below and quick filter button disappears
        """
        page_designer_obj.click_quick_filter()
        util_obj.synchronize_until_element_disappear(quick_filter_css, main_page_obj.home_page_long_timesleep)
        util_obj.verify_object_visible(quick_filter_css, False, 'Step 06.01')
        util_obj.synchronize_with_visble_text(page_filter_grid, 'Region', main_page_obj.home_page_long_timesleep)
        page_designer_obj.verify_filter_dropdown_is_optional('Category:', 'Step 06.02: Verify Category is optional', 1)
        page_designer_obj.verify_filter_dropdown_is_optional('Product Model:', 'Step 06.03: Verify Product Model is optional', 1)
        page_designer_obj.verify_filter_dropdown_is_optional('Region:', 'Step 06.04: Verify region is optional', 1)
        page_designer_obj.verify_filter_dropdown_is_optional('Store Type:', 'Step 06.05: Verify Store type is optional', 1)
        page_designer_obj.verify_filter_date_picker_is_optional('From:', 'Step 06.06: Verify From is optional', 1)
        page_designer_obj.verify_filter_date_picker_is_optional('To:', 'Step 06.07: Verify to is optional', 1)
        
        """
        Step 7: Click on page filter configuration button
                Verify ibx window with the choices filter bar and filter modal window will appears as below
        """
        page_designer_obj.click_filter_configuration()
        util_obj.synchronize_until_element_is_visible('iframe[class="ibx-opaque-frame"]', main_page_obj.home_page_medium_timesleep)
        expected = ['Page Filter Configuration', 'Quick filter type', 'Filter bar', 'Filter modal window', 'OK', 'Cancel']
        actual = util_obj.validate_and_get_webdriver_object(pop_top_css, 'page filter configuration').text.strip().split('\n')
        util_obj.asequal(expected, actual, 'Step 07.00: Verify label of the filter window')
        elems = util_obj.validate_and_get_webdriver_objects('.ibx-radio-button-simple', 'filter configuration')
        status = {}
        for opt in elems:
            status[opt.text.strip()] = True if 'checked' in opt.get_attribute('class') else False
        util_obj.asequal(status['Filter bar'], True, 'Step 07.01: Verify Filter bar checked.')
        util_obj.asequal(status['Filter modal window'], False, 'Step 07.02: Verify Filter bar unchecked.')
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 8: Close page without saving
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  