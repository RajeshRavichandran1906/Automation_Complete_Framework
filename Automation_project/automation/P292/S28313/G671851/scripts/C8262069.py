'''
Created on May 23, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262069
TestCase Name = Create and Preview PGX for grids/Page filter styling
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview, Run

class C8262069_TestClass(BaseTestCase):

    def test_C8262069(self):
        
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
        pop_top_css = ".pop-top"
        page_filter_configuration_css = pop_top_css+" div[data-ibx-name='caption'] .ibx-label-text"
        filter_grid_css=".pd-regular-filter-wrapper div[data-ibx-type='pdFilterGrid']"
        panel_titlebar_css=".grid-stack-item-content div[class^='pd-container-title-bar']"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Workspaces->P292_S19901->G513470'
        action_tile = 'Designer'
        action_bar = 'Page'
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
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
        Step 05.00: Click on left arrow to G513470 folder > P292_S19901 domain. 
        """
        page_designer_obj.collapse_content_folder("G513470->P292_S19901")
        
        """
        Step 05.01: Verify Domains appears.
        """
        page_preview_obj.verify_page_domain_tree_node(['Workspaces', 'P292_S19901', 'Retail Samples'], "Step 05.01: Verify Domains appears.")
        
        """
        Step 06.00: Double click on Retail Samples > Portals > Small Widgets.
        Step 07.00: Drag and drop 'Category Sales' onto the Panel 1.
        """
        page_designer_obj.drag_content_item_to_container(content_item_to_drog='Category Sales', container_title_to_drop='Panel 1', content_folder_path='Retail Samples->Portal->Small Widgets')
        sleep(8)
        
        """
        Step 08.00: Click Containers tab. Drag and drop the grid container onto the Panel 2.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_basic_container_to_canvas_container("Grid", "Panel 2")
        sleep(8)
        
        """
        Step 09.00: From the designer toolbar, click on Page filter configuration button.
        """
        page_designer_obj.click_filter_configuration()
        
        """
        Step 09.01: Verify that Page Filter Configuration opens.
        """
        util_obj.synchronize_with_number_of_element(page_filter_configuration_css, expected_number=1, expire_time=30)
        util_obj.verify_element_text(page_filter_configuration_css, expected_text="Page Filter Configuration", msg='Step 09.01: Verify that Page Filter Configuration opens.')
        
        """
        Step 10.00: Click on Create empty filter bar.
        """
        sleep(8)
        page_designer_obj.select_filter_configurations_property('Create empty filter bar')
        
        """
        Step 11.00: Right click on Panel 2 > click Add filter controls.
        """
        page_designer_obj.select_container_context_menu("Panel 2", "Add filter controls")
        
        """
        Step 11.01: Verify Add Filter Controls dialog box opens.
        """
        page_designer_obj.add_filter_controls_dialog().verify_title(step_num="11.01")
        
        """
        Step 12.00: Unchecked STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """ 
        page_designer_obj.add_filter_controls_dialog("STORE_TYPE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE_TO").uncheck()
        
        """
        Step 13.00: Click on Add filter controls.
        """ 
        page_designer_obj.add_filter_controls_dialog().click_add_filter_controls_button()
        
        """
        Step 13.01: Verify grid panel populated with some controls and quick filters shows 3 inside the red circle.
        """ 
        expected_label_list= ['Category:', 'Product Model:', 'Region:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 13.01: Verify grid panel populated with some controls", "Panel 2", model_window=False)
        page_designer_obj.verify_quick_filter_value("3", "Step 13.02")
        
        """
        Step 14.00: Click on Quick Filter button
        """
        page_designer_obj.click_quick_filter()
        sleep(5)
        
        """
        Step 14.01: Verify page filter populated with some controls.
        """
        expected_label_list=['Store Type:', 'From:', 'To:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 14.01: Verify page filter populated with some controls")
        
        """
        Step 15: Click on the Panel 2 (grid container).
        """
        page_designer_obj.select_container("Panel 2")
        
        """
        Step 16: From the designer toolbar,click on Properties button > click style tab and choose Style 2. 
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        page_designer_obj.select_container_style("Style 2")
        
        """
        Step 16.01: Verify that the whole grid area has now style 2
        """ 
        page_designer_obj.verify_container_style_color("Panel 2", 'curious_blue', step_num="16.01")
        
        """
        Step 17: Click on the page filter area and choose Style 3. 
        """
        page_designer_obj.select_filter_grid_cell(cell_num=1)
        page_designer_obj.select_grid_style("Style 3")
        
        """
        Step 17.01: Verify that the whole grid area has now style 3 and the grid panel has style 2 still set.
        """ 
        page_designer_obj.verify_filter_grid_style_color('fern2', step_num='17.01')
        page_designer_obj.verify_container_style_color("Panel 2", 'curious_blue', step_num="17.02")
        
        """
        Step 18.00: Click the preview button. 
        """
        page_designer_obj.click_preview()
        sleep(8)
        
        """
        Step 18.01: Verify all the changes still exist.
        """
        page_designer_run_obj.verify_page_heading_title(['Page Heading'], 'Step 18.01 : Verify page title')
        page_designer_run_obj.verify_containers_title(["Category Sales", "Panel 2", "Panel 3"], 'Step 18.02 : Verify container titles') 
        page_designer_run_obj.verify_filter_control_labels([ 'Store Type:', 'From:', 'To:'], 'Step 18.03 : Verify filter panel heading labels')
        page_designer_run_obj.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:'], 'Step 18.04 : Verify filter panel heading labels', grid_container_title='Panel 2')
        util_obj.verify_element_color_using_css_property(filter_grid_css, 'fern2', msg='Step 18.05 : Verify filter grid styling', attribute='background-color')
        panel2_titlebar_css=self.driver.find_elements_by_css_selector(panel_titlebar_css)
        util_obj.verify_element_color_using_css_property(None, 'curious_blue', msg='Step 18.06 : Verify panel2 styling', attribute='background-color', element_obj=panel2_titlebar_css[1])
        
        """
        Step 19.00: Click on preview button to back to page designer canvas.
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 20.00: Click on Save button and give 'grids and Page filter_styling'> click save and Close the Page Designer from application menu.
        """ 
        page_designer_obj.save_page_from_toolbar('grids and Page filter_styling')
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 21.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()