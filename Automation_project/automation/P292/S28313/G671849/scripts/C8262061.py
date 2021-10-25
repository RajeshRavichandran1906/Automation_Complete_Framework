'''
Created on May 27, 2019.

@author: Niranjan_Das

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262061
TestCase Name = Page Designer with Unlocked Tab Container
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib.webfocus import resource_dialog
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Run
from common.lib import global_variables
import time

class C8262061_TestClass(BaseTestCase):

    def test_C8262061(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_run_obj=Run(self.driver)
        resource_dialog_obj=resource_dialog.Resource_Dialog(self.driver)
        global_var_obj=global_variables.Global_variables()
        
        """
        TESTCASE CSS
        """
        pop_top_css        = ".pop-top"
        containers_css     =".ibx-csl-items-container [title='Containers']"
        resource_dialog_css='.open-dialog-resources.pop-top'
        
        """
        TESTCASE VARIABLES
        """
        case_id           =global_var_obj.current_test_case
        project_id        = core_util_obj.parseinitfile('project_id')
        suite_id          = core_util_obj.parseinitfile('suite_id')
        group_id          = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Workspaces->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile       = 'Designer'
        action_bar        = 'Page'
        
        
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
        Step 3: Click on 'P292_S28313' domain -> G671849 folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 5: Choose the Blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Drag a tab container onto the page;
                Add 4 more tabs to the same panel
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Tab", 1)
        for _ in range(4):
            page_designer_obj.tab_container("Panel 1").click_new_tab_plus_icon()
        
        """
        Step 6.01:Verify Panel 1 has 5 tabs as shown below
        """
        expected_tabs_list=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5']
        page_designer_obj.tab_container("Panel 1").verify_tabs(expected_tabs_list,"06.01")
        
        """
        Step 7: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
            
        """
        Step 7.01:Verify Tab1, Tab2, Tab3, Tab4 and Tab5 are listed as below
        """
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "07.01")
        
        """
        Step 8: Click the + button
        """
        page_designer_obj.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        """
        Step 8.01: Verify Tab 6 is added
        """
        expected_tabs_list=['Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6']
        page_designer_obj.tab_container("Panel 1").verify_tabs(expected_tabs_list, "08.01")
        
        """
        Step 9: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 9.01: Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 and the + sign
        """
        expected_tabs_list=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6']
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "09.01")
        page_designer_obj.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("09.02")
        
        """
        Step 10: Click the Preview button
        """
        page_designer_obj.click_preview()
        
        """
        Step 11: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 11.01: Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 but NO + sign because the panel is locked.
        """
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "11.01")
        page_designer_obj.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("11.02")
        
        """
        Step 12: Click on Tab 1
        """
        page_designer_obj.tab_container("Panel 1").select_tab("Tab 1")
        
        """
        Step 12.01: Verify Tab 1 is now in View
        """
        page_designer_obj.tab_container("Panel 1").verify_selected_tab(['Tab 1'], "12.01")
        
        """
        Step 13: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 13.01: Verify that Tab1 is in bold
        """
        page_designer_obj.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(['Tab 1'], "13.01")
        
        """
        Step 14: Close the Preview
        """
        page_run_obj.go_back_to_design_from_preview()
        """
        Step 15:Select Panel1 and click open the properties pane
        """
        page_designer_obj.select_container("Panel 1")
        page_designer_obj.click_property()
        
        """
        Step 16:In the content customization section Turn off Lock Content switch
        """
        check_box_objs=util_obj.validate_and_get_webdriver_objects("div[data-ibx-type='ibxGrid']>div[class^='pd-ps'][role='checkbox']", "Check box objects")
        lock_content=check_box_objs[3]
        core_util_obj.left_click(lock_content)      
        """
        Step 16.01:Verify that now all the items under that section are enabled;
        Verify that now You see a + in the middle of each tab
        """
        page_designer_obj.tab_container("Panel 1").verify_add_content_button_displayed("16.01")
        
        """
        Step 17:Hover over + sign
        Verify 'Add Content' tool tip appears
        """        
        add_button_obj = self.driver.find_element_by_css_selector(".cont-es-button" )
        add_button_obj_text = add_button_obj.get_attribute('title')
        util_obj.asequal(add_button_obj_text,'Add content',"step:17 Verify 'Add Content' tool tip appears")
        
        """
        Step 18:Go to Preview
        """
        page_designer_obj.click_preview()
        
        """
        Step 19:Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 19.01:Verify that Tab1 is in bold and you see a + sign at the bottom
        """
        page_designer_obj.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 1"], "19.01")
        page_designer_obj.tab_container("Panel 1").verify_add_content_button_displayed("19.02")      
        
        """
        Step 20: Click the + button in the middle of panel 1
        """
        page_designer_obj.tab_container("Panel 1").click_add_content_button()
        page_designer_obj.wait_for_visible_text("div.ibx-dialog-cancel-button", "Cancel")
        
        """
        Step 20.01: Verify Select Item dialog opens with Domains open
        """
        resource_dialog_obj.verify_resource_dialog_is_visible(True, "Step 20.01 : Verify Select Item dialog opens with Domains open")
        
        """
        Step 21: Navigate to Retail Samples --> Portal --> Small widget.Choose 'Category sales'
        """
        resource_dialog_obj.select_resource_from_gridview("Retail Samples", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Portal", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Portal", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Small Widgets", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Small Widgets", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Category Sales", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Category Sales")
        """
        Step 22:Click the Add button
        """
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
        time.sleep(20)
        
        """
        Step 22.01:Verify that the report appears and now the quick filter icon appeared next to refresh
        """
        expected_tabs_list=['Category Sales', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5']
        page_designer_obj.tab_container("Panel 1").verify_tabs(expected_tabs_list, "22.01")
        page_designer_obj.verify_page_header_visible_buttons(['Refresh', 'Show filters'], "Step 22.02 : quick filter icon appeared next to refresh")
        
        """
        Step 23: Click on back to get back to page design mode
        """
        page_run_obj.go_back_to_design_from_preview()
        
        """
        Step 24: Save page as 'C8262061' and close Designer
                 Verify the page appears in the content area
        """
        page_designer_obj.save_page_from_toolbar(case_id)
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 24.01: Verify the page appears in the content area
        """
        core_util_obj.switch_to_previous_window(False)
        util_obj.synchronize_with_visble_text(locator_obj.CONTENT_CSS, "Content", main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_items_in_grid_view([case_id], 'asin', "Step 24.01 : ")
        
        """
        Step 25: Right click on 'C8262061' and select Run in new window
                 Verify the page appears and you see the overflow icon at the top right corner
        """
        main_page_obj.right_click_folder_item_and_select_menu(case_id,"Run in new window")
        
        """
        Step 25.01: Verify the page appears and you see the overflow icon at the top right corner
        """
        core_util_obj.switch_to_new_window()
        time.sleep(10)
        page_run_obj.tab_container("Panel 1").verify_tab_overflow_icon_displayed("25.01")
        
        """
        Step 26: Click on the Overflow icon (Ellipsis)
        """
        page_run_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 26.01: Verify that 'Category Sales' is in bold and + button appears
        """
        page_run_obj.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(['Category Sales'], "26.01")
        
        """
        Step 27: Click on Tab2
        """
        page_run_obj.tab_container("Panel 1").select_tab("Tab 2")
        
        """
        Step 28: Click the + button in the middle of panel 1
        """
        page_designer_obj.tab_container("Panel 1").click_add_content_button()
        
        """
        Step 29: Navigate to 'Retail Samples' --> Portal --> Small widget , Select 'Regional sales trend' and click on Add button
        """
        resource_dialog_obj.select_resource_from_gridview("Retail Samples", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Portal", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Portal", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Small Widgets", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Small Widgets", "double")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Regional Sales Trend", main_page_obj.home_page_medium_timesleep)
        resource_dialog_obj.select_resource_from_gridview("Regional Sales Trend")
        util_obj.synchronize_with_visble_text(resource_dialog_css, "Add", main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog("Add")
        
        """
        Step 29.01: Verify 'Regional sales trend' has been added
        """
        expected_tabs_list=['Category Sales', 'Regional Sales Trend', 'Tab 3']
        page_designer_obj.tab_container("Panel 1").verify_tabs(expected_tabs_list, "29.01")
        
        """
        Step 30: close page in new window
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.CONTENT_CSS, "Content", main_page_obj.home_page_long_timesleep)
      
        """
        Step 31: Signout WF
        """ 
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()