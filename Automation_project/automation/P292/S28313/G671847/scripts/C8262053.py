'''
Created on April 16, 2019

@author: Vishnu Priya\Samuel

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262053
TestCase Name = Web Browser Tab change
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C8262053_TestClass(BaseTestCase):

    def test_C8262053(self):
        
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
        page_canvas_css = ".pd-page-canvas"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->P292_S28313->G671847'
        action_tile = 'Common'
        action_bar = 'Page'
        
        """
        Step 1: Log into WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from the side bar
        """  
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'P292_S28313' domain -> G671847 folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under common category
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Choose blank template
        Verify that the page loads;
        Verify that the browser tab is now Page and not Page Designer
        """
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text(page_canvas_css, '', main_page_obj.home_page_medium_timesleep)
        page_canvas_text = util_obj.validate_and_get_webdriver_object(page_canvas_css, 'page_canvas_text').text
        util_obj.verify_list_values([''], [page_canvas_text], 'Step 5.1: Verify that the page loads')
        actual_browser_tab = self.driver.title
        util_obj.verify_list_values(['Page'], [actual_browser_tab], 'Step 5.2: Verify that the browser tab is now Page and not Page Designer')
        
        """
        Step 6: Close page without saving
        """   
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)
        
        """
        Step 7: Click on 'P292_S28313' domain -> G671847 folder
        """ 
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: Click on Page action tile from under Designer category
        """ 
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9: Choose Grid 2-1 template
        Verify that the page loads;
        Verify that the browser tab is now Page and not Page Designer
        """  
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(page_canvas_css, 'Panel 3', main_page_obj.home_page_medium_timesleep)
        page_canvas_text = util_obj.validate_and_get_webdriver_object(page_canvas_css, 'page_canvas_text').text
        page_canvas_text = page_canvas_text.replace('\n', '')
        util_obj.verify_list_values(['Panel 1Panel 2Panel 3'], [page_canvas_text], 'Step 9.1: Verify that the page loads')
        actual_browser_tab = self.driver.title
        util_obj.verify_list_values(['Page'], [actual_browser_tab], 'Step 9.2: Verify that the browser tab is now Page and not Page Designer')
        
        """
        Step 10: Close page without saving
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()