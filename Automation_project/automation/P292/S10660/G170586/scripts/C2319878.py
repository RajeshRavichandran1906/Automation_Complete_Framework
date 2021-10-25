'''
Created on July 29, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2319878
TestCase Name = Test Replace/Add Content onto the Canvas Area
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.locators.page_designer_design import ContentTab
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C2319878_TestClass(BaseTestCase):

    def test_C2319878(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        pd_locator_obj=ContentTab()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        action_tile = 'Designer'
        action_bar  = 'Page'
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        folder_name="Domains->P292_S10660->G192933"
        PD_SECTION_CSS = "div[data-ibx-type='pdPageSection']"
        
        
        """
        Step 1: Login WF as domain developer.
        Click on Content view from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S10660' domain;
        Click on 'G192933' folder and choose Page action tile from under designer category.
        """
        main_page_obj.expand_repository_folder(folder_name)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 3: Select Blank template.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 4: Click the Containers tab
        """
        page_designer_obj.select_option_from_carousel_items("Containers")
        util_obj.synchronize_with_visble_text(pd_locator_obj.BASIC_CONTAINER_CSS, "Panel", main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 5: Drag each container type onto the page canvas next to each other.
        """
        page_designer_obj.drag_container_item_to_blank_canvas("Panel", 1)
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Panel 1", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas("Tab", 4)
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Tab 1", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas("Carousel", 7)
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Panel 3", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas("Accordion", 10)
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Area 1", main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 5.01 Expected: Verify Panel 1 appears;
        Verify Panel 2 appears with Tab 1;
        Verify carousel container appears;
        Verify accordion appears with Area 1
        """
        page_designer_obj.verify_containers_title(['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4'], msg="Step: 5.01 : Verify all contianers apperas")
        
        """ 
        Step 6: Click the Contents tab
        """
        page_designer_obj.select_option_from_carousel_items("Content")
        util_obj.synchronize_with_visble_text(pd_locator_obj.PARENT_CSS, "Content", main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 7: Click on "G192933 > P292_S10660" domain to two level up;
        Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        page_designer_obj.collapse_content_folder("G192933->P292_S10660")
        
        """ 
        Step 8: Drag the Blue into Panel 1 and Gray onto Panel 2
        """
        page_designer_obj.drag_content_item_to_container("Blue", "Panel 1",content_folder_path="Retail Samples->Portal->Test Widgets")
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Blue", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_content_item_to_container("Gray", "Panel 2",content_folder_path=None)
        util_obj.synchronize_with_visble_text(PD_SECTION_CSS, "Gray", main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 8.01 Expected: Verify the contents added into the containers.
        """
        page_designer_obj.switch_to_container_frame("Blue")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: blue;',"Step 08.01 : Verify the contents added into the containers.")
        page_designer_obj.switch_to_default_page()
        
        page_designer_obj.switch_to_container_frame("Panel 2")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: dimgray;',"Step 08.02 : Verify the contents added into the containers.")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 9: Drag Green over Panel 2
        """
        page_designer_obj.drag_content_item_to_container("Green", "Panel 2",content_folder_path=None)
        
        """ 
        Step 9.01: Verify you get a pop message.
        """
        page_designer_obj.verify_add_content_panel_dialog(['Replace content', 'Add content', 'Cancel'],"Step 09.01 : Verify you get a pop message.")

        
        """ 
        Step 10: Choose Replace content
        """
        page_designer_obj.select_options_add_content_dialog("Replace content")
        
        """ 
        Step 10.01: Verify that Green now is in the place of Gray.
        """
        page_designer_obj.switch_to_container_frame("Panel 2")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: green;',"Step 08.02 : Verify the contents added into the containers.")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 11: Drag Gray onto Panel 2
        """
        page_designer_obj.drag_content_item_to_container("Gray", "Panel 2",content_folder_path=None)
        
        """ 
        Step 11.01: Verify you get a pop message.
        """
        page_designer_obj.verify_add_content_panel_dialog(['Replace content', 'Add content', 'Cancel'],"Step 11.01 : Verify you get a pop message.")

        
        """ 
        Step 12: Choose Add content.
        """
        page_designer_obj.select_options_add_content_dialog("Add content")
        
        
        """ 
        Step 12.01 Expected: Verify that you now have 2 tabs (Green and Gray).
        """
        page_designer_obj.tab_container("Panel 2").verify_tabs(['Green', 'Gray'], 12.01)
        
        """ 
        Step 13: Drag Yellow onto Panel 2
        """
        page_designer_obj.drag_content_item_to_container("Yellow", "Panel 2",content_folder_path=None)
        
        """ 
        Step 14: Choose Cancel
        """
        page_designer_obj.select_options_add_content_dialog("Cancel")
        
        """ 
        Step 14.01 Expected: Verify that the Yellow was not added.
        """
        page_designer_obj.tab_container("Panel 2").verify_tabs(['Green', 'Gray'], 14.01)
        
        """ 
        Step 15: Drag Yellow onto Panel 3
        """
        page_designer_obj.drag_content_item_to_container("Yellow", "Panel 3",content_folder_path=None)
        
        """ 
        Step 15.01:Verify that the Yellow was added
        """
        page_designer_obj.switch_to_container_frame("Panel 3")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: yellow;',"Step 15.01 : Verify that the Yellow was added.")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 16: Drag Red over Panel 3 and choose Add content.
        """
        page_designer_obj.drag_content_item_to_container("Red", "Panel 3",content_folder_path=None)
        page_designer_obj.select_options_add_content_dialog("Add content")
        
        """ 
        Step 17: Drag Silver over Panel 4.
        """
        page_designer_obj.drag_content_item_to_container("Silver", "Panel 4",content_folder_path=None)
        
        """ 
        Step 18: Drag Yellow over Panel 4 and choose Add content.
        """
        page_designer_obj.drag_content_item_to_container("Yellow", "Panel 4",content_folder_path=None)
        page_designer_obj.select_options_add_content_dialog("Add content")
        
        """ 
        Step 18.01: Add content.Verify that another tab was created titled Yellow
        """
        page_designer_obj.accordion_container("Panel 4").verify_area_title(['Silver', 'Yellow'], "18.01")
        
        """ 
        Step 19: Click the ToolBar icon and click Save.
        Step 20: Enter "Canvas Interaction" in Title and click Save.
        """
        page_designer_obj.save_page_from_toolbar("Canvas Interaction")
        
        """ 
        Step 20.01: Verify that the "Canvas Interaction" is now shown in the Canvas selector at the bottom of the page.
        """
        page_designer_obj.verify_page_tab_groups(["Canvas Interaction"], "Step 20.01 : Verify that the Canvas Interaction is now shown in the Canvas selector at the bottom of the page.")
        
        """ 
        Step 21: Click the ToolBar icon and click Close.
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """ 
        Step 22: Right click on the Canvas Interaction page and choose Edit.
        """
        main_page_obj.right_click_folder_item_and_select_menu("Canvas Interaction", "Edit")
        
        """ 
        Step 22.01: Verify that the page designer opens and the page loads with no issues.
        """
        core_util_obj.switch_to_new_window()
        page_designer_obj.verify_page_heading_title(['Page Heading'], msg="Step 22.01 : Verify Page Heading")
        page_designer_obj.verify_page_header_visible_buttons(['Refresh'], msg="Step 22.02 : Verify Page Headear visible buttons")
        page_designer_obj.verify_containers_title(['Blue', 'Panel 2', 'Panel 3', 'Panel 4'],msg="Step 22.03 : Verify container titles")
        page_designer_obj.tab_container("Panel 2").verify_tabs(['Green', 'Gray'], "22.04")
        page_designer_obj.accordion_container("Panel 4").verify_area_title(['Silver', 'Yellow'], "22.05")
        page_designer_obj.switch_to_container_frame("Panel 3")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: yellow;',"Step 22.06 : Verify that the Yellow was added.")
        page_designer_obj.switch_to_default_page()
        
        """ 
        Step 23: Click The toolbar and choose Save as.
        """
        page_designer_obj.select_option_from_application_menu("Save as...")
        
        """ 
        Step 23.01: Verify "Canvas Interaction" in Title and "canvas_interaction" in Name box is displayed.
        """
        page_designer_obj.resource_dialog().verify_title_textbox_value("Canvas Interaction", step_num="23.01")
        page_designer_obj.resource_dialog().verify_name_textbox_value("canvas_interaction", step_num="23.02")
        
        """ 
        Step 24: Close Save as window and page designer.
        """
        main_page_obj.click_button_on_popup_dialog("Cancel")
        
        """
        Step 25 : Sign out WF
        """
        core_util_obj.switch_to_previous_window()
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 
        
        
        