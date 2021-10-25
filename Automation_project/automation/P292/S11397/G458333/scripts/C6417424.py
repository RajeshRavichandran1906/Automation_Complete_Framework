'''
Created on July 10, 2019.

@author: Aftab

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6417424
TestCase Name = Set Background to Page
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.wftools.page_designer import Preview

class C6417424_TestClass(BaseTestCase):

    def test_C6417424(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        main_page_run_obj = wf_mainpage.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = "div[class*='pop-top']"
        containers_css=".ibx-csl-items-container [title='Containers']"
        panel_container_css= "div.grid-stack-item-content"
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Workspaces->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        template = 'Blank'
        link_page = 'lPage'
        dialog_path = ['{0}_{1}'.format(project_id, suite_id), group_id, link_page]
        page_name = 'Link tile background as Page'
        
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
        Step 5: Click on Save button and give title as 'lPage';
                Click save
        """
        page_designer_obj.save_as_page_from_application_menu(link_page)
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 6: Click on designer main menu and select New
        """
        page_designer_obj.select_option_from_application_menu('New')
        
        """
        Step 7: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(template)
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: From Content tab open Repository Widgets;
                Drag and drop Link tile widget on to the page canvas
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        util_obj.synchronize_with_number_of_element(panel_container_css, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 9: From the designer toolbar click on Properties
        """
        page_designer_obj.click_property()
        util_obj.synchronize_with_visble_text("div[class*='container-settings']","Link Tile", page_designer_obj.home_page_long_timesleep)
        
        """
        Step 10: Click on ellipsis next to 'Background';
        """
        setting_tab = util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[1])
        
        """
        Step 11: Click Domains from Breadcrumbs;
                Expand 'P292_S11397' domain -> 'G458333' folder;
                Select 'lPage' and click on Select Background button
                Verify Select background dialog disappears;
                Verify 'lpage' background is applied in the link tile widget as below and the background path text box shows IBFS:/WFC/Repository/P292_S11397/G458333/lpage
        """
        util_obj.synchronize_with_visble_text(pop_top_css, repository_folder.split('->')[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog(repository_folder.split('->')[0])
        for option in dialog_path:
            util_obj.synchronize_with_visble_text(pop_top_css, option, main_page_obj.home_page_long_timesleep)
            if option != link_page:
                main_page_obj.select_file_or_folder_from_resource_dialog(option, selection_type='double', view_type='grid_view')
            else:
                main_page_obj.select_file_or_folder_from_resource_dialog(option, view_type='grid_view')
        util_obj.synchronize_until_element_disappear(".ibx-dialog-ok-button.ibx-widget-disabled", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select background')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_popup_dialog_is_displayed(False, 'Step 11.00: Verify Select background dialog disappears.')
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=IBFS:/WFC/Repository/P292_S11397/G458333/lpage', 'Content=Not selected', 'Target=Viewer'], msg="Step 11.01 : Verify link tile settings appears")
        
        """
        Step 12: Click on ellipsis next to 'Content';
        """
        setting_tab = util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[2])
        
        """
        Step 13: Click Domains from Breadcrumbs;
                Expand Retail Samples -> Portals -> Small Widget -> select 'Regional Sales Trend' and click on Select Content button
                Verify Select Content dialog disappears;
                Verify content path text box shows IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional Sales Trend.fex
        """
        util_obj.synchronize_with_visble_text(pop_top_css, repository_folder.split('->')[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog(repository_folder.split('->')[0])
        for  option in ['Retail Samples', 'Portal', 'Small Widgets', 'Regional Sales Trend']:
            util_obj.synchronize_with_visble_text(pop_top_css, option, main_page_obj.home_page_long_timesleep)
            if option != 'Regional Sales Trend':
                main_page_obj.select_file_or_folder_from_resource_dialog(option, selection_type='double', view_type='grid_view')
            else:
                main_page_obj.select_file_or_folder_from_resource_dialog(option, view_type='grid_view')
        util_obj.synchronize_until_element_disappear(".ibx-dialog-ok-button.ibx-widget-disabled", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select content')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_popup_dialog_is_displayed(False, 'Step 13.00: Verify Select Content dialog disappears.')
        expected_path = ['Background=IBFS:/WFC/Repository/P292_S11397/G458333/lpage', 'Content=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Sales_Trend.fex', 'Target=Viewer']
        page_designer_obj.verify_setting_tab_properties("Link Tile", expected_path, msg="Step 13.01 : Verify link tile settings appears")
        
        """
        Step 14: Click Preview and click on Link tile widget.
                Verify that 'Regional Sales Trend' opens in same window without any error.
        """
        page_designer_obj.click_preview()
        page_designer_obj.select_link_tile_widget_in_canvas(1)
        core_util_obj.switch_to_frame(frame_css="[src*='Regional_Sales_Trend']")
        util_obj.synchronize_with_number_of_element("#jschart_HOLD_0 .risers [class*='riser']", 4, main_page_obj.home_page_long_timesleep)
        util_obj.verify_picture_using_sikuli('step14.png', "Step 14: Verify that 'Regional Sales Trend' opens in same window without any error.")
        core_util_obj.switch_to_default_content()
        
        """
        Step 15: Click on back button to get back to page designer canvas
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 16: Click on Save button;
                Enter title as 'Link tile background as Page' and click save
        """
        page_designer_obj.save_as_page_from_application_menu(page_name)
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        
        """
        Step 17: Close page designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_name, main_page_obj.home_page_long_timesleep)
        
        """
        Step 18: Double click on 'Link tile background as Page';
                Click on Link tile widget
                Verify that 'Regional Sales Trend' run in a same window without any error.
        """
        main_page_obj.double_click_on_content_area_items(page_name)
        core_util_obj.switch_to_frame(frame_css="[class='ibx-iframe-frame'][src*='"+page_name.replace(' ', '_').lower()+"']")
        page_designer_obj.select_link_tile_widget_in_canvas(1)
        core_util_obj.switch_to_frame(frame_css="[src*='Regional_Sales_Trend']")
        util_obj.synchronize_with_number_of_element("#jschart_HOLD_0 .risers [class*='riser']", 4, main_page_obj.home_page_long_timesleep)
        util_obj.verify_picture_using_sikuli('step18.png', "Step 18: Verify that 'Regional Sales Trend' opens in same window without any error.")
        core_util_obj.switch_to_default_content()
        
        """
        Step 19: Close page
        """
        main_page_run_obj.close()
        
        """
        Step 20: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  