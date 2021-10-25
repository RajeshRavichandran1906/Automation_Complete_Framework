'''
Created on July 02, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6185760
TestCase Name = Add Link Tile onto a regular panel
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C6185760_TestClass(BaseTestCase):

    def test_C6185760(self):
        
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
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 5: Click on Container tab;
        Drag and drop a regular panel on to the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Panel", 1)
        
        """ 
        Step 6: From Content tab Open Repository Widgets;
        Drag and drop Link tile widget over the panel on to the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
       
        
        """ 
        Step 6.01 Expected: Verify the title and tool bar of the link tile widget are hidden by default as below
        """
        page_designer_obj.verify_containers_title([], msg="Step 06.01 : Verify Container title of the link tile widget hidden by default")
        page_designer_obj.verify_container_title_bar_visible_buttons("Panel 1", [], msg="Step 06.02 : Verify Container title of the link tool bar widget hidden by default")
        
        """ 
        Step 7: From the designer toolbar click open Properties pane;
        Switch on Title and Toolbar buttons.
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab_settings_option("Container Settings", "radio_button", "Title")
        page_designer_obj.select_property_tab_settings_option("Container Settings", "radio_button", "Toolbar")
        
        """ 
        Step 7.01 Expected: Verify link tile panel title appears as 'Panel 1' and the tool bar appears as below
        """
        page_designer_obj.verify_containers_title(['Panel 1'], msg="Step 07.01 : Verify link tile panel title appears")
        page_designer_obj.verify_container_title_bar_visible_buttons("Panel 1", ['Maximize', 'Options'], msg="Step 07.02 : Verify link tile tool bar appears")
        
        """ 
        Step 7.02 Expected: Verify link tile settings appears as below in properties pane
        """
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=Not selected', 'Content=Not selected', 'Target=Viewer'], msg="Step 07.03 : Verify link tile settings appears")
        
        
        """ 
        Step 8: Click on Application menu -> Save As;
        Enter title as 'Link tile on a Panel' and click save.
        """
        page_designer_obj.save_as_page_from_application_menu('Link tile on a Panel')
        
        """ 
        Step 9: Close page designer
        """
        page_designer_obj.switch_to_previous_window()
        
        """ 
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  