"""-------------------------------------------------------------------------------------------
Created on July 23, 2019
@author: Prabhakaran

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22267772&group_by=cases:section_id&group_order=asc&group_id=169245
Test Case Title =  Test Header/Toolbar properties
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design,Preview,Run
from common.wftools.wf_mainpage import Wf_Mainpage, Run as R
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import time

class C2321162_TestClass(BaseTestCase):

    def test_C2321162(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        pd_preview = Preview(self.driver)
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
            STEP 4 : Choose the Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Click Containers tab and drag Panel, Tab, Carousel and Accordion containers onto the page canvas next to each other and drag the Grid under the Panel 1.
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
        pd_design.drag_container_item_to_blank_canvas("Tab", 4)
        pd_design.drag_container_item_to_blank_canvas("Carousel", 7)
        pd_design.drag_container_item_to_blank_canvas("Accordion", 11)
        pd_design.drag_container_item_to_blank_canvas("Grid", 49, element_location= "bottom_middle", yoffset= -2)
 
        """
            STEP 6 : Click on the Page Heading.
        """
        page_heading_obj = utils.validate_and_get_webdriver_object(".pd-page-header", "page heading css")
        core_utils.left_click(page_heading_obj)
        
        """
            STEP 7 : Open the properties panel.
        """
        pd_design.click_property()
        
        """
            Step 7.1 : Verify that the properties Panel is loaded and the Page Settings is shown
        """
        pd_design.verify_setting_tab_properties("Page Settings", ['ID=PAGE', 'Classes=', 'Title=on', 'Toolbar=on'], "Step 7.1 : Verify that the properties Panel is loaded and the Page Settings is shown")
        
        """
            STEP 8 : Toggle OFF Title in Page Settings properties.
        """
        pd_design.select_property_tab_settings_option("Page Settings", "radio_button", "Title")
        
        """
            Step 8.1 : Verify that the Page header no longer shows
        """
        pd_design.verify_page_heading_title([''], "Step 8.1 : Verify that the Page header no longer shows")

        """
            STEP 9 : Click the preview button.
        """
        pd_design.click_preview()
        
        """
            Step 9.1 : Verify that the Page header no longer shows
        """
        pd_preview.verify_page_heading_title([''], "Step 9.1 : Verify that the Page header no longer shows")

        """
            STEP 10 : Return back to Designer.
        """
        pd_run.go_back_to_design_from_preview()
        
        """
            STEP 11 : Save the page as "C2321162" and close page designer.
        """
        pd_design.click_property()
        pd_design.save_as_page_from_application_menu("C2321162")
        pd_design.close_page_designer_from_application_menu()
        
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 12 : Run "C2321162" page.
        """
        main_page.right_click_folder_item_and_select_menu("C2321162", "Run")
        time.sleep(10)
        main_run.switch_to_frame()
        
        """
            STEP 12.1 : Verify that the Page header no longer shows
        """
        pd_run.verify_page_heading_title([''], "Step 12.1 : Verify that the Page header no longer shows")
        pd_design.switch_to_default_page()

        """
            STEP 13 : Close Run window.
        """
        main_run.close()
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
            
        """
            STEP 14 : Edit "C2321162" page.
        """
        main_page.right_click_folder_item_and_select_menu("C2321162", "Edit")
        core_utils.switch_to_new_window()
        utils.synchronize_until_element_is_visible(".pd-toolbar-settings", main_page.home_page_long_timesleep)
        
        """
            STEP 15 : Open Properties.
        """
        pd_design.click_property()
 
        """
            STEP 16 : Toggle ON Title in Page Settings properties.
        """
        pd_design.select_property_tab_settings_option("Page Settings", "radio_button", "Title")
        
        """
            STEP 16.1 : Verify that the Page header shows
        """
        pd_design.verify_page_heading_title(['Page Heading'], "Step 16.1 : Verify that the Page header shows")
        
        """
            STEP 17 : Toggle OFF Toolbar in Page Settings properties.
        """
        pd_design.select_property_tab_settings_option("Page Settings", "radio_button", "Toolbar")
        
        """
            STEP 17.1 : Verify the toolbar is not visible in the page.
        """
        pd_design.verify_page_header_visible_buttons([], "Step 17.1 : Verify the toolbar is not visible in the page.")
        
        """
            STEP 18 : Click Preview.
        """
        pd_design.click_preview()

        """
            STEP 18.1 : Verify the toolbar is not visible in the page.
        """
        pd_preview.verify_page_header_visible_buttons([], "Step 18.1 : Verify the toolbar is not visible in the page.")
        
        """
            STEP 19 : Return back to Designer.
        """
        pd_run.go_back_to_design_from_preview()
        
        """
            STEP 20 : Save and Close the page.
        """
        pd_design.click_toolbar_save()
        time.sleep(10)
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 21 : Run "C2321162" page.
        """
        main_page.right_click_folder_item_and_select_menu("C2321162", "Run")
        time.sleep(10)
        main_run.switch_to_frame()
        
        """
            STEP 21.1 : Verify the toolbar is not visible in the page.
        """
        pd_run.verify_page_header_visible_buttons([], "Step 21.1 : Verify the toolbar is not visible in the page")
        
        """
            STEP 22 : Close Run window.
        """
        main_run.switch_to_default_content()
        main_run.close()
        
        """
            STEP 23 : Sign out WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu() 
        
if __name__ == '__main__':
    unittest.main()