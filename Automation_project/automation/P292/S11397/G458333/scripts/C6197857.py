'''
Created on July 08, 2019.

@author: Aftab

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6197857
TestCase Name = Set property to content and New Window
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
from common.wftools.chart import Chart

class C6197857_TestClass(BaseTestCase):

    def test_C6197857(self):
        
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
        chart_obj = Chart(self.driver)
        
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
        page_name = 'Link tile background and content path new'
        
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
                Drag and drop Link tile widget on to the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        util_obj.synchronize_with_number_of_element(panel_container_css, 1, main_page_obj.home_page_long_timesleep)
         
        """
        Step 6: From the designer toolbar click on Properties
        """
        page_designer_obj.click_property()
         
        """
        Step 7: Click on ellipsis next to 'Background';
        """
        setting_tab = util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[1])
         
        """
        Step 8: Click Domains from Breadcrumbs in Select background dialog;
                Expand Retail Samples -> Portals -> Test Widget -> select Blue and click on Select Background button
                Verify Select background dialog disappears;
                Verify background path text box shows IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html
        """
        util_obj.synchronize_with_visble_text(pop_top_css, repository_folder.split('->')[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog(repository_folder.split('->')[0])
        for  option in ['Retail Samples', 'Portal', 'Test Widgets', 'Blue']:
            util_obj.synchronize_with_visble_text(pop_top_css, option, main_page_obj.home_page_long_timesleep)
            if option != 'Blue':
                main_page_obj.select_file_or_folder_from_resource_dialog(option, selection_type='double', view_type='grid_view')
            else:
                main_page_obj.select_file_or_folder_from_resource_dialog(option, view_type='grid_view')
        util_obj.synchronize_until_element_disappear(".ibx-dialog-ok-button.ibx-widget-disabled", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select background')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_popup_dialog_is_displayed(False, 'Step 08.00: Verify Select background dialog disappears.')
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html', 'Content=Not selected', 'Target=Viewer'], msg="Step 08.01 : Verify link tile settings appears")
         
        """
        Step 9: Click on ellipsis next to 'Content';
        """
        setting_tab = util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[2])
         
        """
        Step 10: Click Domains from Breadcrumbs; :
                Expand Retail Samples -> Portals -> Small Widget -> select 'Regional Profit by Category' and click on Select Content button
                Verify Select Content dialog disappears;
                Verify content path text box shows IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex
        """
        util_obj.synchronize_with_visble_text(pop_top_css, repository_folder.split('->')[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.select_crumb_item_from_resource_dialog(repository_folder.split('->')[0])
        for  option in ['Retail Samples', 'Portal', 'Small Widgets', 'Regional Profit by Category']:
            util_obj.synchronize_with_visble_text(pop_top_css, option, main_page_obj.home_page_long_timesleep)
            if option != 'Regional Profit by Category':
                main_page_obj.select_file_or_folder_from_resource_dialog(option, selection_type='double', view_type='grid_view')
            else:
                main_page_obj.select_file_or_folder_from_resource_dialog(option, view_type='grid_view')
        util_obj.synchronize_until_element_disappear(".ibx-dialog-ok-button.ibx-widget-disabled", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Select content')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_popup_dialog_is_displayed(False, 'Step 09.00: Verify Select Content dialog disappears.')
        expected_path = ['Background=IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html', 'Content=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex', 'Target=Viewer']
        page_designer_obj.verify_setting_tab_properties("Link Tile", expected_path, msg="Step 09.01 : Verify link tile settings appears")
         
        """
        Step 11: Click Target dropdown select 'New Window'
        """
        page_designer_obj.select_property_tab_settings_option('Link Tile', 'drop_down', 'Target', 'New window')
         
        """
        Step 12: Click Preview and click on Link tile widget
                Verify that 'Regional Profit by Category' opens in a new window without any error.
        """
        page_designer_obj.click_preview()
        page_designer_obj.select_link_tile_widget_in_canvas(1)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element("#jschart_HOLD_0 .risers rect[class*='riser']", 28, main_page_obj.home_page_long_timesleep)
        chart_obj.verify_y_axis_title_in_run_window(['Gross Profit'], msg="Step 16.02")
        chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 16.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], msg="Step 16.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 .risers rect[class*='riser']", 3, 9, msg="Step 16.05")
         
        """
        Step 13: Close new window with 'Regional Profit by Category' widget
        """
        core_util_obj.switch_to_previous_window()
         
        """
        Step 14: Click on back button to get back to page designer canvas
        """
        page_preview_obj.go_back_to_design_from_preview()
         
        """
        Step 15: Click on Save button;
                Enter title as 'Link tile background and content path new' and click save.
        """
        page_designer_obj.save_as_page_from_application_menu(page_name)
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_long_timesleep)
         
        """
        Step :16 Close Page Designer.
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_name, main_page_obj.home_page_long_timesleep)
        
        """
        Step 17: Double click on 'Link tile background and content path new';
                Click on Link tile widget
                Verify that 'Regional Profit by Category' opens in a new window without any error as below
        """
        main_page_obj.double_click_on_content_area_items(page_name)
        core_util_obj.switch_to_frame(frame_css="[class='ibx-iframe-frame'][src*='"+page_name.replace(' ', '_').lower()+"']")
        page_designer_obj.select_link_tile_widget_in_canvas(1)
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_new_window()
        
        util_obj.synchronize_with_number_of_element("#jschart_HOLD_0 .risers rect[class*='riser']", 28, main_page_obj.home_page_long_timesleep)
        chart_obj.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 17.01")
        chart_obj.verify_y_axis_title_in_run_window(['Gross Profit'], msg="Step 17.02")
        chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 17.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], msg="Step 17.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 .risers rect[class*='riser']", 1, 28, msg="Step 17.05")
        
        """
        Step 18: Close new window and Page
        """
        core_util_obj.switch_to_previous_window()
        main_page_run_obj.close()
        
        """
        Step 19: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  