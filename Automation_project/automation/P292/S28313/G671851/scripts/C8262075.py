'''
Created on May 24, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262075
TestCase Name = Create and Preview PGX for Page Theme and Grid style
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview, Run

class C8262075_TestClass(BaseTestCase):

    def test_C8262075(self):
        
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
        page_designer_run_obj = Run(self.driver)
        
        """
        TESTCASE CSS
        """
        pd_page_css=".pd-page"
        pop_top_css = ".pop-top"
        page_filter_configuration_css = pop_top_css+" div[data-ibx-name='caption'] .ibx-label-text"
        filter_grid_css=".pd-regular-filter-wrapper div[data-ibx-type='pdFilterGrid']"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        panel2_css = ".grid-stack-item-content div[data-ibxp-title$='TITLE_2']"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Workspaces->P292_S19901->G513470'
        action_tile = 'Designer'
        action_bar = 'Page'
        exp_linear_gradient_midnight_theme = "rgba(0, 0, 0, 0) linear-gradient(to right, rgb(77, 64, 112) 0%, rgb(67, 110, 164) 100%) repeat scroll 0% 0% / auto padding-box border-box"
        exp_linear_gradient_style2_theme = "rgba(0, 0, 0, 0) linear-gradient(rgba(1, 96, 178, 0.4) 0%, rgba(32, 157, 225, 0.7) 100%) repeat scroll 0% 0% / auto padding-box border-box"
        exp_linear_gradient_style3_theme = "rgba(0, 197, 221, 0.7) linear-gradient(rgba(4, 129, 151, 0.4) 0%, rgba(0, 197, 221, 0.7) 100%) repeat scroll 0% 0% / auto padding-box border-box"
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Expand 'P292_S19901' domain > click on G513470 folder.
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Click on Designer and Create a new PGX Page using Grid 2-1 template. 
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.00: From the designer toolbar,click on Properties button > click style tab. 
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        
        """
        Step 06.00: Under Page Style > change Theme to 'Midnight'.  
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Midnight')
        
        """
        Step 06.01: Verify applied theme reflects the whole page canvas.  
        """
        act_linear_gradient_midnight_theme=self.driver.find_element_by_css_selector(pd_page_css).value_of_css_property('background')
        util_obj.asequal(exp_linear_gradient_midnight_theme, act_linear_gradient_midnight_theme, 'Step 06.01: Verify applied theme reflects the whole page canvas.')
        
        """
        Step 07.00: Click on properties tab to close it
        """
        page_designer_obj.click_property()
        
        """
        Step 08.00: Click on left arrow to G513470 folder > P292_S19901 domain. 
        """
        page_designer_obj.collapse_content_folder("G513470->P292_S19901")
        
        """
        Step 08.01: Verify Domains appears.
        """
        page_preview_obj.verify_page_domain_tree_node(['Workspaces', 'P292_S19901', 'Retail Samples'], "Step 08.01: Verify Domains appears.")
        
        """
        Step 09.00: Double click on Retail Samples > Portals > Small Widgets.
        Step 10.00: Drag and drop 'Category Sales' onto the Panel 1.
        """
        page_designer_obj.drag_content_item_to_container(content_item_to_drog='Category Sales', container_title_to_drop='Panel 1', content_folder_path='Retail Samples->Portal->Small Widgets')
        sleep(8)
        
        """
        Step 11.00: Click Containers tab. Drag and drop the grid container onto the Panel 2.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_basic_container_to_canvas_container("Grid", "Panel 2")
        sleep(8)
        
        """
        Step 12.00: From the designer toolbar, click on Page filter configuration button.
        """
        page_designer_obj.click_filter_configuration()
        
        """
        Step 12.01: Verify that Page Filter Configuration opens.
        """
        util_obj.synchronize_with_number_of_element(page_filter_configuration_css, expected_number=1, expire_time=30)
        util_obj.verify_element_text(page_filter_configuration_css, expected_text="Page Filter Configuration", msg='Step 12.01: Verify that Page Filter Configuration opens.')
        
        """
        Step 13.00: Click on Create empty filter bar.
        """
        sleep(8)
        page_designer_obj.select_filter_configurations_property('Create empty filter bar')
        
        """
        Step 14.00: Right click on Panel 2 > click Add filter controls.
        """
        page_designer_obj.select_container_context_menu("Panel 2", "Add filter controls")
        
        """
        Step 14.01: Verify Add Filter Controls dialog box opens.
        """
        page_designer_obj.add_filter_controls_dialog().verify_title(step_num="14.01")
        
        """
        Step 15.00: Unchecked BUSINESS_REGION,STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """ 
        page_designer_obj.add_filter_controls_dialog("BUSINESS_REGION").uncheck()
        page_designer_obj.add_filter_controls_dialog("STORE_TYPE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE_TO").uncheck()
        
        """
        Step 16.00: Click on Add filter controls.
        """ 
        page_designer_obj.add_filter_controls_dialog().click_add_filter_controls_button()
        
        """
        Step 16.01: Verify grid panel populated with some controls and quick filters shows 4 inside the red circle.
        """ 
        expected_label_list= ['Category:', 'Product Model:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 16.01: Verify grid panel populated with some controls", "Panel 2", model_window=False)
        page_designer_obj.verify_quick_filter_value("4", "Step 16.02")
        
        """
        Step 17.00: Click on Quick Filter button
        """
        page_designer_obj.click_quick_filter()
        sleep(5)
        
        """
        Step 17.01: Verify page filter populated with some controls.
        """
        expected_label_list=['Region:', 'Store Type:', 'From:', 'To:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 17.01: Verify page filter populated with some controls")
        
        """
        Step 18: Click on the Panel 2 (grid container).
        """
        page_designer_obj.select_container("Panel 2")
        
        """
        Step 19: From the designer toolbar,click on Properties button > click style tab and choose Style 2. 
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        page_designer_obj.select_container_style("Style 2")
        
        """
        Step 19.01: Verify that the whole grid area has now style 2
        """ 
        act_linear_gradient_style2_theme=self.driver.find_element_by_css_selector(panel2_css).value_of_css_property('background')
        util_obj.asequal(exp_linear_gradient_style2_theme, act_linear_gradient_style2_theme, 'Step 19.01: Verify that the whole grid area has now style 2')
        
        """
        Step 20: Click on the page filter area and choose Style 3. 
        """
        page_designer_obj.select_filter_grid_cell(cell_num=1)
        page_designer_obj.select_grid_style("Style 3")
        
        """
        Step 20.01: Verify that the whole grid area has now style 3 and the grid panel has style 2 still set.
        """ 
        act_linear_gradient_style3_theme=self.driver.find_element_by_css_selector(filter_grid_css).value_of_css_property('background')
        util_obj.asequal(exp_linear_gradient_style3_theme, act_linear_gradient_style3_theme, 'Step 20.01: Verify that the whole grid area has now style 3')
        util_obj.asequal(exp_linear_gradient_style2_theme, act_linear_gradient_style2_theme, 'Step 20.02: Verify that grid panel has style 2 still set.')
        
        """
        Step 21.00: Click on Page filter configuration button > Change to Filter modal window > Click OK. 
        """
        page_designer_obj.click_filter_configuration()
        util_obj.synchronize_with_number_of_element(page_filter_configuration_css, expected_number=1, expire_time=30)
        page_designer_obj.select_filter_configurations_property('Filter modal window')
        
        """
        Step 21.01: Verify all the changes still exist
        """
        selections_dialog_css="div[class^='ibx-dialog-main-box'] [class^='ibx-title-bar-caption'][data-ibx-type='ibxLabel'] div[class='ibx-label-text']"
        util_obj.synchronize_with_visble_text(selections_dialog_css, 'Selections', expire_time=30)
        page_designer_run_obj.verify_page_heading_title(['Page Heading'], 'Step 21.01 : Verify page title')
        page_designer_run_obj.verify_containers_title(["Category Sales", "Panel 2", "Panel 3"], 'Step 21.02 : Verify container titles')
        page_designer_run_obj.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], 'Step 21.03 : Verify filter panel heading labels', model_window=True)
        page_designer_run_obj.verify_filter_control_labels(['Category:', 'Product Model:'], 'Step 21.04 : Verify filter panel heading labels', grid_container_title='Panel 2') 
        util_obj.asequal(exp_linear_gradient_midnight_theme, act_linear_gradient_midnight_theme, 'Step 21.05 : Verify applied theme reflects the whole page canvas.')
        util_obj.asequal(exp_linear_gradient_style3_theme, act_linear_gradient_style3_theme, 'Step 21.06 : Verify that the whole grid area has now style 3')
        util_obj.asequal(exp_linear_gradient_style2_theme, act_linear_gradient_style2_theme, 'Step 21.07 : Verify that grid panel has style 2 still set.')
        
        """
        Step 22.00: Click the preview button. 
        """
        page_designer_obj.click_preview()
        sleep(8)
        
        """
        Step 22.01: Verify all the changes still exist.
        """
        page_designer_run_obj.verify_page_heading_title(['Page Heading'], 'Step 22.01 : Verify page title')
        page_designer_run_obj.verify_containers_title(["Category Sales", "Panel 2", "Panel 3"], 'Step 22.02 : Verify container titles') 
        page_designer_run_obj.verify_filter_control_labels(['Category:', 'Product Model:'], 'Step 22.03 : Verify filter panel heading labels', grid_container_title='Panel 2')
        util_obj.asequal(exp_linear_gradient_midnight_theme, act_linear_gradient_midnight_theme, 'Step 22.04 : Verify applied theme reflects the whole page canvas.')
        util_obj.asequal(exp_linear_gradient_style2_theme, act_linear_gradient_style2_theme, 'Step 22.05 : Verify that grid panel has style 2 still set.')
        
        """
        Step 23.00: Click on preview button to back to page designer canvas.
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 24.00: Click on Save button and give 'page theme and grid styling'> click save and Close the Page Designer from the application menu
        """ 
        page_designer_obj.save_page_from_toolbar('page theme and grid styling')
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 25.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()