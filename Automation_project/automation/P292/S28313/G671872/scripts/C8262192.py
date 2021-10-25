'''
Created on May 31, 2019.

@author: Niranjan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262192
TestCase Name = Add multiple required parameters into portal and verify filter modal window
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators import wf_mainpage_locators
from common.lib import global_variables
from common.lib.webfocus import resource_dialog
from common.wftools.page_designer import Design, Preview

class C8262192_TestClass(BaseTestCase):

    def test_C8262192(self):
        
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
        global_var_obj=global_variables.Global_variables()
        resource_dialog_obj=resource_dialog.Resource_Dialog(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)

        
        """
        COMMON TEST CASE VARIABLES 
        """
        CASE_ID     =global_var_obj.current_test_case
        PROJECT_ID  = core_util_obj.parseinitfile('project_id')
        SUITE_ID    = core_util_obj.parseinitfile('suite_id')
        GROUP_ID    = core_util_obj.parseinitfile('group_id')
        DATA_SET_NAME_1=CASE_ID + '_DataSet_01'
        DATA_SET_NAME_2=CASE_ID + '_DataSet_02'
        CONTAINER_ITEM_1='22 - Single Select Dynamic Required'
        CONTAINER_ITEM_2='28 - Multi-Select Dynamic Required'
        REPOSITORY_FOLDER = 'Domains->{0}_{1}->{2}'.format(PROJECT_ID, SUITE_ID, GROUP_ID)
        PORTAL_TITLE="C6779805"
        ACTION_TILE = 'Designer'
        ACTION_BAR  = 'Portal'
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        resource_dialog_css='.open-dialog-resources.pop-top'
        filter_window_css=".pd-filter-window"
        
        """
            STEP 01 : Login to WF as Developer.Navigate to P292_S19901/G520447 folder.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(REPOSITORY_FOLDER)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ACTION_TILE, main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 02 : Click create new V5 portal action tile under Designer.
        """
        main_page_obj.select_action_bar_tab(ACTION_TILE)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ACTION_BAR, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(ACTION_BAR)
        
        """
            STEP 03 : Enter "C6779805" in Title and check Create My Pages Menu and click Create button.
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=PORTAL_TITLE)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
            STEP 04 : Publish and Run "C6779805"" portal.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_TITLE, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Publish")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_TITLE, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Run")
        
        """
            STEP 05 : Click + button under My Pages in left Navigation bar.
        """
        core_util_obj.switch_to_new_window()
        two_level_side.click_on_plus_icon_under_the_folder_in_left_sidebar("My Pages")
        
        """
            STEP 05.01 : Verify New Page pop-up window appears.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_popup_dialog_caption("New Page", "Step 05.01 : Verify New Page pop-up window appears.")
        
        """
            STEP 06 : Select Grid 2-1 template.
        """
        template_obj.select_new_page_template('Grid 2-1')
        
        """
            STEP 06.01 : Verify page created successfully and Filter icon is not available in page toolbar.
        """
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 06.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 06.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 06.03 : Filter icon is not available in page toolbar")
        
        """
            STEP 07: Click Add content (+) in Panel 1 and Add "22 - Single Select Dynamic Required" (report with required parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        resource_dialog_obj.select_resource_from_gridview("P398_S10799", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Reference Items", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Reference Items", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "22 - Single Select Dynamic Required", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("22 - Single Select Dynamic Required")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
    
        """
            STEP 07.01 : Verify "22 - Single Select Dynamic Required" report added into panel 1 and filter modal window opens when required parameter report is added.
        """
        main_page_obj.verify_popup_dialog_caption("Selections", "Step 08.01 : Verify '22 - Single Select Dynamic Required' report added into panel 1 and filter modal window opens when required parameter report is added.")
        
        """
            STEP 08: Close filter modal window.
        """
        main_page_obj.close_view_dialog("Selections")
        
        """
            STEP 09: Click Add content (+) in Panel 2 and Add "28 - Multi-Select Dynamic Required" (report with required parameter) from P398_S10799 > Reference Items folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 2")
        resource_dialog_obj.select_crumb_item("Reference Items")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "28 - Multi-Select Dynamic Required", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("28 - Multi-Select Dynamic Required")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
        
        """
            STEP 09.01 : Verify "28 - Multi-Select Dynamic Required" report added into panel 2 and filter modal window opens when required parameter report is added.
        """
        main_page_obj.verify_popup_dialog_caption("Selections", "Step 09.01 : Verify '28 - Multi-Select Dynamic Required' report added into panel 2 and filter modal window opens when required parameter report is added.")
        
        """
            STEP 10: Click Submit button.
        """
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 10.01: Verify solid red border applied in required filter control and filter modal window does not closed.
        """
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 10.01 : Filter modal window does not closed.")
        page_designer_obj.verify_filter_dropdown_is_not_optional('Select North America', "Step 10.02 : Verify solid red border applied in required filter control 1", filter_control_position=1, model_window=True)
        page_designer_obj.verify_filter_dropdown_is_not_optional('Select North America', "Step 10.03 : Verify solid red border applied in required filter control 2",filter_control_position=2, model_window=True)
        
        """
            STEP 11: Select "North America" in first dropdown control and click Submit button.
        """
        option_list_to_select=["North America"]
        page_preview_obj.select_filter_dropdown_option('Select North America', option_list_to_select, model_window=True)
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 11.01 : Verify filter modal window does not closed.
        """
        main_page_obj.verify_popup_dialog_is_displayed(True, "Step 11.01 : Verify filter modal window does not closed.")
        
        """
            Step 12: Select "EMEA" and "North America" values in required dropdown control and click Submit button.
        """
        option_list_to_select=["EMEA","North America"]
        page_preview_obj.select_filter_dropdown_option('Select North America', option_list_to_select, filter_control_position=2, model_window=True)
        filter_window_elem=util_obj.validate_and_get_webdriver_object(filter_window_css, "filter_window_css")
        core_util_obj.python_left_click(filter_window_elem)
        main_page_obj.click_button_on_popup_dialog("Submit")
        
        """
            STEP 12.01 : Verify filter modal window closed and selected conditions applied in the page.
        """
        main_page_obj.verify_popup_dialog_is_displayed(False, "Step 12.01 : Verify filter modal window closed")
        
        page_preview_obj.switch_to_container_frame(CONTAINER_ITEM_1)
        page_preview_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='North America', time_out=page_designer_obj.home_page_medium_timesleep)
#         page_designer_obj.create_html_report_data_set(DATA_SET_NAME_1)
        page_preview_obj.verify_html_report_data_set(DATA_SET_NAME_1, 'Step 12.02 : Verify selected condition applied in Panel 1.')
        page_preview_obj.switch_to_default_page()
        
        page_preview_obj.switch_to_container_frame(CONTAINER_ITEM_2)
        page_preview_obj.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=page_designer_obj.home_page_medium_timesleep)
#         page_designer_obj.create_html_report_data_set(DATA_SET_NAME_2)
        page_preview_obj.verify_html_report_data_set(DATA_SET_NAME_2, 'Step 12.03 : Verify selected condition applied in Panel 2.')
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 13 : Close "C6779805" portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
            STEP 14 : Delete "C6779805" portal.
        """
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
        
        """
            STEP 15 : Sign out WF.
        """
       
if __name__ == '__main__':
    unittest.main()