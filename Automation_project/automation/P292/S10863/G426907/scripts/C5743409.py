'''
Created on July 10, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743409
TestCase Name =Add Container title with special characters
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C5743409_TestClass(BaseTestCase):

    def test_C5743409(self):
        
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
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from side bar
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
        Step 5: Drag and drop '!@#$%^&*()_+' report from under 'G426906' folder;
        """
        page_designer_obj.drag_content_item_to_blank_canvas('!@#$%^&*()_+', 1)
        
        """ 
        Step 5.01: Verify container and content appears as below
        """
        page_designer_obj.verify_containers_title(['!@#$%^&*()_+'], msg="Step 05.01 : Verify container")
        page_designer_obj.verify_container_title_bar_visible_buttons('!@#$%^&*()_+', ['Maximize', 'Options'], msg="Step 05.02 : Verify container visible buttons")
        page_designer_obj.switch_to_container_frame('!@#$%^&*()_+')
        content_obj=util_obj.validate_and_get_webdriver_object("[class=errorMain]>a", "Error main")
        expected_output=util_obj.get_element_attribute(content_obj, "text")
        actual_output='No output'
        util_obj.asequal(actual_output, expected_output, "Step 05.03 : Verify Content")
        
        """ 
        Step 6: Close page without saving
        """
        page_designer_obj.switch_to_default_page()
        page_designer_obj.close_page_designer_without_save_page()
        
        """ 
        Step 7: Sign out WF
        """
        core_util_obj.switch_to_previous_window(False)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()

        