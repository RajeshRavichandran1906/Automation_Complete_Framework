'''
Created on June 11, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852636
TestCase Name = Show On Default 
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as miscellaneous_obj
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5852636_TestClass(BaseTestCase):

    def test_C5852636(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        pd_locator_obj = page_designer_locators.PageDesigner()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        container_settings_pane_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings']"
        label_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings'] div[data-ibx-type='ibxLabel']"
        show_on_prop_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings'] div[data-ibx-row='{0}'].pd-container-device"
        page_section_css = pd_locator_obj.PAGE_SECTION_PARENT_CSS
        blank_grid_css = page_section_css + " div[class='pd-page-section-grid-box']"
        
        """
        TESTCASE VARIABLES
        """
        Case_ID = 'C5852636'
        domain = 'P292_S11397'
        repository_folder = 'Domains->'+domain+'->G435308'
        designer_action_tile = 'Designer'
        page_action_bar = 'Page'
        blank_template = 'Blank'
        report_action_bar = 'Report'
        property_label = 'Show On'
        expected_list = ['Desktop', 'Tablet', 'Mobile']
        sleep_time = 5
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Expand 'P292_S11397' domain; Click on 'G435308' folder and choose Page action tile from under designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(designer_action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(page_action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, blank_template, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Choose Blank template
        """
        page_designer_obj.select_page_designer_template(blank_template)
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.00: Click on Containers tab
        """
        page_designer_obj.select_option_from_carousel_items(option_name='Containers')
        
        """
        Step 06.00: Drag Panel, Tab, Carousel and Accordion containers one after another and drop in the page canvas
        """
        page_designer_obj.drag_container_item_to_blank_canvas(container_name_to_drag='Panel', blank_grid_index_to_drop=1)
        sleep(sleep_time)
        page_designer_obj.drag_container_item_to_blank_canvas(container_name_to_drag='Tab', blank_grid_index_to_drop=4)
        sleep(sleep_time)
        page_designer_obj.drag_container_item_to_blank_canvas(container_name_to_drag='Carousel', blank_grid_index_to_drop=7)
        sleep(sleep_time)
        page_designer_obj.drag_container_item_to_blank_canvas(container_name_to_drag='Accordion', blank_grid_index_to_drop=10)
        sleep(sleep_time)
        
        """
        Step 07.00: Click on panel 1 and click open properties panel
        """
        page_designer_obj.select_container("Panel 1")
        page_designer_obj.click_property()
        
        """
        Step 07.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        labels = util_obj.validate_and_get_webdriver_objects(label_css, 'Container Settings labels')
        label_list = [el.text.strip() for el in labels if el.text.strip() != '']
        util_obj.asin(property_label, label_list, "Step 07.01: Verify show on properties label appears")
        
        label_index = label_list.index(property_label)
        show_on_prop_obj = util_obj.validate_and_get_webdriver_object(show_on_prop_css.format(label_index+1), 'Show on properties')
        prop_list = show_on_prop_obj.find_elements_by_css_selector("div[data-ibx-type='ibxRadioButton']")
        actual_list = [el.get_attribute('title') for el in prop_list]
        util_obj.as_List_equal(actual_list, expected_list, "Step 07.02: Verify show on properties appear as below")
        
        """
        Step 08.00: Click on panel 2 (tabbed container)
        """
        page_designer_obj.select_container("Panel 2")
        
        """
        Step 08.01: Verify show on properties appear as below
        """
        util_obj.asin(property_label, label_list, "Step 08.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 08.02: Verify show on properties appear as below")
        
        """
        Step 09.00: Click on panel 3 (carousel container)
        """
        page_designer_obj.select_container("Panel 3")
        
        """
        Step 09.01: Verify show on properties appear as below
        """
        util_obj.asin(property_label, label_list, "Step 09.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 09.02: Verify show on properties appear as below")
        
        """
        Step 10.00: Click on panel 4 (accordion container)
        """
        page_designer_obj.select_container("Panel 4")
        
        """
        Step 10.01: Verify show on properties appear as below
        """
        util_obj.asin(property_label, label_list, "Step 10.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 10.02: Verify show on properties appear as below")
        
        """
        Step 11.00: Drag and drop a Grid container under Panel 1
        """
        page_designer_obj.select_container("Panel 1")
        page_designer_obj.drag_container_item_to_blank_canvas(container_name_to_drag='Grid', blank_grid_index_to_drop=49, element_location =  'bottom_middle', yoffset=-5)
        
        """
        Step 11.01: Verify show on properties appear as below
        """
        util_obj.asin(property_label, label_list, "Step 11.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 11.02: Verify show on properties appear as below")
        
        """
        Step 12.00: Right click on the current section and Choose 'Insert section below'
        """
        blank_grid_obj = util_obj.validate_and_get_webdriver_objects(blank_grid_css, 'Blank Grid Section')
        core_util_obj.right_click(blank_grid_obj[113])
        miscellaneous_obj.select_page_designer_context_menu(self, 'Insert section below')
        
        """
        Step 12.01: Verify that a new section has been added
        """
        page_section_obj = util_obj.validate_and_get_webdriver_objects(page_section_css, 'Page Section')
        util_obj.asequal(len(page_section_obj), 2, "Step 12.01: Verify that a new section has been added")
        
        """
        Step 13.00: Drag and drop Explorer from repository widgets to the second section
        """
        page_designer_obj.select_option_from_carousel_items(option_name='Content')
        page_designer_obj.expand_and_collapse_repository_widgets_tab('expand')
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas('Explorer', blank_grid_index_to_drop=121)
        
        """
        Step 13.01: Verify show on properties for explorer widget appears as below
        """
        util_obj.asin(property_label, label_list, "Step 13.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 13.02: Verify show on properties appear as below")
        
        """
        Step 14.00: Drag and drop link tile to section 1 next to the last panel (grid panel-Panel5)
        """
        util_obj.mouse_scroll('up', '2', option='uiautomation')
        sleep(sleep_time)
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas('Link tile', blank_grid_index_to_drop=64)
        
        """
        Step 14.01: Verify show on properties for explorer widget appears as below
        """
        util_obj.asin(property_label, label_list, "Step 14.01: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 14.02: Verify show on properties appear as below")
        
        """
        Step 15.00: Click on save button; Enter page title as 'C5852636' and click save button
        """
        page_designer_obj.save_page_from_toolbar(Case_ID)
        
        """
        Step 16.00: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 17.00: Right click on 'C5852636' and select Publish
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'C5852636', main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(Case_ID, context_menu_item_path='Publish')
        main_page_obj.verify_content_area_item_publish_or_unpublish(Case_ID, 'publish', 'Step 17:00 Verify C5852636 is published.')
        sleep(sleep_time)
        
        """
        Step 18.00: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()        