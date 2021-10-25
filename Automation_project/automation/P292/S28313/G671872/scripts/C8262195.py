'''
Created on Jun 4, 2019

@author: Aftab/Rajesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/21055115
Test Case Name = Create multiple personal pages with parameters
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.wftools import designer_portal
from common.wftools import page_designer
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators import wf_mainpage_locators
from common.lib import global_variables
from common.lib.webfocus import resource_dialog
from common.wftools import chart
from common.wftools.page_designer import Preview
import time


class C8262195_TestClass(BaseTestCase):

    def test_C8262195(self):
        
        """
        CLASS OBJECTS 
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        two_level_side = designer_portal.Two_Level_Side(self.driver)
        template_obj = designer_portal.New_Page_Template_Window(self.driver)
        portal_canvas_obj = designer_portal.Canvas(self.driver)
        global_var_obj = global_variables.Global_variables()
        page_designer_design = page_designer.Design(self.driver)
        page_designer_preview = page_designer.Preview(self.driver)
        resource_dialog_obj = resource_dialog.Resource_Dialog(self.driver)
        chart_obj=chart.Chart(self.driver)
        page_preview_obj = Preview(self.driver)
        
        """
        COMMON TEST CASE VARIABLES 
        """
        case_id     = global_var_obj.current_test_case
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Portal'
        DATA_SET_NAME1 = case_id + '_DataSet_01'
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        page_heading_css = ".pd-page-runner:not([style*='none']) div[class^='pd-page-title ibx']"
        submit_css = ".pd-filter-window.pop-top"
        filter_window_css = ".pd-filter-window"
        category_sales_css = "#jschart_HOLD_0"
        
        """
            STEP 1 : Login to WF as Developer.Navigate to P292_S19901/G520447 folder.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_short_timesleep)
        
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)

        """
            STEP 2 : Click create new V5 portal action tile under Designer.
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_short_timesleep)
        
        main_page_obj.select_action_bar_tabs_option(action_bar)

        """
            STEP 3 : Enter "C6779831" in Title and check Create My Pages Menu and click Create button.
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        PORTAL_TITLE="C6779831"
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=PORTAL_TITLE)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
 
        """
            STEP 4 : Publish and Run "C6779831" portal.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_TITLE, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Publish")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_TITLE, main_page_obj.home_page_short_timesleep)
        time.sleep(5)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Run")

        """
            STEP 5 : Click + button under My Pages in left Navigation bar.
        """
        core_util_obj.switch_to_new_window()
        two_level_side.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_short_timesleep)
        
        """
            STEP 5.01 : Verify New Page pop-up window appears.
        """
        main_page_obj.verify_popup_dialog_caption("New Page", "Step 05.01 : Verify New Page pop-up window appears.")
        
        """
            STEP 6 : Select Grid 2-1 template.
        """
        template_obj.select_new_page_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 6.01 : Verify page created successfully and Filter icon is not available in the page toolbar.
        """
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 06.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 06.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 06.03 : Filter icon is not available in page toolbar")

        """
            STEP 7 : Click Add content (+) in Panel 1 and Add "Category Sales" (report with parameters) from Retail Samples > Portal > Small Widgets folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        page_designer_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        page_designer_design.resource_dialog().click_button("Add")
        page_designer_design.switch_to_container_frame("Category Sales")
        util_obj.synchronize_with_visble_text(category_sales_css, "Revenue", main_page_obj.home_page_medium_timesleep)
        page_designer_design.switch_to_default_page()
    
        """
            STEP 7.01 : Verify filter icon appears in page toolbar.
        """
        expected_buttons_name_list=['Share', 'Refresh', 'Show filters', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "STEP 7.01 : Verify filter icon appears in page toolbar")

        """
            STEP 8 : Click Add content (+) in Panel 2 and Add "28 - Multi-Select Dynamic Required" (report with required parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 2")
        resource_dialog_obj.select_crumb_item("Domains")
        page_designer_design.resource_dialog().navigate_to_folder_and_select_file("P398_S10799->Reference Items", "28 - Multi-Select Dynamic Required")
        page_designer_design.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(submit_css, "Submit", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 8.01 : Verify "28 - Multi-Select Dynamic Required" report added into panel 2 and filter modal window opens when required parameter report is added.
        """
        page_designer_design.verify_filter_control_labels(["Category:", "Product Model:", "Region:", "Store Type:", "From:", "To:", "Select North America"], "STEP 08.01 : Filter modal window opens when required parameter report is added.", model_window=True)
        
        """
            STEP : 9 Close filter modal window.
        """
        page_designer_design.close_filter_model_window()
        expected_containers_title = ["28 - Multi-Select Dynamic Required"]
        portal_canvas_obj.verify_specific_containers_title(expected_containers_title, "STEP 08.02 : Verify '28 - Multi-Select Dynamic Required' report added into panel 1")
        
        """
            STEP 10 : Click + button under My Pages in left Navigation bar and select Grid 2-1 template.
        """
        two_level_side.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_short_timesleep)
        
        template_obj.select_new_page_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(page_heading_css,"Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 10.01 :Verify page created successfully and Filter icon is not available in the page toolbar.
        """
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 10.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 10.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 10.03 : Filter icon is not available in page toolbar")
        
        """
            STEP 11 : Click Add content (+) in Panel 1 and Add "Category Sales" (report with parameters) from Retail Samples > Portal > Small Widgets folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        resource_dialog_obj.select_crumb_item("Domains")
        page_designer_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        page_designer_design.resource_dialog().click_button("Add")
        portal_canvas_obj.switch_to_panel_frame("Category Sales")
        util_obj.synchronize_with_visble_text(category_sales_css, "Revenue", main_page_obj.home_page_medium_timesleep)
        page_designer_design.switch_to_default_page()
        
        """
            STEP 11.01 : Verify filter icon appears in page toolbar.
        """
        expected_buttons_name_list=['Share', 'Refresh', 'Show filters', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "STEP 11.01 : Verify filter icon appears in page toolbar")
        
        """
            STEP 12 : Click Add content (+) in Panel 2 and Add "28 - Multi-Select Dynamic Required" (report with required parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 2")
        resource_dialog_obj.select_crumb_item("Domains")
        page_designer_design.resource_dialog().navigate_to_folder_and_select_file("P398_S10799->Reference Items", "28 - Multi-Select Dynamic Required")
        page_designer_design.resource_dialog().click_button("Add")
        util_obj.synchronize_with_visble_text(submit_css, "Submit", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 12.01 : Verify "28 - Multi-Select Dynamic Required" report added into panel 2 and filter modal window opens when required parameter report is added.
        """
        page_designer_design.verify_filter_control_labels(["Category:", "Product Model:", "Region:", "Store Type:", "From:", "To:", "Select North America"], "STEP 12.01 : Filter modal window opens when required parameter report is added.", model_window=True)
        
        """
            STEP 13 : Click Submit button.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 13.01 : Verify solid red border applied in required filter control and filter modal window does not closed.
        """
        page_designer_design.verify_filter_dropdown_is_not_optional("Select North America", "STEP 13.01 : Verify solid red border applied in required filter control and filter modal window does not closed.", model_window=True)
        
        """
            STEP 14 : Select "Camcorder" and "Computers" in Category: filter control and select "North America" value in "Select North America" dropdown control and click Submit button.
        """
        page_designer_preview.select_multiple_options_from_filter_dropdown('Category:', ['Camcorder', 'Computers'], model_window=True)
        page_designer_preview.select_filter_dropdown_option("Select North America", ["North America"], model_window=True)
        filter_window_elem=util_obj.validate_and_get_webdriver_object(filter_window_css, "filter_window_css")
        core_util_obj.python_left_click(filter_window_elem)
        main_page_obj.click_button_on_popup_dialog("Submit")
        portal_canvas_obj.switch_to_panel_frame("Category Sales")
        util_obj.synchronize_with_visble_text(category_sales_css, "Revenue", main_page_obj.home_page_medium_timesleep)
        page_designer_design.switch_to_default_page()
        
        """
            STEP 14.01 : Verify selected condition applied in the page.
        """
        portal_canvas_obj.switch_to_panel_frame('Category Sales')
        expected_label_list=['Revenue', '257.8M', 'Product Category', 'Camcorder', 'Computers']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="STEP 14.01 : Verify selected condition applied in the page.")
        page_preview_obj.switch_to_default_page()
        
        portal_canvas_obj.switch_to_panel_frame("28 - Multi-Select Dynamic Required")
        page_designer_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", "North America", main_page_obj.home_page_short_timesleep)
        #page_designer_design.create_html_report_data_set(DATA_SET_NAME1)
        page_designer_design.verify_html_report_data_set(DATA_SET_NAME1, "STEP 14.02 : Verify selected condition applied in the page.")
        page_designer_design.switch_to_default_page()
        
        """
            STEP 15 : Click Filter icon and click Reset button.
        """
        portal_canvas_obj.click_show_filters()
        main_page_obj.click_button_on_popup_dialog("Reset")
        time.sleep(15)
        
        """
            STEP 15.01 : Verify selected values in filter controls are reset back to its original state.
        """
        page_designer_preview.verify_selected_value_of_filter_dropdown("Category:", ["All"], "STEP 15.01 : Verify selected values in filter controls are reset back to its original state.", model_window=True)
        page_designer_preview.verify_selected_value_of_filter_dropdown("Select North America", ["Make a selection..."], "STEP 15.02 : Verify selected values in filter controls are reset back to its original state.", model_window=True)
        
        """
            STEP 16 : Close "C6779831" portal.
        """
        core_util_obj.switch_to_previous_window()
 
        """
            STEP 17 : Delete "C6779831" portal.
        """
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
        
        """
            STEP 18 : Sign out WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 