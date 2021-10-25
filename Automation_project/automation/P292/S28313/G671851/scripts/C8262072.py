'''
Created on May 20, 2019.

@author: AA14564

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262072
TestCase Name = Create and Preview PGX grids/Modal Page filter styling
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262072_TestClass(BaseTestCase):

    def test_C8262072(self):
        
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
        domain = 'Workspaces'
        repository_folder = '{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar = 'Page'
        template = "Grid 2-1"
        file_path = 'Retail Samples->Portal->Small Widgets'
        panel = 'Panel {0}'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S19901' domain > click on G513470 folder.
        """
        main_page_obj.expand_repository_folder('{0}->{1}'.format(domain, repository_folder))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Designer and Create a new PGX Page using Grid 2-1 template.
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_top_css, template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(template)
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on left arrow to G513470 folder > P292_S19901 domain.
                Verify Domains appears.
        """
        page_designer_obj.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        page_designer_obj.verify_page_domain_tree_node(['{0}_{1}'.format(project_id, suite_id), 'Retail Samples'], 'Step 05.00 : Verify Domains appears.')
        
        """
        Step 6: Double click on Retail Samples > Portals > Small Widgets.
        """
        """
        Step 7: Drag and drop 'Category Sales' onto the Panel 1.
        """
        page_designer_obj.drag_content_item_to_container('Category Sales', panel.format('1'), content_folder_path=file_path)
        
        """
        Step 8: Click Containers tab. Drag and drop the grid container onto the Panel 2.
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        page_designer_obj.drag_basic_container_to_canvas_container(template[:-4], panel.format('2'))
        
        """
        Step 9: From the designer toolbar, click on Page filter configuration button.
                Verify that Page Filter Configuration opens.
        """
        """
        Step 10: Click on Create empty filter bar.
        """
        page_designer_obj.click_filter_configuration()
        page_designer_obj.select_filter_configurations_property("Create empty filter bar")
        
        """
        Step 11: Right click on Panel 2 > click Add filter controls.
                 Verify Add Filter Controls dialog box opens.
        """
        page_designer_obj.select_container_context_menu('Panel 2', 'Add filter controls')
        
        """
        Step 12: Unchecked BUSINESS_REGION,STORE_TYPE, TIME_DATE and TIME_DATE_TO.
        """
        page_designer_obj.add_filter_controls_dialog(parameter='BUSINESS_REGION').uncheck()
        page_designer_obj.add_filter_controls_dialog(parameter='STORE_TYPE').uncheck()
        page_designer_obj.add_filter_controls_dialog(parameter='TIME_DATE').uncheck()
        page_designer_obj.add_filter_controls_dialog(parameter='TIME_DATE_TO').uncheck()
        
        """
        Step 13: Click on Add filter controls.
                 Verify grid panel populated with some controls and quick filters shows 4 inside the red circle.
        """
        page_designer_obj.add_filter_controls_dialog().click_add_filter_controls_button()
        page_designer_obj.verify_filter_control_labels(['Category:', 'Product Model:'], 'Step 13.00 : Verify', grid_container_title=panel.format('2'))
        
        """
        Step 14: Click on quick filer button.
                 Verify page filter populated with some controls.
        """
        page_designer_obj.click_quick_filter()
        page_designer_obj.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], 'Step 14.00 : Verify page filter populated with some controls.')
        
        """
        Step 15: Click on the Panel 2 (grid container).
        """
        page_designer_obj.select_container('Panel 2')
        
        """
        Step 16: From the designer toolbar,click on Properties button > click style tab and choose Style 2.
                 Verify that the whole grid area has now style 2
        """
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab('style')
        page_designer_obj.select_container_style('Style 2')
        page_designer_obj.verify_container_style_color(panel.format('2'), 'curious_blue', '16.00')
        
        """
        Step 17: Click on the page filter area and choose Style 3.
                 Verify that the whole grid area has now style 3 and the grid panel has style 2 still set.
        """
        page_designer_obj.select_filter_grid_cell(1)
        page_designer_obj.select_grid_style('Style 3')
        page_designer_obj.verify_filter_grid_style_color('fern2', '17.00')
        page_designer_obj.verify_container_style_color(panel.format('2'), 'curious_blue', '17.01')
        
        """
        Step 18: Click on Page filter configuration button > Change to Filter modal window > Click OK.
                 Verify all the changes still exist
        """
        page_designer_obj.click_filter_configuration()
        page_designer_obj.select_filter_configurations_property('Filter modal window')
        page_designer_obj.verify_filter_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], 'Step 18.00 : Verify page filter populated with some controls.', model_window=True)
        page_designer_obj.verify_filter_grid_style_color('fern2', '18.01', model_window=True)
        
        """
        Step 19: Click the preview button.
                 Verify all the changes still exist.
        """
        page_designer_obj.click_preview()
        page_preview_obj.verify_container_style_color('Category Sales', 'black', '17.00')
        page_preview_obj.verify_container_style_color(panel.format('2'), 'curious_blue', '17.01')
        page_preview_obj.verify_container_style_color(panel.format('3'), 'black', '17.02')
        
        """
        Step 20: Click on preview button to back to page designer canvas.
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
        Step 21: Click on Save button and give 'grids and Model page filter_styling'> click save and Close the Page Designer from application menu.
        """
        page_designer_obj.save_page_from_toolbar('grids and Model page filter_styling')
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 22: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
      
if __name__ == '__main__':
    unittest.main()