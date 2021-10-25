'''
Created on July 05, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6197856
TestCase Name = Set Property to the content and Viewer
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview
from common.wftools.chart import Chart

class C6197856_TestClass(BaseTestCase):

    def test_C6197856(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        chart_obj = Chart(self.driver)
        main_page_run=wf_mainpage.Run(self.driver)
        
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
        repository_folder = 'Workspaces->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        page_name = "Link tile background and content path"
        
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
        Step 5: From Content tab Open Repository Widgets;
        Drag and drop Link tile widget over the panel on to the page canvas.
        """
        page_designer_obj.expand_and_collapse_repository_widgets_tab("expand")
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas("Link tile", 1)
        
        """ 
        Step 6: From the designer toolbar click open Properties pane;
        """
        page_designer_obj.click_property()
        util_obj.synchronize_with_visble_text("div[class*='container-settings']","Link Tile",190)
        
        
        """ 
        Step 6.01 Expected: Verify that the Link Tile section appears with the following options:
        1.Background path Not selected by default with ellipsis button to choose
        2.Content path Not selected by default with ellipsis button to choose
        3.Target Viewer as default with dropdown menu
        """
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=Not selected', 'Content=Not selected', 'Target=Viewer'], msg="Step 06.01 : Verify link tile settings appears")

        """ 
        Step 7: Click on ellipsis next to 'Background';
        """
        setting_tab=util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[1])
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption","Select background",190)
        
        """ 
        Step 7.01 Expected : Verify Select background dialog appears
        """
        main_page_obj.verify_popup_dialog_caption("Select background", "Step 07.01 : Verify Select background dialog appears")
        
        """ 
        Step 8: Click Domains from Breadcrumbs;
        Expand Retail Samples -> Portals -> Test Widget -> select Blue and click on Select Background button
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
        
        """ 
        Step 8.01 Expected : Verify Select background dialog disappears;
        Verify blue background is applied in the link tile widget as below and the background path text box shows IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html
        """
        main_page_obj.verify_popup_dialog_is_displayed(False, "Step 08.01 : Verify Select background dialog disappears")
        util_obj.verify_picture_using_sikuli('Step08.02.png', 'Step 08.02:Verify blue background is applied in the link tile widget')
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html', 'Content=Not selected', 'Target=Viewer'], msg="Step 08.03 : Verify Background path text box show")
        
        """ 
        Step 9: Click on ellipsis next to 'Content';
        """
        setting_tab=util_obj.validate_and_get_webdriver_object("div[class*='container-settings']", "Settings")
        ellipsis = util_obj.validate_and_get_webdriver_objects("div[class*='ellipsis-h']", 'Settings links', parent_object=setting_tab)
        core_util_obj.left_click(ellipsis[2])
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption","Select content",190)
        
        """ 
        Step 9.01 Expected : Verify Select Content dialog appears
        """
        main_page_obj.verify_popup_dialog_caption("Select content", "Step 09.01 : Verify Verify Select Content dialog appears")
        
        """ 
        Step 10: Click Domains from Breadcrumbs;
        Expand Retail Samples -> Portals -> Small Widget -> select 'Regional Profit by Category' and click on Select Content button
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
        
        """ 
        Step 10.01 Expected : Verify Select Content dialog disappears;
        Verify content path text box shows IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex
        """
        main_page_obj.verify_popup_dialog_is_displayed(False, "Step 10.01 : Verify Select Content dialog disappears")
        page_designer_obj.verify_setting_tab_properties("Link Tile", ['Background=IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html', 'Content=IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex', 'Target=Viewer'], msg="Step 10.02 : Verify content path text box shows")
        
        """ 
        Step 11 : Leave Target as a 'Viewer'
        """
        
        """ 
        Step 12 : Click Preview and click on Link tile widget.
        """
        page_designer_obj.click_preview()
        util_obj.synchronize_with_visble_text("div[data-ibx-type='pdTool']","Page Heading",190)
        page_designer_obj.select_container("")
        
        """ 
        Step 12.01 Expected : Verify that 'Regional Profit by Category' opens in a same window without any error.
        """
        core_util_obj.switch_to_frame("iframe[class='ibx-iframe-frame']")
        chart_obj.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 12.01")
        chart_obj.verify_y_axis_title_in_run_window(['Gross Profit'], msg="Step 12.02")
        chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 12.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], msg="Step 12.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 28, msg="Step 12.05")
        
        """ 
        Step 13 : Click on back button to get back to page designer canvas.
        """
        page_designer_obj.switch_to_default_page()
        page_preview_obj.go_back_to_design_from_preview()
        
        """ 
        Step 14 : Click on Save button;
        Enter title as 'Link tile background and content path' and click save
        """
        page_designer_obj.save_page_from_toolbar(page_name)
        
        """ 
        Step 15 : Close page designer
        """
        page_designer_obj.switch_to_previous_window()
        
        """ 
        Step 16 : Double click on 'Link tile background and content path';
        Click on Link tile widget
        """
        main_page_obj.double_click_on_content_area_items(page_name)
        core_util_obj.switch_to_frame(frame_css="iframe[class='ibx-iframe-frame']")
        link_tile=util_obj.validate_and_get_webdriver_object("div[data-ibx-type='pdContainer']","Link tile")
        core_util_obj.left_click(link_tile)
        
        """ 
        Step 16.01 Expected : Verify that 'Regional Profit by Category' opens in a same window without any error.
        """
        core_util_obj.switch_to_frame(frame_css="iframe[class='ibx-iframe-frame']")
        chart_obj.verify_x_axis_title_in_run_window(['Product Category'], msg="Step 16.01")
        chart_obj.verify_y_axis_title_in_run_window(['Gross Profit'], msg="Step 16.02")
        chart_obj.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 16.03")
        chart_obj.verify_y_axis_label_in_run_window(['0', '20M', '40M', '60M', '80M', '100M'], msg="Step 16.04")
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 28, msg="Step 16.05")
        
        """ 
        Step 17 : Close page
        """
        page_designer_obj.switch_to_default_page()
        main_page_run.close()
        
        """ 
        Step 18: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()
        