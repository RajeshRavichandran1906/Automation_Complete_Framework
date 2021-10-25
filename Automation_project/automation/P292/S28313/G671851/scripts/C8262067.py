'''
Created on May 17, 2019.

@author: Prabakaran

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262067
TestCase Name = Check defaults for blank grids
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C8262067_TestClass(BaseTestCase):

    def test_C8262067(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        filter_cell_css="div[data-ibx-type='pdFilterGrid'] div[data-ibx-type=\"pdFilterCell\"]"
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
        Step 05: Click Containers tab. Drag and drop the grid container onto the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        page_designer_obj.drag_container_item_to_blank_canvas("Grid", 1)
        
        """
        Step 06: From the designer toolbar, click on Page filter configuration button.
        Verify that Page Filter Configuration opens.
        """
        page_designer_obj.click_filter_configuration()
        
        """
        Step 06.01: Verify that Page Filter Configuration opens.
        """
        page_filter_configuration_css=".pop-top div[data-ibx-name='caption'] .ibx-label-text"
        util_obj.verify_element_text(page_filter_configuration_css, expected_text="Page Filter Configuration", msg='Step 06.01 : Verify that Page Filter Configuration opens.')
        """
        Step 07: Click on Create empty filter bar.
        """ 
        page_designer_obj.select_filter_configurations_property("Create empty filter bar")
    
        """
        Step 08: From the designer toolbar,click on Properties button > click style tab.
        """ 
        page_designer_obj.click_property()
        page_designer_obj.select_property_tab("Style")
        
        """
        Step 08.01: Verify that the Container style section appears with 8 options (default,style 2 to style 8)
        """ 
        page_designer_obj.verify_container_style_options(step_num="08.01")
        
        """
        Step 09: Click on the page filter area.
        """ 
        filter_area=util_obj.validate_and_get_webdriver_objects(filter_cell_css, 'filter_cell')
        core_util_obj.left_click(filter_area[0])
        
        """
        Step 09.01: Verify that the Grid style section appears with 8 options (default, style 2 to style 8)
        """ 
        page_designer_obj.verify_grid_style_options(step_num="09.01")
        
        """
        Step 10: Close the Page Designer from application menu without saving.
        """ 
        page_designer_obj.close_page_designer_without_save_page()
        
        """
        Step 11: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()