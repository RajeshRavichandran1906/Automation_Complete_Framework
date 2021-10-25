"""-------------------------------------------------------------------------------------------
Created on July 8, 2019
@author: Vpriya/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22062745
Test Case Title =  Check with Max Width
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design, Preview, Run as R
from common.wftools.wf_mainpage import Wf_Mainpage,Run
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.page_designer_design import PageDesignerDesign
from common.lib.webfocus.resource_dialog import Resource_Dialog
import time

class C6281302_TestClass(BaseTestCase):

    def test_C6281302(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_page_run = Run(self.driver)
        pd_designer = PageDesignerDesign(self.driver)
        resource_dialog = Resource_Dialog(self.driver)
        pd_preview = Preview(self.driver)
        pd_run = R(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
 
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
 
        """
            STEP 3 : Expand 'P292_S11397' domain -> 'G470364' folder; 
            Right click on 'C6281302' and select Edit
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.right_click_folder_item_and_select_menu("C6281302", "Edit")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 4 : Expand Repository widget in resource selector and drag link tile over the top 4 panels
        """
        pd_design.expand_and_collapse_content_tab("collapse")
        pd_design.expand_and_collapse_repository_widgets_tab("expand")
        
        pd_design.drag_repository_widget_to_canvas_container("Link tile", "Panel 1")
        pd_design.drag_repository_widget_to_canvas_container("Link tile", "Panel 2")
        pd_design.drag_repository_widget_to_canvas_container("Link tile", "Panel 3")
        pd_design.drag_repository_widget_to_canvas_container("Link tile", "Panel 4")

        """
            STEP 5 : Click on Link tile 1 and click open properties pane
        """
        pd_design.select_link_tile_widget_in_canvas(1)
        pd_design.click_property()
 
        """
            STEP 6 : Click on ellipsis next to 'Background';
            Click Domains from Breadcrumbs in Select background dialog;
            Expand Retail Samples -> Portals -> Test Widget -> select 'Blue' and click on Select Background button
        """
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Blue")
        pd_design.resource_dialog().click_button("Select background")
        
        """
            STEP 7 : Click on ellipsis next to 'Content';
            Click Domains from Breadcrumbs in Select background dialog;
            Expand Retail Samples -> Portals -> Small widgets -> Select 'Category Sales' and click on Select Content button
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        pd_design.resource_dialog().click_button("Select content")
 
        """
            STEP 8 : Click on Link tile 2;
            Click on ellipsis next to 'Background';
            Select 'Grey' and click on Select Background button
        """
        pd_design.select_link_tile_widget_in_canvas(2)
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Gray")
        pd_design.resource_dialog().click_button("Select background")
        
        """
            STEP 9 : Click on ellipsis next to 'Content';
            Select 'Regional Sales trend' and click on Select Content button
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Regional Sales Trend")
        pd_design.resource_dialog().click_button("Select content")
 
        """
            STEP 10 : Click on Link tile 3;
            Click on ellipsis next to 'Background';
            Select 'Green' and click on Select Background button
        """
        pd_design.select_link_tile_widget_in_canvas(3)
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Green")
        pd_design.resource_dialog().click_button("Select background")
        
        """
            STEP 11 : Click on ellipsis next to 'Content';
            Select 'Discount by Region' and click on Select Content button
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Discount by Region")
        pd_design.resource_dialog().click_button("Select content")
 
        """
            STEP 12 : Click on Link tile 4;
            Click on ellipsis next to 'Background';
            Select 'Red' and click on Select Background button
        """
        pd_design.select_link_tile_widget_in_canvas(4)
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Red")
        pd_design.resource_dialog().click_button("Select background")
 
        """
            STEP 13 : Click on ellipsis next to 'Content';
            Select 'Regional profit by Category' and click on Select Content button
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Regional Profit by Category")
        pd_design.resource_dialog().click_button("Select content")
 
        """
            STEP 14 :In section 2
            Drag 1 link tile widget, 2 tabbed containers , 1 carousel container, 1 accordion container and 1 explorer widget one after another
        """
        pd_design.select_page_section(2)
        pd_design.select_option_from_carousel_items("Content")
        pd_design.drag_repository_widgets_item_to_blank_canvas("Link tile", 1, section_num=2)
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Tab", 4, section_num=2)
        pd_design.drag_container_item_to_blank_canvas("Tab", 7, section_num=2)
        pd_design.drag_container_item_to_blank_canvas("Carousel", 10, section_num=2)
        pd_design.drag_container_item_to_blank_canvas("Accordion", 10, section_num=2)
        
        pd_design.select_option_from_carousel_items("Content")
        pd_design.drag_repository_widgets_item_to_blank_canvas("Explorer", 10, section_num=2)
        
        """
            STEP 15 : Click on section 2
        """
        pd_design.select_page_section(2)
        time.sleep(5)

        """
            Step 15.01 : Verify Row height for section 2 is still set to 60px
        """
        rowheight_textbox_obj = utils.validate_and_get_webdriver_object("input[placeholder='60px']", "row height")
        actual_value = rowheight_textbox_obj.get_attribute("placeholder").strip()
        msg = "Step 15.01 : Verify Row height for section 2 is still set to 60px"
        utils.asequal("60px", actual_value, msg)
        
        """
            STEP 16 : Click on Link tile 1 under section2;
            Click on ellipsis next to 'Background';
            Select 'Yellow' and click on Select Background button
        """
        pd_design.select_link_tile_widget_in_canvas(5)
        ellipsis_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-background-path-btn']", "Ellipsis button")
        core_utils.left_click(ellipsis_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Test Widgets", "Yellow")
        pd_design.resource_dialog().click_button("Select background")
        
        """
            STEP 17 : Click on ellipsis next to 'Content';
            Select 'Average cost vs sales' and click on Select Content button
        """
        content_obj = utils.validate_and_get_webdriver_object("div[class^='pd-ps-value pd-ps-content-path-btn']", "Content button")
        core_utils.left_click(content_obj)
        pd_design.wait_for_visible_text(".ibx-dialog-cancel-button", "Cancel")
        resource_dialog.select_crumb_item("Workspaces")
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Average Cost v Sales")
        pd_design.resource_dialog().click_button("Select content")
        
        """
            STEP 18 : Click on section 2 and turn on Collapsible switch under section settings in properties pane
        """
        pd_design.select_page_section(2)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
 
        """
            STEP 19 : Click on section 1 and turn on Collapsible switch under section settings in properties pane
        """
        pd_design.select_page_section(1)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        """
            STEP 20 : Click on preview button
        """
        pd_design.click_preview()
        
        """
            Step 20.01 : Verify both sections appear as below and its contents;
            Verify collapsible buttons for both sections appears as below too
        """
        pd_preview.verify_containers_title(['Panel 5', 'Panel 6', 'Panel 7', 'Panel 13', 'Panel 9', 'Panel 10', 'Panel 11', 'Panel 12'], "Step 20.01 : Verify both sections appear as below and its contents")
        par_section_obj = pd_designer._get_page_section_object(1)
        collapsible_button = utils.validate_and_get_webdriver_object("div.ibx-accordion-page-button ", "Collapsible button", parent_object=par_section_obj)
        actual_values = collapsible_button.get_attribute('class').strip()
        msg = "Step 20.02 : Verify collapsible buttons for both sections appears as below too "
        utils.as_notin("acc-btn-hide", actual_values, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        collapsible_button = utils.validate_and_get_webdriver_object("div.ibx-accordion-page-button ", "Collapsible button", parent_object=par_section_obj)
        actual_values = collapsible_button.get_attribute('class').strip()
        msg = "Step 20.03 : Verify collapsible buttons for both sections appears as below too "
        utils.as_notin("acc-btn-hide", actual_values, msg)
        
        """
            STEP 21 : Click Save;
            Enter title as 'Row height with diff panels' and click save
        """
        pd_run.go_back_to_design_from_preview()
        pd_design.save_as_page_from_application_menu("Row height with diff panels")
 
        """
            STEP 22 : Close designer
        """
        pd_design.close_page_designer_from_application_menu()

        """
            STEP 23 : Right click on 'Row height with diff panels' and select Run
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.right_click_folder_item_and_select_menu("Row height with diff panels", "Run")
        
        time.sleep(10)
        main_page_run.switch_to_frame()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")

        """
            Step 23.01 : Verify both sections appear as below and its contents;
            Verify collapsible buttons for both sections appears as below too
        """
        pd_preview.verify_containers_title(['Panel 5', 'Panel 6', 'Panel 7', 'Panel 13', 'Panel 9', 'Panel 10', 'Panel 11', 'Panel 12'], "Step 23.01 : Verify both sections appear as below and its contents")
        par_section_obj = pd_designer._get_page_section_object(1)
        collapsible_button = utils.validate_and_get_webdriver_object("div.ibx-accordion-page-button ", "Collapsible button", parent_object=par_section_obj)
        actual_values = collapsible_button.get_attribute('class').strip()
        msg = "Step 23.02 : Verify collapsible buttons for both sections appears as below too "
        utils.as_notin("acc-btn-hide", actual_values, msg)
        
        par_section_obj = pd_designer._get_page_section_object(2)
        collapsible_button = utils.validate_and_get_webdriver_object("div.ibx-accordion-page-button ", "Collapsible button", parent_object=par_section_obj)
        actual_values = collapsible_button.get_attribute('class').strip()
        msg = "Step 23.03 : Verify collapsible buttons for both sections appears as below too "
        utils.as_notin("acc-btn-hide", actual_values, msg)
        
        """
            STEP 24 : Close page
        """
        main_page_run.switch_to_default_content()
        main_page_run.close()
        
        """
            STEP 25 : Signout WF.
        """
        main_page.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()         