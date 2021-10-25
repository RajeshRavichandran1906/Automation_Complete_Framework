'''
Created on May 30, 2019.

@author: Niranjan

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262189
TestCase Name = Create new Personal page and add a report with optional parameter
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.wftools import designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators import wf_mainpage_locators
from common.lib.webfocus import resource_dialog
from common.wftools import chart
from common.wftools.page_designer import Preview
from common.locators.portal_designer import Vfive_Designer

class C8262189_TestClass(BaseTestCase):

    def test_C8262189(self):
        
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
        resource_dialog_obj=resource_dialog.Resource_Dialog(self.driver)
        chart_obj=chart.Chart(self.driver)
        page_preview_obj = Preview(self.driver)

        
        """
        COMMON TEST CASE VARIABLES 
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Portal'
        PORTAL_TITLE = "C6779514"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        resource_dialog_css='.open-dialog-resources.pop-top'
        
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
        portal_obj.delete_portal_if_exists(PORTAL_TITLE)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
            STEP 03 : Enter "C6779514" in Title and check Create My Pages Menu and click Create button.
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.NEW_PORTAL_CREATE_BTN_CSS, 'Create', Global_variables.longwait)
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=PORTAL_TITLE)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
            STEP 04 : Publish and Run "C6779514" portal.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, PORTAL_TITLE, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Publish")
        main_page_obj.verify_content_area_folder_publish_or_unpublish(PORTAL_TITLE, "publish", 'Step 4: Verify {0} is published.'.format(PORTAL_TITLE))
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Run")
        
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
        util_obj.synchronize_with_visble_text(Vfive_Designer.page_header_css, "Page Heading", main_page_obj.home_page_long_timesleep)
        
        """
            STEP 06.01 : Verify page created successfully and Filter icon is not available in page toolbar.
        """
        portal_canvas_obj.verify_page_header_title("Page Heading", "Step 06.01 : Verified Page Header")
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_canvas_obj.verify_all_containers_title(expected_containers_title, "Step 06.02 : Verify all containers titles.")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 06.03 : Filter icon is not available in page toolbar")
        
        """
            STEP 07: Click Add content (+) in Pan
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 1")
        util_obj.synchronize_with_visble_text(resource_dialog_obj.resource_dialog_css, 'Retail Samples', main_page_obj.home_page_long_timesleep)
        
        """
            Step 08: Select "Arc - Sales by Region" (report without parameters) from Retail Samples > Charts folder and click Add.
        """
        resource_dialog_obj.select_resource_from_gridview("Retail Samples", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Charts", main_page_obj.home_page_short_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Charts", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Arc - Sales by Region", main_page_obj.home_page_short_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Arc - Sales by Region")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_short_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
    
        """
            STEP 08.01 : Verify "Arc - Sales by Region" report added in panel 1 and Filter icon not visible in page toolbar.
        """
        expected_containers_title=['Arc - Sales by Region']
        portal_canvas_obj.verify_specific_containers_title(expected_containers_title, "Step 08.01 : Verify 'Arc - Sales by Region' report added in panel 1")
        expected_buttons_list=['Maximize', 'Options']
        portal_canvas_obj.verify_container_title_bar_all_buttons("Arc - Sales by Region", expected_buttons_list, "Step 08.02 : Verify Container title bar buttons")
        expected_buttons_name_list=['Share', 'Refresh', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 08.03 : Filter icon is not available in page toolbar")
        
        portal_canvas_obj.switch_to_panel_frame('Arc - Sales by Region')
        expected_label_list=['$0.00', '$50,000,000.00', '$100,000,000.00', '$150,000,000.00', '$200,000,000.00', '$250,000,000.00', '$300,000,000.00', '$350,000,000.00', '$400,000,000.00', '$450,000,000.00', '$500,000,000.00', '$550,000,000.00', '$600,000,000.00', 'Oceania', 'South America', 'EMEA', 'North America']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="Step 08.04 : Verify x and y lables in Panel 1")
        page_preview_obj.switch_to_default_page()
        portal_canvas_obj
        
        """
            Step 09: Click Add content (+) in Panel 2 and Add "Category Sales" (report with parameters) from Retail Samples > Portal > Small Widgets folder.
        """
        portal_canvas_obj.click_on_panel_add_content_button_in_container("Panel 2")
        util_obj.synchronize_with_visble_text(resource_dialog_obj.resource_dialog_css, 'Retail Samples', main_page_obj.home_page_long_timesleep)
        resource_dialog_obj.select_crumb_item("Retail Samples")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Portal", main_page_obj.home_page_short_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Portal", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Small Widgets", main_page_obj.home_page_short_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Small Widgets", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Category Sales", main_page_obj.home_page_short_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Category Sales")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_short_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
        
        """
            STEP 09.01 : Verify "Category Sales" report added to panel 2 and Filter icon is visible in the page toolbar when report with parameters are added.
        """
        expected_containers_title=['Category Sales']
        portal_canvas_obj.verify_specific_containers_title(expected_containers_title, "Step 09.01 : Verify 'Category Sales' report added to panel 2")
        expected_buttons_list=['Maximize', 'Options']
        portal_canvas_obj.verify_container_title_bar_all_buttons('Category Sales', expected_buttons_list, "Step 09.02 : Verify Container title bar buttons")
        expected_buttons_name_list=['Share', 'Refresh', 'Show filters', 'Delete']
        portal_canvas_obj.verify_page_header_all_buttons(expected_buttons_name_list, "Step 09.03 : Filter icon is visible in the page toolbar when report with parameters are added.")
        
        portal_canvas_obj.switch_to_panel_frame('Category Sales')
        expected_label_list=['Revenue', '1.1B', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_label_list, xyz_axis_label_css="text", msg="Step 09.04 : Verify All the lables in Panel 1")
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 10 : Close "C6779514" portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
            STEP 11 : Delete "C6779514" portal.
        """
        main_page_obj.right_click_folder_item_and_select_menu(PORTAL_TITLE, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
       
if __name__ == '__main__':
    unittest.main()