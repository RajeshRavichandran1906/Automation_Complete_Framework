"""-------------------------------------------------------------------------------------------
Created on July 04, 2019
@author: Aftab/Samuel

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6185758
Test Case Title =  Check Show On Desktop
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages import page_designer_miscelaneous  
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Run, Design
from common.lib.javascript import JavaScript


class C5852638_TestClass(BaseTestCase):

    def test_C5852638(self):
        
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
        miscellaneous_obj=page_designer_miscelaneous.PageDesignerMiscelaneous(self.driver)
        page_designer_run_obj = Run(self.driver)
        java_script_obj = JavaScript(self.driver)
        
        """
        TESTCASE CSS
        """
        tablet_icon_css = "[class*='tablet']"
        mobile_icon_css = "[class*='mobile']"
        delete_cell_css = '.pop-top [data-ibx-name*="Delete"]'
        
        """
        TESTCASE VARIABLES
        """
        edit_fex_name = 'C5852637'
        domain = 'P292_S11397'
        repository_folder = 'Domains->'+domain+'->G435308'
        report_action_bar = 'Report'
        panel5_data_expected_data = ['Panel 5 Category: Store Type:']
        expected_panel_list = ['Category Sales', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6']
        expected_tablet_size = [(600, 960)]
        expected_mobile_size = ['Panel 2', 'Panel 3', 'Panel 4', 'Panel 5']
        
        """
        LOCAL FUNCTIONS
        """
        def drag_filter_to_panel(filter_name, yoffset=0):
            filter_obj = miscellaneous_obj.get_pd_filter_control_object(filter_name)
            panel5_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 5')
            tar = core_util_obj.get_web_element_coordinate(panel5_grid_obj, element_location='middle', yoffset=yoffset)
            src = core_util_obj.get_web_element_coordinate(filter_obj, 'middle')
            core_util_obj.drag_and_drop(int(src['x']), int(src['y']), int(tar['x']), int(tar['y']))
            
        def right_click_empty_filter_cell_and_delete(index):
            filter_grid_obj = miscellaneous_obj.get_filter_grid_object()
            grid_cell_objs = util_obj.validate_and_get_webdriver_objects("div[class*='pd-filter-cell']", "Filter grid cell", parent_object=filter_grid_obj)
            cell_object = grid_cell_objs[index]
            core_util_obj.right_click(cell_object, element_location="middle", xoffset=2, yoffset=2)
            delete_cell_objs = util_obj.validate_and_get_webdriver_object(delete_cell_css, 'delete_cell_objs')
            core_util_obj.python_left_click(delete_cell_objs, element_location="middle")
            
        def verify_empty_filter_cells_deleted(index, expected_text, step_no):
            filter_grid_obj = miscellaneous_obj.get_filter_grid_object()
            grid_cell_objs = util_obj.validate_and_get_webdriver_objects("div[class*='pd-filter-cell']", "Filter grid cell", parent_object=filter_grid_obj)
            cell_object = grid_cell_objs[index]
            if cell_object.text == expected_text:
                print(step_no+'Verify empty cells has been deleted')
            else:
                print(step_no+'Empty cells not deleted')
            
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Expand 'P292_S11397' domain -> 'G435308' folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        
        """
        Right click on 'C5852637' and click on Edit menu
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(edit_fex_name, context_menu_item_path='Edit')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_locator_obj.PD_CONTAINER_CSS, 7, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Select first section and click open properties panel;
        """
        page_section_css = pd_locator_obj.PAGE_SECTION_PARENT_CSS
        first_section_css = page_section_css+":not([class*='radio-group-checked'])"
        first_section_obj = util_obj.validate_and_get_webdriver_object(first_section_css, 'First section in PD Page canvas')
        core_util_obj.left_click(first_section_obj, element_location='start')
        page_designer_obj.click_property()
        
        """
        Turn on Collapsible switch
        """
        section_settings_pane_css = "div[class^='section-settings'] div[data-ibxp-btn-options*='Section Settings']"
        collapsible_switch_css = section_settings_pane_css+" div[data-ibx-type='ibxSwitch'][class*='collapsible'][data-ibxp-checked='false']"
        collapsible_switch = util_obj.validate_and_get_webdriver_object(collapsible_switch_css, 'Collapsible switch')
        core_util_obj.left_click(collapsible_switch)
        
        """
        Step 05.00: Select second section and Turn on Collapsible switch in properties panel
        """
        second_section_css = page_section_css+"[class*='radio-group-checked'] [class^='ibx-accordion-page-content']"
        second_section_obj = util_obj.validate_and_get_webdriver_object(second_section_css, 'Second section in PD Page canvas')
        util_obj.click_on_screen(second_section_obj, coordinate_type='start', click_type=0)
        collapsible_switch = util_obj.validate_and_get_webdriver_object(collapsible_switch_css, 'Collapsible switch')
        core_util_obj.left_click(collapsible_switch)
        
        """
        Step 06.00: Navigate to Retail Samples domain --> portal --> small widgets in the tree
        """
        page_designer_obj.collapse_content_folder('G435308->P292_S11397')
        
        """
        Step 07.00: Drag and drop 'Category sales' into panel 1,
        """
        page_designer_obj.select_container("Panel 1")
        page_designer_obj.drag_content_item_to_container("Category Sales", "Panel 1", content_folder_path="Retail Samples->Portal->Small Widgets")
        
        """
        'Regional Sales trend' to panel 2
        """
        page_designer_obj.select_container("Panel 2")
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.drag_content_item_to_container("Regional Sales Trend", "Panel 2", content_folder_path="Small Widgets")
        
        """
        'Discount by region' to panel 3
        """
        page_designer_obj.select_container("Panel 3")
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.drag_content_item_to_container("Discount by Region", "Panel 3", content_folder_path="Small Widgets")
        
        """
        Step 08.00: Drag and drop 'Region profit by category' to panel 3 and choose 'Add content' in Add content dialog
        """
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.drag_content_item_to_container("Regional Profit by Category", "Panel 3", content_folder_path="Small Widgets")
        add_content_css = "div[data-ibx-type='ibxDialog'][class*='pop-top'] div[data-ibx-type='ibxButton'][class*='pd-add-content-add']"
        add_content = util_obj.validate_and_get_webdriver_object(add_content_css, 'Add Content')
        core_util_obj.left_click(add_content)
        
        """
        Step 09.00: Drag and drop 'Average cost V sales' to panel 4
        """
        page_designer_obj.select_container("Panel 4")
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.drag_content_item_to_container("Average Cost v Sales", "Panel 4", content_folder_path="Small Widgets")
        
        """
        Step 10.00: Click on quick filter icon
        """
        page_designer_obj.click_quick_filter()
        
        """
        Step 10.01: Verify filters added as below
        """
        page_designer_run_obj.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], 'Step 10.01: Verify filters added as below')
        
        """
        Step 11.00: Move 'Category' and 'Store Type' filter controls to the grid panel (Panel 5)
        """
        drag_filter_to_panel('Category:', yoffset=-50)
        drag_filter_to_panel('Store Type:')
        
        """
        Step 11.01: Verify filter controls in filter pane and panel5 appears as below
        """
        page_designer_run_obj.verify_filter_control_labels(['Product Model:', 'Region:', 'From:', 'To:'], 'Step 11.01 : Verify filter controls in filter pane appears as below')
        panel5_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 5')
        panel5_data = panel5_grid_obj.text.replace('\n', ' ')
        util_obj.as_List_equal(panel5_data_expected_data, [panel5_data],"Step 11.02: Verify panel5 appears as below")
        
        """
        Step 12.00: Right click on both the empty cells and click delete
        """
        right_click_empty_filter_cell_and_delete(0)
        right_click_empty_filter_cell_and_delete(2)
        
        """
        Step 12.01: Verify empty cells has been deleted and filter controls has been adjusted as below
        """
        page_designer_run_obj.verify_filter_control_labels(['Product Model:', 'Region:', 'From:', 'To:'], 'Step 12.01: Verify empty cells has been deleted')
        verify_empty_filter_cells_deleted(0, 'Product Model:', 'Step 12.02: ')
        verify_empty_filter_cells_deleted(2, 'From:', 'Step 12.03: ')
        
        """
        Step 13.00: Click on panel 1 and deselect the Mobile show on property
        [this means it will NOT show on the mobile device]
        """
        page_designer_obj.select_container("Category Sales")
        mobile_icon_obj = util_obj.validate_and_get_webdriver_object(mobile_icon_css, "Filter grid cell")
        core_util_obj.python_left_click(mobile_icon_obj, element_location="middle")
        
        """
        Step 14.00: Click on Panel 6, deselect the Tablet and Mobile show on properties
        [this means it will only show on the desktop]
        """
        panel6_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 6')
        java_script_obj.scrollIntoView(panel6_grid_obj)
        page_designer_obj.select_container("Panel 6")
        mobile_icon_obj = util_obj.validate_and_get_webdriver_objects(mobile_icon_css, "Filter grid cell")
        core_util_obj.python_left_click(mobile_icon_obj[1], element_location="middle")
        tablet_icon_obj = util_obj.validate_and_get_webdriver_object(tablet_icon_css, "Filter grid cell")
        core_util_obj.python_left_click(tablet_icon_obj, element_location="middle")
        
        """
        Step 15.00: Click on preview button
        """
        page_designer_obj.click_preview()
        
        """
        'Step 15.01: Verify all panels appear as below as this is simulating the desktop
        """
        page_designer_run_obj.verify_filter_control_labels(['Product Model:', 'Region:', 'From:', 'To:'], 'Step 15.01: Verify all panels appear as below as this is simulating the desktop')
        page_designer_run_obj.verify_containers_title(expected_panel_list, 'Step 15.01: Verify all panels appear as below as this is simulating the desktop')
        panel5_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 5')
        panel5_data = panel5_grid_obj.text.replace('\n', ' ')
        util_obj.as_List_equal(panel5_data_expected_data, [panel5_data],"Step 15.02: Verify all panels appear as below as this is simulating the desktop")
             
        """
        Step 16.00: Shrink the browser to tablet size
        """
        util_obj.set_browser_window_size(600, 960)
       
        """
        Step 16.01: Verify panel 6 will not show, other panels appears as below
        """
        page_designer_run_obj.verify_containers_title(['Category Sales', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5'], 'Step 16.01: Verify panel 6 will not show, other panels appears as below')
        actual_win_size = self.driver.get_window_size()
        actual_tablet_size = actual_win_size['width'],actual_win_size['height']
        util_obj.as_List_equal([actual_tablet_size], expected_tablet_size, 'Step 16.01: Verify window size')
        
        """
        Step 17.00: Shrink the browser to mobile size
        """
        util_obj.set_browser_window_size(412, 732)
        
        """
        Step 17.01: Verify both Panel1 and panel6 will not show, other panels appears as below
        """
        page_designer_run_obj.verify_containers_title(expected_mobile_size, 'Step 17.01: Verify both Panel1 and panel6 will not show, other panels appears as below')
        actual_win_size = self.driver.get_window_size()
        actual_range = range(412,520)
        actual_status = actual_win_size['width'] in actual_range
        util_obj.asequal(actual_status, True, 'Step 17.02: Verify window size')
        
        """
        Step 18.00: Resize the browser back to its original maxed state
        """
        self.driver.maximize_window()
       
        """
        Step 18.01: Verify all panels appear as below as this is simulating the desktop
        """
        page_designer_run_obj.verify_filter_control_labels(['Product Model:', 'Region:', 'From:', 'To:'], 'Step 15.01: Verify all panels appear as below as this is simulating the desktop')
        page_designer_run_obj.verify_containers_title(expected_panel_list, 'Step 18.01: Verify all panels appear as below as this is simulating the desktop')
        panel5_grid_obj = miscellaneous_obj.get_pd_container_object('Panel 5')
        panel5_data = panel5_grid_obj.text.replace('\n', ' ')
        util_obj.as_List_equal(panel5_data_expected_data, [panel5_data],"Step 18.02: Verify all panels appear as below as this is simulating the desktop")
        
        """
        Step 19.00: Click on back button to get back to designer
        """
        page_designer_run_obj.go_back_to_design_from_preview()
                
        """
        Step 20.00: Click on main menu -> Save as;
        Enter title as 'C5852638' button and close designer
        """
        page_designer_obj.save_as_page_from_application_menu('C5852638')
        page_designer_obj.switch_to_previous_window()
        
        """
        Step 21.00: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
                
        
if __name__ == '__main__':
    unittest.main()