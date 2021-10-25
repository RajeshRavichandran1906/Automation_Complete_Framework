'''
Created on July 05, 2019.

@author: Aftab

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6185762
TestCase Name = Add Link Tile onto a tabbed panel
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C6185762_TestClass(BaseTestCase):

    def test_C6185762(self):
        
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
        Step 5: Click on Container tab;
                Drag and drop two regular panels and a tabbed container on to the page canvas one after other
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Panel", 1)
        util_obj.synchronize_with_visble_text(selected_page_css, "Panel 1", main_page_obj.home_page_long_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas("Panel", 4)
        util_obj.synchronize_with_visble_text(selected_page_css, "Panel 2", main_page_obj.home_page_long_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas("Tab", 7)
        util_obj.synchronize_with_visble_text(selected_page_css, "Panel 3", main_page_obj.home_page_long_timesleep)
        
        """
        Step 6: From Content tab open Repository Widgets;
                Drag and drop Link tile widget over the tabbed container on to the page canvas.
                Verify the link tile widget is added as a new panel not as a new tab in panel 3 as below
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 7)
        util_obj.synchronize_with_number_of_element(panel_container_css, 4, main_page_obj.home_page_long_timesleep)
        page_designer_obj.select_container('')
        
        """
        Step 7: From the designer toolbar click on Properties.
                Verify Link tile properties setting appears as below
        """
        page_designer_obj.click_property()
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=Not selected', 'Content=Not selected', 'Target=Viewer'], msg="Step 07.03 : Verify link tile settings appears")
        
        """
        Step 8: Click on the tab container(panel 3)
                Verify Link tile properties setting doesn't appear.
        """
        page_designer_obj.select_container('Panel 3')
        page_designer_obj.verify_setting_tabs(['Container Settings', 'Content Customization', 'Content'], "Step 08.00: Verify Link tile properties setting doesn't appear.")
        
        """
        Step 9: Click on Application menu -> Save;
                Enter title as 'Link tile on a tabbed container' and click save.
        """
        page_designer_obj.save_as_page_from_application_menu('Link tile on a tabbed container')
        
        """
        Step 10: Close page designer
        """
        page_designer_obj.switch_to_previous_window()
        
        """
        Step 11: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  