'''
Created on May 28, 2019.

@author: Niranjan_Das

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262062
TestCase Name = Maximize Container with OverFlow
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design,Run
from common.lib import global_variables

class C8262062_TestClass(BaseTestCase):

    def test_C8262062(self):
        
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
        global_var_obj=global_variables.Global_variables()
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        case_id     =global_var_obj.current_test_case
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        
        
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
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Tab", 1)
        
        """
        Step 7:Add 8 more tabs to panel1 by clicking on Add new tab icon
        """
        for _ in range(4):            
            page_designer_obj.tab_container("Panel 1").click_new_tab_plus_icon()
        for _ in range(4):
            page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
            page_designer_obj.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
            
        """
        Step 8: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 8.01:Verify all Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8 appears and Tab 9 is in bold with a + button
        """
        expected_tabs_list=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6', 'Tab 7', 'Tab 8', 'Tab 9']
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "08.01")
        page_designer_obj.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 9"], "08.02")
        page_designer_obj.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("08.03")
        
        """
        Step 09: Click the Preview button
        """
        page_designer_obj.click_preview()
        
        """
        Step 10: Maximize Panel1
        """
        page_designer_obj.tab_container("Panel 1").maximize()
        
        """
        Step 10.01: Verify ellipsis does not appears as all the tabs can be displayed
        """
        page_designer_obj.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("10.01")
        
        """
        Step 11:Resize the browser
        """
        page_designer_obj.tab_container("Panel 1").minimize()
        
        """
        Step 11.01: Verify ellipsis now appears
        """
        page_designer_obj.tab_container("Panel 1").verify_tab_overflow_icon_displayed("11.01")
        
        """
        Step 12: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 12.01:Verify user can see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8, Tab9 and NO + sign as the panel is locked.
        """
        expected_tabs_list=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6', 'Tab 7', 'Tab 8', 'Tab 9']
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "12.01")
        page_designer_obj.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("12.02")
        
        """
        Step 13:Resize the browser
        """
        page_designer_obj.tab_container("Panel 1").maximize()
        
        """
        Step 13.01: Verify ellipsis does not appears as all the tabs can be displayed
        """
        page_designer_obj.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("13.01")
        
        """
        Step 14: Close the Preview
        """
        page_run_obj.go_back_to_design_from_preview()
        
        """
        Step 15: Save page as 'C8262062' and close Designer
                 Verify the page appears in the content area
        """
        page_designer_obj.save_page_from_toolbar(case_id)
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 15.01: Verify 'C8262062' page appears in the content area
        """
        core_util_obj.switch_to_previous_window(False)
        main_page_obj.verify_items_in_grid_view([case_id], 'asin', "Step 15.01: ")
        
        """
        Step 16: Right click on 'C8262062' and select Run in new window
        """
        main_page_obj.right_click_folder_item_and_select_menu(case_id,"Run in new window")
        core_util_obj.switch_to_new_window()
        
        """
        Step 17: Maximize Panel1
        """
        page_designer_obj.tab_container("Panel 1").maximize()
        
        """
        Step 17.01: Verify ellipsis does not appears as all the tabs can be displayed
        """
        page_designer_obj.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("17.01")
        
        """
        Step 18:Resize the browser
        """
        page_designer_obj.tab_container("Panel 1").minimize()
        
        """
        Step 19: Click on the Overflow icon (Ellipsis)
        """
        page_designer_obj.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
        Step 19.01:Verify user can see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8, Tab9 and NO + sign as the panel is locked.
        """
        expected_tabs_list=['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6', 'Tab 7', 'Tab 8', 'Tab 9']
        page_designer_obj.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(expected_tabs_list, "19.01")
        page_designer_obj.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("19.02")
        
        """
        Step 20:Resize the browser
        """
        page_designer_obj.tab_container("Panel 1").maximize()
        
        """
        Step 20.01: Verify ellipsis does not appears as all the tabs can be displayed
        """
        page_designer_obj.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("20.01")

        """
        Step 21: close page in new window
        """
        core_util_obj.switch_to_previous_window()
      
        """
        Step 22: Signout WF
        """ 
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()