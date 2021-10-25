'''
Created on May 20, 2019.

@author: Niranjan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262068
TestCase Name = Check defaults for populated grids
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262068_TestClass(BaseTestCase):

    def test_C8262068(self):
        
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
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05: Click on left arrow to G513470 folder > P292_S19901 domain.
        Verify Domains appears.
        """
        page_designer_obj.collapse_content_folder("G513470->P292_S19901")
        page_preview_obj.verify_page_domain_tree_node(['Workspaces', 'P292_S19901', 'Retail Samples'], "Step 05.01: Verify Domains appears.")
        
        """
        Step 06: Click on Retail Samples > Portals > Small Widgets.
        """
        # step 6 will also execute by the method in step 7.
        """
        Step 07: Drag and drop 'Category Sales' onto the page canvas.
        """
        page_designer_obj.drag_content_item_to_blank_canvas("Category Sales", 1,"Retail Samples->Portal->Small Widgets")
        util_obj.synchronize_with_number_of_element("div .grid-stack-item-content iframe",1, main_page_obj.home_page_medium_timesleep)
        """
        Step 07.01: Verify that quick filter shows 6 inside the red circle.
        """
        page_designer_obj.verify_quick_filter_value("6", "Step 07.01")
        
        """
        Step 08: Click Containers tab. Drag and drop the grid container onto the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Grid", 4)
        
        """
        Step 09: From the designer toolbar, click on Page filter configuration button.
        Verify that Page Filter Configuration opens.
        """
        page_designer_obj.click_filter_configuration()
        
        """
        Step 09.01: Verify that Page Filter Configuration opens.
        """
        page_filter_configuration_css=".pop-top div[data-ibx-name='caption'] .ibx-label-text"
        util_obj.verify_element_text(page_filter_configuration_css, expected_text="Page Filter Configuration", msg='Step 09.01: Verify that Page Filter Configuration opens.')
        
        """
        Step 10: Click on Create empty filter bar.
        """ 
        page_designer_obj.select_filter_configurations_property("Create empty filter bar")
    
        """
        Step 11: Right click on Panel 2 > click Add filter controls.
        """
        page_designer_obj.select_container_context_menu("Panel 2", "Add filter controls")
        
        """
        Step 11.01: Verify Add Filter Controls dialog box opens.
        """
        page_designer_obj.add_filter_controls_dialog().verify_title(step_num="11.01")
        """
        Step 12: Unchecked STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """ 
        page_designer_obj.add_filter_controls_dialog("STORE_TYPE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE").uncheck()
        page_designer_obj.add_filter_controls_dialog("TIME_DATE_TO").uncheck()
        
        """
        Step 13: Click on Add filter controls.
        """ 
        page_designer_obj.add_filter_controls_dialog().click_add_filter_controls_button()
        
        """
        Step 13.01: Verify grid panel populated with some controls and quick filters shows 3 inside the red circle.
        """ 
        expected_label_list= ['Category:', 'Product Model:', 'Region:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 13.01: Verify grid panel populated with some controls", "Panel 2", model_window=False)
        page_designer_obj.verify_quick_filter_value("3", "Step 13.02")
        
        """
        Step 14:Click on Quick Filter button
        """
        page_designer_obj.click_quick_filter()
        
        """
        Step 14.01:Verify page filter populated with some controls.
        """
        expected_label_list=['Store Type:', 'From:', 'To:']
        page_designer_obj.verify_filter_control_labels(expected_label_list, "Step 14.01: Verify page filter populated with some controls")
        
        """
        Step 15:Click on the cell in Panel 2 (grid container).
        """
        page_designer_obj.select_filter_grid_cell(cell_num=1, grid_container_title="Panel 2")
        
        """
        Step 16:From the designer toolbar,click on Properties button > click style tab.
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        
        """
        Step 16.01: Verify that the Grid style section appears with 8 options (default, style 2 to style 8)
        """ 
        page_designer_obj.verify_grid_style_options(step_num="16.01")
        
        """
        Step 17: Click on the empty cell in filter bar.
        """
        page_designer_obj.select_filter_grid_cell(cell_num=1)
        """
        Step 17.01: Verify that the Grid style section appears with 8 options (default, style 2 to style 8)
        """ 
        page_designer_obj.verify_grid_style_options(step_num="17.01")
        
        """
        Step 18: Click on Save button and enter 'Populated grid' > Save.
        """ 
        page_designer_obj.save_page_from_toolbar('Populated grid')
        
        """
        Step 19: Close the Page Designer from application menu.
        """ 
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 20: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()