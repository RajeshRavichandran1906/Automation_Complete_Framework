'''
Created on Jul 11, 2019

@author: Aftab

Test rail link: http://172.19.2.180/testrail/index.php?/cases/view/5743395
Test case name: Create empty filter bar

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5743395_TestClass(BaseTestCase):

    def test_C5743395(self):
        
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
        util_obj.synchronize_with_number_of_element(locator_obj.content_area_css,1, main_page_obj.home_page_medium_timesleep)
                 
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
        5 : Click on page filter configuration button
        '''
        page_designer_obj.click_filter_configuration()
        util_obj.synchronize_until_element_is_visible('iframe[class="ibx-opaque-frame"]', main_page_obj.home_page_medium_timesleep)
        
        '''
        5.01 : Verify filter configuration dialog and options appears as below
        '''
        expected = ['Page Filter Configuration', 'Quick filter type', 'Filter bar', 'Create empty filter bar', 'Filter modal window', 'Create empty filter modal window', 'OK', 'Cancel']
        actual = util_obj.validate_and_get_webdriver_object(pop_top_css, 'page filter configuration').text.strip().split('\n')
        util_obj.asequal(expected, actual, 'Step 05.00: Verify label of the filter window')
        elems = util_obj.validate_and_get_webdriver_objects('.ibx-radio-button-simple', 'filter configuration')
        status = {}
        for opt in elems:
            status[opt.text.strip()] = True if 'checked' in opt.get_attribute('class') else False
        util_obj.asequal(status['Filter bar'], True, 'Step 05.01: Verify Filter bar checked.')
        util_obj.asequal(status['Filter modal window'], False, 'Step 05.02: Verify Filter bar unchecked.')
                
        '''
        6 : Select 'create empty filter bar'
        '''
        page_designer_obj.select_filter_configurations_property('Create empty filter bar')
        util_obj.synchronize_until_element_disappear(pop_top_css, 9)
        
        '''
        6.01 : Verify empty filter bar appears as below
        '''
        page_designer_obj.verify_page_heading_title(['Page Heading'],'Step 06.00 : Verify page title')
        page_designer_obj.verify_page_header_visible_buttons(['Refresh', 'Show filters'], 'Step 06.1 : Verify Refresh and Filter button are display on page header')
        page_designer_obj.verify_number_of_filter_grid_cells(4,'Step 06.02: Verify empty filter bar')
        
        '''
        7 : Close page without saving
        '''
        core_util_obj.switch_to_previous_window()
        
        '''
        8 : Sign out WF
        ''' 
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  

