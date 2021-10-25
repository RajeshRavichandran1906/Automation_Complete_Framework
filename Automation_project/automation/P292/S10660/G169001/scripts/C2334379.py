"""-------------------------------------------------------------------------------------------
Created on July 26, 2019
@author: Niranjan Das

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2334379&group_by=cases:section_id&group_id=169001&group_order=asc
Test Case Title =  Create IBX page with Grid 4-2-1 template
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design 
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2334379_TestClass(BaseTestCase):

    def test_C2334379(self):
        
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
        
        """
            STEP 1 : Login WF as domain developer.
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            STEP 2 : Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Expand 'P292_S10660' domain;
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
            STEP 3.1 : Verify that page designer opens.
        """
        page_designer_obj = utils.validate_and_get_webdriver_object(pop_top_css, "Page designer popup css")
        actual_result = page_designer_obj.is_displayed()
        msg = "Step 3.1 : Verify that page designer opens."
        utils.asequal(True, actual_result, msg)
        
        """
            STEP 4 : Choose the Grid 4-2-1 template
        """
        pd_design.select_page_designer_template("Grid 4-2-1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 4.1 : Verify the Content tab is already highlighted and tree shows on the left.
        """
        content_tab_obj = utils.validate_and_get_webdriver_object("div[title='Content']", "Content tab css")
        actual_result = content_tab_obj.get_attribute('aria-selected')
        msg = "Step 4.1 : Verify the Content tab is already highlighted and tree shows on the left"
        utils.asequal("true", actual_result, msg)
        
        content_tree_obj = utils.validate_and_get_webdriver_object("div[class*='pd-left-pane ibxtool-left-pane ibx-widget']", "Content tree css")
        actual_result = content_tree_obj.is_displayed()
        msg = "Step 4.2 : Verify the Content tab is already highlighted and tree shows on the left"
        utils.asequal(True, actual_result, msg)
        
        """
            STEP 5 : Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G192932")
        pd_design.collapse_content_folder("P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 6 : Drag Blue, Gray, Green, Red and Silver onto the panels respectively.
        """
        pd_design.drag_content_item_to_container_and_verify_drop_color("Blue", "Panel 1", "Step 6.1")
        pd_design.drag_content_item_to_container_and_verify_drop_color("Gray", "Panel 2", "Step 6.2")
        pd_design.drag_content_item_to_container_and_verify_drop_color("Green", "Panel 3", "Step 6.3")
        pd_design.drag_content_item_to_container_and_verify_drop_color("Red", "Panel 4", "Step 6.4")
        pd_design.drag_content_item_to_container_and_verify_drop_color("Silver", "Panel 5", "Step 6.5")
        
        """
            STEP 6.1 : As you drag you should see a blue rectangle and it shows where you can drop the item.
            Verify content added into the Grid 4-2-1 template:
        """
        pd_design.verify_containers_title(['Blue', 'Gray', 'Green', 'Red', 'Silver', 'Panel 6', 'Panel 7'], "Step 6.6 : Verify content added into the Grid 4-2-1 template:")

        """
            STEP 7 : Click Tool bar and click Close.
            STEP 8 : Click NO in the popup.
        """
        pd_design.close_page_designer_without_save_page()
        pd_design.switch_to_previous_window(driver_close = False)
        
        """
            STEP 9 : Signout WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()