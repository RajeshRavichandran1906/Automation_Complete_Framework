'''
Created on Jul 12, 2019

@author: Aftab

Test rail link: http://172.19.2.180/testrail/index.php?/cases/view/5743394
Test case name: Quick Filter type : Filter modal window

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
import time

class C5743394_TestClass(BaseTestCase):

    def test_C5743394(self):
        
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
        
        '''
        1 : Login WF as domain developer
        '''
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
         
        '''
        2 : Click on Content view from side bar
        '''
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
         
        '''
        3 : Expand 'P292_S10863' domain -> 'G426906' folder;
            Click on Page action tile from under Designer category
        '''
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()

        '''
        4 : Choose blank template
        '''
        util_obj.synchronize_with_visble_text(pop_top_css, template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(template)
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        '''
        5 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        '''
        page_designer_obj.collapse_content_folder('G426906->P292_S10863')
        content_folder = 'Retail Samples->Portal->Small Widgets'
        page_designer_obj.drag_content_item_to_blank_canvas('Category Sales', 1, content_folder)
        
        '''
        6 : Click on page filter configuration button;
            Choose "Filter Modal window' and click OK
        '''
        page_designer_obj.click_filter_configuration()
        util_obj.synchronize_until_element_is_visible('iframe[class="ibx-opaque-frame"]', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_filter_configurations_property('Filter modal window')
        util_obj.synchronize_until_element_disappear(pop_top_css, 9)
        
        '''
        7 : Click on the quick filter button
        '''
        page_designer_obj.click_quick_filter()
        util_obj.synchronize_until_element_is_visible(pop_top_css, main_page_obj.home_page_medium_timesleep)
        
        '''
        7.01 : Verify filter modal window appears as below
        '''
        actual = util_obj.validate_and_get_webdriver_object(pop_top_css, 'filter modal window').text.strip().split('\n')
        expected = ['Selections', 'Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:']
        util_obj.asequal(expected, actual, 'Step 07.00: Verify label of the filter window')
        page_designer_obj.verify_number_of_filter_grid_cells(8,'Step 07.01: Verify 8 filter grid cells')
        time.sleep(2)
        page_designer_obj.verify_filter_dropdown_is_optional('Category:', 'Step 07.02: Verify Category is optional', 1, model_window=True)
        page_designer_obj.verify_filter_dropdown_is_optional('Product Model:', 'Step 07.03: Verify Product Model is optional', 1, model_window=True)
        page_designer_obj.verify_filter_dropdown_is_optional('Region:', 'Step 07.04: Verify region is optional', 1, model_window=True)
        page_designer_obj.verify_filter_dropdown_is_optional('Store Type:', 'Step 07.05: Verify Store type is optional', 1, model_window=True)
        page_designer_obj.verify_filter_date_picker_is_optional('From:', 'Step 07.06: Verify From is optional', 1, model_window=True)
        page_designer_obj.verify_filter_date_picker_is_optional('To:', 'Step 07.07: Verify to is optional', 1, model_window=True)
        
        '''
        8 : Close page without saving
        '''
        core_util_obj.switch_to_previous_window()
        
        '''
        9 : Sign out WF
        ''' 
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  
