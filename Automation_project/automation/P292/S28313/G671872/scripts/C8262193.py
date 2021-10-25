'''
Created on June 03, 2019.

@author: Varun/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262193
TestCase Name = Add multiple reports with parameters into portal and verify filter modal window 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators import wf_mainpage_locators
from common.wftools.page_designer import Design,Preview
from common.locators import portal_designer

class C8262193_TestClass(BaseTestCase):

    def test_C8262193(self):
        
        """
        CLASS OBJECTS 
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        two_level_side=designer_portal.Two_Level_Side(self.driver)
        template_obj=designer_portal.New_Page_Template_Window(self.driver)
        portal_canvas_obj=designer_portal.Canvas(self.driver)
        page_design_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        potal_locator_obj=portal_designer.Vfive_Designer()

        
        """
        COMMON TEST CASE VARIABLES 
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Portal'
        portal_title= "C6779818"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        
        """
            STEP 01 : Login to WF as Developer.Navigate to P292_S19901/G520447 folder.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)
        
        """
            STEP 02 : Click create new V5 portal action tile under Designer.
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
            STEP 03 : Enter "C6779818" in Title and check Create My Pages Menu and click Create button.
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_title)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
            STEP 04 : Publish and Run "C6779818" portal.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Publish")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Run")
        
        """
            STEP 05 : Click + button under My Pages in left Navigation bar.
        """
        core_util_obj.switch_to_new_window()
        two_level_side.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        
        """
            STEP 05.01 : Verify New Page pop-up window appears.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 3-3-3', main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_popup_dialog_caption("New Page", "Step 05.01 : Verify New Page pop-up window appears.")
        
        """
            STEP 06 : Select Grid 3-3-3 template.
        """
        template_obj.select_new_page_template('Grid 3-3-3')
        
        """
            STEP 06.01 : Verify page created successfully and Filter icon is not available in page toolbar.
        """
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 06.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7', 'Panel 8', 'Panel 9']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 06.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 06.03 : Filter icon is not available in page toolbar")
        
        """
            STEP 07: Click Add content (+) in Panel 1 and Add "Category Sales" (report with parameters) from Retail Samples > Portal > Small Widgets folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        page_design_obj.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 07.01 : Verify Filter icon visible in toolbar.
        """
        expected_buttons_name_list=['Share', 'Refresh', 'Show filters', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 07.01 : Filter icon is visible in the page toolbar")
        
        """
            STEP 08 : Click Show filters icon in toolbar.
        """
        page_preview_obj.click_show_filters()
        
        """
            STEP 08.01 : Verify filter modal appears with a 4 column grid.
            And with Submit and Reset buttons present at lower right corner of the filter modal window.
        """
        expected_label_list=['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:']
        page_design_obj.verify_filter_control_labels(expected_label_list, "Step 08.01 : Verify filter modal appears with a 4 column grid", model_window=True)
        expected_buttons=['Submit','Reset']
        page_design_obj.verify_filter_modal_window_buttons(expected_buttons, "Step 08.02 : Submit and Reset buttons present")
        
        """
            STEP 09 : Close filter modal window.
        """
        page_design_obj.close_filter_model_window()
        
        """
            STEP 10: Click Add content (+) in Panel 2
            Add "28 - Multi-Select Dynamic Required" (report with required parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 2")
        main_page_obj.select_crumb_item_from_resource_dialog("Domains")
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file("P398_S10799->Reference Items", "28 - Multi-Select Dynamic Required")
        page_design_obj.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 10.01 : Verify "Select North America" filter control added next to the available filter controls.
        """
        expected_label_list=['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:', 'Select North America']
        page_design_obj.verify_filter_control_labels(expected_label_list, "Step 09.01 : Verify 'Select North America' filter control added next to the available filter controls.", model_window=True)
        
        """
            STEP 11 : Close filter modal window.
        """
        page_design_obj.close_filter_model_window()
        
        """
            STEP 12: Click Add content (+) in Panel 3
            Add "02 - Simple Input Optional All" (report with parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 3")
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file(None, "02 - Simple Input Optional All")
        page_design_obj.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 13: Click Add content (+) in Panel 4
            Add "12 - Slider Range Optional Other" (report with parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 4")
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file(None, "12 - Slider Range Optional Other")
        page_design_obj.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 14: Click Add content (+) in Panel 5
            Add "16 - Date Range Required" (report with parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 5")
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file(None, "16 - Date Range Required")
        page_design_obj.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(potal_locator_obj.page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        
        """
            STEP 14.01 : Verify filter modal window opens up and newly found parameters are added next to the available controls in 4 column grid filter modal window.
        """
        expected_label_list=['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:', 'Select North America', 'Move Slider', 'Move Slider', 'Select 2016/03/10 through 2016/03/17', 'Select 2016/03/17:']
        page_design_obj.verify_filter_control_labels(expected_label_list, "Step 14.01 : Verify filter modal appears with a 4 column grid", model_window=True)
        expected_buttons=['Submit','Reset']
        page_design_obj.verify_filter_modal_window_buttons(expected_buttons, "Step 14.02 : Submit and Reset buttons present")
        
        """
            STEP 15: Click Submit button.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 15: Verify solid red border applied to all required filter controls and filter modal window does not closed.
        """
        page_design_obj.verify_filter_dropdown_is_not_optional("Select North America", "Step 15.01 : Verify solid red border applied to 'Select North America'", model_window=True)
        page_design_obj.verify_filter_date_picker_is_not_optional("Select 2016/03/10 through 2016/03/17", "Step 15.02 : Verify solid red border applied to 'Select 2016/03/10 through 2016/03/17'", model_window=True)
        page_design_obj.verify_filter_date_picker_is_not_optional("Select 2016/03/17:", "Step 15.03 : Verify solid red border applied to 'Select 2016/03/17:'", model_window=True)
        
        """
            STEP 16 : Close filter modal window.
        """
        page_design_obj.close_filter_model_window()
        
        """
            STEP 17 : Close "C6779818" portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
            STEP 18 : Delete "C6779818" portal.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
       
if __name__ == '__main__':
    unittest.main()