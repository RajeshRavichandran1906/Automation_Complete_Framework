'''
Created on May 28, 2019.

@author: Niranjan_Das

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262063
TestCase Name = Page Selection
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Preview

class C8262063_TestClass(BaseTestCase):

    def test_C8262063(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj=Preview(self.driver)
        
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
        Step 3: Click on 'P292_S28313' domain -> G671849 folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 5: Choose 'Grid 2-1' template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 6: Click on Panel
        """
        page_designer_obj.select_container("Panel 1")
        
        """ 
        Step 7: Click on properties panel
        """
        page_designer_obj.click_property()
        page_designer_obj.wait_for_visible_text("div.pd-settings-tab-page", "Container")
        
        """ 
        Step 7.01: Verify Container settings appears in properties panel
        """
        expected_tabs=['Container Settings', 'Content Customization', 'Content']
        page_designer_obj.verify_setting_tabs(expected_tabs, "Step 7.01 :Verify Container settings appears in properties panel")
        
        """ 
        Step 8: Click on 'Page 1' tab at the bottom of the page
        """
        page_designer_obj.select_page_from_bottom_tab("Page 1")
        page_designer_obj.wait_for_visible_text(".pd-settings-tab-page", "Page")
        
        """ 
        Step 8.01: Verify Page settings appears in properties panel
        """
        expected_tabs=['Page Settings', 'Embedded Resources']
        page_designer_obj.verify_setting_tabs(expected_tabs, "Step 8.01 :Verify Page settings appears in properties panel")
        
        """ 
        Step 9: Click Preview button
        """
        page_designer_obj.click_preview()
        
        """ 
        Step 9.01: Verify 'Page 1' tab does NOT appear at the bottom
        """
        page_preview_obj.verify_preview_is_displayed("Step 9.01 :Verify 'Page 1' tab does NOT appear at the bottom")
        
        """ 
        Step 10: Click Preview button
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """ 
        Step 11: Close page without saving
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(False)
        
        """
        Step 12: Signout WF
        """ 
        util_obj.synchronize_with_visble_text(locator_obj.CONTENT_CSS, "Content", main_page_obj.home_page_long_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()
