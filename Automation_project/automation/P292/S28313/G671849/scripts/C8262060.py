'''
Created on May 24, 2019.

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262060
TestCase Name = Page Designer with Locked Tab Container
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview, Run
from common.lib.global_variables import Global_variables

class C8262060_TestClass(BaseTestCase):

    def test_C8262060(self):
        
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
        page_run_obj = Run(self.driver)
        glob_variable = Global_variables()
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar = 'Page'
        
        
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
                Verify Panel 1 has 5 tabs as shown below
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Tab", 1)
        for i in range(1, 5):
            page_designer_obj.tab_container('Panel 1').click_new_tab_plus_icon()
        del i
        page_designer_obj.tab_container('Panel 1').verify_tabs(['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5'], '06.00')
         
        """
        Step 7: Click on the Overflow icon (Ellipsis)
                Verify Tab1, Tab2, Tab3, Tab4 and Tab5 are listed as below
        """
        page_designer_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_designer_obj.tab_container('Panel 1').verify_tabs_in_tab_overflow_popup(['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5'], '07.00')
         
        """
        Step 8: Click the + button
                Verify Tab 6 is added
        """
        page_designer_obj.tab_container('Panel 1').click_new_tab_plus_icon_in_tab_overflow_popup()
        page_designer_obj.tab_container('Panel 1').verify_tabs(['Tab 6'], '08.00', compare_type='asin')
         
        """
        Step 9: Click on the Overflow icon (Ellipsis)
                Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 and the + sign
        """
        page_designer_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_designer_obj.tab_container('Panel 1').verify_tabs_in_tab_overflow_popup(['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6'], '09.00')
        page_designer_obj.tab_container('Panel 1').verify_new_tab_plus_icon_displayed_in_tab_overflow_popup('09.01')
         
        """
        Step 10: Click the Preview button
        """
        page_designer_obj.click_preview()
         
        """
        Step 11: Click on the Overflow icon (Ellipsis)
                 Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 but NO + sign because the panel is locked.
        """
        page_preview_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_preview_obj.tab_container('Panel 1').verify_tabs_in_tab_overflow_popup(['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6'], '11.00')
        page_preview_obj.tab_container('Panel 1').verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup('11.01')
         
        """
        Step 12: Click on Tab 1
                 Verify Tab 1 is now in View
        """
        page_preview_obj.tab_container('Panel 1').select_tab_from_tab_overflow_popup('Tab 1')
        page_preview_obj.tab_container('Panel 1').verify_selected_tab(['Tab 1'], '12.00')
         
        """
        Step 13: Click on the Overflow icon (Ellipsis)
                 Verify that Tab1 is in bold
        """
        page_preview_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_preview_obj.tab_container('Panel 1').verify_selected_tab_in_tab_overflow_popup(['Tab 1'], '13.00')
         
        """
        Step 14: Close the Preview
        """
        page_preview_obj.go_back_to_design_from_preview()
         
        """
        Step 15: Save page as 'C8262060' and close Designer
                 Verify the page appears in the content area
        """
        page_designer_obj.save_page_from_toolbar(glob_variable.current_test_case)
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, glob_variable.current_test_case, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([glob_variable.current_test_case], 'asin', 'Step 16.00 : Verify the page appears in the content area')
         
        """
        Step 16: Right click on 'C8262060' and select Run
                 Verify the page appears and you see the overflow icon at the top right corner
        """
        page_designer_obj.run_page_designer(glob_variable.current_test_case)
        page_run_obj.swtich_to_homepage_runwindow_frame()
        page_run_obj.verify_page_heading_title(['Page Heading'], 'Step 16.00 : Verify the page appears.')
        page_run_obj.tab_container('Panel 1').verify_tab_overflow_icon_displayed('16.01')
         
        """
        Step 17: Click on the Overflow icon (Ellipsis)
                 Verify that Tab1 is in bold and NO + button
        """
        page_run_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_run_obj.tab_container('Panel 1').verify_selected_tab_in_tab_overflow_popup(['Tab 1'], '17.00')
        page_run_obj.tab_container('Panel 1').verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup('17.01')
         
        """
        Step 18: Choose Tab 4
                 Verify Tab 4 is now in view
        """
        page_run_obj.tab_container('Panel 1').select_tab_from_tab_overflow_popup('Tab 4')
        page_run_obj.tab_container('Panel 1').verify_selected_tab(['Tab 4'], '18.00')
         
        """
        Step 19: Click on the Overflow icon (Ellipsis)
                 Verify that Tab 4 is in bold and NO + button
        """
        page_run_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_run_obj.tab_container('Panel 1').verify_selected_tab_in_tab_overflow_popup(['Tab 4'], '19.00')
        page_run_obj.tab_container('Panel 1').verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup('19.01')
         
        """
        Step 20: Close page
        """
        page_run_obj.close_homepage_run_window()
        
        """
        Step 21: Right click on 'C8262060' and select Run in new window
        """
        page_designer_obj.run_page_designer_in_new_window(glob_variable.current_test_case)
        util_obj.synchronize_with_visble_text('.pd-container-title', 'Panel 1', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 22: Click on the Overflow icon (Ellipsis)
                 Verify that Tab1 is in bold and NO + button
        """
        page_run_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_run_obj.tab_container('Panel 1').verify_selected_tab_in_tab_overflow_popup(['Tab 1'], '22.00')
        page_run_obj.tab_container('Panel 1').verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup('22.01')
        
        """
        Step 23: Choose Tab 4
                 Verify Tab 4 is now in view
        """
        page_run_obj.tab_container('Panel 1').select_tab_from_tab_overflow_popup('Tab 4')
        page_run_obj.tab_container('Panel 1').verify_selected_tab(['Tab 4'], '23.00')
        
        """
        Step 24: Click on the Overflow icon (Ellipsis)
                 Verify that Tab 4 is in bold and NO + button
        """
        page_run_obj.tab_container('Panel 1').click_tab_overflow_icon()
        page_run_obj.tab_container('Panel 1').verify_selected_tab_in_tab_overflow_popup(['Tab 4'], '24.00')
        page_run_obj.tab_container('Panel 1').verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup('24.01')
        
        """
        Step 25: Close page in new window
        """
        core_util_obj.switch_to_previous_window()

        """
        Step 26: Signout WF
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, glob_variable.current_test_case, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()