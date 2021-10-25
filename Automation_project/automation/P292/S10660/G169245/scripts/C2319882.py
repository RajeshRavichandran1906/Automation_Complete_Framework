"""-------------------------------------------------------------------------------------------
Created on July 19, 2019
@author: Prabhakaran

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22267705&group_by=cases:section_id&group_order=asc&group_id=169245
Test Case Title =  Create Sections/Collapse
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
from common.pages.wf_mainpage import Wf_Mainpage as main
from common.pages.page_designer_design import PageDesignerDesign

class C2319882_TestClass(BaseTestCase):

    def test_C2319882(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        main_obj = main(self.driver)
        pd_design_designer = PageDesignerDesign(self.driver)
    
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
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            STEP 2 : Click on Content view from side bar
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
            STEP 4 : Choose the Blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Click Containers tab and drag Panel, Tab, Carousel and Accordion containers onto the page canvas next to each other and drag the Grid under the Panel 1
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
        pd_design.drag_container_item_to_blank_canvas("Tab", 4)
        pd_design.drag_container_item_to_blank_canvas("Carousel", 7)
        pd_design.drag_container_item_to_blank_canvas("Accordion", 11)
        pd_design.drag_container_item_to_blank_canvas("Grid", 49, element_location='bottom_middle',yoffset=-1 )
        
        """
            STEP 6 : Right click on the grid next to Panel 4
        """
        grid_obj = utils.validate_and_get_webdriver_object("div[class*='pd-page-acc-section'] div[class='pd-page-section-grid-box']:nth-child(70)", "Grid cell css")
        core_utils.python_right_click(grid_obj)
        pd_design.wait_for_visible_text(".pop-top", "Format")
        
        """
            STEP 6.01 : Verify following menu appears
        """
        main_obj.verify_context_menu_item(['Settings', 'Format', 'Delete section', 'Insert section above', 'Insert section below'], "Step 6.01 : Verify following menu appears")
        
        """
            STEP 7 : Choose Insert section above
        """
        main_obj.select_context_menu_item("Insert section above")

        """
            STEP 7.01 : Verify that section was created above the one you were working with
        """
        pd_design.verify_number_of_page_sections(2, "Step 7.01 : Verify that section was created above the one you were working with")
        section_obj = pd_design_designer._get_page_section_object(1)
        actual_result = section_obj.text
        msg = "Step 7.02 : Verify that section was created above the one you were working with"
        utils.asequal("", actual_result, msg)

        """
            STEP 8 : Right click on the grid next to Panel 4
        """
        grid_obj = utils.validate_and_get_webdriver_object("div[class*='pd-page-acc-section'] div[class='pd-page-section-grid-box']:nth-child(130)", "Grid cell css")
        core_utils.python_right_click(grid_obj)
        pd_design.wait_for_visible_text(".pop-top", "Format")
        
        """
            STEP 9 : Choose Insert section below
        """
        main_obj.select_context_menu_item("Insert section below")
        
        """
            STEP 9.01 : Verify that section was created below the one you were working with
        """
        pd_design.verify_number_of_page_sections(3, "Step 9.01 : Verify that section was created below the one you were working with")
        section_obj = pd_design_designer._get_page_section_object(3)
        actual_result = section_obj.text
        msg = "Step 9.02 : Verify that section was created below the one you were working with"
        utils.asequal("", actual_result, msg)
        
        """
            STEP 10 : Right click on Section 1 and choose Settings
        """
        pd_design.select_page_section(1)
        pd_design.click_property()

        """
            STEP 10.01 : The properties panel will appear on the right with Collapsible.
        """
        pd_design.verify_setting_tab_properties("Section Settings", ['ID=SECTION', 'Classes=', 'Collapsible=off', 'Row height=off'], "Step 10.01 : The properties panel will appear on the right with Collapsible.")

        """
            STEP 11 : Turn on Collapsible
        """
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        """
            STEP 11.01 : Verify that you see the centered collapsible arrow in Section 1
        """
        pd_design.select_page_section(1)
        utils.verify_picture_using_sikuli("C2319882_step11.png", "Step 11.01 : Verify that you see the centered collapsible arrow in Section 1")
        
        """
            STEP 12 : With the properties panel opened click on each section and toggle on Collapsible
        """
        pd_design.select_page_section(2)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        pd_design.select_page_section(3)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")

        """
            STEP 12.01 : Verify collapsible arrow added in all the sections.
        """
        pd_design.select_page_section(2)
        utils.verify_picture_using_sikuli("C2319882_step12.01.png", "Step 12.01 : Verify collapsible arrow added in all the sections")
        
        pd_design.select_page_section(3)
        utils.verify_picture_using_sikuli("C2319882_step12.02.png", "Step 12.02 : Verify collapsible arrow added in all the sections")
        
        """
            STEP 13 : Close designer without saving.
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 14 : Sign out WF.
        """
        main_page.signout_from_username_dropdown_menu() 

if __name__ == '__main__':
    unittest.main()