'''
Created on May 11, 2019

@author: AA14564

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262055
TestCase Name = CTRL-ALT-C no longer brings up resource editor in PD
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
import sys
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as kb

class C8262055_TestClass(BaseTestCase):

    def test_C8262055(self):
        
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
        bottom_page_tab_css = "[class*='ibx-tab-position-bottom'] [data-ibx-name*='itemsContainer'] [data-ibx-name*='itemsBox'] [class*='wb-tab-button']"
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Common'
        action_bar = 'Page'
        page_name = "PD-1137"
        expected_tab = [page_name]
        error_data = ['Error', 'Uncaught']
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from side bar
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
        Step 4: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Choose 'Grid 2-1' template
        """
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(page_canvas_css, 'Panel1', main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(15, pause_time=25)
        
        """
        Step 6: Save as 'PD-1137' and exit designer
        """
        page_designer_obj.save_page_from_toolbar(page_name)
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 7: Right click on 'PD-1137' from content area and select edit
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(page_name, context_menu_item_path='Edit')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_canvas_css, 'Panel1', main_page_obj.home_page_long_timesleep)
        
        """
        Step 8: Hit CTRL+ALT+C
                Verify no action takes place;
                Verify it neither brings up resource editor nor F12 console
        """
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.press_key(pykeyboard.alt_key)
            pykeyboard.tap_key(character=u'\u0063')
            pykeyboard.release_key(pykeyboard.alt_key)
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            kb.send('ctrl+alt+c')
        time.sleep(3)
        util_obj.synchronize_with_visble_text(bottom_page_tab_css, page_name, main_page_obj.home_page_short_timesleep)
        tab_page_list = [tab.text.strip() for tab in util_obj.validate_and_get_webdriver_objects(bottom_page_tab_css, 'bottom page tab css') if tab.text != '']
        util_obj.as_List_equal(expected_tab, tab_page_list, 'Step 08: Verify no action takes place')
        log_data = util_obj.get_console_log()
        for exp_data_ in error_data:
            for index_, act_data_ in enumerate(log_data):
                if exp_data_ in str(act_data_):
                    status = log_data[index_]
                else:
                    status = True
        util_obj.asequal(True, status, 'Step 08.01: Verify it neither brings up resource editor nor F12 console.')
        
        """
        Step 9: Close page
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 10: Sign out WF
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()