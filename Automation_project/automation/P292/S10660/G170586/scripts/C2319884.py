"""-------------------------------------------------------------------------------------------
Created on August 01, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2319884&group_by=cases:section_id&group_id=170586&group_order=asc
Test Case Title =  Save page with collapsed sections
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.pages.page_designer_design import PageDesignerDesign
from common.lib.webfocus.resource_dialog import Resource_Dialog
from common.pages.wf_mainpage import Wf_Mainpage as main
from common.lib.javascript import JavaScript
import time

class C2319884_TestClass(BaseTestCase):

    def test_C2319884(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        page_designer = PageDesignerDesign(self.driver)
        resource_dialog = Resource_Dialog(self.driver)
        main_obj = main(self.driver)
        javascript = JavaScript(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        FOLDER_XPATH = """//div[contains(@class,'sd-tab-page')]//div[contains(text(),'P292_S10660~!@#$%^&*()_+=-`{}|][":;')]"""
        
        """
            STEP 1 : Login WF as domain developer;
            Click on Content view from side bar.
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Expand 'P292_S10660' domain;
            Click on 'G192933' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder("P292_S10660->G192933")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
 
        """
            STEP 3 : Select Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 4 : Click on "G192933 > P292_S10660" domain to two level up;
            Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G192933")
        pd_design.collapse_content_folder("P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 5 : Drag Blue, Gray, Green and Red onto the page canvas respectively.
        """
        pd_design.drag_content_item_to_blank_canvas("Blue", 1)
        pd_design.drag_content_item_to_blank_canvas("Gray", 4)
        pd_design.drag_content_item_to_blank_canvas("Green", 7)
        pd_design.drag_content_item_to_blank_canvas("Red", 10)
        
        """
            STEP 6 : Right click on the section and select Insert section above;
            Right click on the section and select Insert section below;
            Right click on the section and select Settings.
        """
        sec_obj1 = page_designer._get_page_section_object(1)
        core_utils.right_click(sec_obj1, element_location="top_left", xoffset=0, yoffset=0)
        pd_design.wait_for_visible_text(".ibx-popup", "Format")
        
        main_obj.select_context_menu_item("Insert section above")
        
        sec_obj2 = page_designer._get_page_section_object(2)
        core_utils.right_click(sec_obj2, element_location="top_left", xoffset=0, yoffset=0)
        pd_design.wait_for_visible_text(".ibx-popup", "Format")
        
        main_obj.select_context_menu_item("Insert section below")
        time.sleep(10)
        
        """
            STEP 7 : Toggle ON Collapsible for all the sections.
        """
        pd_design.select_page_section(1)
        pd_design.click_property()
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        pd_design.select_page_section(2)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        pd_design.select_page_section(3)
        pd_design.select_property_tab_settings_option("Section Settings", "radio_button", "Collapsible")
        
        """
            STEP 8 : Click the Collapse icon "^" for Section 1.
        """
        pd_design.select_page_section(1)
        section_1 = page_designer._get_page_section_object(1)
        section1_obj = section_1.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='acc-rotate-glyph']")
        core_utils.python_left_click(section1_obj)
        time.sleep(7)
        
        """
            STEP 8.1 : Verify Section 1 is collapsed.
        """
        sec_obj = section_1.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='ibx-accordion-page-button']")
        actual_result = sec_obj.get_attribute("aria-expanded")
        msg = "Step 8.1 : Verify Section 1 is collapsed."
        utils.asequal("false", actual_result, msg)
        
        """
            STEP 9 : Click the Collapse icon "^" for Section 3.
        """
        pd_design.select_page_section(3)
        section_3 = page_designer._get_page_section_object(3)
        section3_obj = section_3.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='acc-rotate-glyph']")
        core_utils.python_left_click(section3_obj)
        time.sleep(7)
        
        """
            STEP 9.1 :Verify Section 3 is collapsed.
        """
        section_3 = page_designer._get_page_section_object(3)
        sec_obj = section_3.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='ibx-accordion-page-button']")
        actual_result = sec_obj.get_attribute("aria-expanded")
        msg = "Step 9.1 : Verify Section 3 is collapsed."
        utils.asequal("false", actual_result, msg)
        
        """
            STEP 10 : Click the Tool bar Icon and choose Save as...
            STEP 11 : Enter "C2319884" in Title and click Save as.
        """
        pd_design.save_as_page_from_application_menu("C2319884")
        
        """
            STEP 12 : Click the Tool bar icon and choose Close.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 13 : Edit "C2319884" page.
        """
        main_page.right_click_folder_item_and_select_menu("C2319884", "Edit")
        time.sleep(13)
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        time.sleep(7)
        
        """
            STEP 13.1 : Verify that the collapsed sections remains collapsed.
        """      
        section_1 = page_designer._get_page_section_object(1)  
        sec_obj = section_1.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='ibx-accordion-page-button']")
        actual_result = sec_obj.get_attribute("aria-expanded")
        msg = "Step 13.1 : Verify that the collapsed sections remains collapsed."
        utils.asequal("false", actual_result, msg)
        
        section_3 = page_designer._get_page_section_object(3)
        sec_obj = section_3.find_element_by_css_selector("div[class*='pd-page-acc-section'] div[class*='ibx-accordion-page-button']")
        actual_result = sec_obj.get_attribute("aria-expanded")
        msg = "Step 13.2 : Verify that the collapsed sections remains collapsed."
        utils.asequal("false", actual_result, msg)
        
        """
            STEP 14 : Click the Tool bar icon and choose Save as...
        """
        pd_design.select_option_from_application_menu("Save as...")
        pd_design.wait_for_visible_text("div[class*='ibx-dialog-cancel-button']", "Cancel")
        
        """
            STEP 15 : Navigate to "P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./" domain.
        """
        resource_dialog.select_crumb_item("Workspaces")
        folder = self.driver.find_element_by_xpath(FOLDER_XPATH)
        javascript.scrollIntoView(folder)
        core_utils.python_doubble_click(folder)
        
        """
            STEP 16 : Enter "C2319884~!@#$%^&*()_+=-`{}|][":;'?><,./" in Title and click Save as.
        """
        pd_design.resource_dialog().enter_title("""C2319884~!@#$%^&*()_+=-`{}|][":;'?><,./""")
        pd_design.resource_dialog().click_button("Save as")
        
        """
            STEP 17 : Close the page
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """   
            STEP 18 : Sign out WF.
        """
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()