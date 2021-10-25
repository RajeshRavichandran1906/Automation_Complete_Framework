'''
Created on May 23, 2019.

@author: Niranjan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262078
TestCase Name = Create and Preview PGX for Container Theme and Grid style
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262078_TestClass(BaseTestCase):

    def test_C8262078(self):
        
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
        repository_folder = 'Workspaces->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar = 'Page'
        
        """
        Step 01: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 02: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03: Expand 'P292_S19901' domain > click on G513470 folder.
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04: Click on Designer and Create a new PGX Page using blank template.
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05:From the designer toolbar,click on Properties button > click style tab.
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        
        """
        Step 06:Click on Panel 1. Choose Style 2 in Properties panel.
        """
        page_designer_obj.select_container("Panel 1")
        page_designer_obj.select_container_style("Style 2")
        
        """
        Step 07:Click on Panel 2. Choose Style 2 in Properties panel.
        """
        page_designer_obj.select_container("Panel 2")
        page_designer_obj.select_container_style("Style 2")
        
        """
        Step 08:Click on Panel 3. Choose Style 2 in Properties panel.
        """
        page_designer_obj.select_container("Panel 3")
        page_designer_obj.select_container_style("Style 2")
        
        """
        Step 09: Click on left arrow to G513470 folder > P292_S19901 domain.
        Verify Domains appears.
        """
        page_designer_obj.collapse_content_folder("G513470->P292_S19901")
        page_preview_obj.verify_page_domain_tree_node(['Workspaces', 'P292_S19901', 'Retail Samples'], "Step 09.01 : Verify Domains appears.")
        
        """
        Step 10: Click on Retail Samples > Portals > Small Widgets.
        """
        # step 6 will also execute by the method in step 7.
        """
        Step 11: Drag and drop 'Category Sales' onto the Panel 1.
        """
        page_designer_obj.drag_content_item_to_container("Category Sales", "Panel 1", container_position=1, content_folder_path="Retail Samples->Portal->Small Widgets")
#         util_obj.synchronize_with_number_of_element("div .grid-stack-item-content iframe",1, main_page_obj.home_page_medium_timesleep)
        """
        Step 11.01: Verify that quick filter shows 6 inside the red circle.
        """
        page_designer_obj.verify_quick_filter_value("6", "Step 11.01")
        
        """
        Step 12: Click Containers tab. Drag and drop the grid container onto the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_basic_container_to_canvas_container("Grid", "Panel 2")
        
        """
        Step 13: From the designer toolbar, click on Page filter configuration button.
        """
        page_designer_obj.click_filter_configuration()
        
        """
        Step 13.01: Verify that Page Filter Configuration opens.
        """
        page_filter_configuration_css=".pop-top div[data-ibx-name='caption'] .ibx-label-text"
        util_obj.verify_element_text(page_filter_configuration_css, expected_text="Page Filter Configuration", msg='Step 13.01 : Verify that Page Filter Configuration opens.')
        
        """
        Step 14: Click on Create empty filter bar.
        """ 
        page_designer_obj.select_filter_configurations_property("Create empty filter bar")
    
        """
        Step 15: Right click on Panel 2 > click Add filter controls.
        """
        page_designer_obj.select_container_context_menu("Panel 2", "Add filter controls")
        
        """
        Step 15.01: Verify Add Filter Controls dialog box opens.
        """
        page_designer_obj.add_filter_controls_dialog().verify_title(step_num="15.01")
        
        """
        Step 16: BUSINESS_REGION,STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """ 
        page_designer_obj.add_filter_controls_dialog("BUSINESS_REGION").uncheck()
        page_designer_obj.add_filter_controls_dialog("STORE_TYPE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE_TO").uncheck()
        
        """
        Step 17: Click on Add filter controls.
        """ 
        page_designer_obj.add_filter_controls_dialog().click_add_filter_controls_button()
        
        """
        Step 17.01: Verify grid panel populated with some controls and quick filters shows 4 inside the red circle.
        """ 
        expected_label_list= ['Category:', 'Product Model:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 17.01 : Verify grid panel populated with some controls", "Panel 2")
        page_designer_obj.verify_quick_filter_value("4", "Step 17.02")
        
        """
        Step 18:Click on Quick Filter button
        """
        page_designer_obj.click_quick_filter()
        
        """
        Step 18.01:Verify page filter populated with some controls.
        """
        expected_label_list= ['Region:', 'Store Type:', 'From:', 'To:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 18.01 : Verify page filter populated with some controls")
        
        """
        Step 19:Click on the Panel 2 (grid container).
        """
        page_designer_obj.select_container("Panel 2")
        
        """
        Step 20:Choose Style 3 in Properties panel.
        """
        page_designer_obj.select_container_style("Style 3")
        
        """
        Step 20.01: Verify that the whole grid area has now style 3
        """
        page_designer_obj.verify_container_style_color("Panel 2", "fern2", "20.01")

        """
        Step 21: Click on the page filter area and choose Style 4.
        """
        page_designer_obj.select_filter_grid_cell(cell_num=1)
        page_designer_obj.select_grid_style("Style 4")
        
        """
        Step 21.01: Verify that the whole grid area has now style 4 and the grid panel has style 2 and 3 still set
        """ 
        page_designer_obj.verify_filter_grid_style_color("Sea_Serpent", "21.01")
        page_designer_obj.verify_container_style_color("Category Sales", "curious_blue", "21.03")
        page_designer_obj.verify_container_style_color("Panel 2", "fern2", "21.02")
        page_designer_obj.verify_container_style_color("Panel 3", "curious_blue", "21.03")
        
        """
        Step 22: Click on Page filter configuration button > Change to Filter modal window > Click OK.
        """
        page_designer_obj.click_filter_configuration()
        page_designer_obj.select_filter_configurations_property("Filter modal window")
        
        """
        Step 22.01: Verify all the changes still exist
        """ 
        page_designer_obj.verify_filter_grid_style_color("Sea_Serpent", "21.01",model_window=True)
        
        """
        Step 23: Click the preview button.
        """ 
        page_designer_obj.click_preview()
        
        """
        Step 23.01: Verify all the changes still exist.
        """ 
        page_designer_obj.verify_container_style_color("Category Sales", "curious_blue", "21.01")
        page_designer_obj.verify_container_style_color("Panel 2", "fern2", "21.02")
        page_designer_obj.verify_container_style_color("Panel 3", "curious_blue", "21.03")
        expected_label_list= ['Category:', 'Product Model:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 23.04 : Verify grid panel populated with some controls", "Panel 2")
        
        """
        Step 24:  Click on the filter button to bring up the modal.
        """ 
        page_preview_obj.click_show_filters()
        
        """
        Step 24.01:  Verify all the changes still exist
        """ 
        page_designer_obj.verify_filter_grid_style_color("Sea_Serpent", "24.01",model_window=True)
        
        """
        Step 25: Click on preview button to back to page designer canvas.
        """ 
        page_designer_obj.close_filter_model_window()
        page_preview_obj.go_back_to_design_from_preview(5)
        
        """
        Step 26: Click on Save button and give 'container theme and grid styling'> click save and Close the Page Designer from application menu.
        """ 
        page_designer_obj.save_page_from_toolbar('container theme and grid styling')        
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 27: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()