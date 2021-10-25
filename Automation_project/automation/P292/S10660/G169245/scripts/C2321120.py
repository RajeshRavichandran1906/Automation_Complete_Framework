"""-------------------------------------------------------------------------------------------
Created on July 22, 2019
@author: Rajesh/Vpriya

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22267758&group_by=cases:section_id&group_id=169245&group_order=asc
Test Case Title =  Test Label Position
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design,Run
from common.wftools.wf_mainpage import Wf_Mainpage, Run as R
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import time

class C2321120_TestClass(BaseTestCase):

    def test_C2321120(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        pd_run = Run(self.driver)
        main_page = Wf_Mainpage(self.driver)
        main_run = R(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
    
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
            STEP 4 : Choose Grid 2-1 template.
        """
        pd_design.select_page_designer_template("Grid 2-1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Drag and drop Category Sales report into Panel 1, present in Retail Samples > Portal > Small Widgets folder.
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G192932")
        pd_design.collapse_content_folder("P292_S10660")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        pd_design.wait_for_number_of_element("div[class^='pd-toolbar-filter']", 1)
        
        """
            STEP 5.1 : Verify quick filter appears in top right corner which has a number in red color.
        """
        pd_design.verify_quick_filter_properties({'text':'6', 'background_color':'mandy', 'font_size':'12px', 'position':'absolute', 'text_align':'center'}, "Step 5.1 : Verify quick filter appears in top right corner which has a number in red color.")
        
        """
            STEP 6 : Click on quick filter.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[class*='pd-regular-filter-wrapper']", "Category:")
        
        """
            STEP 6.1 : Verify filter bar appears with filter control.
        """
        pd_design.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 6.1 : Verify filter bar appears with filter control.")
        
        """
            STEP 7 : Open the properties panel and click on "Category:" control.
        """
        pd_design.click_property()
        pd_design.select_filter_grid_cell(1, click_on_location='middle')
        
        """
            STEP 8 : Select Style tab in Properties.
        """
        pd_design.select_property_tab("Style")
        
        """
            STEP 8.1 : Verify by default Label above is selected in Label Position.
        """
        utils.verify_picture_using_sikuli("C2321120_step8.png", "Step 8.1 : Verify by default Label above is selected in Label Position")
        
        """
            STEP 9 : Click on "Product Model:" filter control and select "Label left" in Label Position.
        """
        pd_design.select_filter_grid_cell(2, click_on_location='middle')
        
        left_label_obj = utils.validate_and_get_webdriver_object("div[title='Label left']", "left label css")
        core_utils.left_click(left_label_obj)
        
        """
            STEP 9.1 : Verify filter control label moved to left.
        """
        product_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box left']", "Product Model css")
        actual_result = product_model_obj.get_attribute("class")
        msg = "Step 9.1 : Verify filter control label moved to left."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box left", actual_result, msg)
                
        """
            STEP 10 : Click on "Region:" filter control and select "Label right" in Label Position.
        """
        pd_design.select_filter_grid_cell(3, click_on_location='middle')
        
        right_label_obj = utils.validate_and_get_webdriver_object("div[title='Label right", "Right label css")
        core_utils.left_click(right_label_obj)
        
        """
            STEP 10.1 : Verify filter control label moved to right.
        """
        region_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box right']", "Region css")
        actual_result = region_model_obj.get_attribute("class")
        msg = "Step 10.1 : Verify filter control label moved to right."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box right", actual_result, msg)
        
        """
            STEP 11 : Click on "Store Type:" filter control and select "Hide Label" in Label Position.
        """
        pd_design.select_filter_grid_cell(4, click_on_location='middle')
        
        hide_label_obj = utils.validate_and_get_webdriver_object("div[title='Hide label'", "Hide label css")
        core_utils.left_click(hide_label_obj)
        
        """
            STEP 11.1 : Verify filter control label not visible.
        """
        store_filter_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box none']", "Store filter css")
        actual_result = store_filter_obj.get_attribute("class")
        msg = "Step 11.1 : Verify filter control label not visible."
        utils.asin("fbx-child-sizing-content-box none", actual_result, msg)
        
        """
            STEP 12 : Click Preview.
        """
        pd_design.click_preview()
        
        """
            STEP 12.1 : Verify applied label position is retained in live preview.
        """
        product_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box left']", "Product Model css")
        actual_result = product_model_obj.get_attribute("class")
        msg = "Step 12.1 : Verify applied label position is retained in live preview.."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box left", actual_result, msg)
        
        region_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box right']", "Region css")
        actual_result = region_model_obj.get_attribute("class")
        msg = "Step 12.2 : Verify applied label position is retained in live preview.."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box right", actual_result, msg)
        
        store_filter_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box none']", "Store filter css")
        actual_result = store_filter_obj.get_attribute("class")
        msg = "Step 12.3 : Verify applied label position is retained in live preview."
        utils.asin("fbx-child-sizing-content-box none", actual_result, msg)

        """
            STEP 13 : Return back to designer.
        """
        pd_run.go_back_to_design_from_preview()
        
        """
            STEP 14 : Save page as "C2321120" and Close the designer.
        """
        pd_design.save_as_page_from_application_menu("C2321120")
        pd_design.close_page_designer_from_application_menu()
        
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 15 : Run "C2321120" page.
        """
        main_page.right_click_folder_item_and_select_menu("C2321120", "Run")
        time.sleep(10)
        main_run.switch_to_frame()
        
        """
            STEP 15.1 : Verify applied label position is retained in run time.
        """
        product_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box left']", "Product Model css")
        actual_result = product_model_obj.get_attribute("class")
        msg = "Step 15.1 : Verify applied label position is retained in run time."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box left", actual_result, msg)
        
        region_model_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box right']", "Region css")
        actual_result = region_model_obj.get_attribute("class")
        msg = "Step 15.2 : Verify applied label position is retained in run time."
        utils.asin("fbx-row", actual_result, msg)
        utils.asin("fbx-child-sizing-content-box right", actual_result, msg)
        
        store_filter_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box none']", "Store filter css")
        actual_result = store_filter_obj.get_attribute("class")
        msg = "Step 15.3 : Verify applied label position is retained in run time"
        utils.asin("fbx-child-sizing-content-box none", actual_result, msg)
        
        """
            STEP 16 : Close run window.
        """
        pd_design.switch_to_default_page()
        main_run.close()
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
 
        """
            STEP 17 : Sign out WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu() 
 
if __name__ == '__main__':
    unittest.main()