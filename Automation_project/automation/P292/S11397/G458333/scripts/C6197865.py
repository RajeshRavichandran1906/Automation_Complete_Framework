'''
Created on July 09, 2019.

@author: Aftab

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6197865
TestCase Name = Check Content menus
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C6197865_TestClass(BaseTestCase):

    def test_C6197865(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        selected_page_css = ".tpg-selected .pd-page-canvas"
        panel_container_css= "div.grid-stack-item-content"
        
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
        Step 3: Expand 'P292_S11397' domain;
                Click on 'G458333' folder and click on 'page' action tile from under Designer category
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
        Step 5: From Content tab open Repository Widgets;
                Drag and drop Link tile widget to the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        util_obj.synchronize_with_number_of_element(panel_container_css, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 6: Click Container tab and add regular panel on to the page canvas next to link tile widget
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Panel", 4)
        util_obj.synchronize_with_visble_text(selected_page_css, "Panel 2", main_page_obj.home_page_long_timesleep)
        
        """
        Step 7: Right click on Panel 2.
                Verify that the following context menu appears
                1.Refresh
                2.Edit title
                3.Settings
                4.Style
                5.Delete container
        """
        page_designer_obj.verify_container_context_menu('Panel 2', ['Refresh', 'Edit title', 'Settings', 'Format', 'Delete container'], '07.00')
        
        """
        Step 8: Right click on Link tile widget (first panel)
                Verify that the context menu should be same as the Panel 2:
                1.Refresh
                2.Edit title
                3.Settings
                4.Style
                5.Delete container
        """
        page_designer_obj.verify_container_context_menu('', ['Refresh', 'Edit title', 'Settings', 'Format', 'Delete container'], '08.00')
        
        """
        Step 9: Close page without saving
        """
        page_designer_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_long_timesleep)
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  