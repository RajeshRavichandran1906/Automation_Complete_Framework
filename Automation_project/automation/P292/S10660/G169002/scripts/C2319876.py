"""-------------------------------------------------------------------------------------------
Created on July 22, 2019
@author: Rajesh/Vpriya

Test Case Link  =  Test Control Tab
Test Case Title =  http://172.19.2.180/testrail/index.php?/tests/view/22267700
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2319876_TestClass(BaseTestCase):

    def test_C2319876(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        panel_grid_css = "div[class^='pd-cont-filter-grid'] div[data-grid-row='0']"
        panel_grid2_css = "div[class^='pd-cont-filter-grid'] div[data-grid-row='1']"
        text_control_css = "div[class^='pd-filter-wrapper'] div[class*='pd-filter-btn-label']"
        submit_control_css = "div[class^='pd-filter-wrapper'] div[class*='pd-filter-btn-submit']"
        submit_reset_css = "div[class^='pd-cont-filter-grid'] div[data-grid-row='1'] div[data-ibx-type='pdFilterPanel']"
        
        """
            STEP 1 : Login WF as domain developer;
            Click on Content view from side bar
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Expand 'P292_S10660' domain;
            Click on 'G192932' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)

        """
            STEP 3 : Choose the Blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 4 : Click Containers tab and drag Panel, Tab, Carousel and Accordion containers onto the page canvas next to each other and drag the Grid under the Panel 1
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
        pd_design.drag_container_item_to_blank_canvas("Tab", 4)
        pd_design.drag_container_item_to_blank_canvas("Carousel", 7)
        pd_design.drag_container_item_to_blank_canvas("Accordion", 11)
        pd_design.drag_container_item_to_blank_canvas("Grid", 49, element_location='bottom_middle', yoffset=-1)

        """
            STEP 5 : Click the Controls Tab
        """
        pd_design.select_option_from_carousel_items("Controls")
        
        """
            STEP 5.1 : Verify that you see Text and Submit controls.
        """
        control_obj = utils.validate_and_get_webdriver_objects(".pd-filter-wrapper .pd-filter-btn", "Control css")
        actual_list = []
        for x in control_obj:
            actual_list.append(x.text.strip())
        msg = "Step 5.1 : Verify that you see Text and Submit controls"
        utils.asequal(['Text', 'Submit'], actual_list, msg)
        
        """
            STEP 6 : Drag Text control into the grid panel.
        """
        pd_design.select_option_from_carousel_items("Controls")
        label_obj = utils.validate_and_get_webdriver_object(text_control_css, "Label css")
        grid_drop_obj = utils.validate_and_get_webdriver_object(panel_grid_css, "panel Grid css")
        utils.drag_drop_using_uisoup(label_obj, grid_drop_obj)
        pd_design.wait_for_visible_text(panel_grid_css, "Label")
        
        """
            STEP 6.1 : Verify "Label" added in the grid container.
        """
        actual_result = utils.validate_and_get_webdriver_object(panel_grid_css, "panel Grid css").text.strip()
        msg = "Step 6.1 : Verify 'Label' added in the grid container"
        utils.asin("Label", actual_result, msg)
        
        """
            STEP 7 : Drag Submit onto the second row of the grid panel.
        """
        submit_obj = utils.validate_and_get_webdriver_object(submit_control_css, "submit css")
        grid2_drop_obj = utils.validate_and_get_webdriver_object(panel_grid2_css, "grid2 css")
        utils.drag_drop_using_uisoup(submit_obj, grid2_drop_obj)
        pd_design.wait_for_visible_text(panel_grid2_css, "Submit")
        
        """
            STEP 7.1 : Verify Submit and Reset buttons are added.
        """
        submit_reset_obj = utils.validate_and_get_webdriver_objects(submit_reset_css, "Submit reset css")
        actual_result = []
        for x in submit_reset_obj:
            actual_result.append(x.text.strip())
        msg = "Step 7.1 : Verify Submit and Reset buttons are added."
        utils.asequal(['Submit', 'Reset'], actual_result, msg)
        
        """
            STEP 8 : Close designer without saving.
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        
        """
            STEP 9 : Sign out WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu() 
        
if __name__ == '__main__':
    unittest.main()