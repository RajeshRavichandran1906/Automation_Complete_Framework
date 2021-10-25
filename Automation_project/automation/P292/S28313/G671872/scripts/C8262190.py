'''
Created on June 03, 2019.

@author: Varun/Prasanth

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262190
TestCase Name = Add optional parameters into portal and verify filter modal window 
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators import wf_mainpage_locators
from common.wftools import chart
from common.wftools.page_designer import Design,Preview
from common.locators.portal_designer import Vfive_Designer

class C8262190_TestClass(BaseTestCase):

    def test_C8262190(self):
        
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
        chart_obj=chart.Chart(self.driver)
        page_design_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        vfive_obj = Vfive_Designer()

        
        """
        COMMON TEST CASE VARIABLES 
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Portal'
        portal_title="C6779535"
        
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
            STEP 03 : Enter "C6779535" in Title and check Create My Pages Menu and click Create button.
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_title)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
            STEP 04 : Publish and Run "C6779535" portal.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Publish")
        main_page_obj.verify_content_area_folder_publish_or_unpublish(portal_title, "publish", 'Step 4: Verify {0} is published.'.format(portal_title))
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Run")
        
        """
            STEP 05 : Click + button under My Pages in left Navigation bar.
        """
        core_util_obj.switch_to_new_window()
        two_level_side.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        
        """
            STEP 05.01 : Verify New Page pop-up window appears.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_popup_dialog_caption("New Page", "Step 05.01 : Verify New Page pop-up window appears.")
        
        """
            STEP 06 : Select Grid 2-1 template.
        """
        template_obj.select_new_page_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(vfive_obj.page_header_css, main_page_obj.home_page_long_timesleep)
        
        """
            STEP 06.01 : Verify page created successfully and Filter icon is not available in page toolbar.
        """
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 06.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 06.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 06.03 : Filter icon is not available in page toolbar")
        
        """
            STEP 07: Click Add content (+) in Panel1
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        
        """
            Step 08: Select "Category Sales" (report with parameters) from Retail Samples > Portal > Small Widgets folder.
            click Add button.
        """
        page_design_obj.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        page_design_obj.resource_dialog().click_button("Add")
        
        """
            STEP 08.01 : Verify "Category Sales" report added into panel 1.
            Filter icon is visible in the page toolbar when report with parameters are added.
        """
        expected_containers_title=['Category Sales']
        portal_canvas_obj.verify_specific_containers_title(expected_containers_title, "Step 08.01 : Verify 'Category Sales' report added in panel 1")
        expected_buttons_list=['Maximize', 'Options']
        portal_canvas_obj.verify_container_title_bar_all_buttons("Category Sales", expected_buttons_list, "Step 08.02 : Verify Container title bar buttons")
        expected_buttons_name_list=['Share', 'Refresh', 'Show filters', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 08.03 : Filter icon is visible in the page toolbar")
        
        portal_canvas_obj.switch_to_panel_frame('Category Sales')
        expected_label_list=['Revenue', '1.1B', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="Step 08.04 : Verify 'Category Sales' report added into panel 1")
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 09 : Click Show filters icon in toolbar.
        """
        page_preview_obj.click_show_filters()
        
        """
            STEP 09.01 : Verify filter modal appears with a 4 column grid.
            And with Submit and Reset buttons present at lower right corner of the filter modal window.
        """
        expected_label_list=['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:']
        page_design_obj.verify_filter_control_labels(expected_label_list, "Step 09.01 : Verify filter modal appears with a 4 column grid", model_window=True)
        expected_buttons=['Submit','Reset']
        page_design_obj.verify_filter_modal_window_buttons(expected_buttons, "Step 09.02 : Submit and Reset buttons present")
        
        """
            STEP 10 : Click on Region: dropdown and select "North America" value.
        """
        option_list_to_select=["North America"]
        page_preview_obj.select_filter_dropdown_option("Region:", option_list_to_select, model_window=True)
        
        """
            STEP 10.01 : Verify Category Sales report in panel 1 does not updated.
        """
        portal_canvas_obj.switch_to_panel_frame('Category Sales')
        expected_label_list=['Revenue', '1.1B', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="Step 10.01 : Verify Category Sales report in panel 1 does not updated.")
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 11: Click Submit button.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 11.01: Verify "Category Sales" report updated with selected condition.
        """
        portal_canvas_obj.switch_to_panel_frame('Category Sales')
        expected_label_list=['Revenue', '609.9M', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="Step 11.01 : Verify 'Category Sales' report updated with selected condition")
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 12 : Close "C6779535" portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
            STEP 13 : Delete "C6779535" portal.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
       
if __name__ == '__main__':
    unittest.main()