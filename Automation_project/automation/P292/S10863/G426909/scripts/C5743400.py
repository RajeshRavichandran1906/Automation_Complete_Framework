"""-------------------------------------------------------------------------------------------
Created on Aug 12, 2019
@author: Aftab

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743400
Test Case Title =  Check Delete menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main
from common.locators import wf_mainpage_locators
import pyautogui

class C5743400_TestClass(BaseTestCase):

    def test_C5743400(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_obj=main(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        quick_filter_css = "[title='Quick filter']"
        panel_grid_css = "div[class^='pd-cont-filter-grid'] div[data-grid-row='0']"
        text_control_css = "div[class^='pd-filter-wrapper'] div[class*='pd-filter-btn-label']"
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
 
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Expand 'P292_S10863' domain -> 'G426906' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("{0}->{1}_{2}".format(group_id, project_id, suite_id))
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        utils.synchronize_until_element_is_visible(quick_filter_css, main_page.home_page_long_timesleep)
        
        """
            STEP 6 : Click on quick filter icon
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_disappear(quick_filter_css, main_page.home_page_long_timesleep)
        
        """
            STEP 7 : Right click on Category filter control and choose 'Delete Control' menu
        """
        pd_design.select_filter_grid_cell(1, click_on_location='middle')
        pd_design.select_filter_grid_cell(1, click_on_location='middle', click_type='right')
        main_obj.select_context_menu_item("Delete control")
        
        """
            Step 07.01 : Verify that cell is deleted and the quick filter icon shows 1 as below
        """
        pd_design.verify_filter_control_labels(['Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 07.01 : Verify that cell is deleted and the quick filter icon shows 1 as below")
        pd_design.verify_quick_filter_value('1', "Step 07.01")
        
        """
            STEP 8 : Click on quick filter icon to re add that filter
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_disappear(quick_filter_css, main_page.home_page_long_timesleep)
        
        """
            Step 08.01 : Verify 'Category' filter control has been re added as below and the control is highlighted in red
        """
        pd_design.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 08.01 : Verify 'Category' filter control has been re added as below and the control is highlighted in red")
        pd_design.verify_filter_control_panel_is_selected("Category:", "Step 08.02 : Verify 'Category' filter control has been re added as below and the control is highlighted in red")
        
        """
            STEP 9 : Right click on Category filter control and choose 'Delete Control' menu
        """
        pd_design.select_filter_grid_cell(1, click_on_location='middle')
        pd_design.select_filter_grid_cell(1, click_on_location='middle', click_type='right')
        pd_design.wait_for_visible_text(pop_top_css, "Style")
        main_obj.select_context_menu_item("Delete control")
        
        """
            Step 09.01 : Verify that cell is deleted and the quick filter icon shows 1 as below
        """
        pd_design.verify_filter_control_labels(['Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 07.01 : Verify that cell is deleted and the quick filter icon shows 1 as below")
        pd_design.verify_quick_filter_value('1', "Step 09.01")
        
        """
            STEP 10 : Drag and drop a grid panel next to category sales panel
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Grid", 4)
        
        """
            STEP 11 : Drag and drop Text control to the grid panel
        """
        pd_design.select_option_from_carousel_items("Controls")
        label_obj = utils.validate_and_get_webdriver_object(text_control_css, "Label css")
        grid_drop_obj = utils.validate_and_get_webdriver_object(panel_grid_css, "panel Grid css")
        utils.drag_drop_using_uisoup(label_obj, grid_drop_obj)
        pd_design.wait_for_visible_text(panel_grid_css, "Label")
        
        """
            Step 11.01 : Verify text control added in grid as below
        """
        actual_result = utils.validate_and_get_webdriver_object(panel_grid_css, "panel Grid css").text.strip()
        msg = "Step 11.01 : Verify text control added in grid as below"
        utils.asin("Label", actual_result, msg)
        
        """
            STEP 12 : Right click on the first cell in grid where the control has been added
        """
        pd_design.select_filter_grid_cell(1, grid_container_title='Panel 2', click_on_location='middle', click_type='right')
        pd_design.wait_for_visible_text(pop_top_css, "Style")
        
        """
            Step 12.01 : Verify context menu appears as below
        """
        main_obj.verify_context_menu_item(['Edit label', 'Settings', 'Style', 'Delete control'], 'Step 12.01 : Verify context menu appears as below')
        
        """
            STEP 13 :  Select 'Delete Control'
        """
        main_obj.select_context_menu_item("Delete control")
        pd_design.wait_for_visible_text(panel_grid_css, '')
        
        """
            Step 13.01 : Verify control has been deleted
        """
        actual_result_ = utils.validate_and_get_webdriver_object(panel_grid_css, "panel Grid css").text.strip()
        msg = "Step 13.01 : Verify control has been deleted"
        utils.asequal('', actual_result_, msg)
        
        """
            STEP 14 : Right click on first empty grid cell
        """
        pd_design.select_filter_grid_cell(1, grid_container_title='Panel 2', click_on_location='middle', click_type='right')
        pd_design.wait_for_visible_text(pop_top_css, "Style")
        
        """
            Step 14.01 : Verify context menus appears as below
        """
        main_obj.verify_context_menu_item(['Add filter controls', 'Insert row above', 'Insert row below', 'Style', 'Delete cell', 'Delete grid'], "Step 14.01 : Verify context menus appears as below")
        
        """
            STEP 15 : Choose 'Delete cell'
        """
        main_obj.select_context_menu_item("Delete cell")
        
        """
            Step 15.01 : Verify first cell has been deleted and the grid panel now has only 3 cells
        """
        actual_result = len(utils.validate_and_get_webdriver_objects("div[class^='pd-cont-filter-grid'] div[class^='pd-filter-cell']", "Grid cell Css"))
        msg = "Step 15.01 : Verify first cell has been deleted and the grid panel now has only 3 cells"
        utils.asequal(3, actual_result, msg)
        
        """
            Step 16 : Drag and drop "Product Model:" filter control into the first cell of the grid container.
        """
        sourceobj = utils.validate_and_get_webdriver_object(".pd-filter-cell:nth-child(2)", "Source of product model")
        targetobj = utils.validate_and_get_webdriver_object(".pd-cont-filter-grid .pd-filter-cell:nth-child(1)", "Target of product model")
        source_cord = core_utils.get_web_element_coordinate(sourceobj)
        target_cord = core_utils.get_web_element_coordinate(targetobj)
        pyautogui.mouseDown(source_cord['x'], source_cord['y'], duration=1)
        pyautogui.moveTo(target_cord['x'], target_cord['y'], duration=1)
        pyautogui.mouseUp(target_cord['x'], target_cord['y'])
        
        """
            Step 16.01 : Verify filter control added into the grid container.
        """
        actual_result = utils.validate_and_get_webdriver_object('.pd-cont-filter-grid .pd-filter-cell:nth-child(1)', "label of control").text.strip()
        msg = "Step 16.01 : Verify label of filter control added in grid as below"
        utils.asequal("Product Model:", actual_result, msg)
        
        """
            Step 17 : Right click on Product Model filter control and choose 'Delete Control' menu.
        """
        pd_design.select_filter_grid_cell(1, grid_container_title='Panel 2', click_on_location='middle', click_type='right')
        pd_design.wait_for_visible_text(pop_top_css, "Style")
        main_obj.select_context_menu_item("Delete control")
        
        """
            Step 17.01 : Verify the filter control deleted in grid container and the quick filter icon shows 2.
        """
        actual_result_ = utils.validate_and_get_webdriver_object('.pd-cont-filter-grid .pd-filter-cell:nth-child(1)', "label of control").text.strip()
        msg = "Step 17.01 : Verify filter control has been deleted"
        utils.asequal('', actual_result_, msg)
        pd_design.verify_quick_filter_value('2', "Step 17.02")
        
        """
            STEP 18 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 19 : Sign out WF
        """
        main_page.signout_from_username_dropdown_menu()      
        
if __name__ == '__main__':
    unittest.main()