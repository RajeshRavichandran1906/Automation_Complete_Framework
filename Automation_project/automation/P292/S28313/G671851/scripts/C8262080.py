'''
Created on May 22, 2019

@author: Niranjan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262080
TestCase Name = Restore PGX for Container Theme and Grid style
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.locators import wf_mainpage_locators
from common.lib import utillity
from common.lib import core_utility
from common.wftools.page_designer import Run, Design

class C8262080_TestClass(BaseTestCase):

    def test_C8262080(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_design_obj = Design(self.driver)
        page_designer_run_obj = Run(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        fex_name = 'container theme and grid styling1'
        action_tile = 'Designer'
        label_css = "div[data-ibx-type='pdFilterPanel'] div[class*='pd-amper-label'] div[class='ibx-label-text']"

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
        Step 04: Right click on 'container theme and grid styling1' > Edit.
        """
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Edit')
        core_util_obj.switch_to_new_window()
        
        """
        Step 04.01: Verify all the changes still exist
        """
        util_obj.synchronize_with_number_of_element(label_css, 6, main_page_obj.home_page_long_timesleep)
        page_designer_run_obj.verify_page_heading_title(['Page Heading'], 'Step 04.01 : Verify page title')
        page_designer_run_obj.verify_containers_title(["Category Sales", "Panel 2", "Panel 3"], 'Step 04.02 : Verify container titles') 
        expected_label_list=['Category:', 'Product Model:']
        page_designer_run_obj.verify_filter_control_labels(expected_label_list, msg="Step 04.03 : Verify filter lables in grid container", grid_container_title="Panel 2")
        page_designer_run_obj.verify_container_style_color("Category Sales", "curious_blue", step_num="04.04")
        page_designer_run_obj.verify_container_style_color("Panel 2", "fern2", step_num="04.05")
        page_designer_run_obj.verify_container_style_color("Panel 3", "curious_blue", step_num="04.06")
        
        """
        Step 05 : Close the Page Designer from application menu.
        """
        page_designer_design_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()